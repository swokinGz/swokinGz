import sys
sys.path.insert(0, "/tmp/futuristic2")
from common import chrome_shell, esc, CYAN, MAGENTA, PURPLE, DIM, FAINT, LINE

width = 720
top_h = 34
pad_left = 26
y0 = 14 + top_h + 34

# snapshot values (static — regenerate make_all.py to refresh from GitHub)
stats = [
    ("REPOS", 3, 10, CYAN),
    ("CONTRIBUTIONS", 11, 30, MAGENTA),
    ("STARS", 1, 5, PURPLE),
    ("FOLLOWERS", 0, 10, CYAN),
]

body = []
body.append(f'  <text x="{pad_left}" y="{y0}" fill="{CYAN}" font-size="13">&gt;&gt; TELEMETRY // github.stats.pull()</text>')

col_w = (width - 2*pad_left) / 4
y_num = y0 + 54
y_bar = y_num + 14
y_label = y_bar + 22

for i, (label, val, maxv, color) in enumerate(stats):
    cx = pad_left + i*col_w
    bar_w = col_w - 30
    fill_w = max(4, bar_w * min(val, maxv) / maxv)
    body.append(f'  <text x="{cx}" y="{y_num}" fill="{color}" font-size="26" font-weight="bold">{val}</text>')
    body.append(f'  <rect x="{cx}" y="{y_bar}" width="{bar_w}" height="5" rx="2.5" fill="{LINE}"/>')
    body.append(f'  <rect x="{cx}" y="{y_bar}" width="{fill_w:.1f}" height="5" rx="2.5" fill="{color}"/>')
    body.append(f'  <text x="{cx}" y="{y_label}" fill="{DIM}" font-size="10.5" letter-spacing="1">{esc(label)}</text>')

y = y_label + 34
body.append(f'  <line x1="{pad_left}" y1="{y}" x2="{width-26}" y2="{y}" stroke="{LINE}" stroke-width="1"/>')
y += 30
body.append(f'  <text x="{pad_left}" y="{y}" fill="{CYAN}" font-size="12.5">&gt;&gt; LANGUAGE_STACK</text>')
y += 12
bar_w = width - 2*pad_left - 90
y_bar2 = y + 14
body.append(f'  <text x="{pad_left}" y="{y_bar2+5}" fill="{DIM}" font-size="12">HTML</text>')
body.append(f'  <rect x="{pad_left+70}" y="{y_bar2-9}" width="{bar_w}" height="10" rx="5" fill="{LINE}"/>')
body.append(f'  <rect x="{pad_left+70}" y="{y_bar2-9}" width="{bar_w}" height="10" rx="5" fill="{MAGENTA}"/>')
body.append(f'  <text x="{pad_left+70+bar_w+10}" y="{y_bar2+5}" fill="{DIM}" font-size="11">100%</text>')

y = y_bar2 + 30
height = y

svg = chrome_shell(width, height, "MODULE_03://TELEMETRY", "\n".join(body))
with open("telemetry.svg", "w") as f:
    f.write(svg)
print("height", height)
