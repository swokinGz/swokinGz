import subprocess, html

NAME = "SWOKINGZ"
PROMPT = "swokingz@github:~$ ./wordmark.sh --name"

ascii_art = subprocess.run(
    ["figlet", "-f", "big", NAME], capture_output=True, text=True
).stdout.rstrip("\n").split("\n")

while ascii_art and ascii_art[-1].strip() == "":
    ascii_art.pop()

char_w = 9.6
line_h = 20
font_size = 15
pad_left = 24
pad_top_terminal = 40
art_top = pad_top_terminal + 26 + 34

width = max(len(PROMPT), max((len(l) for l in ascii_art), default=0)) * char_w + pad_left * 2 + 20
height = art_top + line_h * len(ascii_art) + 28

def esc(s):
    return html.escape(s)

stagger = 0.09
line_fade = 0.35
hold = 2.2
fade_out = 0.4
tail = 0.8
start = 0.4

cycle = start + len(ascii_art) * stagger + line_fade + hold + fade_out + tail
kt_in = start / cycle
kt_hold_end = (start + len(ascii_art) * stagger + line_fade + hold) / cycle
kt_out = (start + len(ascii_art) * stagger + line_fade + hold + fade_out) / cycle

svg_parts = []
svg_parts.append(f'''<svg width="{int(width)}" height="{int(height)}" viewBox="0 0 {int(width)} {int(height)}" xmlns="http://www.w3.org/2000/svg" font-family="'JetBrains Mono','Fira Code',monospace">
  <rect width="100%" height="100%" rx="10" fill="#0d1117"/>
  <rect width="100%" height="{pad_top_terminal}" rx="10" fill="#161b22"/>
  <rect y="{pad_top_terminal-10}" width="100%" height="10" fill="#161b22"/>
  <circle cx="22" cy="{pad_top_terminal/2}" r="6" fill="#ff5f56"/>
  <circle cx="42" cy="{pad_top_terminal/2}" r="6" fill="#ffbd2e"/>
  <circle cx="62" cy="{pad_top_terminal/2}" r="6" fill="#27c93f"/>
  <text x="50%" y="{pad_top_terminal/2 + 4}" text-anchor="middle" fill="#8b949e" font-size="12">{esc(PROMPT)}</text>
''')

for i, line in enumerate(ascii_art):
    y = art_top + i * line_h
    begin = start + i * stagger
    kt0 = begin / cycle
    kt1 = (begin + line_fade) / cycle
    keyTimes = f"0;{kt0:.4f};{kt1:.4f};{kt_hold_end:.4f};{kt_out:.4f};1"
    values = "0;0;1;1;0;0"
    text = esc(line) if line.strip() else "&#160;"
    svg_parts.append(
        f'  <text x="{pad_left}" y="{y}" fill="#39d0d8" font-size="{font_size}" opacity="0">{text}'
        f'<animate attributeName="opacity" values="{values}" keyTimes="{keyTimes}" '
        f'dur="{cycle:.3f}s" begin="0s" repeatCount="indefinite"/>'
        f'</text>\n'
    )

sub_begin = start + len(ascii_art) * stagger + line_fade + 0.15
kt_sub0 = sub_begin / cycle
kt_sub1 = (sub_begin + 0.5) / cycle
svg_parts.append(f'''
  <text x="{pad_left}" y="{art_top + len(ascii_art)*line_h + 6}" fill="#8b949e" font-size="12" opacity="0">
    Service Desk Analyst · ITSM / ITIL · Cybersecurity in progress
    <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{kt_sub0:.4f};{kt_sub1:.4f};{kt_hold_end:.4f};{kt_out:.4f};1" dur="{cycle:.3f}s" begin="0s" repeatCount="indefinite"/>
  </text>
''')

svg_parts.append("</svg>")

with open("/tmp/wordmark/wordmark.svg", "w") as f:
    f.write("".join(svg_parts))

print("width", width, "height", height, "lines", len(ascii_art), "cycle", cycle)
