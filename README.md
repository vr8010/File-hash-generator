🔐 File Hash Generator

A Python command-line tool that generates cryptographic hash values for files to verify file integrity and detect tampering.

📌 Overview

File Hash Generator is a lightweight cybersecurity utility that allows users to generate cryptographic hash values for any file. Hashes are commonly used in security, digital forensics, and software verification to ensure that files have not been modified or corrupted.

This tool supports multiple hashing algorithms and efficiently processes even large files by reading them in chunks.

✨ Features
🔑 Generate MD5, SHA1, and SHA256 hashes
📁 Verify file integrity
📊 Display file size in human-readable format
⚡ Efficient processing of large files
🖥️ Simple command-line interface
🧩 No external dependencies
🛡️ Built-in error handling
🛠️ Installation
1️⃣ Clone the Repository
   ```
git clone https://github.com/vr8010/file-hash-generator.git
cd file-hash-generator
```
2️⃣ Run the Script
```
python hash_generator.py
```
🚀 Usage
Run the program:
```
python hash_generator.py
```
Enter the file path when prompted:
```
Enter file path: test.txt
```
The tool will generate hash values for the file.
```
📷 Example Output
========================================
=== File Hash Generator ===
========================================

Enter file path: test.txt

File Name : test.txt
File Size : 2.1 KB

Generating hashes...
MD5    : 5eb63bbbe01eeed093cb22bb8f5acdc3
SHA1   : 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed
SHA256 : b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
```
⚙️ Requirements
```
Python 3.6+
```
Uses only Python Standard Library
🧠 How It Works

The tool uses Python’s hashlib module to generate cryptographic hashes.

Algorithm	Bit Length	Hex Length	Use Case
MD5	128-bit	32 chars	Basic file verification
SHA1	160-bit	40 chars	Legacy verification
SHA256	256-bit	64 chars	Secure file validation

To efficiently handle large files, the program reads the file in 8KB chunks instead of loading the entire file into memory.

💡 Use Cases
Verify file integrity after download
Detect file tampering or corruption
Compare files for equality
Digital forensics and security auditing
Learning cryptographic hashing concepts
⚠️ Disclaimer

This tool is intended for educational and legitimate security purposes only.
Always ensure you have proper authorization before analyzing files.

                                    
🤝 Contributing

Contributions are welcome!

If you’d like to improve this project:

Fork the repository
Create a new branch
Submit a Pull Request
📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Vishal Rathod

GitHub:
```
https://github.com/vr8010
```
