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
   cd Password-Strength-Analyzer
   ```
2. Open `/home/runner/work/Password-Strength-Analyzer/Password-Strength-Analyzer/analyze.html` directly in a modern browser.

## 📱 Responsive Browser Notes

- The UI is mobile-first and adapts for phones, tablets, laptops, and wide desktop screens.
- On narrow devices, content stacks vertically and the mock database table scrolls horizontally inside its card.
- For best results, use an up-to-date Chromium, Firefox, or Safari browser.

## ☁️ Streamlit Community Cloud Deployment

This repository includes a Streamlit wrapper so the same HTML app can be hosted on Streamlit Community Cloud.

1. Push your code to GitHub.
2. In Streamlit Community Cloud, choose:
   - **Repository:** `Nisha-research/Password-Strength-Analyzer`
   - **Branch:** `main`
   - **Main file path:** `app.py`
3. Deploy.

Local Streamlit run:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## 🔒 Demo Security Note

- Pepper values shown in the educational visualizer are illustrative placeholders only.
- Real application peppers are secrets and must remain server-side (not in browser code and not in source control).
- This project does not send passwords to a server; all analysis runs in-browser.
