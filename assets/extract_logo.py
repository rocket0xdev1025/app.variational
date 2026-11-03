html = open("shots/dom.html", encoding="utf-8").read()
needle = 'aria-label="Variational Omni"'
i = html.find(needle)
s = html.rfind("<svg", 0, i)
e = html.find("</svg>", i) + 6
svg = html[s:e]
svg = svg.replace(' class="h-[19px] shrink-0"', "")
open("logo-wordmark.svg", "w", encoding="utf-8").write(svg)
print(len(svg))
