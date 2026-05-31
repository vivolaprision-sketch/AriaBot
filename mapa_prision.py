# =====================================================================
# mapa_prision.py — Visor de Mapa de La Prisión
# Módulo para AriaBot | Developed by: SMaSeR 2026
#
# INTEGRACIÓN EN AriaBot.py:
#   1. Copiar Mapa.png en la misma carpeta que AriaBot.py
#   2. Añadir en el bloque de imports locales:
#        try:
#            import mapa_prision as _mapa_module
#        except ImportError:
#            _mapa_module = None
#   3. Añadir función toggle y botón (ver final de este archivo)
# =====================================================================

import os
import sys
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

try:
    from PIL import Image, ImageTk
    PIL_OK = True
except ImportError:
    PIL_OK = False

# ── Paleta idéntica a AriaBot ──
BG_MAIN        = "#0F1015"
BG_CARD        = "#161822"
BG_PANEL_INNER = "#0B0C10"
ACCENT_CYAN    = "#00F0FF"
ACCENT_GREEN   = "#00FF88"
ACCENT_RED     = "#FF2A2A"
TEXT_MAIN      = "#C8CBD8"
TEXT_DIM       = "#6A6E85"
BORDER_COL     = "#1E2230"

# ── Nombre del archivo del mapa (mismo directorio que el .py / .exe) ──
MAP_FILENAME = "Mapa.png"

# ── Leyenda: (clave, etiqueta, color_hex, símbolo_unicode) ──
LEGEND_ITEMS = [
    ("accesos_principales",  "Accesos Principales",         "#FF2A2A", "●"),
    ("accesos_secundarios",  "Accesos Secundarios",         "#00FF88", "●"),
    ("cocinas",              "Cocinas",                     "#4488FF", "✦"),
    ("ropas",                "Ropas (Camisas y Pantalones)","#CC44FF", "✦"),
    ("armas",                "Armas y Municiones",          "#FF6644", "✦"),
    ("varios",               "Varios (Megáfonos, Móviles…)","#44FF88", "✦"),
    ("protecciones",         "Protecciones",                "#FFB700", "✦"),
    ("aprendices",           "Aprendices (Material Costura)","#FF8844","✦"),
]


