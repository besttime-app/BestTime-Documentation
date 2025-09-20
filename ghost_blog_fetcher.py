#!/usr/bin/env python3
"""
Ghost Blog Fetcher

A Python script to fetch blog posts from a Ghost blog using the Content API
with filtering capabilities for labels/categories and other metadata.

Usage:
    python ghost_blog_fetcher.py [options]

Requirements:
    pip install requests python-dateutil
"""

import requests
import json
import argparse
from datetime import datetime
from typing import List, Dict, Optional, Any
from urllib.parse import urljoin
import sys
from pathlib import Path

class GhostBlogFetcher:
    """A class to fetch and filter blog posts from Ghost blog."""
    
    def __init__(self, api_url: str, content_api_key: str, verbose: bool = False):
        """
        Initialize the Ghost blog fetcher.
        
        Args:
            api_url (str): The Ghost blog API URL (e.g., https://blog.besttime.app)
            content_api_key (str): The Ghost Content API key
            verbose (bool): Enable verbose logging
        """
        self.api_url = api_url.rstrip('/')
        self.content_api_key = content_api_key
        self.verbose = verbose
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def _make_request(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Make a request to the Ghost API.
        
        Args:
            endpoint (str): The API endpoint
            params (Dict[str, Any]): Query parameters
            
        Returns:
            Dict[str, Any]: The API response
            
        Raises:
            requests.RequestException: If the request fails
        """
        url = urljoin(self.api_url, f"/ghost/api/v3/content/{endpoint}")
        
        if params is None:
            params = {}
        
        params['key'] = self.content_api_key
        
        try:
            if self.verbose:
                print(f"Making request to: {url}")
                print(f"Params: {params}")
            
            response = self.session.get(url, params=params)
            
            if self.verbose:
                print(f"Response status: {response.status_code}")
            
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error making request to {url}: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response content: {e.response.text}")
            raise
    
    def get_posts(self, 
                  limit: int = 15,
                  page: int = 1,
                  include: str = "tags,authors",
                  filter_tag: Optional[str] = None,
                  filter_author: Optional[str] = None,
                  filter_status: str = "published",
                  order: str = "published_at DESC") -> Dict[str, Any]:
        """
        Fetch blog posts with optional filtering.
        
        Args:
            limit (int): Number of posts to fetch per page (max 15 for free tier)
            page (int): Page number
            include (str): Related data to include (tags,authors,etc.)
            filter_tag (str): Filter by tag slug
            filter_author (str): Filter by author slug
            filter_status (str): Filter by status (published, draft, etc.)
            order (str): Sort order
            
        Returns:
            Dict[str, Any]: Posts data from Ghost API
        """
        params = {
            'limit': limit,
            'page': page,
            'include': include,
            'order': order
        }
        
        # Build filter string - try different approaches
        filter_parts = []
        
        # For now, let's try without status filter and see if that works
        # Add tag filter if specified
        if filter_tag:
            filter_parts.append(f"tag:{filter_tag}")
        
        # Add author filter if specified
        if filter_author:
            filter_parts.append(f"author:{filter_author}")
        
        # Only add filter if we have filter parts
        if filter_parts:
            params['filter'] = "+".join(filter_parts)
        
        return self._make_request('posts/', params)
    
    def get_all_posts(self, 
                     filter_tag: Optional[str] = None,
                     filter_author: Optional[str] = None,
                     max_pages: int = 10) -> List[Dict[str, Any]]:
        """
        Fetch all blog posts across multiple pages.
        
        Args:
            filter_tag (str): Filter by tag slug
            filter_author (str): Filter by author slug
            max_pages (int): Maximum number of pages to fetch
            
        Returns:
            List[Dict[str, Any]]: List of all posts
        """
        all_posts = []
        page = 1
        
        while page <= max_pages:
            print(f"Fetching page {page}...")
            response = self.get_posts(
                limit=15,
                page=page,
                filter_tag=filter_tag,
                filter_author=filter_author
            )
            
            posts = response.get('posts', [])
            if not posts:
                break
                
            all_posts.extend(posts)
            page += 1
        
        return all_posts
    
    def get_tags(self) -> List[Dict[str, Any]]:
        """Fetch all available tags."""
        return self._make_request('tags/').get('tags', [])
    
    def get_authors(self) -> List[Dict[str, Any]]:
        """Fetch all available authors."""
        return self._make_request('authors/').get('authors', [])
    
    def find_tag_by_name(self, tag_name: str) -> Optional[Dict[str, Any]]:
        """
        Find a tag by its display name (case-insensitive).
        
        Args:
            tag_name (str): The tag display name to search for
            
        Returns:
            Optional[Dict[str, Any]]: The tag data if found, None otherwise
        """
        tags = self.get_tags()
        tag_name_lower = tag_name.lower()
        
        for tag in tags:
            if tag.get('name', '').lower() == tag_name_lower:
                return tag
        
        return None
    
    def find_author_by_name(self, author_name: str) -> Optional[Dict[str, Any]]:
        """
        Find an author by their display name (case-insensitive).
        
        Args:
            author_name (str): The author display name to search for
            
        Returns:
            Optional[Dict[str, Any]]: The author data if found, None otherwise
        """
        authors = self.get_authors()
        author_name_lower = author_name.lower()
        
        for author in authors:
            if author.get('name', '').lower() == author_name_lower:
                return author
        
        return None
    
    def format_post(self, post: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format a post for better readability.
        
        Args:
            post (Dict[str, Any]): Raw post data from Ghost
            
        Returns:
            Dict[str, Any]: Formatted post data
        """
        return {
            'id': post.get('id'),
            'title': post.get('title'),
            'slug': post.get('slug'),
            'excerpt': post.get('excerpt'),
            'html': post.get('html'),
            'plaintext': post.get('plaintext'),
            'feature_image': post.get('feature_image'),
            'published_at': post.get('published_at'),
            'updated_at': post.get('updated_at'),
            'url': post.get('url'),
            'tags': [tag.get('name') for tag in post.get('tags', [])],
            'tag_slugs': [tag.get('slug') for tag in post.get('tags', [])],
            'authors': [author.get('name') for author in post.get('authors', [])],
            'author_slugs': [author.get('slug') for author in post.get('authors', [])],
            'meta_title': post.get('meta_title'),
            'meta_description': post.get('meta_description'),
            'reading_time': post.get('reading_time')
        }
    
    def save_posts_to_json(self, posts: List[Dict[str, Any]], filename: str) -> None:
        """
        Save posts to a JSON file.
        
        Args:
            posts (List[Dict[str, Any]]): List of posts to save
            filename (str): Output filename
        """
        formatted_posts = [self.format_post(post) for post in posts]
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({
                'fetched_at': datetime.now().isoformat(),
                'total_posts': len(formatted_posts),
                'posts': formatted_posts
            }, f, indent=2, ensure_ascii=False)
        
        print(f"Saved {len(formatted_posts)} posts to {filename}")
    
    def save_posts_to_markdown(self, posts: List[Dict[str, Any]], filename: str) -> None:
        """
        Save posts to a markdown file.
        
        Args:
            posts (List[Dict[str, Any]]): List of posts to save
            filename (str): Output filename
        """
        formatted_posts = [self.format_post(post) for post in posts]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# Blog Posts\n\n")
            f.write(f"*Fetched on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
            f.write(f"Total posts: {len(formatted_posts)}\n\n")
            
            for post in formatted_posts:
                f.write(f"## {post['title']}\n\n")
                f.write(f"**Published:** {post['published_at']}\n\n")
                f.write(f"**URL:** {post['url']}\n\n")
                f.write(f"**Tags:** {', '.join(post['tags'])}\n\n")
                f.write(f"**Authors:** {', '.join(post['authors'])}\n\n")
                if post['excerpt']:
                    f.write(f"**Excerpt:** {post['excerpt']}\n\n")
                f.write("---\n\n")
        
        print(f"Saved {len(formatted_posts)} posts to {filename}")


def main():
    """Main function to run the Ghost blog fetcher."""
    parser = argparse.ArgumentParser(description='Fetch blog posts from Ghost blog')
    parser.add_argument('--api-url', default='https://blog.besttime.app',
                       help='Ghost blog API URL')
    parser.add_argument('--content-api-key',
                       help='Ghost Content API key')
    parser.add_argument('--filter-tag', help='Filter posts by tag slug or name')
    parser.add_argument('--filter-author', help='Filter posts by author slug or name')
    parser.add_argument('--max-pages', type=int, default=10,
                       help='Maximum number of pages to fetch')
    parser.add_argument('--output-format', choices=['json', 'markdown', 'both'], 
                       default='json', help='Output format')
    parser.add_argument('--output-file', help='Output filename (without extension)')
    parser.add_argument('--list-tags', action='store_true',
                       help='List all available tags and exit')
    parser.add_argument('--list-authors', action='store_true',
                       help='List all available authors and exit')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose logging for debugging')
    
    args = parser.parse_args()
    
    # Initialize the fetcher
    fetcher = GhostBlogFetcher(args.api_url, args.content_api_key, verbose=args.verbose)
    
    try:
        # List tags if requested
        if args.list_tags:
            tags = fetcher.get_tags()
            print("Available tags:")
            for tag in tags:
                print(f"  - {tag.get('name')} (slug: {tag.get('slug')})")
            return
        
        # List authors if requested
        if args.list_authors:
            authors = fetcher.get_authors()
            print("Available authors:")
            for author in authors:
                print(f"  - {author.get('name')} (slug: {author.get('slug')})")
            return
        
        # Resolve tag and author names to slugs if needed
        resolved_tag = args.filter_tag
        resolved_author = args.filter_author
        
        if args.filter_tag:
            # Try to find tag by name first, then use as slug
            tag_data = fetcher.find_tag_by_name(args.filter_tag)
            if tag_data:
                resolved_tag = tag_data.get('slug')
                print(f"Found tag '{args.filter_tag}' with slug '{resolved_tag}'")
            else:
                print(f"Using '{args.filter_tag}' as tag slug")
        
        if args.filter_author:
            # Try to find author by name first, then use as slug
            author_data = fetcher.find_author_by_name(args.filter_author)
            if author_data:
                resolved_author = author_data.get('slug')
                print(f"Found author '{args.filter_author}' with slug '{resolved_author}'")
            else:
                print(f"Using '{args.filter_author}' as author slug")
        
        # Fetch posts
        print("Fetching blog posts...")
        posts = fetcher.get_all_posts(
            filter_tag=resolved_tag,
            filter_author=resolved_author,
            max_pages=args.max_pages
        )
        
        if not posts:
            print("No posts found with the specified filters.")
            return
        
        print(f"Found {len(posts)} posts")
        
        # Generate output filename if not provided
        if not args.output_file:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filter_suffix = ""
            if args.filter_tag:
                filter_suffix += f"_tag-{args.filter_tag}"
            if args.filter_author:
                filter_suffix += f"_author-{args.filter_author}"
            args.output_file = f"ghost_posts{filter_suffix}_{timestamp}"
        
        # Save in requested format(s)
        if args.output_format in ['json', 'both']:
            fetcher.save_posts_to_json(posts, f"{args.output_file}.json")
        
        if args.output_format in ['markdown', 'both']:
            fetcher.save_posts_to_markdown(posts, f"{args.output_file}.md")
        
        # Print summary
        print(f"\nSummary:")
        print(f"  Total posts: {len(posts)}")
        if resolved_tag:
            print(f"  Filtered by tag: {resolved_tag}")
        if resolved_author:
            print(f"  Filtered by author: {resolved_author}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
