import re, sys
s = open(sys.argv[1], encoding="utf-8", errors="ignore").read()
urls = set(re.findall(r"https?://[^\"'\s)]+", s))
paths = set(re.findall(r'"(/[a-zA-Z0-9_\-./]{3,80})"', s))
print("URLS")
for u in sorted(urls):
    print(u)
print("---PATHS---")
for p in sorted(paths):
    if any(k in p for k in ("api", "quote", "market", "asset", "metadata", "price", "config")):
        print(p)
