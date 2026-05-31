#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════╗
║   GENERADOR MAESTRO DE BANDERAS  v6              ║
║   La Prisión 2026 — ASCII Flag Engine            ║
║   · 500 variantes                                ║
║   · Marcos largos estilo MSN/BBS/IRC             ║
║   · Respeta mayúsculas/minúsculas                ║
║   · Sustituciones ASCII por letra                ║
║   · Editor de color carácter a carácter          ║
║   · 3 zonas clicables por resultado              ║
╚══════════════════════════════════════════════════╝
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random

# ─────────────────────────────────────────────
#  PALETA DE COLORES
# ─────────────────────────────────────────────
COLORS = {
    '#r': '#cc0000',   '#R': '#dd6666',
    '#g': '#00dd00',   '#G': '#55ee55',
    '#b': '#0000dd',   '#B': '#0099ff',
    '#y': '#ffff00',   '#Y': '#ffff88',
    '#c': '#00d6c1',   '#C': '#66ffee',
    '#m': '#aa00ff',   '#M': '#cc66ff',
    '#w': '#ffffff',   '#W': '#bcbac7',
    '#o': '#ff6800',   '#O': '#ffaa55',
    '#p': '#470f51',   '#P': '#884488',
    '#t': '#0e6b61',   '#T': '#00d6c1',
    '#n': '#808080',   '#N': '#aaaaaa',
    '#e': '#af918f',   '#E': '#ccaaaa',
}

COLOR_KEYS  = list(COLORS.keys())
COLOR_CODES = [k[1] for k in COLOR_KEYS]

COLOR_NAMES = {
    'r':'Rojo', 'R':'Rojo Claro', 'g':'Verde', 'G':'Verde Claro',
    'b':'Azul', 'B':'Azul Claro', 'y':'Amarillo', 'Y':'Amarillo Claro',
    'c':'Cyan', 'C':'Cyan Claro', 'm':'Magenta', 'M':'Magenta Claro',
    'w':'Blanco', 'W':'Gris', 'o':'Naranja', 'O':'Naranja Claro',
    'p':'Violeta', 'P':'Violeta Claro', 't':'Teal', 'T':'Teal Claro',
    'n':'Gris oscuro', 'N':'Gris Claro', 'e':'Fuego', 'E':'Fuego Claro',
}

DARK_CODES = {'y', 'Y', 'w', 'W', 'C', 'G', 'T', 'N', 'O'}

DEFAULT_CYCLE = ['r','g','b','y','c','m','o','p','t','e',
                 'R','G','B','Y','C','M','O','P','T','E']

# ─────────────────────────────────────────────
#  SUSTITUCIONES ASCII POR LETRA
# ─────────────────────────────────────────────
ASCII_SUBS_UPPER = {
    'A': ['/-\\', '/\\', '4', '^', 'Λ', '∧', '/^\\', 'Ä', 'Á'],
    'B': ['|3', '8', 'ß', '|B', 'l3', '|8', 'Β'],
    'C': ['(', '<', '©', '{', 'Ç', '¢', '['],
    'D': ['|)', '|>', 'Ð', 'D)', '|D', 'cl'],
    'E': ['3', '€', 'Ê', '|=', 'ε', '£', 'Ë'],
    'F': ['|=', 'ph', 'ƒ', '|#', 'Ƒ'],
    'G': ['6', '9', 'C-', '(_+', 'Ğ'],
    'H': ['|-|', ']-[', '#', '}{', '[-]', 'H'],
    'I': ['1', '!', '|', '¡', 'ï', 'Ï', ']['],
    'J': ['_|', '_/', 'Ĵ', ',|', '¿'],
    'K': ['|<', '|{', '|(', '|X'],
    'L': ['|_', '1_', 'Ł', '£', '|__'],
    'M': ['|V|', '|\\/|', 'ΛΛ', '/\\/\\', 'Μ'],
    'N': ['|\\|', '/\\/', '|V', 'И', '|/|', 'Ñ'],
    'O': ['0', '()', 'Ø', '°', 'Θ', 'Ö', '[]', 'Φ', '¤', 'Ó'],
    'P': ['|D', '|°', '|*', 'Þ', '℗'],
    'Q': ['0_', '(_,)', '0,', 'Ω', '¶', 'Ô'],
    'R': ['|2', '|?', '®', 'Я', '|²'],
    'S': ['5', '$', '§', 'Š', 'ß'],
    'T': ['+', '†', '7', 'Ŧ', '-|-', 'Τ'],
    'U': ['|_|', '(_)', 'Ü', 'µ', 'υ', 'Ú'],
    'V': ['\\/', '|/', '√', '\\|', 'Ṽ'],
    'W': ['\\/\\/', 'VV', 'Ŵ', '\\|/', 'ω'],
    'X': ['><', '}{', '×', 'Ж', 'Ξ', '※'],
    'Y': ['`/', 'Ŷ', '¥', 'γ', '-/-'],
    'Z': ['2', '≥', 'Ζ', '7_', '%', 'Ž'],
}

ASCII_SUBS_LOWER = {
    'a': ['@', 'á', 'ä', 'α', '4'],
    'b': ['6', 'ь', 'β', '|b'],
    'c': ['¢', 'ç', '<', '©'],
    'd': ['∂', 'δ', 'ð', 'cl'],
    'e': ['ë', 'é', 'ε', '€', '3'],
    'f': ['ƒ', 'ph', '|='],
    'g': ['9', 'ğ', 'q'],
    'h': ['ħ', 'н', '#'],
    'i': ['ï', 'í', 'ι', '1', '!'],
    'j': ['ĵ', ',/'],
    'k': ['|<', 'κ'],
    'l': ['1', 'ł', '|', '£'],
    'm': ['µ', 'ɱ', '/\\/\\'],
    'n': ['η', 'ñ', 'ŋ', '/\\'],
    'o': ['ø', 'ö', 'ó', '0', 'σ', '()', '°', 'θ'],
    'p': ['ρ', 'þ', '|°'],
    'q': ['9', 'φ'],
    'r': ['ŗ', 'г', '|2'],
    's': ['$', '5', 'š', 'ş', '§'],
    't': ['+', '†', '7', 'τ'],
    'u': ['ü', 'ú', 'υ', 'µ'],
    'v': ['\\/', 'ν', '√'],
    'w': ['\\/\\/', 'ω', 'vv'],
    'x': ['×', 'χ', '><', '※'],
    'y': ['¥', 'γ', '`/'],
    'z': ['ζ', '2', 'ž'],
}

