# Password-Strength-Analyzer
A tool to check the strength of password.

# 🔐 Ultimate Password Security Playground

An interactive, client-side security tool and educational playground that analyzes password strength and visually explains modern cryptographic concepts like Salting, Peppering, and Hashing.

Unlike standard password meters that rely on outdated Regex rules (requiring symbols and uppercase letters), this tool uses modern NIST guidelines and dictionary-matching to teach users *why* passphrases are secure.

## ✨ Features

* 🧠 **Intelligent Analysis:** Powered by Dropbox's `zxcvbn` engine to detect dictionary words, common names, predictable patterns, and spatial keyboard walks (like "qwerty").
* 🎲 **Passphrase Generator:** One-click generation of strong, memorable, multi-word passphrases (Diceware style).
* 🎓 **Interactive Educational Visualizer:** As you type, watch how a modern server secures your password using:
  * **Salts:** Unique random strings added to prevent rainbow table attacks.
  * **Peppers:** Secret application-level keys hidden from the database.
  * **Hashes:** Simulating algorithms like bcrypt or Argon2.
* 🚨 **Reuse Prevention Simulator:** Checks inputs against a mock database to demonstrate how systems prevent users from recycling compromised passwords.
* 🎨 **Modern Glassmorphism UI:** Features dynamic gradient backgrounds, segmented strength meters, shake animations for errors, and a confetti reward for achieving maximum security.

## 🛠️ Tech Stack

This project is built to be lightweight and accessible with zero build steps.

* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Security Logic:** [`zxcvbn`](https://github.com/dropbox/zxcvbn) (via CDN)
* **Animations:** `canvas-confetti` (via CDN)

## 🚀 Quick Start

Because this tool is entirely client-side, you don't need Node.js, npm, or a server to run it.

1. Clone the repository:
   ```bash
   git clone https://github.com/Nisha-research/Password-Strength-Analyzer.git
