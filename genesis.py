import hashlib
import binascii
import struct

# Monero Genesis Information
genesis_timestamp = 1577836800  # Unix timestamp for the genesis block
genesis_nonce = 10000           # Nonce for the genesis block
premine_address = "45VirJ4TnTLEhMXY4mVsG1SUWMb8FML2BQ7PGaNMs7TTSQKLNMKqw8j9puJkkE2nk1eCZ3NKBjDfx4MrdTqpte489pvn1tm"  # Address to receive the premine
premine_amount = 1000000000            # Premine amount (in atomic units)

# Monero Genesis Constants
genesis_prev_hash = "0000000000000000000000000000000000000000000000000000000000000000"
genesis_merkle_root = "0000000000000000000000000000000000000000000000000000000000000000"
genesis_difficulty = 1

# Create the Monero genesis block header
genesis_header = struct.pack(
    "<I32s32sIII", genesis_timestamp, bytes.fromhex(genesis_prev_hash),
    bytes.fromhex(genesis_merkle_root), genesis_nonce, genesis_difficulty, premine_amount
)

# Compute the hash of the genesis block header
genesis_hash = hashlib.sha256(hashlib.sha256(genesis_header).digest()).digest()
genesis_hash_hex = binascii.hexlify(genesis_hash[::-1]).decode()

# Print the generated Monero genesis block
print("Genesis Block Information:")
print("Timestamp:", genesis_timestamp)
print("Previous Hash:", genesis_prev_hash)
print("Merkle Root:", genesis_merkle_root)
print("Nonce:", genesis_nonce)
print("Difficulty:", genesis_difficulty)
print("Premine Address:", premine_address)
print("Premine Amount:", premine_amount)
print("Genesis Hash:", genesis_hash_hex)