# ─────────────────────────────────────────────
#  MARCOS
# ─────────────────────────────────────────────
FRAMES = [
    ('(¯`·._.·[',         ']·._.·´¯)'),
    ('¨°o.O',             'O.o°¨'),
    ('×÷·.·´¯`·)»',       '«(·´¯`·.·÷×'),
    ('··^v´¯`×)',          '(×´¯`v^··'),
    (",.-~*'¨¯¨'*·~-.¸-(_",  "_)-,.-~*'¨¯¨'*·~-.¸"),
    ('- - --^[',           ']^-- - -'),
    ('•·.·´¯`·.·•',        '•·.·´¯`·.·•'),
    ('`·.¸¸.·´´¯`··._.·',  '·._.··`¯´´·.¸¸.·`'),
    ('(¯`·._)',             '(_.·´¯)'),
    ("¯¨'*·~-.¸¸,.-~*'",   "*·~-.,¸¸-.~·*'¨¯"),
    ("Oº°'¨",              "¨'°ºO"),
    ('×º°"˜`"°º×',         '×º°"˜`"°º×'),
    ("Ooo'\"",              "\"'oooO"),
    ('×oo"~`"oox',          'xoo"~`"oo×'),
    ('<º))))><.·´¯`·.',     '¸.·´¯`·.¸><((((º>'),
    ('- -¤--^]',            '[^--¤- -'),
    ('~²ºº²~',              '~²ºº²~'),
    ('._|.<(+_+)>.|_.',     '._|.<(+_+)>.|_.'),
    ('..|..<(+_',            '_+>..|..'),
    ('-·=»‡«=·-',           '-·=»‡«=·-'),
    ('•°o.O',               'O.o°•'),
    ('––––•(-•',            '•-)•––––'),
    ('(¯`•¸·´¯)',           '(¯`·¸•´¯)'),
    ('··¤(`×[¤',            '¤]×´)¤··'),
    ('—(•·÷[',              ']÷·•)—'),
    ('·ï¡÷¡ï·',             '·ï¡÷¡ï·'),
    ('·!¦[·',               '·]¦!·'),
    ('°º¤ø,¸¸,ø¤º°`',       '`°º¤ø,¸¸,ø¤º°'),
    ('»-(¯`v´¯)-»',         '«-(¯`v´¯)-«'),
    ('°l||l°',              '°l||l°'),
    ('•°¤*(¯`°(F)(',         ')(F)°´¯)*¤°•'),
    ('—¤÷(`[¤*',            '*¤]´)÷¤—'),
    ('¸.´)(`·[',            ']·´)(`.¸'),
    ('·÷±‡±',               '±‡±÷·'),
    ('+*¨^¨*+',             '+*¨^¨*+'),
    ('°°°·.°·..·°¯°·._.·',  '·._.·°¯°·..·°.·°°°'),
    ('•´¯`•.',               '.•´¯`•'),
    (']|I{•——»',             '«——•}I|['),
    ("§.•´¨'°÷•..×",        "×..•´¨'°÷•..§"),
    ('•°¯`••',               '••´¯°•'),
    ('(¯`·.¸¸.·´¯`·.¸¸.->', '<-.¸¸.·´¯`·.¸¸.·´¯)'),
    ('(¯`·._(¯`·._( ',       ' )_.·´¯)_.·´¯)'),
    ('-=[',                  ']=-'),
    ('<(',                   ')>'),
    ('»·',                   '·«'),
    ('†·',                   '·†'),
    ('‡·',                   '·‡'),
    ('<o))',                  '((o>'),
    ('·-[',                  ']-·'),
    ('»»·',                  '·««'),
    ('<<·',                  '·>>'),
    ('±·',                   '·±'),
    ('§·',                   '·§'),
    ('>>>·',                 '·<<<'),
    ('//',                   '\\\\'),
    ('╔►',                   '◄╗'),
    ('◄╗',                   '╔►'),
    ('·:·',                  '·:·'),
    ('.#.',                  '.#.'),
    ('-·-',                  '-·-'),
    ('-<·',                  '·>-'),
    ('(·',                   '·)'),
    ('~·',                   '·~'),
    ('=>[',                  ']<='),
    ('╔══[',                 ']══╗'),
    ('║►',                   '◄║'),
    ('╠═[',                  ']═╣'),
    ('-·=»',                 '«=·-'),
    ('·.¸¸.·♥·.¸¸.·',       '·.¸¸.·♥·.¸¸.·'),
    ('·.¸¸.→',               '←.¸¸.·'),
    ('-={[',                  ']}}=-'),
    ('·.·´¯`·.·',            '·.·´¯`·.·'),
    ('×·.·´¯`·.·×',          '×·.·´¯`·.·×'),
    ('-=·~·=-',               '-=·~·=-'),
    ('•._.•[',                ']•._.•'),
    ('·°¯`·.',                '.·´¯°·'),
    ('¸.·´¯)',                '(¯`·.¸'),
    ('¤·.¸¸.·¤·.¸¸.·¤',      '¤·.¸¸.·¤·.¸¸.·¤'),
    ('[·¤·]',                 '[·¤·]'),
    ('•——[',                  ']——•'),
    ('~*•.¸¸.•*~',            '~*•.¸¸.•*~'),
    ('·´¯`·»',                '«·´¯`·'),
    ('o-O=[',                 ']=O-o'),
    ('·._.·[',                ']·._.·'),
    ('-·=»‡«=·-·',            '·-·=»‡«=·-'),
    ('¯`·.¸¸.->·',            '·<-.¸¸.·´¯'),
    ('×÷·.·[',                '].·÷×'),
    ('»»=[',                  ']=««'),
    ('·°º¤ø',                 'ø¤º°·'),
    ('((_|_))',               '((_|_))'),
    ('(>o<)',                  '(>o<)'),
    ('·l||l·',                '·l||l·'),
    ('•·.·[¤',                '¤]·.·•'),
    ('·.(¯`·[',               ']·´¯).·'),
    ('_|¯|_[',                ']_|¯|_'),
    ('(¯_(¯_[',               ']_¯)_¯)'),
    ('-={[>',                  '<]}=-'),
    ('·÷[¤·',                 '·¤]÷·'),
    ('-·:·-',                 '-·:·-'),
    ('°·._.·°',               '°·._.·°'),
    ('(·.·)',                  '(·.·)'),
    ('*·~-.,¸¸[',             '],¸¸-·~·*'),
    ('·.¸(¯`[',               ']´¯)¸.·'),
    ('~`¨¨`~·[',              ']·~`¨¨`~'),
    ('·]••´º´•»',             '«•´º´••[·'),
    ('¤·[',                   ']·¤'),
    ('«·[',                   ']·»'),
    ('//==[',                  ']==\\\\'),
    ('~={[',                   ']}=~'),
    ('¦¦°º¤',                 '¤º°¦¦'),
    ('*•.¸¸',                 '¸¸.•*'),
    ('·°º¤ø,¸¸,',             ',¸¸,ø¤º°·'),
    ('{•------»',             '«------•}'),
    ('·.¸¸.→[',               ']←.¸¸.·'),
    ('·´¯)(¯`·',              '·´¯)(¯`·'),
    ('-<[',                    ']>-'),
    ('·^·[',                  ']·^·'),
    ('¸.•*¨[',                ']¨*•.¸'),
    ('·.¸*[',                 ']*¸.·'),
    ('-»[',                    ']-«'),
    ('†[',                    ']†'),
    ('†††[',                  ']†††'),
    ('‡[',                    ']‡'),
    ('☠[',                    ']☠'),
    ('⚔[',                    ']⚔'),
    ('☽[',                    ']☾'),
    ('⛧[',                    ']⛧'),
    ('𝕯[',                    ']𝖉'),
    ('※[',                    ']※'),
    ('卍[',                    ']卐'),
    ('¥¥[',                   ']¥¥'),
    ('✨[',                    ']✨'),
    ('★·[',                   ']·★'),
    ('☆*[',                   ']*☆'),
    ('✦[',                    ']✦'),
    ('✧·[',                   ']·✧'),
    ('❤·[',                   ']·❤'),
    ('♡·[',                   ']·♡'),
    ('🌸[',                   ']🌸'),
    ('✿·[',                   ']·✿'),
    ('◦•◦[',                  ']◦•◦'),
    ('˚₊·[',                  ']·₊˚'),
    ('⋆·[',                   ']·⋆'),
    ('┌──[',                  ']──┐'),
    ('╓──[',                  ']──╖'),
    ('╒══[',                  ']══╕'),
    ('╠══[',                  ']══╣'),
    ('█▓▒░[',                 ']░▒▓█'),
    ('▓▒░[',                  ']░▒▓'),
    ('▶[',                    ']◀'),
    ('►[',                    ']◄'),
    ('◈[',                    ']◈'),
    ('◉·[',                   ']·◉'),
    ('-=<[',                  ']>=-'),
    ('-[::',                  '::]-'),
    ('>>[',                   ']<<'),
    ('|>-[',                  ']-<|'),
    ('/::[',                  ']::'),
    ('-x=[',                  ']=x-'),
    ('≡[',                    ']≡'),
    ('¡!¡[',                  ']¡!¡'),
    ('°°[',                   ']°°'),
    ('-<>-[',                 ']-<>-'),
    ('「[',                   ']」'),
    ('【[',                   ']】'),
    ('〖[',                   ']〗'),
    ('〘[',                   ']〙'),
    ('⌈[',                   ']⌉'),
    ('⌊[',                   ']⌋'),
    ('❰[',                   ']❱'),
    ('❲[',                    ']❳'),
    ('⦃[',                   ']⦄'),
]

# ─────────────────────────────────────────────
#  HELPERS DE COLOR
# ─────────────────────────────────────────────
def make_gradient(nick, c1, c2, c3=None):
    n = len(nick)
    if n == 0:
        return nick
    if c3 and n >= 4:
        half = n // 2
        result = ''
        for i, ch in enumerate(nick):
            if i < half:
                col = c1 if (i / max(half - 1, 1)) < 0.5 else c2
            else:
                col = c2 if ((i - half) / max(n - half - 1, 1)) < 0.5 else c3
            result += f'#{col}{ch}'
        return result
    else:
        result = ''
        for i, ch in enumerate(nick):
            col = c1 if (i / max(n - 1, 1)) < 0.5 else c2
            result += f'#{col}{ch}'
        return result

def apply_alternating(nick, colors):
    if not colors:
        return nick
    return ''.join(f'#{colors[i % len(colors)]}{ch}' for i, ch in enumerate(nick))

def apply_solid(nick, col):
    return f'#{col}{nick}'

# ─────────────────────────────────────────────
#  PARSEO Y STRIP
# ─────────────────────────────────────────────
def parse_flag(flag_str):
    segs, i, col, txt = [], 0, 'white', ''
    while i < len(flag_str):
        if flag_str[i] == '#' and i + 1 < len(flag_str) and '#' + flag_str[i + 1] in COLORS:
            if txt:
                segs.append((txt, col))
                txt = ''
            col = COLORS['#' + flag_str[i + 1]]
            i += 2
            continue
        txt += flag_str[i]
        i += 1
    if txt:
        segs.append((txt, col))
    return segs

def strip_colors(s):
    r, i = '', 0
    while i < len(s):
        if s[i] == '#' and i + 1 < len(s) and '#' + s[i + 1] in COLORS:
            i += 2
        else:
            r += s[i]
            i += 1
    return r

def flag_to_char_list(flag_str):
    result = []
    i = 0
    current_code = 'w'
    while i < len(flag_str):
        if flag_str[i] == '#' and i + 1 < len(flag_str) and '#' + flag_str[i + 1] in COLORS:
            current_code = flag_str[i + 1]
            i += 2
            continue
        result.append((flag_str[i], current_code))
        i += 1
    return result

def char_list_to_flag(char_list):
    if not char_list:
        return ''
    result = ''
    prev_code = None
    for ch, code in char_list:
        if code != prev_code:
            result += f'#{code}'
            prev_code = code
        result += ch
    return result

# ─────────────────────────────────────────────
#  SUSTITUCIÓN
# ─────────────────────────────────────────────
def substitute_nick(nick):
    options_per_pos = []
    for ch in nick:
        opts = [ch]
        table = ASCII_SUBS_UPPER if ch.isupper() else ASCII_SUBS_LOWER
        opts += table.get(ch, [])
        options_per_pos.append(list(dict.fromkeys(opts)))

    results = {nick}
    for _ in range(120):
        variant = ''
        for opts in options_per_pos:
            if random.random() < 0.55 and len(opts) > 1:
                variant += random.choice(opts[1:])
            else:
                variant += opts[0]
        results.add(variant)

    for i, opts in enumerate(options_per_pos):
        for sub in opts[1:]:
            results.add(nick[:i] + sub + nick[i + 1:])

    return sorted(results, key=lambda x: (x == nick, len(x)))


