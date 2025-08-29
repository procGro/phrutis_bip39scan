import hashlib
import base58
from bip32 import BIP32
from coincurve.keys import PrivateKey, PublicKey
from pybip39 import Mnemonic
from eth_hash.auto import keccak

def mnemonic_to_seed(mnemonic_phrase: str, passphrase: str = "") -> bytes:
    """
    Converts a BIP39 mnemonic phrase to a seed.
    """
    seed = Mnemonic.to_seed(mnemonic_phrase, passphrase)
    return seed

def derive_private_key(seed: bytes, path: str) -> PrivateKey:
    """
    Derives a private key from a seed and a BIP32 derivation path.
    """
    # Create a BIP32 object from the seed
    bip32_key = BIP32.from_seed(seed)

    # Derive the key using the path
    derived_key = bip32_key.get_privkey_from_path(path)

    # Return a coincurve PrivateKey object
    return PrivateKey(derived_key)

def generate_eth_address(private_key: PrivateKey) -> str:
    """
    Generates an EIP-55 checksummed Ethereum address from a private key.
    """
    # Get the public key from the private key
    public_key = private_key.public_key

    # Get the uncompressed public key, remove the 0x04 prefix
    uncompressed_pub = public_key.format(compressed=False)[1:]

    # Hash the public key with Keccak-256
    address_hash = keccak(uncompressed_pub)

    # Take the last 20 bytes of the hash
    address_bytes = address_hash[-20:]
    address = address_bytes.hex()

    # EIP-55 Checksum
    address_hash_hex = keccak(address.encode('utf-8')).hex()
    checksum_address = "0x"

    for i, char in enumerate(address):
        if int(address_hash_hex[i], 16) >= 8:
            checksum_address += char.upper()
        else:
            checksum_address += char

    return checksum_address

def hash160(pub_key_bytes: bytes) -> bytes:
    """Computes the RIPEMD160(SHA256(b)) of a byte sequence."""
    return hashlib.new('ripemd160', hashlib.sha256(pub_key_bytes).digest()).digest()

def generate_btc_address(private_key: PrivateKey, address_type: str = 'P2PKH') -> str:
    """
    Generates a Bitcoin address from a private key for various address types.
    """
    public_key = private_key.public_key

    if address_type == 'P2PKH':
        pub_key_bytes = public_key.format(compressed=True)
        hashed_pub_key = hash160(pub_key_bytes)
        # P2PKH mainnet address has version byte 0x00
        return base58.b58encode_check(b'\x00' + hashed_pub_key)

    elif address_type == 'P2PKH_UNCOMPRESSED':
        pub_key_bytes = public_key.format(compressed=False)
        hashed_pub_key = hash160(pub_key_bytes)
        # P2PKH mainnet address has version byte 0x00
        return base58.b58encode_check(b'\x00' + hashed_pub_key)

    elif address_type == 'P2SH': # P2WPKH-nested-in-P2SH
        pub_key_bytes = public_key.format(compressed=True)
        hashed_pub_key = hash160(pub_key_bytes)
        # Script is 0x0014{20-byte-key-hash}
        redeem_script = b'\x00\x14' + hashed_pub_key
        script_hash = hash160(redeem_script)
        # P2SH mainnet address has version byte 0x05
        return base58.b58encode_check(b'\x05' + script_hash)

    elif address_type == 'bech32': # P2WPKH
        pub_key_bytes = public_key.format(compressed=True)
        hashed_pub_key = hash160(pub_key_bytes)
        # Witness program is version 0
        witness_version = 0
        # Mainnet HRP is 'bc'
        return bech32.encode('bc', witness_version, hashed_pub_key)

    else:
        raise ValueError(f"Unknown address type: {address_type}")
