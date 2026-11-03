import sys
path, needle = sys.argv[1], sys.argv[2]
s = open(path, encoding="utf-8", errors="ignore").read()
i = 0
n = 0
while n < 8:
    j = s.find(needle, i)
    if j < 0:
        break
    print("\n====", j, "====")
    print(s[max(0, j-180): j+420].replace("\n", " "))
    i = j + len(needle)
    n += 1
print("done", n)