# ─────────────────────────────────────────────
#  GENERADOR DE 500 VARIANTES
#
#  Devuelve lista de 4-tuplas:
#    (ftype, flag_completo, left_code, right_code)
#  left_code  = marco izquierdo con su color (ej. '#b(¯`·._.·[')
#  right_code = marco derecho con su color  (ej. '#B]·._.·´¯)')
#  El nick coloreado = flag_completo[len(left_code) : -len(right_code) si right_code else len]
# ─────────────────────────────────────────────
def generate_flags(nick, c1, c2, c3=None):
    flags = []
    c3e = c3 if c3 else c2

    nick_variants = substitute_nick(nick)
    while len(nick_variants) < 25:
        nick_variants = list(dict.fromkeys(nick_variants + substitute_nick(nick)))
    nick_variants = list(dict.fromkeys(nick_variants))[:60]

    def pn():
        return random.choice(nick_variants)
    def rf():
        return random.choice(FRAMES)

    # Helper central: construye la 4-tupla con partes exactas
    def add(ftype, lc, pre, body, rc, suf):
        """
        lc  = color code del marco izq  (ej. 'b')
        pre = texto del marco izq       (ej. '(¯`·._.·[')
        body= nick coloreado            (ej. '#bDa#Bni')
        rc  = color code del marco dch  (ej. 'B')
        suf = texto del marco dch       (ej. ']·._.·´¯)')
        """
        left_code  = f'#{lc}{pre}'
        right_code = f'#{rc}{suf}'
        full_flag  = left_code + body + right_code
        flags.append((ftype, full_flag, left_code, right_code))

    # Para patrones especiales donde left/right no siguen lc+pre
    def add_raw(ftype, full_flag, left_code, right_code):
        flags.append((ftype, full_flag, left_code, right_code))

    # ── 1. CLÁSICO (60) ──────────────────────
    for _ in range(60):
        n = pn(); pre, suf = rf()
        body = make_gradient(n, c1, c2, c3)
        add('CLÁSICO', c1, pre, body, c2, suf)

    # ── 2. ALTERNADO (50) ────────────────────
    for _ in range(50):
        n = pn(); pre, suf = rf()
        body = apply_alternating(n, [c1, c2, c3e] if c3 else [c1, c2])
        add('ALTERNADO', c1, pre, body, c2, suf)

    # ── 3. MINIMALISTA (40) ──────────────────
    min_frames = [
        ('-=[', ']=-'), ('-·[', ']-·'), ('·:·', '·:·'),
        ('»·', '·«'), ('†·', '·†'), ('‡·', '·‡'),
        ('<<', '>>'), ('(·', '·)'), ('.:.', '.:.'),
        ('╔►', '◄╗'), ('±·', '·±'), ('§·', '·§'),
        ('✦', '✦'), ('★·', '·★'), ('──[', ']──'),
        ('«[', ']»'), ('▶', '◀'), ('◈', '◈'),
        ('→[', ']←'), ('¤[', ']¤'),
    ]
    for i in range(40):
        n = pn(); pre, suf = min_frames[i % len(min_frames)]
        body = make_gradient(n, c1, c2)
        add('MINIMALISTA', c1, pre, body, c1, suf)

    # ── 4. RETRO 90S (45) ────────────────────
    for i in range(45):
        n = pn()
        pat = i % 14
        try:
            if pat == 0:
                pre, suf = rf()
                lf = random.choice([x[0] for x in FRAMES])
                rf2 = random.choice([x[1] for x in FRAMES])
                body = make_gradient(n, c2, c1)
                lcode = f'#{c1}{lf}'; rcode = f'#{c2}{rf2}'
                add_raw('RETRO 90S', lcode+body+rcode, lcode, rcode)
            elif pat == 1:
                pre, suf = rf()
                body = f'#{c1}{n[0]}' + ''.join(f'#{c2}{ch}' for ch in n[1:])
                add('RETRO 90S', c1, pre, body, c2, suf)
            elif pat == 2:
                body = apply_alternating(n, [c1, c2])
                add_raw('RETRO 90S', f'#{c2}·{body}#{c1}·', f'#{c2}·', f'#{c1}·')
            elif pat == 3:
                body = make_gradient(n, c1, c2)
                add_raw('RETRO 90S', f'#{c1}>>{body}#{c2}<<', f'#{c1}>>', f'#{c2}<<')
            elif pat == 4:
                pre, suf = rf()
                body = apply_solid(n, c1)
                add('RETRO 90S', c2, pre, body, c2, suf)
            elif pat == 5:
                body = make_gradient(n, c1, c2)
                add_raw('RETRO 90S', f'#{c1}:::{body}#{c2}:::', f'#{c1}:::', f'#{c2}:::')
            elif pat == 6:
                body = make_gradient(n, c2, c1)
                add_raw('RETRO 90S', f'#{c1}†{body}#{c2}†', f'#{c1}†', f'#{c2}†')
            elif pat == 7:
                body = make_gradient(n, c1, c2)
                add_raw('RETRO 90S', f'#{c2}-<{body}#{c1}>-', f'#{c2}-<', f'#{c1}>-')
            elif pat == 8:
                body = apply_alternating(n, [c1, c2, c1])
                add_raw('RETRO 90S', f'#{c1}({body}#{c2})', f'#{c1}(', f'#{c2})')
            elif pat == 9:
                body = f'#{c1}{n}'
                add_raw('RETRO 90S', f'#{c2}//{body}#{c2}\\\\', f'#{c2}//', f'#{c2}\\\\')
            elif pat == 10:
                body = make_gradient(n, c1, c2)
                add_raw('RETRO 90S', f'#{c1}>{body}#{c2}<', f'#{c1}>', f'#{c2}<')
            elif pat == 11:
                body = f'#{c1}{n}'
                add_raw('RETRO 90S', f'#{c2}[{body}#{c2}]', f'#{c2}[', f'#{c2}]')
            elif pat == 12:
                body = make_gradient(n, c2, c1)
                add_raw('RETRO 90S', f'#{c1}·.·{body}#{c2}·.·', f'#{c1}·.·', f'#{c2}·.·')
            else:
                body = apply_alternating(n, [c1, c2])
                add_raw('RETRO 90S', f'#{c2}~~{body}#{c1}~~', f'#{c2}~~', f'#{c1}~~')
        except Exception:
            body = make_gradient(n, c1, c2)
            add_raw('RETRO 90S', f'#{c1}>>{body}#{c2}<<', f'#{c1}>>', f'#{c2}<<')

    # ── 5. OVERKILL (60) ─────────────────────
    for i in range(60):
        n = pn(); pat = i % 22
        try:
            if pat == 0:
                pre, suf = rf(); body = make_gradient(n, c1, c3e)
                add('OVERKILL', c1, pre, body, c2, suf)
            elif pat == 1:
                pre, suf = rf(); body = apply_alternating(n, [c1, c2, c3e])
                add('OVERKILL', c3e, pre, body, c3e, suf)
            elif pat == 2:
                body = make_gradient(n, c1, c3e)
                add_raw('OVERKILL', f'#{c1}╔►#{c2}«{body}#{c2}»#{c1}◄╗',
                        f'#{c1}╔►#{c2}«', f'#{c2}»#{c1}◄╗')
            elif pat == 3:
                body = make_gradient(n, c1, c2)
                add_raw('OVERKILL', f'#{c3e}·§·{body}#{c3e}·§·', f'#{c3e}·§·', f'#{c3e}·§·')
            elif pat == 4:
                body = apply_alternating(n, [c1, c3e, c2])
                add_raw('OVERKILL', f'#{c1}=={body}#{c1}==', f'#{c1}==', f'#{c1}==')
            elif pat == 5:
                body = make_gradient(n, c2, c1)
                add_raw('OVERKILL', f'#{c3e}·>·{body}#{c3e}·<·', f'#{c3e}·>·', f'#{c3e}·<·')
            elif pat == 6:
                body = make_gradient(n, c1, c2)
                add_raw('OVERKILL', f'#{c1}[-{body}-#{c1}]', f'#{c1}[-', f'-#{c1}]')
            elif pat == 7:
                body = apply_alternating(n, [c1, c2])
                add_raw('OVERKILL', f'#{c2}±±{body}#{c2}±±', f'#{c2}±±', f'#{c2}±±')
            elif pat == 8:
                body = make_gradient(n, c1, c3e)
                add_raw('OVERKILL', f'#{c3e}(¡{body}#{c3e}!)', f'#{c3e}(¡', f'#{c3e}!)')
            elif pat == 9:
                body = apply_alternating(n, [c2, c3e, c1])
                add_raw('OVERKILL', f'#{c1}·°·{body}#{c1}·°·', f'#{c1}·°·', f'#{c1}·°·')
            elif pat == 10:
                pre, suf = rf(); body = make_gradient(n, c3e, c1)
                add('OVERKILL', c1, pre, body, c1, suf)
            elif pat == 11:
                body_rest = make_gradient(n[1:], c2, c3e) if len(n) > 1 else ''
                full = f'#{c1}>>>#{c2}{n[0]}{body_rest}#{c1}<<<'
                add_raw('OVERKILL', full, f'#{c1}>>>', f'#{c1}<<<')
            elif pat == 12:
                body = make_gradient(n, c1, c2)
                add_raw('OVERKILL', f'#{c3e}-·=»{body}#{c3e}«=·-', f'#{c3e}-·=»', f'#{c3e}«=·-')
            elif pat == 13:
                body = apply_alternating(n, [c3e, c1, c2])
                add_raw('OVERKILL', f'#{c1}-·-{body}#{c1}-·-', f'#{c1}-·-', f'#{c1}-·-')
            elif pat == 14:
                body = make_gradient(n, c1, c3e)
                add_raw('OVERKILL', f'#{c2}·.¸¸.·{body}#{c2}·.¸¸.·', f'#{c2}·.¸¸.·', f'#{c2}·.¸¸.·')
            elif pat == 15:
                body = apply_alternating(n, [c1, c2, c3e])
                add_raw('OVERKILL', f'#{c1}»»{body}#{c1}««', f'#{c1}»»', f'#{c1}««')
            elif pat == 16:
                body = make_gradient(n, c2, c1)
                add_raw('OVERKILL', f'#{c3e}·†·{body}#{c3e}·†·', f'#{c3e}·†·', f'#{c3e}·†·')
            elif pat == 17:
                body = make_gradient(n, c1, c2)
                add_raw('OVERKILL', f'#{c1}<o)){body}#{c1}((o>', f'#{c1}<o))', f'#{c1}((o>')
            elif pat == 18:
                body = make_gradient(n, c2, c3e)
                add_raw('OVERKILL', f'#{c2}×÷·{body}#{c2}·÷×', f'#{c2}×÷·', f'#{c2}·÷×')
            elif pat == 19:
                body = apply_alternating(n, [c1, c3e, c2])
                add_raw('OVERKILL', f'#{c3e}¤·.¸{body}#{c3e}¸.·¤', f'#{c3e}¤·.¸', f'#{c3e}¸.·¤')
            elif pat == 20:
                body = apply_alternating(n, [c2, c1, c3e])
                add_raw('OVERKILL', f'#{c1}~~{body}#{c2}~~', f'#{c1}~~', f'#{c2}~~')
            else:
                body_rest = ''.join(f'#{c3e}{ch}' for ch in n[1:]) if len(n) > 1 else ''
                full = f'#{c3e}:::#{c1}{n[0]}{body_rest}#{c1}:::'
                add_raw('OVERKILL', full, f'#{c3e}:::', f'#{c1}:::')
        except Exception:
            body = make_gradient(n, c1, c3e)
            add_raw('OVERKILL', f'#{c1}╔►{body}#{c2}◄╗', f'#{c1}╔►', f'#{c2}◄╗')

    # ── 6. GÓTICO (40) ───────────────────────
    gothic_pre = ['†[','‡[','☠·[','⛧[','†††[','‡‡[','⚔·[','☽·[','※[','卍[',
                  '·†·[','·‡·[','∴[','∵[','↯[']
    gothic_suf = [']†',']‡',']·☠',']·⛧',']†††',']‡‡',']·⚔',']·☾',']※',']卐',
                  ']·†·',']·‡·',']∴',']∵',']↯']
    for i in range(40):
        n = pn()
        pre = gothic_pre[i % len(gothic_pre)]
        suf = gothic_suf[i % len(gothic_suf)]
        pat = i % 5
        if pat == 0:   body = make_gradient(n, c1, c2, c3)
        elif pat == 1: body = apply_alternating(n, [c1, c2])
        elif pat == 2: body = apply_solid(n, c1)
        elif pat == 3: body = apply_alternating(n, [c2, c1, c3e])
        else:          body = make_gradient(n, c3e, c1)
        add('GÓTICO', c1, pre, body, c2, suf)

    # ── 7. SPARKLE (40) ──────────────────────
    sparkle_pre = ['✨[','★·[','☆*[','✦[','✧·[','❤·[','♡·[','✿·[','◦•◦[',
                   '˚₊·[','⋆·[','🌸[','·✨·[','·★·[','·✧·[']
    sparkle_suf = [']✨',']·★',']☆*',']✦',']·✧',']·❤',']·♡',']·✿',']◦•◦',
                   ']·₊˚',']·⋆',']🌸',']·✨·',']·★·',']·✧·']
    for i in range(40):
        n = pn()
        pre = sparkle_pre[i % len(sparkle_pre)]
        suf = sparkle_suf[i % len(sparkle_suf)]
        pat = i % 4
        if pat == 0:   body = make_gradient(n, c1, c2, c3)
        elif pat == 1: body = apply_alternating(n, [c1, c2, c3e])
        elif pat == 2: body = apply_solid(n, c2)
        else:          body = apply_alternating(n, [c2, c1])
        add('SPARKLE', c1, pre, body, c2, suf)

    # ── 8. CYBER (40) ────────────────────────
    cyber_pre = ['-=<[','-[::','===[','¡!¡[','-x=[','|>-[','//::[',
                 '>>[','°°[','-<>-[','//[','.::[','==[','=[','<|[']
    cyber_suf = [']>=-','::]-',']===',']¡!¡',']=x-',']-<|',']:://',
                 ']<<',']°°',']-<>-',']\\\\',']::.',']==',']=',' |>]']
    for i in range(40):
        n = pn()
        pre = cyber_pre[i % len(cyber_pre)]
        suf = cyber_suf[i % len(cyber_suf)]
        pat = i % 5
        if pat == 0:   body = apply_alternating(n, [c1, c2])
        elif pat == 1: body = make_gradient(n, c1, c2, c3)
        elif pat == 2: body = apply_solid(n, c1)
        elif pat == 3: body = apply_alternating(n, [c2, c3e, c1])
        else:          body = make_gradient(n, c2, c1)
        add('CYBER', c1, pre, body, c2, suf)

    # ── 9. IRC/BBS (40) ──────────────────────
    irc_pre = ['·]••´º´•»','¤·[','«·[','¦¦°º¤','*•.¸¸','·°º¤ø,¸¸,',
               '{•------»','·.¸¸.→[','¸.•*¨[','·.¸*[','-»[','·^·[',
               '·´¯)(¯`·[','-<[','//==[']
    irc_suf = ['«•´º´••[·',']·¤',']·»','¤º°¦¦','¸¸.•*',',¸¸,ø¤º°·',
               '«------•}',']←.¸¸.·',']¨*•.¸',']*¸.·',']-«',']·^·',
               ']·´¯)(¯`·',']>-',']==\\\\']
    for i in range(40):
        n = pn()
        pre = irc_pre[i % len(irc_pre)]
        suf = irc_suf[i % len(irc_suf)]
        pat = i % 4
        if pat == 0:   body = make_gradient(n, c1, c2, c3)
        elif pat == 1: body = apply_alternating(n, [c1, c2])
        elif pat == 2: body = apply_solid(n, c2)
        else:          body = make_gradient(n, c3e, c2)
        add('IRC/BBS', c1, pre, body, c2, suf)

    # ── 10. TERMINAL (40) ────────────────────
    box_pre = ['┌──[','╓──[','╒══[','╔══[','╠══[','█▓▒░[','▓▒░[',
               '▶[','►[','◈[','◉·[','╔►◄[','│◄[','╔─[','╠─[']
    box_suf = [']──┐',']──╖',']══╕',']══╗',']══╣',']░▒▓█',']░▒▓',
               ']◀',']◄',']◈',']·◉',']►◄╗',']►│',']─╗',']─╣']
    for i in range(40):
        n = pn()
        pre = box_pre[i % len(box_pre)]
        suf = box_suf[i % len(box_suf)]
        pat = i % 4
        if pat == 0:   body = make_gradient(n, c1, c2, c3)
        elif pat == 1: body = apply_solid(n, c1)
        elif pat == 2: body = apply_alternating(n, [c1, c2])
        else:          body = apply_alternating(n, [c3e, c1, c2])
        add('TERMINAL', c1, pre, body, c2, suf)

    # ── 11. ELEGANTE (45) ────────────────────
    unicode_pre = ['「[','【[','〖[','〘[','⌈[','⌊[','❰[','❲[','⦃[',
                   '《[','〈[','⟦[','⟨[','「✦[','【✧[']
    unicode_suf = (']」',']】',']〗',']〙',']⌉',']⌋',']❱',']❳',']⦄',
                   ']》',']〉',']⟧',']⟩',']✦」',']✧】')
    for i in range(45):
        n = pn()
        pre = unicode_pre[i % len(unicode_pre)]
        suf = unicode_suf[i % len(unicode_suf)]
        pat = i % 5
        if pat == 0:   body = make_gradient(n, c1, c2, c3)
        elif pat == 1: body = apply_alternating(n, [c1, c2, c3e])
        elif pat == 2: body = apply_solid(n, c2)
        elif pat == 3: body = make_gradient(n, c3e, c1)
        else:          body = apply_alternating(n, [c2, c1])
        add('ELEGANTE', c1, pre, body, c2, suf)

    # Rellenar hasta 500
    while len(flags) < 500:
        n = pn(); pre, suf = rf()
        body = make_gradient(n, c1, c2, c3)
        add('CLÁSICO', c1, pre, body, c2, suf)

    return flags[:500]


