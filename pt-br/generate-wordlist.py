#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import itertools

def load_list_from_file(filename):
    if not filename:
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def combine_words(first_list, second_list):
    combined = set()
    for first in first_list:
        for second in second_list:
            combined.add(f"{first}{second}")
    return sorted(combined)


def main():
    parser = argparse.ArgumentParser(description="Generate a wordlist using prefixes, base words, and suffixes.")
    parser.add_argument("-b", "--base", required=True, help="File with base words (one per line)")
    parser.add_argument("-p", "--prefixes", required=False, help="File with prefix list (one per line)")
    parser.add_argument("-s", "--suffixes", required=False, help="File with suffix list (one per line)")
    parser.add_argument("-o", "--output", required=True, help="Output filename")

    args = parser.parse_args()

    if not args.prefixes and not args.suffixes:
        print("[!] You must provide at least one of --prefixes or --suffixes.")
        return

    base_words = load_list_from_file(args.base)
    prefixes = load_list_from_file(args.prefixes)
    suffixes = load_list_from_file(args.suffixes)

    print(f"[+] Base words: {len(base_words)}")
    print(f"[+] Prefixes: {len(prefixes)}")
    print(f"[+] Suffixes: {len(suffixes)}")

    wordlist = set(base_words)
    if prefixes:
        wordlist = wordlist.union(combine_words(prefixes, base_words))
    if suffixes:
        wordlist = wordlist.union(combine_words(base_words, suffixes))

    wordlist = sorted(wordlist)

    with open(args.output, "w", encoding="utf-8") as f:
        for word in wordlist:
            f.write(word + "\n")

    print(f"[+] Generated wordlist with {len(wordlist)} words.")

if __name__ == "__main__":
    main()
