import re
import sys

path = sys.argv[1]
out = sys.argv[2]
s = open(path, encoding="utf-8", errors="ignore").read()
print("len", len(s))
strs = re.findall(r'"((?:\\.|[^"\\]){2,120})"', s)
seen = set()
out_lines = []
for x in strs:
    if x in seen:
        continue
    seen.add(x)
    if re.search(r"[A-Za-z]", x):
        out_lines.append(x)
print("strings", len(out_lines))
open(out, "w", encoding="utf-8").write("\n".join(out_lines))
