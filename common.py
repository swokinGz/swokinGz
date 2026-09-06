import html

CYAN = "#00fff2"
MAGENTA = "#ff2079"
PURPLE = "#7b2ff7"
BG0 = "#05060a"
BG1 = "#0a0e17"
DIM = "#8b9bb4"
FAINT = "#4a5568"
LINE = "#1c2333"

FONT = "'JetBrains Mono','Fira Code',monospace"

def esc(s):
    return html.escape(s)

def chrome_shell(width, height, unit_label, body_svg, blink=True):
    """Wraps body_svg (already-positioned elements) in the terminal-window chrome:
    gradient rounded border, top bar with 3 dots, right-aligned unit label."""
    top_h = 34
    dots = f'''
  <circle cx="30" cy="{14+top_h/2}" r="4" fill="{MAGENTA}"/>
  <circle cx="46" cy="{14+top_h/2}" r="4" fill="{PURPLE}">
    {'<animate attributeName="opacity" values="1;0.3;1" dur="1.4s" repeatCount="indefinite"/>' if blink else ''}
  </circle>
  <circle cx="62" cy="{14+top_h/2}" r="4" fill="{CYAN}">
    {'<animate attributeName="opacity" values="0.4;1;0.4" dur="1.1s" repeatCount="indefinite"/>' if blink else ''}
  </circle>'''
    return f'''<svg width="{width}" height="{int(height)}" viewBox="0 0 {width} {int(height)}" xmlns="http://www.w3.org/2000/svg" font-family="{FONT}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{BG0}"/>
      <stop offset="1" stop-color="{BG1}"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{CYAN}"/>
      <stop offset="0.5" stop-color="{PURPLE}"/>
      <stop offset="1" stop-color="{MAGENTA}"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="12" fill="url(#bg)" stroke="url(#edge)" stroke-width="1.5"/>
  <rect x="14" y="14" width="{width-28}" height="{top_h}" fill="none" stroke="{LINE}" stroke-width="1"/>
  {dots}
  <text x="{width-24}" y="{14+top_h/2+4}" text-anchor="end" fill="{FAINT}" font-size="11" letter-spacing="2">{esc(unit_label)}</text>
{body_svg}
</svg>'''
