#!/usr/bin/env python3
"""
YouTube Thumbnail Fetcher
Extracts and downloads YouTube video thumbnails for use as cover images.
"""

import sys
import re
import urllib.request
import urllib.error
from pathlib import Path


def extract_video_id(url):
    """
    Extract YouTube video ID from various URL formats.
    
    Supports:
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtube.com/watch?v=VIDEO_ID
    - https://m.youtube.com/watch?v=VIDEO_ID
    """
    patterns = [
        r'(?:https?://)?(?:www\.)?youtu\.be/([a-zA-Z0-9_-]{11})',
        r'(?:https?://)?(?:www\.)?(?:m\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None


def get_thumbnail_url(video_id, quality='maxresdefault'):
    """
    Get YouTube thumbnail URL for a video ID.
    
    Quality options (in order of preference):
    - maxresdefault: 1280x720 (best quality, not always available)
    - sddefault: 640x480
    - hqdefault: 480x360
    - mqdefault: 320x180
    - default: 120x90
    """
    return f"https://img.youtube.com/vi/{video_id}/{quality}.jpg"


def download_thumbnail(video_id, output_path=None, quality='maxresdefault'):
    """
    Download YouTube thumbnail to a file.
    
    Args:
        video_id: YouTube video ID
        output_path: Path to save the image (default: {video_id}.jpg)
        quality: Thumbnail quality (default: maxresdefault)
    
    Returns:
        Path to the downloaded file or None if failed
    """
    if output_path is None:
        output_path = f"{video_id}.jpg"
    
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Try different quality levels if maxresdefault is not available
    qualities = [quality, 'sddefault', 'hqdefault', 'mqdefault', 'default']
    
    for q in qualities:
        url = get_thumbnail_url(video_id, q)
        try:
            print(f"Trying to download {q} quality from: {url}")
            urllib.request.urlretrieve(url, output_path)
            
            # Check if file is valid (not a placeholder)
            if output_path.stat().st_size > 1000:  # Valid images are usually > 1KB
                print(f"✓ Successfully downloaded thumbnail: {output_path}")
                print(f"  Quality: {q}")
                print(f"  URL: {url}")
                return str(output_path)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                continue
            else:
                print(f"Error downloading {q}: {e}")
        except Exception as e:
            print(f"Error downloading {q}: {e}")
    
    print("✗ Failed to download thumbnail in any quality")
    return None


def main():
    """Main function for CLI usage."""
    if len(sys.argv) < 2:
        print("Usage: python youtube_thumbnail.py <youtube_url> [output_path]")
        print("\nExamples:")
        print("  python youtube_thumbnail.py https://youtu.be/0fHb1DeYvCQ")
        print("  python youtube_thumbnail.py https://youtu.be/0fHb1DeYvCQ cover.jpg")
        print("  python youtube_thumbnail.py https://youtu.be/0fHb1DeYvCQ static/covers/video.jpg")
        sys.exit(1)
    
    url = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    print(f"Processing URL: {url}")
    
    video_id = extract_video_id(url)
    if not video_id:
        print("✗ Error: Could not extract video ID from URL")
        print("  Supported formats:")
        print("    - https://youtu.be/VIDEO_ID")
        print("    - https://www.youtube.com/watch?v=VIDEO_ID")
        sys.exit(1)
    
    print(f"Video ID: {video_id}")
    
    result = download_thumbnail(video_id, output_path)
    
    if result:
        print(f"\n✓ Thumbnail URL for markdown:")
        print(f'  cover_image = "{get_thumbnail_url(video_id)}"')
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()

# Made with Bob
