# 🔐 Caesar Cipher Breaker with Frequency Analysis

A Python project that demonstrates how frequency analysis can be used to assist in breaking a Caesar Cipher. The project combines text preprocessing, character frequency analysis, data visualization, and brute-force decryption.

## 📌 Overview

The Caesar Cipher is one of the oldest encryption techniques, where each letter is shifted by a fixed number of positions in the alphabet.

This project automates the process of:

* Reading an encrypted text;
* Cleaning and preprocessing the data;
* Counting the frequency of each character;
* Visualizing the character distribution;
* Testing all 26 possible Caesar Cipher keys.

The project was developed as a practical way to improve my Python skills while exploring a classic cryptography problem.

---

## 🚀 Features

* Text preprocessing
* Character frequency analysis
* Data visualization using Matplotlib
* Data manipulation with Pandas
* Brute-force Caesar Cipher decryption
* Modular project structure

---

## 📂 Project Structure

```text
.
├── texto.py          # Encrypted text
├── analise1.py       # Text preprocessing
├── frequencia2.py    # Frequency analysis and visualization
└── cifra3.py         # Caesar Cipher brute-force decryption
```

---

## ⚙️ How it works

### 1. Text preprocessing

The script reads the encrypted text and removes every character except letters and spaces. All letters are converted to lowercase to standardize the analysis.

### 2. Frequency analysis

Each character is counted and stored in a dictionary.

The frequency data is then converted into a Pandas DataFrame and displayed as a bar chart using Matplotlib.

### 3. Brute-force decryption

Since a Caesar Cipher has only 26 possible keys, the script generates every possible decryption and prints the result for each key.

The correct plaintext can then be identified by inspecting the generated outputs.

---

## 🛠 Technologies

* Python
* Pandas
* Matplotlib

---

## 📈 Future Improvements

This project is still evolving. Planned improvements include:

* Automatic key detection using English letter frequency analysis;
* Ranking candidate decryptions;
* Support for larger text files;
* Exporting decrypted text to a file;
* Improved project organization.

---

## 🎯 Learning Objectives

This project was created to practice:

* File handling
* Functions
* Loops
* Dictionaries
* Modular programming
* Data analysis with Pandas
* Data visualization with Matplotlib
* Basic cryptography concepts

---

## 👨‍💻 Author

Developed by **Carlos Daniel** as a personal project to practice Python and explore classical cryptography techniques.
