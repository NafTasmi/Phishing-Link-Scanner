# Phishing Link Scanner 🔍

A Python-based desktop application that scans URLs for potential phishing threats using multiple detection techniques. This tool provides a user-friendly graphical interface for analyzing suspicious links in real-time.

## Features ✨

### **URL Analysis Checks**
- ✅ HTTPS protocol validation
- ✅ IP address detection in URLs
- ✅ URL shortener identification
- ✅ Suspicious keyword scanning
- ✅ Subdomain count analysis
- ✅ Domain age verification via WHOIS lookup

### **User Interface**
- 🎯 Clean and intuitive Tkinter GUI
- 🔍 Real-time scanning with visual feedback
- 📊 Risk scoring system (0-100 scale)
- 📝 Detailed issue reporting
- 💡 Safety tips and recommendations

## Screenshot 🖼️

```
┌─────────────────────────────────────────────┐
│      🔍 Phishing Link Scanner              │
│                                             │
│  Enter URL: [https://_________________]    │
│                                             │
│              [ Scan URL ]                   │
│                                             │
│  Scanning: https://example.com              │
│  ====================================      │
│                                             │
│  Risk Score: 25/100                         │
│  Status: ⚠️ Caution Advised                │
│                                             │
│  Issues Found:                              │
│    • ⚠️ Contains suspicious keywords        │
│                                             │
└─────────────────────────────────────────────┘
```

## Installation ⚙️

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step-by-Step Setup
```bash
# 1. Clone the repository
git clone https://github.com/yourusername/phishing-link-scanner.git
cd phishing-link-scanner

# 2. Install required packages
pip install -r requirements.txt
```

### Required Packages
Create a `requirements.txt` file with:
```
requests>=2.28.0
python-whois>=0.9.0
```

## Usage 🚀

1. **Launch the application:**
```bash
python pls.py
```

2. **Enter a URL** in the input field (starts with `https://` by default)

3. **Click "Scan URL"** to initiate analysis

4. **Review results** including:
   - Risk score and status
   - Detected issues
   - Safety recommendations

## How It Works 🔬

### Detection Algorithm
The scanner uses a weighted scoring system based on phishing indicators:

| Check | Weight | Description |
|-------|--------|-------------|
| No HTTPS | 20 points | Missing secure protocol |
| IP Address | 30 points | Direct IP instead of domain |
| URL Shortener | 15 points | Known shortening services |
| Suspicious Keywords | 10 points | Common phishing terms |
| Excessive Subdomains | 25 points | More than 3 subdomains |
| New Domain | 35 points | Registered <30 days ago |

### Risk Classification
- **0-19**: ✅ Likely Safe
- **20-50**: ⚠️ Caution Advised  
- **51-100**: ⚠️ HIGH RISK

## Project Structure 📁

```
phishing-link-scanner/
│
├── pls.py                    # Main application file
├── README.md                 # This documentation
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
└── examples/
    ├── test_urls.txt        # Sample URLs for testing
    └── screenshots/         # Application screenshots
```

## Example Output 📋

```text
Scanning: https://secure-paypal-login.verify-account.com
==================================================
Risk Score: 80/100
Status: ⚠️ HIGH RISK

Issues Found:
  • ⚠️ Contains suspicious keywords
  • ⚠️ Too many subdomains
  • ⚠️ New domain (5 days old)

Safety Tips:
  • Check for HTTPS padlock
  • Verify domain spelling
  • Don't enter credentials on suspicious sites
  • Use 2FA when possible
  • Report phishing attempts
```

## Limitations ⚠️

- **Basic Detection**: Uses heuristic rules, not machine learning
- **No Real-time Blacklist**: Doesn't query live phishing databases
- **False Positives**: New legitimate sites may be flagged
- **Limited Scope**: Desktop-only, no API or web service

## Future Enhancements 🚧

Planned features for upcoming versions:
- [ ] Integration with VirusTotal API
- [ ] Google Safe Browsing support
- [ ] Machine learning classification
- [ ] Email scanning capability
- [ ] Browser extension version
- [ ] Report export (PDF/CSV)

## Contributing 🤝

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Security Note 🔒

⚠️ **Disclaimer**: This tool is for educational purposes only. It may produce false positives/negatives. Always verify suspicious links through multiple sources before taking action.


---

*⭐ If you found this project useful, please consider giving it a star!*
