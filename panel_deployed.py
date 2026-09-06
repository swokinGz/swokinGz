import sys
sys.path.insert(0, "/tmp/futuristic2")
from common import chrome_shell, esc, CYAN, MAGENTA, PURPLE, DIM, FAINT, LINE

width = 720
top_h = 34
pad_left = 26
y0 = 14 + top_h + 34

body = []
body.append(f'  <text x="{pad_left}" y="{y0}" fill="{CYAN}" font-size="13">&gt;&gt; DEPLOYED_UNITS // repos.list(--pinned)</text>')

card_y = y0 + 22
card_h = 96
card_w = width - 2*pad_left
body.append(f'  <a href="https://github.com/swokinGz/ChrisCyberSec-Portfolio" target="_blank">')
body.append(f'  <rect x="{pad_left}" y="{card_y}" width="{card_w}" height="{card_h}" rx="8" fill="none" stroke="{LINE}" stroke-width="1.2"/>')
body.append(f'  <circle cx="{pad_left+18}" cy="{card_y+24}" r="4" fill="{MAGENTA}"/>')
body.append(f'  <text x="{pad_left+34}" y="{card_y+29}" fill="{DIM}" font-size="14" font-weight="bold">ChrisCyberSec-Portfolio</text>')
body.append(f'  <text x="{pad_left+18}" y="{card_y+52}" fill="{FAINT}" font-size="11.5">A featured build from this profile — cybersecurity portfolio.</text>')
body.append(f'  <rect x="{pad_left+18}" y="{card_y+66}" width="52" height="20" rx="10" fill="none" stroke="{PURPLE}" stroke-width="1"/>')
body.append(f'  <text x="{pad_left+44}" y="{card_y+80}" text-anchor="middle" fill="{PURPLE}" font-size="10.5">HTML</text>')
body.append(f'  <text x="{pad_left+84}" y="{card_y+80}" fill="{DIM}" font-size="11.5">&#9733; 1 star</text>')
body.append(f'  </a>')

y = card_y + card_h + 20
height = y

svg = chrome_shell(width, height, "MODULE_04://DEPLOYED", "\n".join(body))
with open("deployed.svg", "w") as f:
    f.write(svg)
print("height", height)
