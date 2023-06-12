import hashlib
import binascii
import struct
from monero.wallet import address as monero_address

# Monero Genesis Information
genesis_timestamp = 1577836800  # Unix timestamp for the genesis block
genesis_nonce = 10000           # Nonce for the genesis block
premine_address = "45VirJ4TnTLEhMXY4mVsG1SUWMb8FML2BQ7PGaNMs7TTSQKLNMKqw8j9puJkkE2nk1eCZ3NKBjDfx4MrdTqpte489pvn1tm"  # Address to receive the premine
premine_amount = 1000000000            # Premine amount (in atomic units)

# Monero Genesis Constants
genesis_prev_hash = "0000000000000000000000000000000000000000000000000000000000000000"
genesis_merkle_root = "0000000000000000000000000000000000000000000000000000000000000000"
genesis_difficulty = 1

# Convert Monero address from Base58 to hexadecimal
decoded_address = monero_address.decode(premine_address)
hex_address = binascii.hexlify(decoded_address.to_binary()).decode()

# Create the genesis transaction structure
tx_version = 1
tx_unlock_time = 0
tx_vin = struct.pack("<Q", 0)  # Number of transaction inputs (always 0)
tx_vout = struct.pack("<Q", 1)  # Number of transaction outputs (always 1)

# Create the transaction output
tx_output_amount = struct.pack("<Q", premine_amount)
tx_output_script_size = struct.pack("<B", len(hex_address))
tx_output_script = binascii.unhexlify(hex_address.encode())

# Compute the hash of the transaction structure
tx_structure_hash = hashlib.sha256(
    struct.pack("<II", tx_version, tx_unlock_time) + tx_vin + tx_vout +
    tx_output_amount + tx_output_script_size + tx_output_script
).digest()

# Create the Monero genesis block header
genesis_header = struct.pack(
    "<I32s32sIII", genesis_timestamp, bytes.fromhex(genesis_prev_hash),
    bytes.fromhex(genesis_merkle_root), genesis_nonce, genesis_difficulty, len(tx_structure_hash)
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
print()
print("Genesis Transaction Information:")
print("Version:", tx_version)
print("Unlock Time:", tx_unlock_time)
print("Input Count:", struct.unpack("<Q", tx_vin)[0])
print("Output Count:", struct.unpack("<Q", tx_vout)[0])
print("Output Amount:", struct.unpack("<Q", tx_output_amount)[0])
print("Output Script Size:", struct.unpack("<B", tx_output_script_size)[0])
print("Output Script:", binascii.hexlify(tx_output_script).decode())