# ─────────────────────────────────────────────
#  UI CONSTANTS
# ─────────────────────────────────────────────
TYPE_COLORS = {
    'CLÁSICO':    '#00ccaa', 'ALTERNADO':  '#ffaa33',
    'MINIMALISTA':'#4488ff', 'RETRO 90S':  '#ff6644',
    'OVERKILL':   '#cc44ff', 'GÓTICO':     '#aa44cc',
    'SPARKLE':    '#ff88cc', 'CYBER':      '#44ffcc',
    'IRC/BBS':    '#ffdd44', 'TERMINAL':   '#88ff44',
    'ELEGANTE':   '#88ccff',
}
TYPE_BG = {
    'CLÁSICO':    '#0a2a22', 'ALTERNADO':  '#2a1a00',
    'MINIMALISTA':'#0a1a3a', 'RETRO 90S':  '#2a1000',
    'OVERKILL':   '#1a0a2a', 'GÓTICO':     '#180a20',
    'SPARKLE':    '#2a0a18', 'CYBER':      '#001a20',
    'IRC/BBS':    '#1a1a00', 'TERMINAL':   '#001a00',
    'ELEGANTE':   '#0a1a28',
}
BG       = '#08080e'
BG_PANEL = '#0d1020'
BG_CARD  = '#050810'
FG_DIM   = '#334466'
FG_MID   = '#667799'
FG_HEAD  = '#aaccff'
BG_LEFT  = '#0d1828'; BG_NICK  = '#0d1a0d'; BG_RIGHT  = '#1a0e08'
FG_LEFT  = '#5a88cc'; FG_NICK  = '#44cc44'; FG_RIGHT  = '#cc8844'
BG_LEFT_H = '#1a3060'; BG_NICK_H = '#1a3a1a'; BG_RIGHT_H = '#3a1a08'


def _measure(text, size):
    try:
        import tkinter.font as tkfont
        return tkfont.Font(family='Courier New', size=size, weight='bold').measure(text)
    except Exception:
        return max(1, len(text)) * int(size * 0.62)


