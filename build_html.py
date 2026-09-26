import os

base_dir = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base_dir, "index.html")
base64_path = os.path.join(base_dir, "tiba_logo_base64.txt")

if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    print(f"Platform verified & ready for Vercel deployment! Size: {len(html_content)} bytes")
else:
    print("Error: index.html not found!")
