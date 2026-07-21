import random
import html

with open('final.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

svg_width = 1200
svg_height = len(lines) * 5 + 20

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}">
  <style>
    .ascii {{
      font-family: monospace;
      font-size: 5px;
      white-space: pre;
      fill: #58A6FF;
      opacity: 0;
      animation: glitch-load 2s forwards;
    }}
    @keyframes glitch-load {{
      0%   {{ opacity: 0; filter: blur(4px); transform: translate(2px, -2px); }}
      10%  {{ opacity: 0.8; filter: blur(0px); transform: translate(-2px, 2px); }}
      20%  {{ opacity: 0.2; filter: blur(2px); transform: translate(2px, 0); }}
      30%  {{ opacity: 1; filter: blur(0px); transform: translate(0, 0); }}
      40%  {{ opacity: 0.5; filter: blur(1px); transform: translate(-1px, 1px); }}
      50%  {{ opacity: 1; filter: blur(0px); transform: translate(0, 0); }}
      100% {{ opacity: 1; filter: blur(0px); transform: translate(0, 0); }}
    }}
  </style>
  <g transform="translate(10, 15)">
'''

for i, line in enumerate(lines):
    line = line.rstrip('\n')
    if not line:
        continue
    escaped_line = html.escape(line)
    delay = random.uniform(0, 1.5)
    y_pos = i * 5
    svg_content += f'    <text y="{y_pos}" class="ascii" style="animation-delay: {delay:.2f}s;">{escaped_line}</text>\n'

svg_content += '''  </g>
</svg>
'''

with open('animated_ascii.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("animated_ascii.svg generated!")
