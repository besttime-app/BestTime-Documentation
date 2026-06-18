# Ghost Blog Fetcher

A Python script to fetch blog posts from your Ghost blog using the Content API with filtering capabilities for labels/categories and other metadata.

## Features

- ✅ Fetch all blog posts from your Ghost blog
- ✅ Filter posts by tags/categories
- ✅ Filter posts by authors
- ✅ Export to JSON or Markdown format
- ✅ List available tags and authors
- ✅ Pagination support for large blogs
- ✅ Comprehensive post metadata extraction

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

#### Basic Usage
```bash
# Fetch all posts and save to JSON
python ghost_blog_fetcher.py

# Fetch posts and save to both JSON and Markdown
python ghost_blog_fetcher.py --output-format both

# List all available tags
python ghost_blog_fetcher.py --list-tags

# List all available authors
python ghost_blog_fetcher.py --list-authors
```

#### Filtering Options
```bash
# Filter posts by tag
python ghost_blog_fetcher.py --filter-tag "api-documentation"

# Filter posts by author
python ghost_blog_fetcher.py --filter-author "john-doe"

# Filter by both tag and author
python ghost_blog_fetcher.py --filter-tag "tutorial" --filter-author "jane-smith"

# Limit the number of pages to fetch
python ghost_blog_fetcher.py --max-pages 5
```

#### Custom Output
```bash
# Specify custom output filename
python ghost_blog_fetcher.py --output-file "my_blog_posts"

# Save only to Markdown
python ghost_blog_fetcher.py --output-format markdown --output-file "blog_archive"
```

### Python API Usage

```python
from ghost_blog_fetcher import GhostBlogFetcher

# Initialize the fetcher
fetcher = GhostBlogFetcher(
    api_url="https://blog.besttime.app",
    content_api_key="ee2376b8ad539078f27284c095"
)

# Get all posts
all_posts = fetcher.get_all_posts()

# Filter by tag
tutorial_posts = fetcher.get_all_posts(filter_tag="tutorial")

# Filter by author
author_posts = fetcher.get_all_posts(filter_author="john-doe")

# Get available tags and authors
tags = fetcher.get_tags()
authors = fetcher.get_authors()

# Save to files
fetcher.save_posts_to_json(all_posts, "posts.json")
fetcher.save_posts_to_markdown(all_posts, "posts.md")
```

## Configuration

The script uses the following default values (can be overridden via command line):

- **API URL**: `https://blog.besttime.app`
- **Content API Key**: `ee2376b8ad539078f27284c095`
- **Max Pages**: 10
- **Output Format**: JSON
- **Posts per Page**: 15 (Ghost API limit for free tier)

## Output Formats

### JSON Format
```json
{
  "fetched_at": "2024-01-15T10:30:00",
  "total_posts": 25,
  "posts": [
    {
      "id": "post_id",
      "title": "Post Title",
      "slug": "post-slug",
      "excerpt": "Post excerpt...",
      "html": "<p>Full HTML content...</p>",
      "plaintext": "Plain text content...",
      "feature_image": "https://...",
      "published_at": "2024-01-15T09:00:00.000Z",
      "updated_at": "2024-01-15T09:00:00.000Z",
      "url": "https://blog.besttime.app/post-slug/",
      "tags": ["API", "Documentation"],
      "tag_slugs": ["api", "documentation"],
      "authors": ["John Doe"],
      "author_slugs": ["john-doe"],
      "meta_title": "SEO Title",
      "meta_description": "SEO Description",
      "reading_time": 5
    }
  ]
}
```

### Markdown Format
```markdown
# Blog Posts

*Fetched on 2024-01-15 10:30:00*

Total posts: 25

## Post Title

**Published:** 2024-01-15T09:00:00.000Z

**URL:** https://blog.besttime.app/post-slug/

**Tags:** API, Documentation

**Authors:** John Doe

**Excerpt:** Post excerpt...

---
```

## Examples

Run the example script to see the fetcher in action:
```bash
python example_usage.py
```

## Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--api-url` | Ghost blog API URL | `https://blog.besttime.app` |
| `--content-api-key` | Ghost Content API key | `ee2376b8ad539078f27284c095` |
| `--filter-tag` | Filter posts by tag slug | None |
| `--filter-author` | Filter posts by author slug | None |
| `--max-pages` | Maximum pages to fetch | 10 |
| `--output-format` | Output format (json/markdown/both) | json |
| `--output-file` | Output filename (without extension) | Auto-generated |
| `--list-tags` | List available tags and exit | False |
| `--list-authors` | List available authors and exit | False |

## Error Handling

The script includes comprehensive error handling for:
- Network connectivity issues
- Invalid API credentials
- Ghost API rate limits
- Malformed responses
- File I/O errors

## Notes

- The Ghost Content API has a limit of 15 posts per request for free tier accounts
- The script automatically handles pagination to fetch all posts
- Tag and author filters use slugs, not display names
- All timestamps are in ISO format
- The script preserves all original post metadata from Ghost

## Troubleshooting

1. **Authentication Error**: Verify your Content API key is correct
2. **No Posts Found**: Check if your blog has published posts
3. **Filter Not Working**: Use tag/author slugs, not display names
4. **Rate Limiting**: Reduce `--max-pages` or add delays between requests
