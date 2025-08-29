import sys
import random
from typing import Iterator, List, Optional
import itertools
from pybip39 import Mnemonic

def load_wordlist(filepath: str = '../bip39.txt') -> List[str]:
    """Loads the BIP39 wordlist from a file."""
    with open(filepath, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def sequential_search(template: List[str], wordlist: List[str]) -> Iterator[str]:
    """
    Generates all possible mnemonic phrases from a template with placeholders.
    Used for Mode 1.

    Args:
        template (List[str]): A list of words and '*' placeholders.
        wordlist (List[str]): The list of words to use for placeholders.
    """
    placeholder_indices = [i for i, word in enumerate(template) if word == '*']
    num_placeholders = len(placeholder_indices)

    if not num_placeholders:
        yield " ".join(template)
        return

    # Create an iterator that yields tuples of replacement words
    word_combinations = itertools.product(wordlist, repeat=num_placeholders)

    # Create a mutable copy of the template
    current_phrase = list(template)

    for combination in word_combinations:
        # Fill in the placeholders with the current combination
        for i, word in enumerate(combination):
            current_phrase[placeholder_indices[i]] = word
        yield " ".join(current_phrase)

def from_file_or_stdin(source: str) -> Iterator[str]:
    """
    Yields lines from a file or from stdin.
    Used for Mode 3/4.

    Args:
        source (str): The filepath or 'stdin'.
    """
    if source == 'stdin':
        for line in sys.stdin:
            yield line.strip()
    else:
        with open(source, 'r') as f:
            for line in f:
                yield line.strip()

def random_search(template: List[str], wordlist: List[str], custom_wordlist: Optional[List[str]] = None) -> Iterator[str]:
    """
    Generates random mnemonic phrases from a template with placeholders.
    Used for Mode 2.

    Args:
        template (List[str]): A list of words and '*' placeholders.
        wordlist (List[str]): The main BIP39 wordlist.
        custom_wordlist (Optional[List[str]]): An optional custom list of words for placeholders.
    """
    placeholder_indices = [i for i, word in enumerate(template) if word == '*']
    source_wordlist = custom_wordlist if custom_wordlist else wordlist

    current_phrase = list(template)

    while True:
        for i in placeholder_indices:
            current_phrase[i] = random.choice(source_wordlist)
        yield " ".join(current_phrase)

def from_entropy_source(source: str, lang: str = 'en') -> Iterator[str]:
    """
    Reads hex entropy from a file or stdin and yields mnemonic phrases.
    Used for Mode 5/6.
    """
    if source == 'stdin':
        source_iterator = sys.stdin
    else:
        source_iterator = open(source, 'r')

    for line in source_iterator:
        entropy_hex = line.strip()
        if not entropy_hex:
            continue
        try:
            entropy_bytes = bytes.fromhex(entropy_hex)
            mnemonic = Mnemonic.from_entropy(entropy_bytes, language=lang)
            yield str(mnemonic)
        except (ValueError, IOError) as e:
            print(f"Error processing entropy '{entropy_hex}': {e}", file=sys.stderr)

    if source != 'stdin':
        source_iterator.close()
