import sys
sys.path.insert(0, "/tmp/futuristic2")
from common import chrome_shell, esc, CYAN, MAGENTA, PURPLE, DIM, FAINT, LINE

width = 720
top_h = 34
pad_left = 26
y0 = 14 + top_h + 34

row1 = ["LINUX", "WINDOWS", "PYTHON", "SQL", "GIT", "GITHUB"]
row2 = ["SERVICENOW", "ITIL", "ACTIVE DIRECTORY", "VMWARE"]
row3 = ["TCP/IP - DNS - VPN", "PHISHING & MALWARE ANALYSIS"]

def chip_row(items, y, color):
    parts = []
    x = pad_left
    h = 26
    for item in items:
        w = len(item) * 7.3 + 26
        parts.append(f'  <rect x="{x:.1f}" y="{y-18}" width="{w:.1f}" height="{h}" rx="6" fill="none" stroke="{color}" stroke-width="1.2"/>')
        parts.append(f'  <text x="{x+w/2:.1f}" y="{y-1}" text-anchor="middle" fill="{color}" font-size="11.5" letter-spacing="0.5">{esc(item)}</text>')
        x += w + 14
    return "\n".join(parts), x

body = []
body.append(f'  <text x="{pad_left}" y="{y0}" fill="{CYAN}" font-size="13">&gt;&gt; CORE_STACK // modules.loaded()</text>')

y = y0 + 36
chips1, _ = chip_row(row1, y, CYAN)
body.append(chips1)

y += 46
chips2, _ = chip_row(row2, y, MAGENTA)
body.append(chips2)

y += 46
chips3, _ = chip_row(row3, y, PURPLE)
body.append(chips3)

y += 40
height = y

svg = chrome_shell(width, height, "MODULE_02://CORE_STACK", "\n".join(body))
with open("core_stack.svg", "w") as f:
    f.write(svg)
print("height", height)
