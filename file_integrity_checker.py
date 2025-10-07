import hashlib

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# 📍 Step 1: Get file path from user
file_path = input("Enter the file path to verify: ")

# 📍 Step 2: Ask for original hash
original_hash = input("Enter the original SHA256 hash: ")

# 📍 Step 3: Calculate current hash
current_hash = calculate_hash(file_path)

# 📍 Step 4: Compare
if current_hash == original_hash:
    print("✅ File is INTACT. No changes detected.")
else:
    print("⚠️ WARNING: File has been MODIFIED or TAMPERED!")
