🔗 URLShorr

**URLShorr** - A simple URL shortener tool that converts long URLs into short, shareable links.

## Quick Start

```bash
#for installation
pkg install git
git clone https://github.com/gourav286-code/Urlshorr.git
# Run the tool
python main.py

# Open a short URL directly
python main.py AbC123


```

Features

· Convert long URLs to 6-character short links
· Automatically open links in your browser
· Save all URLs in JSON file (no data loss)
· List all your shortened URLs
· No external dependencies needed

How to Use

```
1. Shorten URL → Paste long URL → Get short link
2. Open Short URL → Enter short code → Browser opens
3. List URLs → View all saved URLs
4. Exit → Close the tool
```

Requirements

· Python 3.6 or higher
· No pip install needed (uses only built-in modules)

Storage

urls.json file is automatically created to store all your URL mappings.

Example

```
Input:  https://amazon.in/s?k=laptop&crid=2M3D3KZQJ8P5L
Output: https://urlshorr.com/XyZ789
```

Project Structure

```
urlshorr/
├── main.py      (Main application)
├── urls.json    (Database - auto created)
└── README.md    (This file)
```

License

MIT License - Free for everyone

---

Made with Python
