#!/usr/bin/env python3
import json
import random
import string
import webbrowser
import sys

class URLShortener:
    def __init__(self, db_file="urls.json"):
        self.db_file = db_file
        self.urls = self.load_urls()
    
    def load_urls(self):
        """Load saved URLs from file"""
        try:
            with open(self.db_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def save_urls(self):
        """Save URLs to file"""
        with open(self.db_file, 'w') as f:
            json.dump(self.urls, f, indent=2)
    
    def generate_short_code(self, length=6):
        """Generate random short code"""
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
    
    def shorten_url(self, long_url):
        """Create short URL from long URL"""
        # Check if URL already exists
        for code, url in self.urls.items():
            if url == long_url:
                return f"https://urlshorr.com/{code}"
        
        # Generate new short code
        short_code = self.generate_short_code()
        while short_code in self.urls:
            short_code = self.generate_short_code()
        
        # Save to database
        self.urls[short_code] = long_url
        self.save_urls()
        
        return f"https://urlshorr.com/{short_code}"
    
    def expand_url(self, short_code):
        """Get original URL from short code"""
        return self.urls.get(short_code, None)
    
    def open_url(self, short_code):
        """Open the original URL in browser"""
        long_url = self.expand_url(short_code)
        if long_url:
            print(f"\n[*] Opening: {long_url}")
            webbrowser.open(long_url)
            return True
        else:
            print(f"\n[!] Invalid short code: {short_code}")
            return False
    
    def list_all_urls(self):
        """Show all shortened URLs"""
        if not self.urls:
            print("\n[!] No URLs found")
            return
        
        print("\n" + "="*60)
        print("   YOUR SHORTENED URLs")
        print("="*60)
        for code, url in self.urls.items():
            print(f"https://urlshorr.com/{code}")
            print(f"  └─ {url[:60]}...")
            print()

def main():
    shortener = URLShortener()
    
    print("="*50)
    print("   URL SHORTENER - urlshorr")
    print("="*50)
    
    while True:
        print("\nOptions:")
        print("1. Shorten a URL")
        print("2. Open short URL")
        print("3. List all URLs")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            long_url = input("Enter long URL: ").strip()
            # Add https:// if missing
            if not long_url.startswith(('http://', 'https://')):
                long_url = 'https://' + long_url
            short_url = shortener.shorten_url(long_url)
            print(f"\n✅ Short URL: {short_url}")
            print(f"   Original: {long_url[:50]}...")
        
        elif choice == '2':
            short_code = input("Enter short code (e.g., AbC123): ").strip()
            shortener.open_url(short_code)
        
        elif choice == '3':
            shortener.list_all_urls()
        
        elif choice == '4':
            print("\n✅ Goodbye!")
            break
        
        else:
            print("\n[!] Invalid choice")

if __name__ == "__main__":
    # Command line support
    if len(sys.argv) > 1:
        shortener = URLShortener()
        short_code = sys.argv[1].replace("https://urlshorr.com/", "")
        shortener.open_url(short_code)
    else:
        main()
