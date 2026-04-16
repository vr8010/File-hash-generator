#!/usr/bin/env python3
"""
File Hash Generator
A command-line tool for generating cryptographic hash values for files.
"""

import hashlib
import os
import sys


def calculate_file_hash(file_path, hash_algorithm):
    """
    Calculate hash for a given file using specified algorithm.
    
    Args:
        file_path: Path to the file
        hash_algorithm: Hash algorithm object (md5, sha1, sha256)
    
    Returns:
        Hexadecimal hash string
    """
    hash_obj = hash_algorithm()
    
    try:
        with open(file_path, 'rb') as file:
            # Read file in chunks to handle large files efficiently
            while chunk := file.read(8192):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def format_file_size(size_bytes):
    """
    Convert bytes to human-readable format.
    
    Args:
        size_bytes: File size in bytes
    
    Returns:
        Formatted string (e.g., "2.1 KB")
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"


def generate_hashes(file_path):
    """
    Generate MD5, SHA1, and SHA256 hashes for a file.
    
    Args:
        file_path: Path to the file
    """
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"\n❌ Error: File '{file_path}' not found!")
        return
    
    if not os.path.isfile(file_path):
        print(f"\n❌ Error: '{file_path}' is not a file!")
        return
    
    # Get file information
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    
    print(f"\nFile Name : {file_name}")
    print(f"File Size : {format_file_size(file_size)}")
    print()
    
    # Generate hashes
    print("Generating hashes...")
    
    md5_hash = calculate_file_hash(file_path, hashlib.md5)
    sha1_hash = calculate_file_hash(file_path, hashlib.sha1)
    sha256_hash = calculate_file_hash(file_path, hashlib.sha256)
    
    if md5_hash and sha1_hash and sha256_hash:
        print(f"MD5    : {md5_hash}")
        print(f"SHA1   : {sha1_hash}")
        print(f"SHA256 : {sha256_hash}")
    else:
        print("\n❌ Failed to generate hashes.")


def main():
    """Main function to run the File Hash Generator."""
    print("=" * 40)
    print("=== File Hash Generator ===")
    print("=" * 40)
    
    try:
        # Get file path from user
        file_path = input("\nEnter file path: ").strip()
        
        if not file_path:
            print("\n❌ Error: No file path provided!")
            sys.exit(1)
        
        # Generate and display hashes
        generate_hashes(file_path)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        sys.exit(1)
    

if __name__ == "__main__":
    main()
