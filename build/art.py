# -*- coding: utf-8 -*-
"""Illustrations drawn in the logo's style: flat brick-red, leaf green,
wheat gold on cream. Used where the site needs imagery and no photograph
exists."""

RED, RED_D, GRN, GRN_D, GOLD, CREAM, LINE = (
    "#BE2A1C", "#911E13", "#5EA11D", "#3E6D13", "#F0A81C", "#FBF3E8", "#EFE3D6")

# A wreath of leaves and berries that rings the hero portrait, echoing the mark.
def wreath():
    import math
    petals = []
    for i in range(24):
        a = i * 15
        if i % 3 == 0:
            petals.append(
                f'<g transform="rotate({a} 100 100)">'
                f'<path d="M100 6c7 7 7 17 0 24-7-7-7-17 0-24Z" fill="{GRN}" opacity=".85"/></g>')
        elif i % 3 == 1:
            petals.append(f'<g transform="rotate({a} 100 100)"><circle cx="100" cy="13" r="4" fill="{GOLD}"/></g>')
        else:
            petals.append(f'<g transform="rotate({a} 100 100)"><circle cx="100" cy="13" r="3" fill="{RED}" opacity=".7"/></g>')
    return (
        '<svg class="hero__wreath" viewBox="0 0 200 200" fill="none" aria-hidden="true">'
        f'<circle cx="100" cy="100" r="87" stroke="{LINE}" stroke-width="1.5" stroke-dasharray="3 7"/>'
        + "".join(petals) + '</svg>')


def _frame(inner):
    return (f'<svg viewBox="0 0 200 200" role="img" aria-hidden="true">'
            f'<circle cx="100" cy="100" r="100" fill="{CREAM}"/>{inner}</svg>')


# 1. A plate of real food — clinical plans built on ordinary meals
def plate():
    return _frame(f'''
<circle cx="100" cy="106" r="58" fill="#fff" stroke="{LINE}" stroke-width="2"/>
<circle cx="100" cy="106" r="45" fill="none" stroke="{LINE}" stroke-width="1.5"/>
<path d="M100 106a34 34 0 0 1 34-34v34Z" fill="{GRN}" opacity=".85"/>
<path d="M100 106h-34a34 34 0 0 1 34-34Z" fill="{GOLD}" opacity=".9"/>
<path d="M100 106v34a34 34 0 0 1-34-34Z" fill="{RED}" opacity=".8"/>
<path d="M100 106h34a34 34 0 0 1-34 34Z" fill="{GRN_D}" opacity=".55"/>
<circle cx="100" cy="106" r="9" fill="#fff"/>
<path d="M52 44c10-2 18 4 19 14-10 2-18-4-19-14Z" fill="{GRN}"/>
<path d="M52 44c8 4 11 11 9 18" stroke="{GRN_D}" stroke-width="2" stroke-linecap="round" fill="none"/>
<circle cx="150" cy="52" r="8" fill="{RED}"/>
<path d="M150 44c3-3 7-3 9-1-2 3-6 4-9 1Z" fill="{GRN}"/>''')


# 2. Home cooking — a pot and wheat, for culturally-rooted plans
def pot():
    return _frame(f'''
<path d="M62 104h76v34a16 16 0 0 1-16 16H78a16 16 0 0 1-16-16v-34Z" fill="{RED}"/>
<rect x="54" y="94" width="92" height="12" rx="6" fill="{RED_D}"/>
<path d="M146 112h10a10 10 0 0 1 0 20h-10" stroke="{RED_D}" stroke-width="6" fill="none" stroke-linecap="round"/>
<path d="M54 112H44a10 10 0 0 0 0 20h10" stroke="{RED_D}" stroke-width="6" fill="none" stroke-linecap="round"/>
<path d="M84 84c0-8 8-10 8-18s-6-10-6-10" stroke="{GRN_D}" stroke-width="4" stroke-linecap="round" fill="none" opacity=".5"/>
<path d="M104 82c0-9 9-11 9-20s-7-11-7-11" stroke="{GRN_D}" stroke-width="4" stroke-linecap="round" fill="none" opacity=".5"/>
<path d="M124 84c0-8 8-10 8-18" stroke="{GRN_D}" stroke-width="4" stroke-linecap="round" fill="none" opacity=".5"/>
<g stroke="{GOLD}" stroke-width="3.5" stroke-linecap="round">
  <path d="M164 150V96"/>
  <path d="M164 104c6-4 10-2 11 3-5 3-9 2-11-3Zm0 0c-6-4-10-2-11 3 5 3 9 2 11-3Z" fill="{GOLD}" stroke="none"/>
  <path d="M164 118c6-4 10-2 11 3-5 3-9 2-11-3Zm0 0c-6-4-10-2-11 3 5 3 9 2 11-3Z" fill="{GOLD}" stroke="none"/>
  <path d="M164 132c6-4 10-2 11 3-5 3-9 2-11-3Zm0 0c-6-4-10-2-11 3 5 3 9 2 11-3Z" fill="{GOLD}" stroke="none"/>
</g>''')


# 3. A hand raising a sprout — habits that keep growing
def sprout():
    return _frame(f'''
<path d="M100 146V96" stroke="{GRN_D}" stroke-width="6" stroke-linecap="round"/>
<path d="M100 112c-4-18-18-26-34-24 2 17 16 28 34 24Z" fill="{GRN}"/>
<path d="M100 100c4-20 20-28 37-26-2 19-18 30-37 26Z" fill="{GRN_D}" opacity=".85"/>
<circle cx="100" cy="74" r="10" fill="{RED}"/>
<path d="M100 64c3-4 8-4 10-1-3 4-7 5-10 1Z" fill="{GOLD}"/>
<path d="M64 150h72a0 0 0 0 1 0 0v6a14 14 0 0 1-14 14H78a14 14 0 0 1-14-14v-6Z" fill="{RED}" opacity=".9"/>
<path d="M60 150h80" stroke="{RED_D}" stroke-width="6" stroke-linecap="round"/>''')