# ══════════════════════════════════════════════════════════════════════
#  VENTANA PRINCIPAL DEL MAPA
# ══════════════════════════════════════════════════════════════════════
class MapaVentana:
    """
    Ventana CTkToplevel con:
      · Zoom con rueda de ratón o botones +/–
      · Desplazamiento con clic + arrastre (botón 1 o 2)
      · Botón CENTRAR
      · Toggles de leyenda para mostrar/ocultar capas de iconos
    """

    ZOOM_MIN  = 0.15
    ZOOM_MAX  = 4.0
    ZOOM_STEP = 0.12        # incremento por clic
    ZOOM_WHEEL= 0.10        # incremento por rueda

    # Posiciones de iconos de la leyenda en el mapa ORIGINAL (px)
    # Formato: { clave: [(x, y, etiqueta_corta), ...] }
    # Coordenadas extraídas visualmente del mapa 1672×941
    ICON_POSITIONS = {
        "cocinas": [
            (447, 499, "Cocina\nOeste"),
            (834, 374, "Cocina\nCentral"),
            (1290, 724, "Cocina\nEste"),
        ],
        "armas": [
            (388, 129, "Almacén\nNorte"),
            (145, 173, "Almacén\nOeste"),
            (836, 204, "Patio\nDescanso N"),
            (1394, 532, "Despachos\nNoreste"),
            (1060, 535, "Entret.\nSur"),
        ],
        "ropas": [
            (572, 345, "Distribuidor\nInterior"),
            (831, 373, "Comedor\nCentral"),
            (1530, 724, "Lavandería\nSur"),
        ],
        "varios": [
            (424, 247, "Sala Juegos\n2N"),
            (760, 454, "Sótano\nSur"),
            (808, 725, "Talleres\nSur"),
        ],
        "protecciones": [
            (397, 129, "Almacén\nNorte"),
            (892, 78,  "Economato\nNorte"),
            (617, 651, "Sala TV\nSur"),
        ],
        "aprendices": [
            (558, 158, "Patio Int.\n1N"),
            (850, 125, "Distribuidor\nInterior"),
            (1061, 425, "Distribuidor\nInterior"),
        ],
        "accesos_principales": [
            # Números en círculos rojos del mapa (aprox)
            (558, 160, "1"), (558, 130, "2"),
            (118, 263, "3"), (224, 272, "4"),
            (1253, 517, "2"), (1294, 622, "5"),
            (1360, 726, "6"), (394, 131, "7"),
            (843, 200, "8"), (1055, 451, "9"),
            (565, 229, "10"), (517, 572, "11"),
            (39,  239, "12"), (280, 192, "13"),
            (155, 191, "14"), (1090, 381, "15"),
            (1384, 724, "16"), (735, 408, "17"),
            (687, 672, "18"), (576, 600, "19"),
            (1011, 210, "20"), (39, 357, "21"),
        ],
        "accesos_secundarios": [
            (449, 598, ""),   # flecha verde izq
            (952, 623, ""),   # flecha verde der
        ],
    }

    def __init__(self, parent, map_path: str):
        self.parent   = parent
        self.map_path = map_path

        # Estado zoom/pan
        self._zoom        = 1.0
        self._offset_x    = 0.0
        self._offset_y    = 0.0
        self._drag_start  = None
        self._drag_offset = (0, 0)

        # Imagen PIL original
        self._img_original: Image.Image | None = None
        self._img_tk: ImageTk.PhotoImage | None = None

        # Visibilidad de capas
        self._layer_visible = {k: True for k, *_ in LEGEND_ITEMS}
        self._layer_btns    = {}

        # Canvas items de iconos { clave: [item_id, ...] }
        self._icon_items: dict[str, list[int]] = {k: [] for k, *_ in LEGEND_ITEMS}

        # Búsqueda de sala
        self._search_hits: list     = []
        self._search_hit_idx: int   = -1

        self._build_window()
        self._load_image()
        self._center_map()
        self._render()

    # ── CONSTRUCCIÓN UI ──────────────────────────────────────────────
    def _build_window(self):
        self.win = ctk.CTkToplevel(self.parent)
        self.win.title("MAPA — La Prisión 2026")
        self.win.geometry("1440x860")
        self.win.minsize(900, 600)
        self.win.configure(fg_color=BG_MAIN)
        self.win.grab_set()
        self.win.focus_force()
        self.win.protocol("WM_DELETE_WINDOW", self._on_close)

        # Layout: header | body (canvas + panel_dcho)
        self.win.grid_rowconfigure(1, weight=1)
        self.win.grid_columnconfigure(0, weight=1)

        self._build_header()
        self._build_body()

    def _build_header(self):
        hdr = ctk.CTkFrame(self.win, fg_color=BG_CARD,
                           corner_radius=0, height=46,
                           border_width=1, border_color=BORDER_COL)
        hdr.grid(row=0, column=0, sticky="ew")
        hdr.grid_propagate(False)
        hdr.grid_columnconfigure(2, weight=1)

        # Logo
        ctk.CTkLabel(hdr, text="  ⛓  MAPA DE LA PRISIÓN",
                     font=("Segoe UI", 15, "bold"),
                     text_color=ACCENT_CYAN
                     ).grid(row=0, column=0, padx=(14, 6), pady=8, sticky="w")

        ctk.CTkLabel(hdr, text="Zoom · Arrastra · Leyenda",
                     font=("Segoe UI", 10),
                     text_color=TEXT_DIM
                     ).grid(row=0, column=1, padx=6, pady=8, sticky="w")

        # Controles de zoom
        zoom_frame = ctk.CTkFrame(hdr, fg_color=BG_PANEL_INNER,
                                  corner_radius=8,
                                  border_width=1, border_color=BORDER_COL)
        zoom_frame.grid(row=0, column=3, padx=8, pady=6, sticky="e")

        for col, (txt, cmd, col_fg) in enumerate([
            ("−", self._zoom_out,    "#FF2A2A"),
            ("+", self._zoom_in,     ACCENT_GREEN),
            ("⊙", self._center_map,  ACCENT_CYAN),
        ]):
            ctk.CTkButton(zoom_frame, text=txt, width=36, height=30,
                          font=("Segoe UI", 14, "bold"),
                          fg_color="#1E2230", hover_color="#2A3050",
                          text_color=col_fg,
                          corner_radius=6,
                          command=cmd
                          ).grid(row=0, column=col, padx=4, pady=4)

        # Label zoom %
        self._zoom_label = ctk.CTkLabel(zoom_frame, text="100%",
                                        font=("Consolas", 10, "bold"),
                                        text_color=TEXT_DIM, width=44)
        self._zoom_label.grid(row=0, column=3, padx=(2, 6))

        # Botón cerrar
        ctk.CTkButton(hdr, text="✕  CERRAR",
                      width=90, height=30,
                      font=("Segoe UI", 10, "bold"),
                      fg_color="#2A0A0A", hover_color="#440F0F",
                      text_color=ACCENT_RED,
                      corner_radius=6,
                      command=self._on_close
                      ).grid(row=0, column=4, padx=(4, 12), pady=6)

    def _build_body(self):
        body = ctk.CTkFrame(self.win, fg_color=BG_MAIN, corner_radius=0)
        body.grid(row=1, column=0, sticky="nsew")
        body.grid_rowconfigure(0, weight=1)
        body.grid_columnconfigure(0, weight=1)

        # ── Canvas del mapa ──
        self.canvas = tk.Canvas(body,
                                bg="#0a0c10",
                                highlightthickness=0,
                                cursor="fleur")
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Bindings del canvas
        self.canvas.bind("<ButtonPress-1>",   self._on_drag_start)
        self.canvas.bind("<B1-Motion>",        self._on_drag_move)
        self.canvas.bind("<ButtonRelease-1>",  self._on_drag_end)
        self.canvas.bind("<ButtonPress-2>",    self._on_drag_start)
        self.canvas.bind("<B2-Motion>",        self._on_drag_move)
        self.canvas.bind("<ButtonRelease-2>",  self._on_drag_end)
        self.canvas.bind("<MouseWheel>",       self._on_mousewheel)
        self.canvas.bind("<Button-4>",         self._on_mousewheel)
        self.canvas.bind("<Button-5>",         self._on_mousewheel)
        self.canvas.bind("<Configure>",        self._on_canvas_resize)

        # ── Panel lateral: leyenda ──
        self._build_legend_panel(body)

    def _build_legend_panel(self, parent):
        panel = ctk.CTkFrame(parent, fg_color=BG_CARD,
                             corner_radius=0, width=220,
                             border_width=1, border_color=BORDER_COL)
        panel.grid(row=0, column=1, sticky="ns")
        panel.grid_propagate(False)
        panel.grid_rowconfigure(9, weight=1)


        # ── Título leyenda ─────────────────────────────────────────────
        ctk.CTkLabel(panel, text="LEYENDA",
                     font=("Segoe UI", 11, "bold"),
                     text_color=ACCENT_CYAN
                     ).pack(pady=(6, 4), padx=14, anchor="w")

        ctk.CTkLabel(panel,
                     text="Clic para mostrar/ocultar",
                     font=("Segoe UI", 9),
                     text_color=TEXT_DIM
                     ).pack(padx=14, anchor="w")

        sep = ctk.CTkFrame(panel, fg_color=BORDER_COL, height=1, corner_radius=0)
        sep.pack(fill="x", padx=10, pady=(8, 6))

        for key, label, color, symbol in LEGEND_ITEMS:
            row_frame = ctk.CTkFrame(panel, fg_color=BG_PANEL_INNER,
                                     corner_radius=8,
                                     border_width=1, border_color=BORDER_COL)
            row_frame.pack(fill="x", padx=10, pady=3)
            row_frame.grid_columnconfigure(1, weight=1)

            # Dot de color
            ctk.CTkLabel(row_frame, text=symbol, width=20,
                         font=("Segoe UI", 14, "bold"),
                         text_color=color
                         ).grid(row=0, column=0, padx=(8, 4), pady=6)

            # Etiqueta
            ctk.CTkLabel(row_frame, text=label,
                         font=("Segoe UI", 10),
                         text_color=TEXT_MAIN,
                         anchor="w", justify="left",
                         wraplength=130
                         ).grid(row=0, column=1, padx=4, pady=6, sticky="w")

            # Toggle ON/OFF
            btn = ctk.CTkButton(row_frame, text="ON", width=38, height=22,
                                font=("Segoe UI", 9, "bold"),
                                fg_color="#1a3a1a", hover_color="#254525",
                                text_color=ACCENT_GREEN,
                                corner_radius=4,
                                command=lambda k=key: self._toggle_layer(k))
            btn.grid(row=0, column=2, padx=(4, 8), pady=6)
            self._layer_btns[key] = btn

        sep2 = ctk.CTkFrame(panel, fg_color=BORDER_COL, height=1, corner_radius=0)
        sep2.pack(fill="x", padx=10, pady=(6, 4))

        # Botones globales
        btns_frame = ctk.CTkFrame(panel, fg_color=BG_PANEL_INNER,
                                   corner_radius=8,
                                   border_width=1, border_color=BORDER_COL)
        btns_frame.pack(fill="x", padx=10, pady=4)

        for txt, cmd, col in [
            ("Mostrar todo",  self._show_all,  ACCENT_GREEN),
            ("Ocultar todo",  self._hide_all,  "#FF6644"),
        ]:
            ctk.CTkButton(btns_frame, text=txt, height=28,
                          font=("Segoe UI", 10, "bold"),
                          fg_color="#1E2230", hover_color="#2A3050",
                          text_color=col,
                          corner_radius=6,
                          command=cmd
                          ).pack(fill="x", padx=8, pady=3)

        # Info footer
        sep3 = ctk.CTkFrame(panel, fg_color=BORDER_COL, height=1, corner_radius=0)
        sep3.pack(fill="x", padx=10, pady=(6, 4))

        info = (
            "Rueda  → Zoom\n"
            "Arrastre → Mover\n"
            "⊙ → Centrar"
        )
        ctk.CTkLabel(panel, text=info,
                     font=("Consolas", 9),
                     text_color=TEXT_DIM,
                     justify="left"
                     ).pack(padx=14, pady=(4, 14), anchor="w")

    # ── CARGA DE IMAGEN ──────────────────────────────────────────────
    def _load_image(self):
        if not PIL_OK:
            messagebox.showerror("Error",
                "Pillow no está instalado.\npip install Pillow")
            return
        try:
            self._img_original = Image.open(self.map_path).convert("RGBA")
        except FileNotFoundError:
            messagebox.showerror("Mapa no encontrado",
                f"No se encontró el archivo:\n{self.map_path}\n\n"
                "Copia Mapa.png en la misma carpeta que AriaBot.py")

    # ── CENTRADO INICIAL ─────────────────────────────────────────────
    def _center_map(self):
        """Pone el zoom al 100%, centra el mapa en el canvas y limpia búsqueda."""
        self.win.update_idletasks()
        cw = self.canvas.winfo_width()  or 1200
        ch = self.canvas.winfo_height() or 800
        if self._img_original is None:
            return
        iw, ih = self._img_original.size
        self._zoom     = 1.0
        self._offset_x = (cw - iw) / 2
        self._offset_y = (ch - ih) / 2
        # Limpiar búsqueda activa
        self._search_hits      = []
        self._search_hit_idx   = -1
        try:
            self._search_var.set("")
            self._search_status_lbl.configure(text="", text_color=TEXT_DIM)
        except AttributeError:
            pass  # aún no construida la UI
        self._render()

    # ── RENDER ───────────────────────────────────────────────────────
    def _render(self):
        """Redibuja el canvas completo: imagen + iconos de leyenda."""
        if self._img_original is None:
            return
        self.canvas.delete("all")
        self._icon_items = {k: [] for k, *_ in LEGEND_ITEMS}

        cw = self.canvas.winfo_width()  or 1200
        ch = self.canvas.winfo_height() or 800

        iw, ih = self._img_original.size
        nw = max(1, int(iw * self._zoom))
        nh = max(1, int(ih * self._zoom))

        # Dibujar fondo oscuro
        self.canvas.create_rectangle(0, 0, cw, ch, fill="#08090e", outline="")

        # Escalar imagen
        try:
            resamp = Image.Resampling.LANCZOS
        except AttributeError:
            resamp = Image.ANTIALIAS  # Pillow < 9

        scaled = self._img_original.resize((nw, nh), resamp)
        self._img_tk = ImageTk.PhotoImage(scaled)

        ox = int(self._offset_x)
        oy = int(self._offset_y)
        self.canvas.create_image(ox, oy, anchor="nw", image=self._img_tk)

        # Borde sutil alrededor del mapa
        self.canvas.create_rectangle(
            ox - 1, oy - 1, ox + nw + 1, oy + nh + 1,
            outline="#1E2230", width=1
        )

        # Dibujar iconos de leyenda
        self._draw_icons()

        # Actualizar label de zoom
        self._zoom_label.configure(text=f"{int(self._zoom * 100)}%")

    def _draw_icons(self):
        """Dibuja iconos sobre el mapa para cada capa visible."""
        legend_map = {k: (col, sym) for k, _, col, sym in LEGEND_ITEMS}
        ox, oy = int(self._offset_x), int(self._offset_y)

        # Conjunto de hits activos para resaltado rápido
        hit_set = set()
        active_hit = None
        if self._search_hits:
            for i, (hkey, hmx, hmy, _) in enumerate(self._search_hits):
                hit_set.add((hkey, hmx, hmy))
            if 0 <= self._search_hit_idx < len(self._search_hits):
                h = self._search_hits[self._search_hit_idx]
                active_hit = (h[0], h[1], h[2])

        for key, positions in self.ICON_POSITIONS.items():
            if not self._layer_visible.get(key, True):
                continue
            color, symbol = legend_map.get(key, ("#ffffff", "●"))
            for (mx, my, label) in positions:
                # Coordenadas en canvas
                cx = ox + int(mx * self._zoom)
                cy = oy + int(my * self._zoom)

                # Radio del icono escalado (mín 5px, máx 18px)
                r = max(5, min(18, int(9 * self._zoom)))
                fs = max(7, min(14, int(8 * self._zoom)))

                is_hit    = (key, mx, my) in hit_set
                is_active = (key, mx, my) == active_hit

                # Halo exterior para hits de búsqueda
                if is_active:
                    # Halo blanco pulsante para el hit activo
                    hr = r + max(4, int(5 * self._zoom))
                    self.canvas.create_oval(
                        cx - hr, cy - hr, cx + hr, cy + hr,
                        fill="", outline="#FFFFFF",
                        width=max(2, int(2.5 * self._zoom))
                    )
                    self.canvas.create_oval(
                        cx - hr - 4, cy - hr - 4, cx + hr + 4, cy + hr + 4,
                        fill="", outline=color,
                        width=1, dash=(4, 3)
                    )
                elif is_hit:
                    # Halo tenue para el resto de hits
                    hr = r + max(3, int(3 * self._zoom))
                    self.canvas.create_oval(
                        cx - hr, cy - hr, cx + hr, cy + hr,
                        fill="", outline=color,
                        width=max(1, int(1.5 * self._zoom)), dash=(3, 3)
                    )

                # Sombra
                self.canvas.create_oval(
                    cx - r + 1, cy - r + 1, cx + r + 1, cy + r + 1,
                    fill="#000000", outline="", stipple="gray50"
                )
                # Relleno — más brillante si es hit activo
                fill_color = "#2a2a1a" if is_active else "#1a1a2a"
                self.canvas.create_oval(
                    cx - r, cy - r, cx + r, cy + r,
                    fill=fill_color,
                    outline="#FFFFFF" if is_active else color,
                    width=max(2, int(2 * self._zoom)) if is_active else max(1, int(1.5 * self._zoom))
                )
                # Símbolo central
                if label:
                    self.canvas.create_text(
                        cx, cy,
                        text=label,
                        font=("Segoe UI", fs, "bold"),
                        fill="#FFFFFF" if is_active else color,
                        anchor="center"
                    )
                else:
                    self.canvas.create_text(
                        cx, cy,
                        text=symbol,
                        font=("Segoe UI", fs),
                        fill="#FFFFFF" if is_active else color,
                        anchor="center"
                    )

    # ── ZOOM ─────────────────────────────────────────────────────────
    def _set_zoom(self, new_zoom: float, pivot_x: float = None, pivot_y: float = None):
        """Aplica nuevo zoom conservando el punto de pivote en pantalla."""
        new_zoom = max(self.ZOOM_MIN, min(self.ZOOM_MAX, new_zoom))
        if new_zoom == self._zoom:
            return

        cw = self.canvas.winfo_width()  or 1200
        ch = self.canvas.winfo_height() or 800

        # Si no hay pivote, usar el centro del canvas
        if pivot_x is None:
            pivot_x = cw / 2
        if pivot_y is None:
            pivot_y = ch / 2

        # Mantener el punto bajo el cursor
        ratio = new_zoom / self._zoom
        self._offset_x = pivot_x - (pivot_x - self._offset_x) * ratio
        self._offset_y = pivot_y - (pivot_y - self._offset_y) * ratio
        self._zoom     = new_zoom
        self._render()

    def _zoom_in(self):
        self._set_zoom(self._zoom + self.ZOOM_STEP)

    def _zoom_out(self):
        self._set_zoom(self._zoom - self.ZOOM_STEP)

    def _on_mousewheel(self, event):
        # Windows/Mac: event.delta; Linux: Button-4/5
        if event.num == 4 or (hasattr(event, 'delta') and event.delta > 0):
            factor = 1 + self.ZOOM_WHEEL
        else:
            factor = 1 - self.ZOOM_WHEEL
        self._set_zoom(self._zoom * factor,
                       pivot_x=event.x, pivot_y=event.y)

    # ── PAN / DRAG ───────────────────────────────────────────────────
    def _on_drag_start(self, event):
        self.canvas.configure(cursor="fleur")
        self._drag_start  = (event.x, event.y)
        self._drag_offset = (self._offset_x, self._offset_y)

    def _on_drag_move(self, event):
        if self._drag_start is None:
            return
        dx = event.x - self._drag_start[0]
        dy = event.y - self._drag_start[1]
        self._offset_x = self._drag_offset[0] + dx
        self._offset_y = self._drag_offset[1] + dy
        self._render()

    def _on_drag_end(self, event):
        self.canvas.configure(cursor="fleur")
        self._drag_start = None

    # ── RESIZE ───────────────────────────────────────────────────────
    def _on_canvas_resize(self, event):
        # Solo re-render si tenemos imagen cargada
        if self._img_original is not None:
            self._render()

    # ── BÚSQUEDA DE SALA ─────────────────────────────────────────────
    def _do_search(self):
        """Busca salas cuya etiqueta contenga el texto introducido."""
        q = self._search_var.get().strip().lower()
        self._search_hits  = []
        self._search_hit_idx = -1

        if not q:
            self._search_status_lbl.configure(text="", text_color=TEXT_DIM)
            self._render()
            return

        for key, positions in self.ICON_POSITIONS.items():
            for (mx, my, label) in positions:
                if q in label.lower().replace("\n", " "):
                    self._search_hits.append((key, mx, my, label))

        total = len(self._search_hits)
        if total == 0:
            self._search_status_lbl.configure(
                text="Sin resultados.", text_color="#FF6644"
            )
            self._render()
            return

        self._search_hit_idx = 0
        self._search_status_lbl.configure(
            text=f"1 / {total}", text_color=ACCENT_GREEN
        )
        self._render()
        self._jump_to_hit(0)

    def _search_next(self):
        if not self._search_hits:
            return
        self._search_hit_idx = (self._search_hit_idx + 1) % len(self._search_hits)
        total = len(self._search_hits)
        self._search_status_lbl.configure(
            text=f"{self._search_hit_idx + 1} / {total}", text_color=ACCENT_GREEN
        )
        self._render()
        self._jump_to_hit(self._search_hit_idx)

    def _search_prev(self):
        if not self._search_hits:
            return
        self._search_hit_idx = (self._search_hit_idx - 1) % len(self._search_hits)
        total = len(self._search_hits)
        self._search_status_lbl.configure(
            text=f"{self._search_hit_idx + 1} / {total}", text_color=ACCENT_GREEN
        )
        self._render()
        self._jump_to_hit(self._search_hit_idx)

    def _jump_to_hit(self, idx: int):
        """Centra el canvas en el icono encontrado y hace zoom si es necesario."""
        if idx < 0 or idx >= len(self._search_hits):
            return
        _, mx, my, _ = self._search_hits[idx]

        # Zoom mínimo de 1.5 para que el icono sea visible
        target_zoom = max(1.5, self._zoom)
        if abs(target_zoom - self._zoom) > 0.01:
            self._zoom = target_zoom

        cw = self.canvas.winfo_width()  or 1200
        ch = self.canvas.winfo_height() or 800
        # Calcular offset para que el punto quede en el centro del canvas
        self._offset_x = cw / 2 - mx * self._zoom
        self._offset_y = ch / 2 - my * self._zoom
        self._render()

    # ── LEYENDA TOGGLES ──────────────────────────────────────────────
    def _toggle_layer(self, key: str):
        self._layer_visible[key] = not self._layer_visible[key]
        visible = self._layer_visible[key]
        btn = self._layer_btns.get(key)
        if btn:
            if visible:
                btn.configure(text="ON",
                              fg_color="#1a3a1a",
                              text_color=ACCENT_GREEN)
            else:
                btn.configure(text="OFF",
                              fg_color="#3a1a1a",
                              text_color="#FF6644")
        self._render()

    def _show_all(self):
        for key in self._layer_visible:
            self._layer_visible[key] = True
            btn = self._layer_btns.get(key)
            if btn:
                btn.configure(text="ON",
                              fg_color="#1a3a1a",
                              text_color=ACCENT_GREEN)
        self._render()

    def _hide_all(self):
        for key in self._layer_visible:
            self._layer_visible[key] = False
            btn = self._layer_btns.get(key)
            if btn:
                btn.configure(text="OFF",
                              fg_color="#3a1a1a",
                              text_color="#FF6644")
        self._render()

    # ── CIERRE ───────────────────────────────────────────────────────
    def _on_close(self):
        # Limpiar imagen de memoria antes de destruir
        self._img_tk       = None
        self._img_original = None
        try:
            self.win.destroy()
        except Exception:
            pass


