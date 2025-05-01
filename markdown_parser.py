"""
Markdown Parser for LeetCode Repository

This script demonstrates how to work with Markdown files in Python.
It can parse the README.md file in the LeetCode repository and extract information.
"""

import os
import re
from collections import Counter

def parse_markdown_file(file_path):
    """
    Parse a Markdown file and extract basic information.
    
    Args:
        file_path: Path to the Markdown file
        
    Returns:
        dict: Dictionary containing information about the Markdown file
    """
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Extract information
        info = {
            "filename": os.path.basename(file_path),
            "size_bytes": os.path.getsize(file_path),
            "content": content,
            "stats": analyze_markdown(content)
        }
        
        return info
    
    except Exception as e:
        return {"error": f"Error parsing file: {str(e)}"}

def analyze_markdown(content):
    """
    Analyze Markdown content and extract statistics.
    
    Args:
        content: Markdown content as string
        
    Returns:
        dict: Statistics about the Markdown content
    """
    stats = {
        "char_count": len(content),
        "word_count": len(content.split()),
        "line_count": content.count('\n') + 1,
    }
    
    # Count headers
    headers = {
        "h1_count": len(re.findall(r'^# .+', content, re.MULTILINE)),
        "h2_count": len(re.findall(r'^## .+', content, re.MULTILINE)),
        "h3_count": len(re.findall(r'^### .+', content, re.MULTILINE)),
    }
    stats.update(headers)
    
    # Count code blocks
    stats["code_blocks"] = content.count('```')
    
    # Most common words (excluding common stop words)
    words = re.findall(r'\b\w+\b', content.lower())
    stop_words = {'the', 'is', 'and', 'to', 'of', 'a', 'in', 'that', 'for'}
    filtered_words = [word for word in words if word not in stop_words]
    word_freq = Counter(filtered_words).most_common(5)
    stats["common_words"] = word_freq
    
    return stats

def main():
    """Main function to demonstrate the Markdown parser."""
    # Path to the README.md file in the current directory
    readme_path = "README.md"
    
    # Parse the Markdown file
    info = parse_markdown_file(readme_path)
    
    # Display the results
    if "error" in info:
        print(f"Error: {info['error']}")
    else:
        print(f"File: {info['filename']}")
        print(f"Size: {info['size_bytes']} bytes")
        print("\nContent:")
        print("-" * 40)
        print(info['content'])
        print("-" * 40)
        
        print("\nStatistics:")
        for key, value in info['stats'].items():
            if key != "common_words":
                print(f"- {key}: {value}")
        
        print("\nMost common words:")
        for word, count in info['stats']['common_words']:
            print(f"- '{word}': {count} occurrences")

if __name__ == "__main__":
    main()
