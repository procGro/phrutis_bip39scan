import argparse
import sys
from database import AddressDatabase
import generators

def main():
    parser = argparse.ArgumentParser(
        description="bip39scan v5.0.1 (phrutis modification 15/08/2025) - Python Replica by Jules",
        epilog="Example:\n   > python bip39scan.py -a addresses.txt -p \"m/0'/0-1\" --bits 128",
        formatter_class=argparse.RawTextHelpFormatter
    )

    # Define all the arguments based on the original tool's help page
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='Print this message.')

    parser.add_argument('-a', '--addresses', type=str,
                        help='The name of the address list, each address of a separate line, or a binary\n'
                             'file previously created with --save-bin. Binary files are faster to read.')

    parser.add_argument('--save-bin', type=str,
                        help='The name of the binary file to write, 20 bytes per address. This is in order\n'
                             'to accelerate loading of addresses.')

    parser.add_argument('-p', '--path', type=str,
                        help="Use this derivation path template, e.g. \"m/44'/60'/0-99'/0/0-99\"\n"
                             "The default is m/44'/0'/0-9'/0-1/0-9 for p2pkh addresses and ethereum,\n"
                             "m/49'/0'/0-9'/0-1/0-9 for p2sh addresses,\n"
                             "m/84'/0'/0-9'/0-1/0-9 for bech32 addresses.")

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Print debug messages.')

    parser.add_argument('-t', '--type', type=str,
                        help='Address type, one of P2SH, P2PKH_UNCOMPRESSED, P2PKH, bech32, ethereum\n'
                             'By default, address type is detected from the address file, if it\'s text.\n'
                             'This options is required when using binary data.')

    parser.add_argument('-S', '--save', type=str,
                        help='Save found results to the file.')

    parser.add_argument('-m', '--mnemo', type=str,
                        help='Read mnemonics from the file, one per line. -m stdin to read from the input pipe.')

    parser.add_argument('--alphabet', type=str,
                        help='Generate mnemonics as passwords from the characters of the given file.\n'
                             'Not compatible with --mnemo option.')

    parser.add_argument('--bits', type=int,
                        help='Generate mnemonics using RNG of the libbitcoin explorer 3.2.0. The integer number is the entropy length:\n'
                             '64 - 6 words, 96 - 9 words, 128 - 12 words, 160 - 15 words, 192 - 18 words, 224 - 21 words\n'
                             '256 - 24 words.')

    parser.add_argument('-e', '--entropy', type=str,
                        help="Read entropy from the file in hex, one per line. If FILE is 'stdin', read from input pipe.")

    parser.add_argument('-l', '--lang', type=str, default='en',
                        help='Language of the mnemonics generated with --bits, one of en, es, es-nfkd, ja, ja-nfkd, it, fr, cs, ru, uk, zh_Hans, zh_Hant, po, ko, tu.\n'
                             'Default is English.')

    parser.add_argument('--start', type=str,
                        help='For generated mnemonics, start from this mnemonic.')

    parser.add_argument('-d', '--devices', type=str,
                        help='Comma-separated list of device indexes (indeces start with 0). By default,\n'
                             'run on all devices. (Note: This is for compatibility, Python version uses CPU cores).')

    parser.add_argument('--bloom', type=str, default='1024M',
                        help='Bloom filter size in GPU, in bytes. Can use K, M, and G suffixes. Default\n'
                             'is 1024M. (Note: This will be used for RAM allocation in Python version).')

    parser.add_argument('--kernel', type=str,
                        help='GPU memory reserved for kernel execution, in bytes. Can use K, M, and G suffixes.\n'
                             'Default depends on the device. (Ignored in Python version).')

    parser.add_argument('--ec-threads', type=int, default=128,
                        help='Number of threads for elliptic curve computations. Default is 128. Should be a multiplier of 32.\n'
                             'Set to 64 if you are experiencing out of memory errors. (Ignored in Python version).')

    parser.add_argument('-w', '--words', type=str,
                        help="Use custom dictionary for '*' placeholders in the mnemo template; each word in a separate text line.\n"
                             "Each word should be a valid BIP39 word in the specified language (--lang).")

    parser.add_argument('--dump', action='store_true',
                        help='Dumps valid mnemonics.')

    parser.add_argument('--core', type=str,
                        help='BIP32 reading from file and receiving stream from external generator.')

    parser.add_argument('--hmac', type=str,
                        help='Read passwords from the file, one per line, and use them as HMAC keys to generate BIP39 seeds.')

    parser.add_argument('--hmac1', type=str,
                        help="Same as --hmac but doesn't check intermediate iterations.")

    parser.add_argument('--iterations', type=int,
                        help='In the --hmac mode: number of hmac iterations to perform.')

    parser.add_argument('--depth', type=int,
                        help='Starting range of generator initialization depth')

    parser.add_argument('-r', '--random', action='store_true',
                        help="Randomize the mnemonics generated with MNEMO templates (see below).")

    parser.add_argument('mnemo_template', nargs='*',
                        help='Mnemonic template, up to 24 words. Can contain placeholders \'*\'. If less than\n'
                             '12 words, the rest are placeholders. Each \'*\' is replaced with one of 2048 words (or one of the words\n'
                             'from the dictionary specified with --words option).')


    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    # --- Main Logic ---

    # TEMP TEST for rbloom
    from rbloom import BloomFilter
    test_filter = BloomFilter(1000, 0.01)
    test_filter.add("hello")
    print("rbloom filter dir:", dir(test_filter))
    # print("rbloom filter dict:", test_filter.__dict__) # rbloom might not have a dict

    address_db = None
    if args.addresses:
        address_db = AddressDatabase()
        # TODO: Add support for .bin files
        address_db.load_from_text_file(args.addresses)

    # Load wordlists
    wordlist = generators.load_wordlist()
    custom_wordlist = None
    if args.words:
        custom_wordlist = generators.load_wordlist(filepath=args.words)

    # --- Generator Selection ---
    candidate_generator = None
    if args.mnemo:
        candidate_generator = generators.from_file_or_stdin(args.mnemo)
    elif args.entropy:
        candidate_generator = generators.from_entropy_source(args.entropy, args.lang)
    elif args.mnemo_template:
        if args.random:
            candidate_generator = generators.random_search(args.mnemo_template, wordlist, custom_wordlist)
        else:
            candidate_generator = generators.sequential_search(args.mnemo_template, custom_wordlist or wordlist)
    # TODO: Add other generator modes here

    # --- Processing Loop ---
    if candidate_generator:
        print("\nStarting mnemonic generation...")
        for i, mnemonic in enumerate(candidate_generator):
            # For now, just print the candidates
            # In the next step, this will be passed to a worker pool
            print(f"  -> Candidate: {mnemonic}")
            if i >= 100: # Limit output for now
                print("...stopping after 100 candidates for this test run.")
                break
    else:
        print("\nNo generation mode selected. Exiting.")

    print("\nArguments parsed successfully.")
    if address_db:
        print("Address database loaded.")
        # Example check:
        # if "14aZB9i8NFiXpeGbS3g7vL7EbNBSWS" in address_db:
        #     print("Test address found in DB!")


if __name__ == "__main__":
    main()
