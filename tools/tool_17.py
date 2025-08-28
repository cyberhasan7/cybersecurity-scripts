```python
import os
import hashlib

def calculate_file_hash(file_path, hash_algorithm='sha256'):
    """
    Calculate the hash of a file.

    :param file_path: Path to the file to hash.
    :param hash_algorithm: Hash algorithm to use (default is sha256).
    :return: Hexadecimal hash string.
    """
    hash_func = None

    # Select the hash function based on user input
    if hash_algorithm == 'md5':
        hash_func = hashlib.md5()
    elif hash_algorithm == 'sha1':
        hash_func = hashlib.sha1()
    elif hash_algorithm == 'sha256':
        hash_func = hashlib.sha256()
    elif hash_algorithm == 'sha512':
        hash_func = hashlib.sha512()
    else:
        raise ValueError("Unsupported hash algorithm. Use 'md5', 'sha1', 'sha256', or 'sha512'.")

    # Read the file and update the hash
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")

    return hash_func.hexdigest()

def verify_file_integrity(file_path, expected_hash, hash_algorithm='sha256'):
    """
    Verify the integrity of a file by comparing its hash to an expected hash.

    :param file_path: Path to the file to verify.
    :param expected_hash: Expected hash string to compare against.
    :param hash_algorithm: Hash algorithm used to calculate the file's hash.
    :return: True if the hashes match, False otherwise.
    """
    calculated_hash = calculate_file_hash(file_path, hash_algorithm)
    return calculated_hash == expected_hash

if __name__ == "__main__":
    # Example usage of the tool
    file_path = 'example.txt'  # Change this to the file you want to hash or verify
    hash_algorithm = 'sha256'   # You can choose 'md5', 'sha1', 'sha256', or 'sha512'

    # Calculate the hash of the file
    try:
        file_hash = calculate_file_hash(file_path, hash_algorithm)
        print(f"The {hash_algorithm} hash of the file '{file_path}' is: {file_hash}")
    except Exception as e:
        print(e)

    # Example expected hash for verification (replace with actual expected hash)
    expected_hash = 'your_expected_hash_here'  # Update with the correct hash for verification

    # Verify file integrity
    is_verified = verify_file_integrity(file_path, expected_hash, hash_algorithm)
    if is_verified:
        print(f"The file '{file_path}' is intact and matches the expected hash.")
    else:
        print(f"The file '{file_path}' has been altered or does not match the expected hash.")
```

This Python script provides a simple tool for calculating and verifying file hashes using specified algorithms (MD5, SHA-1, SHA-256, SHA-512). It includes error handling, comments for clarity, and an example usage block to demonstrate functionality.
# Commit version 15