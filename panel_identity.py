import sys
sys.path.insert(0, "/tmp/futuristic2")
from common import chrome_shell, esc, CYAN, MAGENTA, PURPLE, DIM, FAINT, LINE

width = 720
top_h = 34
pad_left = 26
line_h = 20
y0 = 14 + top_h + 34

rows = [
    ("DESIGNATION", "Christian Danglades"),
    ("UNIT_CLASS", "Service Desk Analyst"),
    ("DEPLOYED_AT", "Tata Consultancy Services"),
    ("ORIGIN", "Londrina, Parana - BR (Nacionalidade: Venezuelana)"),
    ("RUNTIME", "3+ years - incident mgmt / troubleshooting / automation"),
    ("CURRENT_UPGRADE", "Tecnico em Ciberseguranca (UniFil, in progress)"),
    ("", "Google Cybersecurity Professional Certificate [x]"),
    ("LANGUAGE_PACKS", "ES [advanced] / PT [advanced] / EN [intermediate]"),
    ("PERFORMANCE", "92% FCR - High CSAT - Monthly recognition"),
]

label_w = 15  # chars

body = []
body.append(f'  <text x="{pad_left}" y="{y0}" fill="{CYAN}" font-size="13">&gt;&gt; IDENTITY.SCAN // dossier.load()</text>')
y = y0 + 30
for label, value in rows:
    if label:
        body.append(f'  <text x="{pad_left}" y="{y}" fill="{PURPLE}" font-size="13">{esc(label.ljust(label_w))}</text>')
        body.append(f'  <text x="{pad_left+label_w*8.4}" y="{y}" fill="{DIM}" font-size="13">: {esc(value)}</text>')
    else:
        body.append(f'  <text x="{pad_left+label_w*8.4}" y="{y}" fill="{DIM}" font-size="13">  {esc(value)}</text>')
    y += line_h

y += 10
body.append(f'  <line x1="{pad_left}" y1="{y}" x2="{width-26}" y2="{y}" stroke="{LINE}" stroke-width="1"/>')
y += 26
body.append(f'  <text x="{pad_left}" y="{y}" fill="{CYAN}" font-size="12.5">&gt;&gt; TARGET_ROLES</text>')
y += 22
targets = "IT Support (N2) :: IT Infrastructure :: Junior Cybersecurity :: AI Automation"
body.append(f'  <text x="{pad_left}" y="{y}" fill="{MAGENTA}" font-size="12.5">{esc(targets)}</text>')
y += 24

height = y + 20

svg = chrome_shell(width, height, "MODULE_01://IDENTITY", "\n".join(body))
with open("identity.svg", "w") as f:
    f.write(svg)
print("height", height)