# ══════════════════════════════════════════════════════════════════════
#  FUNCIÓN PÚBLICA — usada por AriaBot para abrir/cerrar
# ══════════════════════════════════════════════════════════════════════
_mapa_window_ref: MapaVentana | None = None


def abrir_mapa(parent, base_dir: str = None) -> None:
    """
    Abre la ventana del mapa (o la trae al frente si ya está abierta).

    Parámetros
    ----------
    parent   : widget raíz de AriaBot (root o cualquier CTk widget)
    base_dir : directorio donde está Mapa.png; si es None usa el directorio
               del script/exe actual.
    """
    global _mapa_window_ref

    # Cerrar si ya existe
    if _mapa_window_ref is not None:
        try:
            if _mapa_window_ref.win.winfo_exists():
                _mapa_window_ref.win.focus_force()
                return
        except Exception:
            _mapa_window_ref = None

    # Resolver ruta del mapa
    if base_dir is None:
        if getattr(sys, 'frozen', False):
            base_dir = os.path.dirname(os.path.abspath(sys.executable))
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))

    map_path = os.path.join(base_dir, MAP_FILENAME)

    if not PIL_OK:
        messagebox.showerror(
            "Pillow no instalado",
            "El módulo Pillow es necesario para mostrar el mapa.\n"
            "Instálalo con:  pip install Pillow"
        )
        return

    _mapa_window_ref = MapaVentana(parent, map_path)


