import sys
sys.path.insert(0, "/tmp/futuristic2")
from common import chrome_shell, esc, CYAN, MAGENTA, PURPLE, DIM, FAINT, LINE

width = 720
top_h = 34
pad_left = 26
y0 = 14 + top_h + 34

links = [
    ("GITHUB", "github.com/swokinGz", "https://github.com/swokinGz", CYAN),
    ("LINKEDIN", "linkedin.com/in/christiandanglades", "https://linkedin.com/in/christiandanglades", MAGENTA),
    ("EMAIL", "christiandanglades123@gmail.com", "mailto:christiandanglades123@gmail.com", PURPLE),
    ("WHATSAPP", "+55 43 98838-0063", "https://wa.me/5543988380063", CYAN),
]

body = []
body.append(f'  <text x="{pad_left}" y="{y0}" fill="{CYAN}" font-size="13">&gt;&gt; UPLINK // channels.open()</text>')

y = y0 + 34
for label, text, href, color in links:
    body.append(f'  <a href="{href}" target="_blank">')
    body.append(f'  <rect x="{pad_left}" y="{y-16}" width="120" height="24" rx="5" fill="none" stroke="{color}" stroke-width="1.1"/>')
    body.append(f'  <text x="{pad_left+60}" y="{y}" text-anchor="middle" fill="{color}" font-size="11" letter-spacing="0.5">{esc(label)}</text>')
    body.append(f'  <text x="{pad_left+134}" y="{y}" fill="{DIM}" font-size="12.5">{esc(text)}</text>')
    body.append(f'  </a>')
    y += 38

y += 14
body.append(f'  <line x1="{pad_left}" y1="{y}" x2="{width-26}" y2="{y}" stroke="{LINE}" stroke-width="1"/>')
y += 30
body.append(f'  <text x="{pad_left}" y="{y}" fill="{FAINT}" font-size="12" letter-spacing="1">&gt;&gt; END_OF_TRANSMISSION_<tspan opacity="1"> </tspan></text>')

height = y + 24

svg = chrome_shell(width, height, "MODULE_05://UPLINK", "\n".join(body))
with open("uplink.svg", "w") as f:
    f.write(svg)
print("height", height)
