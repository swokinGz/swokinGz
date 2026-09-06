import subprocess, html

NAME = "SWOKINGZ"

wordmark = subprocess.run(
    ["bash", "wordmark.sh", "--name", NAME], cwd=".",
    capture_output=True, text=True
).stdout.rstrip("\n").split("\n")
while wordmark and wordmark[-1].strip() == "":
    wordmark.pop()

BOOT_LINES = [
    ">> INITIALIZING UNIT: CHRISTIAN.DANGLADES",
    ">> LOADING MODULES: ITSM // ITIL // SERVICENOW",
    ">> LOADING MODULES: CYBERSECURITY.TRAINING",
    ">> CALIBRATING LANGUAGE PACKS: ES // PT // EN",
    ">> STATUS: ONLINE",
]

char_w = 9.4
line_h = 20
font_size = 14
pad_left = 26
width = 720
pad_top_terminal = 34

def esc(s):
    return html.escape(s)

def kt(sec, cycle):
    return f"{max(0.0, min(1.0, sec / cycle)):.4f}"

# --- absolute timeline (seconds) ---
boot_start = 0.3
boot_char_dur = 0.012
boot_line_gap = 0.18
t = boot_start
boot_timings = []
for line in BOOT_LINES:
    dur = max(len(line) * boot_char_dur, 0.25)
    boot_timings.append((t, dur, line))
    t += dur + boot_line_gap
boot_end = t + 0.25

glitch_start = boot_end + 0.15
glitch_dur = 0.5
settle_time = glitch_start + glitch_dur + 0.1
wordmark_h = len(wordmark) * (font_size + 8)
hold = 2.6
fade_out_dur = 0.35
reset_gap = 0.6
cycle = settle_time + hold + fade_out_dur + reset_gap

height = pad_top_terminal + 20 + len(BOOT_LINES) * line_h + 24 + wordmark_h + 80

svg = []
svg.append(f'''<svg width="{width}" height="{int(height)}" viewBox="0 0 {width} {int(height)}" xmlns="http://www.w3.org/2000/svg" font-family="'JetBrains Mono','Fira Code',monospace">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#05060a"/>
      <stop offset="1" stop-color="#0a0e17"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#00fff2"/>
      <stop offset="0.5" stop-color="#7b2ff7"/>
      <stop offset="1" stop-color="#ff2079"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="12" fill="url(#bg)" stroke="url(#edge)" stroke-width="1.5"/>
  <rect x="14" y="14" width="{width-28}" height="{pad_top_terminal}" fill="none" stroke="#1c2333" stroke-width="1"/>
  <circle cx="30" cy="{14+pad_top_terminal/2}" r="4" fill="#ff2079"/>
  <circle cx="46" cy="{14+pad_top_terminal/2}" r="4" fill="#7b2ff7">
    <animate attributeName="opacity" values="1;0.3;1" dur="1.4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="62" cy="{14+pad_top_terminal/2}" r="4" fill="#00fff2">
    <animate attributeName="opacity" values="0.4;1;0.4" dur="1.1s" repeatCount="indefinite"/>
  </circle>
  <text x="{width-24}" y="{14+pad_top_terminal/2+4}" text-anchor="end" fill="#4a5568" font-size="11" letter-spacing="2">UNIT://SWOKINGZ-01</text>
''')

# Boot log lines: clip-rect width grows 0 -> full over its slot, then resets to 0 at cycle end (loop)
y0 = 14 + pad_top_terminal + 26
for i, (begin, dur, line) in enumerate(boot_timings):
    y = y0 + i * line_h
    full_w = len(line) * char_w + 10
    clip_id = f"bc{i}"
    color = "#00fff2" if "STATUS" not in line else "#39ff14"
    kt0, kt1 = kt(begin, cycle), kt(begin + dur, cycle)
    values = f"0;0;{full_w:.1f};{full_w:.1f};0"
    keyTimes = f"0;{kt0};{kt1};1;1"
    svg.append(f'''  <clipPath id="{clip_id}">
    <rect x="0" y="{y-14}" width="0" height="18">
      <animate attributeName="width" values="{values}" keyTimes="{keyTimes}" dur="{cycle:.3f}s" repeatCount="indefinite"/>
    </rect>
  </clipPath>
  <text x="{pad_left}" y="{y}" fill="{color}" font-size="12" clip-path="url(#{clip_id})">{esc(line)}</text>
''')

