from rbloom import BloomFilter

class AddressDatabase:
    """
    Manages a database of addresses for fast lookups using a Bloom filter.
    """
    def __init__(self, capacity=1_000_000_000, error_rate=1e-9):
        """
        Initializes the AddressDatabase.

        Args:
            capacity (int): The estimated number of addresses to be stored.
            error_rate (float): The desired false positive rate.
        """
        print(f"Initializing Bloom filter with capacity={capacity} and error_rate={error_rate}...")
        self._bloom_filter = BloomFilter(capacity=capacity, error_rate=error_rate)

    def load_from_text_file(self, filepath: str):
        """
        Loads addresses from a text file, one per line, into the Bloom filter.
        """
        print(f"Loading addresses from {filepath}...")
        count = 0
        with open(filepath, 'r') as f:
            for line in f:
                address = line.strip()
                if address:
                    self._bloom_filter.add(address)
                    count += 1
        print(f"Loaded {count} addresses into the Bloom filter.")

    def __contains__(self, address: str) -> bool:
        """
        Checks if an address is likely in the database using the Bloom filter.
        """
        return address in self._bloom_filter