def cerrar_mapa() -> None:
    """Cierra la ventana del mapa si está abierta."""
    global _mapa_window_ref
    if _mapa_window_ref is not None:
        try:
            _mapa_window_ref._on_close()
        except Exception:
            pass
        _mapa_window_ref = None


def toggle_mapa(parent, base_dir: str = None) -> None:
    """Abre si está cerrado, cierra si está abierto."""
    global _mapa_window_ref
    if _mapa_window_ref is not None:
        try:
            if _mapa_window_ref.win.winfo_exists():
                cerrar_mapa()
                return
        except Exception:
            _mapa_window_ref = None
    abrir_mapa(parent, base_dir)


# ══════════════════════════════════════════════════════════════════════
#  STANDALONE — prueba sin AriaBot
# ══════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    root.withdraw()   # ocultar raíz
    abrir_mapa(root)
    root.mainloop()


# ══════════════════════════════════════════════════════════════════════
#  FRAGMENTO DE INTEGRACIÓN PARA AriaBot.py
# ══════════════════════════════════════════════════════════════════════
"""
─────────────────────────────────────────────────────────────────────
PASO 1 — En el bloque de imports locales de AriaBot.py añadir:

    try:
        import mapa_prision as _mapa_module
    except ImportError:
        _mapa_module = None

─────────────────────────────────────────────────────────────────────
PASO 2 — Añadir función toggle (antes del bloque de UI):

    def toggle_mapa():
        if _mapa_module is None:
            messagebox.showerror("Módulo no encontrado",
                "No se encontró mapa_prision.py.\\n"
                "Cópialo junto a AriaBot.py.")
            return
        _mapa_module.toggle_mapa(root, BASE_DIR)

─────────────────────────────────────────────────────────────────────
PASO 3 — Añadir botón en hotkey_box (después del botón de Banderas):

    ctk.CTkButton(
        hotkey_box,
        text="🗺 Mapa de La Prisión",
        font=("Segoe UI", 11, "bold"),
        fg_color="#0a1a2a",
        text_color="#00F0FF",
        hover_color="#0d2233",
        command=toggle_mapa,
    ).grid(row=10, column=0, sticky="ew", padx=10, pady=(0, 10))

─────────────────────────────────────────────────────────────────────
ARCHIVOS NECESARIOS en la misma carpeta que AriaBot.py:
    · mapa_prision.py
    · Mapa.png
─────────────────────────────────────────────────────────────────────
"""