def _draw_flag_on_canvas(canvas, flag_str, size=18, center=False):
    canvas.delete('all')
    canvas.update_idletasks()
    segs = parse_flag(flag_str)
    if not segs:
        return
    cw    = canvas.winfo_width()  or 900
    ch_px = canvas.winfo_height() or 56
    widths  = [_measure(t, size) for t, _ in segs]
    total_w = sum(widths)
    x = max(6, (cw - total_w) // 2) if center else 6
    y = ch_px // 2
    for (text, color), w in zip(segs, widths):
        if not text:
            continue
        canvas.create_text(x, y, text=text,
                           font=('Courier New', size, 'bold'),
                           fill=color, anchor='w')
        x += w


class CharColorEditor(tk.Toplevel):
    BTN_W = 3
    def __init__(self, parent, flag_str, on_apply):
        super().__init__(parent)
        self.title('Editor de color — carácter a carácter')
        self.configure(bg=BG)
        self.resizable(True, True)
        self.on_apply  = on_apply
        self.transient(parent)
        self.grab_set()
        self._chars    = flag_to_char_list(flag_str)
        self._pen_code = tk.StringVar(value='r')
        self._char_btns = []
        self._history   = []
        self._build_ui()
        self._refresh_char_buttons()
        self._update_preview()
        self.minsize(740, 540)
        self.update_idletasks()
        pw, ph = parent.winfo_width(), parent.winfo_height()
        px, py = parent.winfo_rootx(), parent.winfo_rooty()
        ww = max(self.winfo_reqwidth(), 740)
        wh = max(self.winfo_reqheight(), 540)
        self.geometry(f'{ww}x{wh}+{max(0,px+(pw-ww)//2)}+{max(0,py+(ph-wh)//2)}')
        self.bind('<Configure>', self._on_resize)

    def _build_ui(self):
        pal = tk.Frame(self, bg=BG_PANEL, bd=1, relief='solid')
        pal.pack(fill='x', padx=10, pady=(10, 4))
        tk.Label(pal, text=' PLUMA — clic en color · clic en caracter para pintar:',
                 font=('Courier New', 8, 'bold'), fg='#ffcc44', bg=BG_PANEL
                 ).pack(anchor='w', padx=8, pady=(6, 2))
        sw = tk.Frame(pal, bg=BG_PANEL)
        sw.pack(fill='x', padx=8, pady=(0, 4))
        for code in COLOR_CODES:
            hc = COLORS['#' + code]
            tk.Button(sw, text=code, bg=hc,
                      fg='black' if code in DARK_CODES else 'white',
                      font=('Courier New', 9, 'bold'),
                      relief='flat', bd=0, width=self.BTN_W, cursor='hand2',
                      command=lambda c=code: self._set_pen(c)
                      ).pack(side='left', padx=2, pady=2)
        pr = tk.Frame(pal, bg=BG_PANEL)
        pr.pack(fill='x', padx=8, pady=(2, 6))
        tk.Label(pr, text='Color activo:', font=('Courier New', 8, 'bold'),
                 fg=FG_MID, bg=BG_PANEL).pack(side='left')
        self._pen_ind = tk.Label(pr, text='  r - Rojo  ',
                                 font=('Courier New', 9, 'bold'),
                                 fg='white', bg='red', relief='flat', padx=6, pady=2)
        self._pen_ind.pack(side='left', padx=8)
        tk.Label(pr, text='Izq=pintar  Der=cuentagotas  Shift+clic=franja',
                 font=('Courier New', 8), fg=FG_DIM, bg=BG_PANEL
                 ).pack(side='left', padx=12)
        co = tk.Frame(self, bg=BG_PANEL, bd=1, relief='solid')
        co.pack(fill='x', padx=10, pady=4)
        tk.Label(co, text=' CARACTERES:',
                 font=('Courier New', 8, 'bold'), fg=FG_HEAD, bg=BG_PANEL
                 ).pack(anchor='w', padx=8, pady=(6, 2))
        self._chars_canvas = tk.Canvas(co, height=86, bg=BG_CARD, highlightthickness=0)
        self._chars_sb = tk.Scrollbar(co, orient='horizontal',
                                      command=self._chars_canvas.xview)
        self._chars_canvas.configure(xscrollcommand=self._chars_sb.set)
        self._chars_sb.pack(side='bottom', fill='x', padx=8, pady=(0, 4))
        self._chars_canvas.pack(fill='x', padx=8, pady=(0, 2))
        self._chars_inner = tk.Frame(self._chars_canvas, bg=BG_CARD)
        self._chars_canvas.create_window((0, 0), window=self._chars_inner, anchor='nw')
        self._chars_inner.bind('<Configure>',
            lambda e: self._chars_canvas.configure(
                scrollregion=self._chars_canvas.bbox('all')))
        tools = tk.Frame(self, bg=BG_PANEL, bd=1, relief='solid')
        tools.pack(fill='x', padx=10, pady=4)
        tk.Label(tools, text=' HERRAMIENTAS:',
                 font=('Courier New', 8, 'bold'), fg=FG_MID, bg=BG_PANEL
                 ).pack(side='left', padx=8, pady=6)
        for txt, cmd, col in [
            ('Deshacer',   self._undo,              '#1a3a6a'),
            ('Degradado',  self._apply_gradient,    '#1a2a0a'),
            ('Alternado',  self._apply_alternating, '#2a1a0a'),
            ('Todo igual', self._paint_all,         '#2a0a1a'),
            ('Invertir',   self._invert_colors,     '#1a1a2a'),
        ]:
            tk.Button(tools, text=txt, font=('Courier New', 9, 'bold'),
                      bg=col, fg='#aaccff',
                      activebackground='#223355', activeforeground='white',
                      relief='flat', bd=0, padx=10, pady=4, cursor='hand2',
                      command=cmd).pack(side='left', padx=4, pady=6)
        pf = tk.Frame(self, bg=BG_PANEL, bd=1, relief='solid')
        pf.pack(fill='x', padx=10, pady=4)
        tk.Label(pf, text=' PREVIEW:', font=('Courier New', 8, 'bold'),
                 fg=FG_DIM, bg=BG_PANEL).pack(anchor='w', padx=8, pady=(4, 0))
        self._prev_canvas = tk.Canvas(pf, height=60, bg=BG_CARD,
                                      highlightthickness=1,
                                      highlightbackground='#1a2a4a')
        self._prev_canvas.pack(fill='x', padx=8, pady=(0, 8))
        self._prev_canvas.bind('<Configure>', self._on_prev_conf)
        cf = tk.Frame(self, bg=BG_PANEL, bd=1, relief='solid')
        cf.pack(fill='x', padx=10, pady=4)
        tk.Label(cf, text=' CODIGO:', font=('Courier New', 8, 'bold'),
                 fg=FG_DIM, bg=BG_PANEL).pack(anchor='w', padx=8, pady=(4, 0))
        self._code_box = scrolledtext.ScrolledText(
            cf, font=('Courier New', 10), bg='#030608', fg='#66ffaa',
            relief='flat', bd=4, height=3, wrap='word')
        self._code_box.pack(fill='x', padx=8, pady=(0, 6))
        br = tk.Frame(self, bg=BG)
        br.pack(fill='x', padx=10, pady=(4, 10))
        for txt, cmd, bg_, fg_ in [
            ('APLICAR Y CERRAR', self._apply_and_close, '#0a3a0a', '#66ff66'),
            ('COPIAR CODIGO',    self._copy_code,       '#0a2a3a', '#66ccff'),
        ]:
            tk.Button(br, text=txt, font=('Courier New', 10, 'bold'),
                      bg=bg_, fg=fg_, relief='flat', bd=0,
                      padx=16, pady=6, cursor='hand2', command=cmd
                      ).pack(side='left', padx=6)
        tk.Button(br, text='CANCELAR',
                  font=('Courier New', 10, 'bold'), bg='#2a0a0a', fg='#ff6644',
                  relief='flat', bd=0, padx=16, pady=6, cursor='hand2',
                  command=self.destroy).pack(side='right', padx=6)

    def _on_prev_conf(self, event):
        try: self.after_cancel(self._prev_job)
        except AttributeError: pass
        self._prev_job = self.after(30, self._update_preview)

    def _on_resize(self, event):
        if event.widget is self:
            try: self.after_cancel(self._rsz_job)
            except AttributeError: pass
            self._rsz_job = self.after(50, self._update_preview)

    def _refresh_char_buttons(self):
        for w in self._chars_inner.winfo_children():
            w.destroy()
        self._char_btns = []
        for idx, (ch, code) in enumerate(self._chars):
            hc  = COLORS.get('#' + code, '#ffffff')
            fgt = '#000' if code in DARK_CODES else '#fff'
            f   = tk.Frame(self._chars_inner, bg=BG_CARD, bd=1, relief='solid')
            f.pack(side='left', padx=1, pady=4)
            btn = tk.Button(f, text=ch, font=('Courier New', 12, 'bold'),
                            bg=hc, fg=fgt, activebackground=hc,
                            relief='flat', bd=0, width=2, padx=2, pady=4,
                            cursor='hand2')
            btn.pack()
            lbl = tk.Label(f, text=code, font=('Courier New', 7),
                           fg=hc, bg=BG_CARD)
            lbl.pack()
            btn.bind('<Button-1>',       lambda e, i=idx: self._paint(i))
            btn.bind('<Button-3>',       lambda e, i=idx: self._eyedrop(i))
            btn.bind('<Shift-Button-1>', lambda e, i=idx: self._paint_segment(i))
            self._char_btns.append((f, btn, lbl))
        self._chars_canvas.update_idletasks()
        self._chars_canvas.configure(scrollregion=self._chars_canvas.bbox('all'))

    def _set_pen(self, code):
        self._pen_code.set(code)
        hc = COLORS['#' + code]
        self._pen_ind.config(text='  ' + code + ' - ' + COLOR_NAMES.get(code, code) + '  ',
                             bg=hc, fg='black' if code in DARK_CODES else 'white')

    def _push_history(self):
        self._history.append(list(self._chars))
        if len(self._history) > 50: self._history.pop(0)

    def _paint(self, idx):
        if idx >= len(self._chars): return
        self._push_history()
        ch, _ = self._chars[idx]
        self._chars[idx] = (ch, self._pen_code.get())
        self._update_btn(idx); self._update_preview()

    def _eyedrop(self, idx):
        if idx >= len(self._chars): return
        self._set_pen(self._chars[idx][1])

    def _paint_segment(self, idx):
        if idx >= len(self._chars): return
        self._push_history()
        _, old = self._chars[idx]; pen = self._pen_code.get()
        ids = [idx]
        for j in range(idx-1, -1, -1):
            if self._chars[j][1] == old: ids.append(j)
            else: break
        for j in range(idx+1, len(self._chars)):
            if self._chars[j][1] == old: ids.append(j)
            else: break
        for i in ids:
            ch, _ = self._chars[i]; self._chars[i] = (ch, pen)
            self._update_btn(i)
        self._update_preview()

    def _update_btn(self, idx):
        if idx >= len(self._char_btns): return
        f, btn, lbl = self._char_btns[idx]
        ch, code = self._chars[idx]
        hc  = COLORS.get('#' + code, '#ffffff')
        fgt = '#000' if code in DARK_CODES else '#fff'
        btn.config(bg=hc, fg=fgt, activebackground=hc)
        lbl.config(text=code, fg=hc)

    def _undo(self):
        if not self._history: return
        self._chars = self._history.pop()
        self._refresh_char_buttons(); self._update_preview()

    def _apply_gradient(self):
        if len(self._chars) < 2: return
        origin = self._chars[0][1]; dest = self._pen_code.get()
        self._push_history(); n = len(self._chars)
        for i, (ch, _) in enumerate(self._chars):
            self._chars[i] = (ch, origin if (i/max(n-1,1)) < 0.5 else dest)
        self._refresh_char_buttons(); self._update_preview()

    def _apply_alternating(self):
        origin = self._chars[0][1] if self._chars else 'w'
        dest = self._pen_code.get(); self._push_history()
        for i, (ch, _) in enumerate(self._chars):
            self._chars[i] = (ch, origin if i%2==0 else dest)
        self._refresh_char_buttons(); self._update_preview()

    def _paint_all(self):
        pen = self._pen_code.get(); self._push_history()
        self._chars = [(ch, pen) for ch, _ in self._chars]
        self._refresh_char_buttons(); self._update_preview()

    def _invert_colors(self):
        self._push_history()
        codes = [c for _, c in self._chars]; codes.reverse()
        self._chars = [(ch, codes[i]) for i, (ch, _) in enumerate(self._chars)]
        self._refresh_char_buttons(); self._update_preview()

    def _get_current_flag(self):
        return char_list_to_flag(self._chars)

    def _update_preview(self):
        fs = self._get_current_flag()
        self._prev_canvas.update_idletasks()
        _draw_flag_on_canvas(self._prev_canvas, fs, size=16, center=True)
        cur = self._code_box.index('insert')
        self._code_box.delete('1.0', 'end')
        self._code_box.insert('1.0', fs)
        try: self._code_box.mark_set('insert', cur)
        except Exception: pass

    def _copy_code(self):
        fs = self._get_current_flag()
        self.clipboard_clear(); self.clipboard_append(fs)

    def _apply_and_close(self):
        self.on_apply(self._get_current_flag()); self.destroy()


class FlagRow(tk.Frame):
    """3 zonas clicables: marco izq / nick / marco dcho."""
    def __init__(self, parent, idx, ftype, flag_str, left_code, right_code,
                 on_click, on_dblclick, **kw):
        bg = TYPE_BG.get(ftype, '#0a0a14')
        super().__init__(parent, bg=bg, **kw)

        # Calcular nick exactamente por las partes guardadas
        rest = flag_str
        if left_code and flag_str.startswith(left_code):
            rest = flag_str[len(left_code):]
        if right_code and rest.endswith(right_code):
            nick_code = rest[:-len(right_code)]
        else:
            nick_code = rest

        self._parts = {'left': left_code, 'nick': nick_code, 'right': right_code}

        tk.Label(self, text='[%03d]' % idx, font=('Courier New', 8),
                 fg='#445566', bg=bg, width=5, anchor='e'
                 ).pack(side='left', padx=(4, 1))
        tk.Label(self, text='%-11s' % ftype, font=('Courier New', 8, 'bold'),
                 fg=TYPE_COLORS.get(ftype, '#aaaaaa'), bg=bg, width=11, anchor='w'
                 ).pack(side='left', padx=(0, 3))
        tk.Frame(self, bg='#1a2030', width=1).pack(side='left', fill='y', pady=2)

        self._labels = {}
        for part, code in [('left', left_code), ('nick', nick_code), ('right', right_code)]:
            raw = strip_colors(code)
            lbl = tk.Label(
                self,
                text=raw if raw.strip() else '.',
                font=('Courier New', 9),
                fg={'left': FG_LEFT, 'nick': FG_NICK, 'right': FG_RIGHT}[part],
                bg={'left': BG_LEFT, 'nick': BG_NICK,  'right': BG_RIGHT}[part],
                cursor='hand2', anchor='w', padx=5, pady=2,
            )
            lbl.pack(side='left', fill='y')
            self._labels[part] = lbl
            lbl.bind('<Enter>',    lambda e, p=part: self._hover(p, True))
            lbl.bind('<Leave>',    lambda e, p=part: self._hover(p, False))
            lbl.bind('<Button-1>', lambda e, p=part: on_click(p, self._parts[p]))
            lbl.bind('<Double-Button-1>', lambda e: on_dblclick())
            if part != 'right':
                tk.Frame(self, bg='#0a1020', width=1).pack(side='left', fill='y', pady=2)

    def _hover(self, part, on):
        bgs_on  = {'left': BG_LEFT_H, 'nick': BG_NICK_H, 'right': BG_RIGHT_H}
        bgs_off = {'left': BG_LEFT,    'nick': BG_NICK,    'right': BG_RIGHT}
        self._labels[part].config(bg=bgs_on[part] if on else bgs_off[part])


class App:
    def __init__(self, root):
        self.root  = root
        self.root.title('GENERADOR MAESTRO DE BANDERAS v6 - La Prision 2026')
        self.root.configure(bg=BG)
        self.root.geometry('1360x960')
        self.root.minsize(1100, 720)
        self.root.resizable(True, True)
        self.flags         = []
        self._edited_flags = {}
        self._shown_rows   = []
        self._shown_data   = []
        self._sel_idx      = -1
        self._asm_left    = tk.StringVar(value='')
        self._asm_nick    = tk.StringVar(value='')
        self._asm_right   = tk.StringVar(value='')
        self._asm_history = []
        self._ui()

    def _ui(self):
        self._build_header()
        self._build_inputs()
        self._build_filters()
        self._build_preview_bar()
        self._build_subs_bar()
        self._build_assembler()
        self._build_body()
        self._build_status()
        ttk.Style().configure('TCombobox',
                              fieldbackground='#111830', background='#111830',
                              foreground='white', selectbackground='#1a3a6a')

    def _build_header(self):
        tf = tk.Frame(self.root, bg=BG)
        tf.pack(fill='x', padx=10, pady=(10, 2))
        tk.Label(tf, text='GENERADOR MAESTRO DE BANDERAS  v6',
                 font=('Courier New', 13, 'bold'), fg='#4488ff', bg=BG).pack()
        tk.Label(tf,
                 text='La Prision 2026  500 Variantes  Clic en zona = ensamblar  Doble clic = editar colores',
                 font=('Courier New', 9), fg=FG_DIM, bg=BG).pack()

    def _build_inputs(self):
        inf = tk.Frame(self.root, bg=BG_PANEL, bd=1, relief='solid')
        inf.pack(fill='x', padx=14, pady=6)
        row = tk.Frame(inf, bg=BG_PANEL)
        row.pack(fill='x', padx=12, pady=10)
        tk.Label(row, text='NICK:', font=('Courier New', 10, 'bold'),
                 fg=FG_HEAD, bg=BG_PANEL).grid(row=0, column=0, padx=4)
        self.nick_var = tk.StringVar()
        self.nick_var.trace_add('write', self._live)
        tk.Entry(row, textvariable=self.nick_var,
                 font=('Courier New', 13, 'bold'),
                 bg='#111830', fg='#ffffff',
                 insertbackground='white', relief='flat', bd=4, width=16
                 ).grid(row=0, column=1, padx=8)
        self.c1_var = tk.StringVar(value='b')
        self.c2_var = tk.StringVar(value='B')
        self.c3_var = tk.StringVar(value='(ninguno)')
        for ci, (lbl, var, extra) in enumerate([
            ('COLOR 1:', self.c1_var, False),
            ('COLOR 2:', self.c2_var, False),
            ('COLOR 3:', self.c3_var, True),
        ], 2):
            tk.Label(row, text=lbl, font=('Courier New', 10, 'bold'),
                     fg=FG_HEAD, bg=BG_PANEL).grid(row=0, column=ci*2, padx=4)
            vals = (['(ninguno)'] + COLOR_CODES) if extra else COLOR_CODES
            cb = ttk.Combobox(row, textvariable=var, width=13,
                              values=vals, state='readonly', font=('Courier New', 10))
            cb.grid(row=0, column=ci*2+1, padx=4)
            cb.bind('<<ComboboxSelected>>', self._live)
        tk.Button(row, text='GENERAR 500',
                  font=('Courier New', 10, 'bold'),
                  bg='#1a3a6a', fg=FG_HEAD,
                  activebackground='#2255aa', activeforeground='white',
                  relief='flat', bd=0, padx=14, pady=4, cursor='hand2',
                  command=self.generate).grid(row=0, column=9, padx=16)
        tk.Button(row, text='COLOREAR NICK',
                  font=('Courier New', 9, 'bold'),
                  bg='#2a0a3a', fg='#dd88ff',
                  activebackground='#3a1055', activeforeground='white',
                  relief='flat', bd=0, padx=10, pady=4, cursor='hand2',
                  command=self._open_free_editor).grid(row=0, column=10, padx=6)

    def _build_filters(self):
        ff = tk.Frame(self.root, bg=BG_PANEL, bd=1, relief='solid')
        ff.pack(fill='x', padx=14, pady=2)
        tk.Label(ff, text=' FILTRAR: ', font=('Courier New', 8, 'bold'),
                 fg=FG_DIM, bg=BG_PANEL).pack(side='left', padx=6)
        self.filter_var = tk.StringVar(value='TODOS')
        for opt in ['TODOS','CLASICO','ALTERNADO','MINIMALISTA','RETRO 90S',
                    'OVERKILL','GOTICO','SPARKLE','CYBER','IRC/BBS','TERMINAL','ELEGANTE']:
            display = opt.replace('CLASICO','CLÁSICO').replace('GOTICO','GÓTICO')
            tk.Radiobutton(ff, text=display, variable=self.filter_var, value=opt,
                           font=('Courier New', 8, 'bold'),
                           fg=TYPE_COLORS.get(display, '#aaaaaa'), bg=BG_PANEL,
                           selectcolor='#1a2a3a', activebackground=BG_PANEL,
                           command=self._apply_filter).pack(side='left', padx=5)

    def _build_preview_bar(self):
        pf = tk.Frame(self.root, bg=BG_PANEL, bd=1, relief='solid')
        pf.pack(fill='x', padx=14, pady=2)
        tk.Label(pf, text=' PREVIEW EN VIVO ', font=('Courier New', 8, 'bold'),
                 fg=FG_DIM, bg=BG_PANEL).pack(anchor='w', padx=10, pady=(4, 0))
        self.preview_canvas = tk.Canvas(pf, height=60, bg=BG_CARD, highlightthickness=0)
        self.preview_canvas.pack(fill='x', padx=10, pady=(0, 6))
        self.preview_canvas.bind('<Configure>', lambda e: self._redraw_live_preview())

    def _build_subs_bar(self):
        sf = tk.Frame(self.root, bg=BG_PANEL, bd=1, relief='solid')
        sf.pack(fill='x', padx=14, pady=2)
        tk.Label(sf, text=' SUSTITUCIONES ASCII ', font=('Courier New', 8, 'bold'),
                 fg=FG_DIM, bg=BG_PANEL).pack(anchor='w', padx=10, pady=(4, 0))
        self.sub_canvas = tk.Canvas(sf, height=32, bg=BG_CARD, highlightthickness=0)
        self.sub_canvas.pack(fill='x', padx=10, pady=(0, 4))

    def _build_assembler(self):
        af = tk.Frame(self.root, bg=BG_PANEL, bd=1, relief='solid')
        af.pack(fill='x', padx=14, pady=2)
        th = tk.Frame(af, bg=BG_PANEL)
        th.pack(fill='x', padx=8, pady=(6, 2))
        tk.Label(th, text='ENSAMBLADOR', font=('Courier New', 9, 'bold'),
                 fg='#ffdd44', bg=BG_PANEL).pack(side='left')
        for txt, col in [('  MARCO IZQ', FG_LEFT), ('  NICK', FG_NICK), ('  MARCO DCHO', FG_RIGHT)]:
            tk.Label(th, text=txt, font=('Courier New', 9, 'bold'),
                     fg=col, bg=BG_PANEL).pack(side='left')
        tk.Label(th, text='  - clic en zona de abajo para rellenar',
                 font=('Courier New', 9), fg='#667799', bg=BG_PANEL).pack(side='left')

        row = tk.Frame(af, bg=BG_PANEL)
        row.pack(fill='x', padx=8, pady=(2, 4))
        row.grid_columnconfigure(1, weight=1)
        row.grid_columnconfigure(3, weight=2)
        row.grid_columnconfigure(5, weight=1)

        tk.Label(row, text='IZQ', font=('Courier New', 8, 'bold'),
                 fg=FG_LEFT, bg=BG_PANEL).grid(row=0, column=0, padx=(4,2), sticky='e')
        tk.Label(row, textvariable=self._asm_left,
                 font=('Courier New', 10), fg=FG_LEFT,
                 bg=BG_LEFT, relief='solid', bd=1, anchor='w', padx=6, pady=3
                 ).grid(row=0, column=1, sticky='ew', padx=4)

        tk.Label(row, text='NICK', font=('Courier New', 8, 'bold'),
                 fg=FG_NICK, bg=BG_PANEL).grid(row=0, column=2, padx=(8,2), sticky='e')
        tk.Label(row, textvariable=self._asm_nick,
                 font=('Courier New', 10), fg=FG_NICK,
                 bg=BG_NICK, relief='solid', bd=1, anchor='w', padx=6, pady=3
                 ).grid(row=0, column=3, sticky='ew', padx=4)

        tk.Label(row, text='DCHO', font=('Courier New', 8, 'bold'),
                 fg=FG_RIGHT, bg=BG_PANEL).grid(row=0, column=4, padx=(8,2), sticky='e')
        tk.Label(row, textvariable=self._asm_right,
                 font=('Courier New', 10), fg=FG_RIGHT,
                 bg=BG_RIGHT, relief='solid', bd=1, anchor='w', padx=6, pady=3
                 ).grid(row=0, column=5, sticky='ew', padx=4)

        btns = tk.Frame(af, bg=BG_PANEL)
        btns.pack(fill='x', padx=8, pady=(0, 4))
        for txt, cmd, bg_, fg_ in [
            ('EDITAR', self._asm_edit,  '#1a1a3a', '#aaccff'),
            ('COPIAR', self._asm_copy,  '#0a2a0a', '#66ff66'),
            ('DESHACER', self._asm_undo, '#1a2a1a', '#88aa88'),
            ('LIMPIAR', self._asm_clear, '#2a0a0a', '#ff6644'),
        ]:
            tk.Button(btns, text=txt, font=('Courier New', 9, 'bold'),
                      bg=bg_, fg=fg_, relief='flat', bd=0,
                      padx=10, pady=3, cursor='hand2', command=cmd
                      ).pack(side='left', padx=4, pady=4)

        self._asm_canvas = tk.Canvas(af, height=52, bg=BG_CARD,
                                     highlightthickness=1,
                                     highlightbackground='#1a2a3a')
        self._asm_canvas.pack(fill='x', padx=8, pady=(0, 6))
        self._asm_canvas.bind('<Configure>', lambda e: self._asm_redraw())

    def _asm_get(self):
        return self._asm_left.get() + self._asm_nick.get() + self._asm_right.get()

    def _asm_redraw(self):
        flag = self._asm_get()
        if strip_colors(flag).strip():
            self._asm_canvas.update_idletasks()
            _draw_flag_on_canvas(self._asm_canvas, flag, size=16, center=True)
        else:
            self._asm_canvas.delete('all')

    def _asm_push(self):
        self._asm_history.append((
            self._asm_left.get(), self._asm_nick.get(), self._asm_right.get()))
        if len(self._asm_history) > 30: self._asm_history.pop(0)

    def _asm_undo(self):
        if not self._asm_history:
            self._status('Nada que deshacer.'); return
        l, n, r = self._asm_history.pop()
        self._asm_left.set(l); self._asm_nick.set(n); self._asm_right.set(r)
        self._asm_redraw()

    def _asm_clear(self):
        self._asm_push()
        self._asm_left.set(''); self._asm_nick.set(''); self._asm_right.set('')
        self._asm_canvas.delete('all')

    def _asm_edit(self):
        flag = self._asm_get()
        if not strip_colors(flag).strip():
            self._status('El ensamblador esta vacio.'); return
        def on_apply(new_flag):
            lc = self._asm_left.get(); rc = self._asm_right.get()
            rest = new_flag
            if lc and new_flag.startswith(lc): rest = new_flag[len(lc):]
            else: lc = ''
            if rc and rest.endswith(rc): nc = rest[:-len(rc)]
            else: nc = rest; rc = ''
            self._asm_push()
            self._asm_left.set(lc); self._asm_nick.set(nc); self._asm_right.set(rc)
            self._asm_redraw()
        CharColorEditor(self.root, flag, on_apply)

    def _asm_copy(self):
        flag = self._asm_get()
        if not strip_colors(flag).strip():
            self._status('El ensamblador esta vacio.'); return
        self.root.clipboard_clear(); self.root.clipboard_append(flag)
        self._status('Copiado al portapapeles.')

    def _on_zone_click(self, part, code):
        self._asm_push()
        if part == 'left':   self._asm_left.set(code)
        elif part == 'nick': self._asm_nick.set(code)
        else:                self._asm_right.set(code)
        self._asm_redraw()
        pname = {'left':'MARCO IZQ','nick':'NICK','right':'MARCO DCHO'}[part]
        self._status('OK: ' + pname + ' = "' + (strip_colors(code) or '(vacio)') + '"')

    def _build_body(self):
        main = tk.Frame(self.root, bg=BG)
        main.pack(fill='both', expand=True, padx=14, pady=4)

        lf = tk.Frame(main, bg=BG_PANEL, bd=1, relief='solid')
        lf.pack(side='left', fill='both', expand=True, padx=(0, 6))
        lf.grid_rowconfigure(1, weight=1)
        lf.grid_columnconfigure(0, weight=1)

        hdr = tk.Frame(lf, bg='#0a0c18')
        hdr.grid(row=0, column=0, sticky='ew', padx=4, pady=(4, 0))
        tk.Label(hdr, text='[#]   TIPO        ', font=('Courier New', 8),
                 fg=FG_DIM, bg='#0a0c18').pack(side='left', padx=4)
        for txt, fg_, bg_ in [(' MARCO IZQ ', FG_LEFT, BG_LEFT),
                               (' NICK ', FG_NICK, BG_NICK),
                               (' MARCO DCHO ', FG_RIGHT, BG_RIGHT)]:
            tk.Label(hdr, text=txt, font=('Courier New', 8, 'bold'),
                     fg=fg_, bg=bg_).pack(side='left')
        tk.Label(hdr, text='  clic en zona = ensamblador | doble clic = editar',
                 font=('Courier New', 7), fg='#334455', bg='#0a0c18').pack(side='left', padx=8)

        lframe = tk.Frame(lf, bg=BG_PANEL)
        lframe.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
        lframe.grid_rowconfigure(0, weight=1)
        lframe.grid_columnconfigure(0, weight=1)

        self._list_canvas = tk.Canvas(lframe, bg='#060912', highlightthickness=0)
        sb = tk.Scrollbar(lframe, orient='vertical', command=self._list_canvas.yview)
        self._list_canvas.configure(yscrollcommand=sb.set)
        sb.grid(row=0, column=1, sticky='ns')
        self._list_canvas.grid(row=0, column=0, sticky='nsew')

        self._list_inner = tk.Frame(self._list_canvas, bg='#060912')
        self._list_cwin  = self._list_canvas.create_window(
            (0, 0), window=self._list_inner, anchor='nw')
        self._list_inner.bind('<Configure>',
            lambda e: self._list_canvas.configure(
                scrollregion=self._list_canvas.bbox('all')))
        self._list_canvas.bind('<Configure>',
            lambda e: self._list_canvas.itemconfigure(self._list_cwin, width=e.width))
        self._list_canvas.bind('<MouseWheel>',
            lambda e: self._list_canvas.yview_scroll(int(-1*(e.delta/120)), 'units'))
        self._list_canvas.bind('<Button-4>',
            lambda e: self._list_canvas.yview_scroll(-1, 'units'))
        self._list_canvas.bind('<Button-5>',
            lambda e: self._list_canvas.yview_scroll(1, 'units'))

        rf2 = tk.Frame(main, bg=BG_PANEL, bd=1, relief='solid', width=460)
        rf2.pack(side='right', fill='y')
        rf2.pack_propagate(False)

        tk.Label(rf2, text=' DETALLE & CODIGO ', font=('Courier New', 8, 'bold'),
                 fg=FG_DIM, bg=BG_PANEL).pack(anchor='w', padx=10, pady=(4, 0))
        self.detail_canvas = tk.Canvas(rf2, height=60, bg=BG_CARD, highlightthickness=0)
        self.detail_canvas.pack(fill='x', padx=8, pady=6)
        self.detail_canvas.bind('<Configure>', lambda e: self._redraw_detail())

        tk.Label(rf2, text='CODIGO PARA .inf:', font=('Courier New', 8, 'bold'),
                 fg=FG_MID, bg=BG_PANEL).pack(anchor='w', padx=10)
        self.code_box = scrolledtext.ScrolledText(
            rf2, font=('Courier New', 10), bg='#030608', fg='#66ffaa',
            relief='flat', bd=4, height=4, wrap='word')
        self.code_box.pack(fill='x', padx=8, pady=(2, 4))

        br2 = tk.Frame(rf2, bg=BG_PANEL)
        br2.pack(fill='x', padx=8, pady=2)
        tk.Button(br2, text='COPIAR SELECCION',
                  font=('Courier New', 9, 'bold'), bg='#0a2a0a', fg='#66ff66',
                  activebackground='#113311', activeforeground='lime',
                  relief='flat', bd=0, padx=8, pady=5, cursor='hand2',
                  command=self.copy_selected).pack(side='left', padx=2)
        tk.Button(br2, text='EDITAR COLORES',
                  font=('Courier New', 9, 'bold'), bg='#1a1a3a', fg='#aaccff',
                  activebackground='#252550', activeforeground='white',
                  relief='flat', bd=0, padx=8, pady=5, cursor='hand2',
                  command=self._open_char_editor).pack(side='left', padx=2)

        for ltext, aname, fcol in [
            ('TIPO:',             'type_label', '#ffcc44'),
            ('LONGITUD VISIBLE:', 'vis_label',  FG_HEAD),
            ('NICK CON SUBS:',    'nick_label', FG_HEAD),
        ]:
            tk.Label(rf2, text=ltext, font=('Courier New', 8, 'bold'),
                     fg=FG_MID, bg=BG_PANEL).pack(anchor='w', padx=10, pady=(6, 0))
            w = tk.Label(rf2, text='-', font=('Courier New', 10, 'bold'),
                         fg=fcol, bg=BG_PANEL, wraplength=420, justify='left')
            w.pack(anchor='w', padx=10)
            setattr(self, aname, w)

    def _build_status(self):
        self._status_var = tk.StringVar(
            value='Escribe un nick y pulsa GENERAR  |  clic en zona = añadir al ensamblador')
        tk.Label(self.root, textvariable=self._status_var,
                 font=('Courier New', 8), fg=FG_DIM, bg=BG, anchor='w'
                 ).pack(fill='x', padx=16, pady=4)

    def _status(self, msg):
        self._status_var.set(msg)

    def generate(self):
        nick = self.nick_var.get().strip()
        if not nick:
            messagebox.showwarning('Sin nick', 'Escribe un nick primero.'); return
        c1, c2 = self.c1_var.get(), self.c2_var.get()
        c3v = self.c3_var.get()
        c3  = None if c3v == '(ninguno)' else c3v
        self._edited_flags = {}; self._sel_idx = -1
        self.flags = generate_flags(nick, c1, c2, c3)
        random.shuffle(self.flags)
        self._populate_rows(self.flags)
        self._status('%d variantes para "%s"' % (len(self.flags), nick))

    def _populate_rows(self, data):
        for w in self._list_inner.winfo_children():
            w.destroy()
        self._shown_rows = []; self._shown_data = list(data); self._sel_idx = -1

        for i, entry in enumerate(data):
            ftype, flag_str, left_code, right_code = entry
            real_idx = self._get_real_idx(entry)
            display_flag = self._edited_flags.get(real_idx, flag_str)
            row = FlagRow(
                self._list_inner, idx=i+1,
                ftype=ftype, flag_str=display_flag,
                left_code=left_code, right_code=right_code,
                on_click=self._on_zone_click,
                on_dblclick=lambda idx=i: self._dbl_row(idx),
            )
            row.pack(fill='x', pady=1)
            row.bind('<Button-1>', lambda e, idx=i: self._select_row(idx))
            self._shown_rows.append(row)

        self._list_canvas.update_idletasks()
        self._list_canvas.configure(scrollregion=self._list_canvas.bbox('all'))
        self._list_canvas.yview_moveto(0)

    def _apply_filter(self):
        filt = self.filter_var.get()
        # Normalizar para comparar con 4-tuplas
        filt_map = {'CLASICO': 'CLÁSICO', 'GOTICO': 'GÓTICO'}
        filt_real = filt_map.get(filt, filt)
        if filt == 'TODOS':
            shown = self.flags
        else:
            shown = [e for e in self.flags if e[0] == filt_real]
        self._populate_rows(shown)

    def _get_real_idx(self, entry):
        ftype, flag_str = entry[0], entry[1]
        for ri, e in enumerate(self.flags):
            if e[0] == ftype and e[1] == flag_str:
                return ri
        return -1

    def _select_row(self, idx):
        if idx < 0 or idx >= len(self._shown_rows): return
        if 0 <= self._sel_idx < len(self._shown_rows):
            self._shown_rows[self._sel_idx].configure(highlightthickness=0)
        self._sel_idx = idx
        self._shown_rows[idx].configure(highlightthickness=1,
                                        highlightbackground='#3a5a88')
        entry = self._shown_data[idx]
        ftype, flag_str = entry[0], entry[1]
        real_idx = self._get_real_idx(entry)
        flag = self._edited_flags.get(real_idx, flag_str)

        self.detail_canvas.update_idletasks()
        _draw_flag_on_canvas(self.detail_canvas, flag, 18, True)
        self.preview_canvas.update_idletasks()
        _draw_flag_on_canvas(self.preview_canvas, flag, 22, True)
        self.code_box.delete('1.0', 'end')
        self.code_box.insert('1.0', flag)
        self.type_label.config(text=ftype, fg=TYPE_COLORS.get(ftype, '#ffcc44'))
        vis = len(strip_colors(flag))
        col = '#66ff66' if vis <= 35 else '#ffaa33' if vis <= 50 else '#ff4444'
        self.vis_label.config(text='%d chars visibles' % vis, fg=col)
        self.nick_label.config(text=strip_colors(flag))

    def _dbl_row(self, idx):
        self._select_row(idx); self._open_char_editor()

    def _get_selected(self):
        if self._sel_idx < 0 or self._sel_idx >= len(self._shown_data):
            return None, None
        entry = self._shown_data[self._sel_idx]
        real_idx = self._get_real_idx(entry)
        flag = self._edited_flags.get(real_idx, entry[1])
        return real_idx, flag

    def _redraw_live_preview(self):
        _, flag = self._get_selected()
        if flag: _draw_flag_on_canvas(self.preview_canvas, flag, 22, True)
        else: self._live()

    def _redraw_detail(self):
        _, flag = self._get_selected()
        if flag: _draw_flag_on_canvas(self.detail_canvas, flag, 18, True)

    def _live(self, *a):
        nick = self.nick_var.get()
        if not nick:
            self.preview_canvas.delete('all'); self.sub_canvas.delete('all'); return
        c1, c2 = self.c1_var.get(), self.c2_var.get()
        c3v = self.c3_var.get(); c3 = None if c3v == '(ninguno)' else c3v
        body = make_gradient(nick, c1, c2, c3)
        self.preview_canvas.update_idletasks()
        _draw_flag_on_canvas(self.preview_canvas,
                             '#' + c1 + '·.¸¸.·' + body + '#' + c2 + '·.¸¸.·', 22, True)
        self._draw_subs(nick, c1)

    def _draw_subs(self, nick, c1):
        self.sub_canvas.delete('all'); self.sub_canvas.update_idletasks()
        cw  = self.sub_canvas.winfo_width() or 900
        ch  = self.sub_canvas.winfo_height() or 32
        x, y, fs = 10, ch // 2, 10; cw_c = int(fs * 0.72)
        for orig in nick:
            table = ASCII_SUBS_UPPER if orig.isupper() else ASCII_SUBS_LOWER
            subs  = table.get(orig, [])
            self.sub_canvas.create_text(x, y, text=orig,
                font=('Courier New', fs, 'bold'), fill='white', anchor='w')
            x += len(orig) * cw_c + 4
            for s in subs[:6]:
                self.sub_canvas.create_text(x, y, text=s,
                    font=('Courier New', fs),
                    fill=COLORS.get('#' + c1, '#4488ff'), anchor='w')
                x += len(s) * cw_c + 4
            self.sub_canvas.create_text(x, y, text='|',
                font=('Courier New', fs), fill='#333355', anchor='w')
            x += 10
            if x > cw - 60: break

    def _open_char_editor(self, event=None):
        real_idx, flag = self._get_selected()
        if flag is None:
            self._status('Selecciona una bandera primero.'); return
        entry = self._shown_data[self._sel_idx]; ftype = entry[0]
        def on_apply(new_flag):
            if real_idx >= 0: self._edited_flags[real_idx] = new_flag
            _draw_flag_on_canvas(self.detail_canvas, new_flag, 18, True)
            _draw_flag_on_canvas(self.preview_canvas, new_flag, 22, True)
            self.code_box.delete('1.0', 'end'); self.code_box.insert('1.0', new_flag)
        CharColorEditor(self.root, flag, on_apply)

    def _open_free_editor(self):
        nick = self.nick_var.get().strip()
        if not nick:
            messagebox.showwarning('Sin nick', 'Escribe un nick primero.'); return
        c1, c2 = self.c1_var.get(), self.c2_var.get()
        c3v = self.c3_var.get(); c3 = None if c3v == '(ninguno)' else c3v
        flag = make_gradient(nick, c1, c2, c3)
        def on_apply(new_flag):
            self.root.clipboard_clear(); self.root.clipboard_append(new_flag)
            self._asm_push(); self._asm_nick.set(new_flag); self._asm_redraw()
        CharColorEditor(self.root, flag, on_apply)

    def copy_selected(self):
        _, flag = self._get_selected()
        if flag is None:
            self._status('Selecciona una bandera primero.'); return
        self.root.clipboard_clear(); self.root.clipboard_append(flag)
        self._status('Copiado.')


def toggle_flag_creator(parent=None):
    if parent is None:
        root = tk.Tk(); App(root); root.mainloop()
    else:
        win = tk.Toplevel(parent); App(win); return win


if __name__ == '__main__':
    root = tk.Tk(); App(root); root.mainloop()
