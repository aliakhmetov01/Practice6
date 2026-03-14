from functools import reduce
import re

games = [
    "Mobile Legends: free",
    "Standoff2: free",
    "Minecraft: paid",
    "Geometry dash: paid",
    "clash royal: free"
]
pat = r"[^:]+"
f_g_names = []
free_games = list(filter(lambda x: "free" in x, games))
for i in free_games:
    match_names = re.search(pat, i)
    f_g_names.append(match_names.group())

upper_names = list(map(str.upper, f_g_names))
for name in upper_names:
    print(f"Free Games: {name}")