 #  Crypto Tool – Personal Cryptography Toolkit

This project is a Python-based cryptography toolkit developed for learning and practicing fundamental concepts in IT Security and classical encryption.

It includes encryption, decryption, analysis, and basic cryptanalysis techniques.

---

## Project Structure

crypto-tool/
│
├── crypto_tool.py # Main CLI menu
├── ciphers.py # Caesar & Vigenère implementations
├── attack.py # Brute force attack tools
├── analyzer.py # Cipher detection logic
├── logger.py # Logging system
├── exporter.py # Result exporting
└── results.txt # Output logs

---

##  Features

### 🔐 Encryption Algorithms
- Caesar Cipher (shift-based substitution)
- Vigenère Cipher (polyalphabetic substitution)

### 🔍 Analysis Tools
- Basic cipher detection (heuristic-based)

### 🧨 Attack Tools
- Brute force attack for Caesar cipher

### 📊 System Features
- Interactive CLI menu
- Continuous execution loop
- Logging of operations
- Result export system

---

## ⚙️ How to Run

```bash id="r4"
python3 crypto_tool.py

Caesar Cipher
Input: hello
Key: 3
Output: khoor
Vigenère Cipher
Input: hello
Key: security
Output: encrypted text

Learning Objectives
Understand classical cryptographic algorithms
Learn symmetric encryption concepts
Practice modular programming in Python
Implement basic cryptanalysis techniques
Work with CLI-based applications


Future Improvements
Automatic cipher detection (AI-based heuristic improvement)
Frequency analysis for stronger cryptanalysis
GUI version (Tkinter)
Export to CSV/JSON
Advanced Vigenère cracking


👩‍💻 Author

Ornella Mesina
IT Security Student – UAS Frankfurt