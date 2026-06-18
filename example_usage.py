#!/usr/bin/env python3
"""
Example usage of the Ghost Blog Fetcher

This script demonstrates various ways to use the GhostBlogFetcher class.
"""

from ghost_blog_fetcher import GhostBlogFetcher
import json

def main():
    # Initialize the fetcher with your Ghost blog credentials
    fetcher = GhostBlogFetcher(
        api_url="https://blog.besttime.app",
        content_api_key="ee2376b8ad539078f27284c095"
    )
    
    print("=== Ghost Blog Fetcher Examples ===\n")
    
    # Example 1: Get all available tags
    print("1. Available tags:")
    tags = fetcher.get_tags()
    for tag in tags[:5]:  # Show first 5 tags
        print(f"   - {tag.get('name')} (slug: {tag.get('slug')})")
    print(f"   ... and {len(tags) - 5} more tags\n")
    
    # Example 2: Get all available authors
    print("2. Available authors:")
    authors = fetcher.get_authors()
    for author in authors:
        print(f"   - {author.get('name')} (slug: {author.get('slug')})")
    print()
    
    # Example 3: Fetch recent posts (first page only)
    print("3. Recent posts (first 5):")
    response = fetcher.get_posts(limit=5)
    posts = response.get('posts', [])
    
    for post in posts:
        print(f"   - {post.get('title')}")
        print(f"     Published: {post.get('published_at')}")
        print(f"     Tags: {[tag.get('name') for tag in post.get('tags', [])]}")
        print()
    
    # Example 4: Filter posts by a specific tag (if any tags exist)
    if tags:
        tag_slug = tags[0].get('slug')
        print(f"4. Posts filtered by tag '{tags[0].get('name')}' (slug: {tag_slug}):")
        filtered_posts = fetcher.get_all_posts(filter_tag=tag_slug, max_pages=1)
        print(f"   Found {len(filtered_posts)} posts with this tag\n")
    
    # Example 5: Save all posts to JSON
    print("5. Saving all posts to JSON...")
    all_posts = fetcher.get_all_posts(max_pages=2)  # Limit to 2 pages for demo
    fetcher.save_posts_to_json(all_posts, "example_blog_posts.json")
    
    # Example 6: Save posts to markdown
    print("6. Saving posts to markdown...")
    fetcher.save_posts_to_markdown(all_posts, "example_blog_posts.md")
    
    print("\n=== Examples completed ===")
    print("Check the generated files:")
    print("- example_blog_posts.json")
    print("- example_blog_posts.md")

if __name__ == "__main__":
    main()
