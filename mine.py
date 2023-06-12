import hashlib
import datetime

def generate_genesis_block(timestamp, premine_amount, premine_address):
    version = 1
    prev_block_hash = "0" * 64  # Assuming this is the first block
    merkle_root = "0" * 64  # Placeholder value for the merkle root
    difficulty = 1
    nonce = 10000

    # Create the coinbase transaction for the premine
    coinbase_tx = f"Reward: {premine_amount} XTE to {premine_address}"

    # Create the genesis block header
    block_header = f"{version}{prev_block_hash}{merkle_root}{timestamp}{difficulty}{nonce}"

    # Hash the block header
    block_hash = hashlib.sha256(block_header.encode()).hexdigest()

    # Create the genesis block by combining the block hash and coinbase transaction
    genesis_block = f"Block Hash: {block_hash}\nCoinbase TX: {coinbase_tx}"

    return genesis_block

# Example usage
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
premine_amount = 1000000000  # Adjust this value as needed
premine_address = "45VirJ4TnTLEhMXY4mVsG1SUWMb8FML2BQ7PGaNMs7TTSQKLNMKqw8j9puJkkE2nk1eCZ3NKBjDfx4MrdTqpte489pvn1tm"  # Replace with the desired premine address

genesis_block = generate_genesis_block(timestamp, premine_amount, premine_address)
print(genesis_block)
