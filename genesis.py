import hashlib
import datetime
import struct

def generate_genesis_block(timestamp, premine_amount, premine_address):
    # Define the initial values
    version = 1
    prev_block_hash = "0" * 64  # Assuming this is the first block
    merkle_root = "0" * 64  # Placeholder value for the merkle root
    difficulty = 1
    nonce = 100
    target = 2 ** 240 // difficulty  # Calculate the target value for PoW verification

    # Create the coinbase transaction for the premine
    coinbase_tx = f"Reward: {premine_amount} XMR to {premine_address}"

    # Construct the block template
    block_template = struct.pack("<I", version)
    block_template += bytes.fromhex(prev_block_hash)
    block_template += bytes.fromhex(merkle_root)
    block_template += struct.pack("<Q", int(timestamp.timestamp()))
    block_template += struct.pack("<I", difficulty)
    block_template += struct.pack("<Q", nonce)
    block_template += struct.pack("<Q", target)
    block_template += coinbase_tx.encode()

    # Hash the block template
    block_hash = hashlib.sha256(block_template).digest()
    block_hash = hashlib.sha256(block_hash).digest()
    block_hash_hex = block_hash[::-1].hex()

    # Create the genesis block by combining the block hash and coinbase transaction
    genesis_block = f"Block Hash: {block_hash_hex}\nCoinbase TX: {coinbase_tx}"

    return genesis_block

# Example usage
timestamp = datetime.datetime(2023, 6, 10)  # Replace with the desired timestamp
premine_amount = 1000000000  # Adjust this value as needed
premine_address = "45VirJ4TnTLEhMXY4mVsG1SUWMb8FML2BQ7PGaNMs7TTSQKLNMKqw8j9puJkkE2nk1eCZ3NKBjDfx4MrdTqpte489pvn1tm"  # Replace with the desired premine address

genesis_block = generate_genesis_block(timestamp, premine_amount, premine_address)
print(genesis_block)