# Divider before wordmark: fades in after boot, fades out on reset
div_y = y0 + len(BOOT_LINES) * line_h + 4
kt_be = kt(boot_end, cycle)
svg.append(f'''  <line x1="{pad_left}" y1="{div_y}" x2="{width-26}" y2="{div_y}" stroke="#1c2333" stroke-width="1" opacity="0">
    <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{kt_be};{kt_be};1;1" dur="{cycle:.3f}s" repeatCount="indefinite"/>
  </line>
''')

# Wordmark with glitch-in effect: 3 offset colored layers, only visible during glitch flicker,
# main clean layer takes over from settle_time and holds until fade-out near cycle end.
wy0 = div_y + font_size + 22
layers = [("#ff2079", -3), ("#00fff2", 3), ("#e8e8ff", 0)]
kt_g0 = kt(glitch_start, cycle)
kt_g1 = kt(glitch_start + glitch_dur * 0.2, cycle)
kt_g2 = kt(glitch_start + glitch_dur * 0.4, cycle)
kt_g3 = kt(glitch_start + glitch_dur * 0.6, cycle)
kt_g4 = kt(glitch_start + glitch_dur * 0.8, cycle)
kt_settle = kt(settle_time, cycle)
kt_fade0 = kt(settle_time + hold, cycle)
kt_fade1 = kt(settle_time + hold + fade_out_dur, cycle)

for line_idx, line in enumerate(wordmark):
    y = wy0 + line_idx * (font_size + 8)
    text_esc = esc(line) if line.strip() else "&#160;"
    for color, dx in layers:
        is_main = dx == 0 and color == "#e8e8ff"
        x_vals = f"{pad_left};{pad_left+dx};{pad_left-dx*1.4};{pad_left+dx*0.6};{pad_left};{pad_left}"
        x_kts = f"0;{kt_g0};{kt_g1};{kt_g3};{kt_settle};1"
        if is_main:
            op_vals = f"0;0;0;1;1;0;0"
            op_kts = f"0;{kt_g0};{kt_settle};{kt_settle};{kt_fade0};{kt_fade1};1"
        else:
            op_vals = f"0;0;0.85;0.85;0;0"
            op_kts = f"0;{kt_g0};{kt_g2};{kt_g4};{kt_settle};1"
        svg.append(
            f'  <text x="{pad_left}" y="{y}" font-size="{font_size+8}" fill="{color}" opacity="0">'
            f'{text_esc}'
            f'<animate attributeName="x" values="{x_vals}" keyTimes="{x_kts}" dur="{cycle:.3f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="{op_vals}" keyTimes="{op_kts}" dur="{cycle:.3f}s" repeatCount="indefinite"/>'
            f'</text>\n'
        )

# Tagline under wordmark
tag_y = wy0 + len(wordmark) * (font_size + 8) + 22
op_vals_tag = f"0;0;1;1;0;0"
op_kts_tag = f"0;{kt_settle};{kt_settle};{kt_fade0};{kt_fade1};1"
svg.append(f'''  <text x="{pad_left}" y="{tag_y}" fill="#8b9bb4" font-size="12.5" letter-spacing="1" opacity="0">
    SERVICE_DESK_ANALYST // ITSM.ITIL.SERVICENOW // CYBERSEC_IN_TRAINING
    <animate attributeName="opacity" values="{op_vals_tag}" keyTimes="{op_kts_tag}" dur="{cycle:.3f}s" repeatCount="indefinite"/>
  </text>
''')

svg.append("</svg>")
out = "".join(svg)
with open("wordmark.svg", "w") as f:
    f.write(out)
print("cycle", cycle, "height", height, "settle", settle_time)
