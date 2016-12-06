
#!/usr/bin/env python3

"""Retreive and print words from a URL.

Usage:
    python3 words.py <URL>
"""

from urllib.request import urlopen
import sys

def fetch_words(url):
    """Fetch a list of words from a URL.
    Args:
        url: the URL of a UTF-8 text document.

    Returns:
        A List of strings containing the words of text document

    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_items(items):
    """Print items at one per line.
    Args:
        An iterable series of printable items.

    """
    for items in items:
        print(items)

def main(url):
    """Print each word from a text document from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    """
    words = fetch_words(url)
    print_items(words)
#import functions into REPL and rendered in script
if __name__ == '__main__':
    main(sys.argv[1])#0th argument is module filename
