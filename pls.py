import tkinter as tk
from tkinter import ttk, messagebox
import re
import requests
from urllib.parse import urlparse
import whois
from datetime import datetime

class PhishingScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Phishing Link Scanner")
        self.root.geometry("500x500")
        
        # Configure styles
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat")
        
        # Title
        title = tk.Label(root, text="🔍 Phishing Link Scanner", 
                        font=("Arial", 16, "bold"), fg="#2c3e50")
        title.pack(pady=20)
        
        # Input frame
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Enter URL:", font=("Arial", 10)).pack(side=tk.LEFT)
        self.url_entry = tk.Entry(input_frame, width=40, font=("Arial", 10))
        self.url_entry.pack(side=tk.LEFT, padx=10)
        self.url_entry.insert(0, "https://")
        
        # Scan button
        scan_btn = ttk.Button(root, text="Scan URL", command=self.scan_url, style="TButton")
        scan_btn.pack(pady=10)
        
        # Results text area
        self.result_text = tk.Text(root, height=15, width=60, font=("Consolas", 9))
        self.result_text.pack(pady=10, padx=20)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(root, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)
    
    def scan_url(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL")
            return
            
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Scanning: {url}\n")
        self.result_text.insert(tk.END, "="*50 + "\n")
        
        try:
            score = 0
            checks = []
            
            # Check 1: URL structure
            if not re.match(r'^https?://', url):
                score += 20
                checks.append("⚠️  No HTTPS protocol")
            
            # Check 2: IP address in URL
            if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url):
                score += 30
                checks.append("⚠️  Contains IP address")
            
            # Check 3: Shortened URL
            shorteners = ['bit.ly', 'tinyurl', 'goo.gl', 'ow.ly', 'is.gd', 'buff.ly', 'adf.ly']
            parsed = urlparse(url)
            if any(short in parsed.netloc for short in shorteners):
                score += 15
                checks.append("⚠️  Uses URL shortener")
            
            # Check 4: Suspicious keywords
            suspicious = ['login', 'verify', 'secure', 'account', 'banking', 'paypal', 'update']
            if any(word in url.lower() for word in suspicious):
                score += 10
                checks.append("⚠️  Contains suspicious keywords")
            
            # Check 5: Too many subdomains
            if parsed.netloc.count('.') > 3:
                score += 25
                checks.append("⚠️  Too many subdomains")
            
            # Check 6: Domain age (if available)
            try:
                domain_info = whois.whois(parsed.netloc)
                if domain_info.creation_date:
                    creation = domain_info.creation_date[0] if isinstance(domain_info.creation_date, list) else domain_info.creation_date
                    age = (datetime.now() - creation).days
                    if age < 30:
                        score += 35
                        checks.append(f"⚠️  New domain ({age} days old)")
            except:
                pass
            
            # Display results
            self.result_text.insert(tk.END, f"\nRisk Score: {score}/100\n")
            self.result_text.insert(tk.END, f"Status: {'⚠️ HIGH RISK' if score > 50 else '✅ Likely Safe' if score < 20 else '⚠️ Caution Advised'}\n\n")
            
            if checks:
                self.result_text.insert(tk.END, "Issues Found:\n")
                for check in checks:
                    self.result_text.insert(tk.END, f"  • {check}\n")
            else:
                self.result_text.insert(tk.END, "✅ No suspicious patterns detected\n")
            
            # Safety tips
            self.result_text.insert(tk.END, "\n" + "="*50 + "\n")
            self.result_text.insert(tk.END, "Safety Tips:\n")
            tips = [
                "• Check for HTTPS padlock",
                "• Verify domain spelling",
                "• Don't enter credentials on suspicious sites",
                "• Use 2FA when possible",
                "• Report phishing attempts"
            ]
            for tip in tips:
                self.result_text.insert(tk.END, f"  {tip}\n")
                
        except Exception as e:
            messagebox.showerror("Error", f"Scan failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhishingScannerGUI(root)
    root.mainloop()