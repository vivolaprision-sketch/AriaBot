# =====================================================================

# AriaBot v1.0

# Developed by: SMaSeR 2026

# =====================================================================



# ================= IMPORTACIONES =================

import sys

import ctypes



# ================= AUTOELEVACIÓN A ADMINISTRADOR =================

def _relaunch_as_admin():

    if not ctypes.windll.shell32.IsUserAnAdmin():

        if getattr(sys, 'frozen', False):

            # Compilado como .exe: sys.executable es el propio exe,
            # los args reales son sys.argv[1:] (sin el nombre del exe)
            params = " ".join(f'"{a}"' for a in sys.argv[1:])

        else:

            # Script .py: el interprete recibe el script como arg[0]
            params = " ".join(f'"{a}"' for a in sys.argv)

        ctypes.windll.shell32.ShellExecuteW(

            None, "runas",

            sys.executable,

            params,

            None, 1

        )

        sys.exit(0)



_relaunch_as_admin()

# ================= ICONO EN BARRA DE TAREAS =================
try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("SMaSeR.AriaBot.1.0")
except Exception:
    pass

# ================= OCULTAR CONSOLA =================

try:

    hwnd_console = ctypes.windll.kernel32.GetConsoleWindow()

    if hwnd_console != 0:

        ctypes.windll.user32.ShowWindow(hwnd_console, 0)

except Exception:

    pass



# ================= RESTO DE DEPENDENCIAS =================

try:

    import time

    import base64

    import random

    import json

    import threading

    import os

    from datetime import datetime

    import customtkinter as ctk

    import tkinter as tk

    from tkinter import simpledialog, filedialog, messagebox

    import pyautogui

    import keyboard as kb

    import cv2

    import numpy as np

    from PIL import Image, ImageTk, ImageGrab

    import requests

    import mss

    from plyer import notification

    # ── Generador de Banderas (módulo local) ──
    try:
        import flag_generator as _fg_module
    except ImportError:
        _fg_module = None

    # ── Guía de La Prisión (módulo local) ──
    try:
        import guia_laprision as _guia_module
    except ImportError:
        _guia_module = None

    # ── Mapa de La Prisión (módulo local) ──
    try:
        import mapa_prision as _mapa_module
    except ImportError:
        _mapa_module = None

except Exception as e:

    print(f"[ERROR CRÍTICO] Fallo al cargar dependencias: {e}")

    input("Presione Enter para salir...")

    sys.exit(1)





# ================= CONFIGURACIÓN DE RED =================

SERVER_URL = "https://smaser.pythonanywhere.com"

SECRET_KEY = "ARIABOTSMASER2026SECRETOABSOLUTOPEPE"

HEADERS    = {"X-AriaBot-Secret": SECRET_KEY}





# ================= ESCALADO DPI =================

try:

    ctypes.windll.shcore.SetProcessDpiAwareness(1)

except Exception:

    try:

        ctypes.windll.user32.SetProcessDPIAware()

    except Exception:

        pass





# ================= CONFIGURACIÓN GLOBAL =================

pyautogui.FAILSAFE = False

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")



BG_MAIN        = "#0F1015"

BG_CARD        = "#161822"

ACCENT_CYAN    = "#00F0FF"

ACCENT_GREEN   = "#00FF88"

ACCENT_RED     = "#FF2A2A"

BG_PANEL_INNER = "#0B0C10"





# ================= RUTAS DEL SISTEMA =================

if getattr(sys, 'frozen', False):
    # En --onefile el exe real está en sys.executable, no en _MEIPASS
    BASE_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))



TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

SAVE_FILE     = os.path.join(BASE_DIR, "Secuencias.json")

HOTKEYS_FILE  = os.path.join(BASE_DIR, "hotkeys.json")

os.makedirs(TEMPLATES_DIR, exist_ok=True)


# ================= HOTKEYS CONFIGURABLES =================
# Valores por defecto. Se sobreescriben al cargar hotkeys.json
HOTKEYS = {
    "guardia":   "f4",
    "autoclick": "f5",
    "afk":       "f6",
    "grabar":    "f7",
    "captura":   "f8",
    "banderas":  "f9",
    "guia":      "f10",
    "mapa":      "f11",
    "detener":   "f12",
}

# Descripción legible para cada acción (para la leyenda)
HOTKEY_DESCS = {
    "guardia":   "Activar/Desactivar Guardia",
    "autoclick": "Autoclick Continuo",
    "afk":       "Loop Evasión AFK",
    "grabar":    "Iniciar / Detener Grabación",
    "captura":   "Capturar Imagen",
    "banderas":  "Banderas",
    "guia":      "Guía de La Prisión",
    "mapa":      "Mapa de La Prisión",
    "detener":   "DETENER TODO",
}


def _load_hotkeys():
    """Carga hotkeys desde hotkeys.json si existe."""
    global HOTKEYS
    try:
        if os.path.exists(HOTKEYS_FILE):
            with open(HOTKEYS_FILE, "r", encoding="utf-8") as f:
                saved = json.load(f)
            for k in HOTKEYS:
                if k in saved and isinstance(saved[k], str):
                    HOTKEYS[k] = saved[k].lower()
    except Exception as e:
        print(f"[HOTKEYS] Error al cargar hotkeys.json: {e}")


def _save_hotkeys():
    """Guarda la configuración actual de hotkeys en hotkeys.json."""
    try:
        with open(HOTKEYS_FILE, "w", encoding="utf-8") as f:
            json.dump(HOTKEYS, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[HOTKEYS] Error al guardar hotkeys.json: {e}")


_load_hotkeys()





# ================= TESSERACT EMBEBIDO =================

TESSERACT_OK = False



def _configurar_tesseract():

    global TESSERACT_OK

    try:

        import pytesseract

        import shutil



        ruta_embebida = os.path.join(BASE_DIR, "Tesseract-OCR", "tesseract.exe")

        ruta_global = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        ruta_path = shutil.which("tesseract")



        if os.path.isfile(ruta_embebida):

            pytesseract.pytesseract.tesseract_cmd = ruta_embebida

            TESSERACT_OK = True

            print(f"[TESSERACT] Cargado desde instalacion embebida: {ruta_embebida}")

        elif os.path.isfile(ruta_global):

            pytesseract.pytesseract.tesseract_cmd = ruta_global

            TESSERACT_OK = True

            print(f"[TESSERACT] Cargado desde instalacion global: {ruta_global}")

        elif ruta_path:

            pytesseract.pytesseract.tesseract_cmd = ruta_path

            TESSERACT_OK = True

            print(f"[TESSERACT] Cargado desde PATH del sistema: {ruta_path}")

        else:

            TESSERACT_OK = False

            print("[TESSERACT] ADVERTENCIA: tesseract.exe no encontrado. La Guardia Anti-Nivel no estara disponible.")



    except ImportError:

        TESSERACT_OK = False

        print("[TESSERACT] ADVERTENCIA: modulo pytesseract no disponible.")



_configurar_tesseract()





# ================= RESOLUCIÓN BASE =================

SCREEN_W, SCREEN_H = pyautogui.size()





# ================= ESTADO GLOBAL =================

clicking         = False

anti_afk_active  = False

sequence_running = False

recording_macro  = False

_capture_active  = False   # bloquea capturas simultáneas



# Bloqueo de ratón durante autoclick

bloquear_raton   = False   # opción activable por el usuario

_locked_pos      = None    # posición donde se activa el bloqueo

_lock_mouse_stop = threading.Event()



templates            = {}

log_lines            = []

master_sequences     = {"Secuencia 1": []}

current_sequence_key = "Secuencia 1"

mouse_listener       = None

key_listener         = None



_last_f5_time  = 0

_last_f6_time  = 0



levelup_watch_active  = False

_levelup_stop_event   = threading.Event()

LEVELUP_KEYWORDS      = [

    "has subido de nivel",

    "subido de nivel",

    "level up",

    "you have gained a level",

    "has ganado un nivel",

    "nuevo nivel",

]

CHAT_REL = {"left": 0.0, "top": 0.82, "right": 0.60, "bottom": 0.98}



try:

    sct = mss.mss()

except Exception:

    sct = None





# ================= NOTIFICACIONES (visible sobre juegos fullscreen) =================
# Usa una ventana Win32 nativa HWND_TOPMOST + WS_EX_TOPMOST + WS_EX_TOOLWINDOW
# dibujada directamente con GDI. No depende de librerías de toast ni del sistema
# de notificaciones de Windows. Funciona sobre DirectX fullscreen en Windows 10/11.

_overlay_lock = threading.Lock()

def enviar_burbuja(titulo, mensaje):
    """Muestra un banner flotante siempre encima de cualquier ventana, incluido
    juegos en pantalla completa. Se cierra solo tras 3 segundos."""

    def _mostrar():
        with _overlay_lock:
            try:
                _mostrar_overlay_win32(titulo, mensaje)
            except Exception:
                # Fallback: plyer como último recurso
                try:
                    notification.notify(
                        title=titulo,
                        message=mensaje,
                        app_name="AriaBot",
                        timeout=3,
                    )
                except Exception:
                    pass

    threading.Thread(target=_mostrar, daemon=True).start()


def _mostrar_overlay_win32(titulo, mensaje, duracion_ms=3000):
    """Crea una ventana GDI sin bordes, siempre en primer plano, en la esquina
    superior derecha. Usa la API Win32 directamente via ctypes."""

    user32   = ctypes.windll.user32
    gdi32    = ctypes.windll.gdi32
    kernel32 = ctypes.windll.kernel32

    # ── Constantes Win32 ──────────────────────────────────────────────────────
    WS_POPUP         = 0x80000000
    WS_VISIBLE       = 0x10000000
    WS_EX_TOPMOST    = 0x00000008
    WS_EX_TOOLWINDOW = 0x00000080
    WS_EX_LAYERED    = 0x00080000
    CS_HREDRAW       = 0x0002
    CS_VREDRAW       = 0x0001
    IDC_ARROW        = 32512
    WM_DESTROY       = 0x0002
    WM_PAINT         = 0x000F
    WM_TIMER         = 0x0113
    WM_LBUTTONDOWN   = 0x0201
    PS_SOLID         = 0
    DT_SINGLELINE    = 0x00000020
    DT_WORDBREAK     = 0x00000010
    DT_NOCLIP        = 0x00000100
    TRANSPARENT_BK   = 1
    LWA_ALPHA        = 0x00000002
    LF_FACESIZE      = 32
    FW_NORMAL        = 400
    FW_BOLD          = 700
    DEFAULT_CHARSET  = 1
    OUT_DEFAULT_PRECIS   = 0
    CLIP_DEFAULT_PRECIS  = 0
    CLEARTYPE_QUALITY    = 5
    DEFAULT_PITCH        = 0

    # ── Dimensiones y posición ────────────────────────────────────────────────
    sw = user32.GetSystemMetrics(0)
    W, H   = 360, 80
    margin = 18
    x = sw - W - margin
    y = margin

    # ── Colores GDI (COLORREF = 0x00BBGGRR) ──────────────────────────────────
    COLOR_BG     = 0x00201510
    COLOR_BORDER = 0x00FF6600
    COLOR_TITLE  = 0x00FFFF00
    COLOR_MSG    = 0x00E0E0E0

    # ── Estructuras ───────────────────────────────────────────────────────────
    class PAINTSTRUCT(ctypes.Structure):
        _fields_ = [
            ("hdc",         ctypes.c_void_p),
            ("fErase",      ctypes.c_int),
            ("rcPaint",     ctypes.c_int * 4),
            ("fRestore",    ctypes.c_int),
            ("fIncUpdate",  ctypes.c_int),
            ("rgbReserved", ctypes.c_byte * 32),
        ]

    class RECT(ctypes.Structure):
        _fields_ = [("left", ctypes.c_long), ("top",    ctypes.c_long),
                    ("right",ctypes.c_long), ("bottom", ctypes.c_long)]

    class LOGFONTW(ctypes.Structure):
        _fields_ = [
            ("lfHeight",          ctypes.c_long),
            ("lfWidth",           ctypes.c_long),
            ("lfEscapement",      ctypes.c_long),
            ("lfOrientation",     ctypes.c_long),
            ("lfWeight",          ctypes.c_long),
            ("lfItalic",          ctypes.c_byte),
            ("lfUnderline",       ctypes.c_byte),
            ("lfStrikeOut",       ctypes.c_byte),
            ("lfCharSet",         ctypes.c_byte),
            ("lfOutPrecision",    ctypes.c_byte),
            ("lfClipPrecision",   ctypes.c_byte),
            ("lfQuality",         ctypes.c_byte),
            ("lfPitchAndFamily",  ctypes.c_byte),
            ("lfFaceName",        ctypes.c_wchar * LF_FACESIZE),
        ]

    def make_font(height, weight):
        lf = LOGFONTW()
        lf.lfHeight        = height
        lf.lfWidth         = 0
        lf.lfWeight        = weight
        lf.lfCharSet       = DEFAULT_CHARSET
        lf.lfOutPrecision  = OUT_DEFAULT_PRECIS
        lf.lfClipPrecision = CLIP_DEFAULT_PRECIS
        lf.lfQuality       = CLEARTYPE_QUALITY
        lf.lfPitchAndFamily = DEFAULT_PITCH
        lf.lfFaceName      = "Segoe UI"
        return gdi32.CreateFontIndirectW(ctypes.byref(lf))

    WNDPROCTYPE = ctypes.WINFUNCTYPE(
        ctypes.c_long, ctypes.c_void_p, ctypes.c_uint,
        ctypes.c_ulonglong, ctypes.c_longlong
    )

    def wnd_proc(hwnd, msg, wparam, lparam):
        if msg == WM_PAINT:
            ps = PAINTSTRUCT()
            hdc = user32.BeginPaint(hwnd, ctypes.byref(ps))

            # Fondo
            rc_full = RECT(0, 0, W, H)
            hbr_bg = gdi32.CreateSolidBrush(COLOR_BG)
            user32.FillRect(hdc, ctypes.byref(rc_full), hbr_bg)
            gdi32.DeleteObject(hbr_bg)

            # Borde
            hpen     = gdi32.CreatePen(PS_SOLID, 2, COLOR_BORDER)
            old_pen  = gdi32.SelectObject(hdc, hpen)
            hbr_null = gdi32.GetStockObject(5)   # NULL_BRUSH
            old_br   = gdi32.SelectObject(hdc, hbr_null)
            gdi32.Rectangle(hdc, 1, 1, W - 1, H - 1)
            gdi32.SelectObject(hdc, old_pen)
            gdi32.SelectObject(hdc, old_br)
            gdi32.DeleteObject(hpen)

            gdi32.SetBkMode(hdc, TRANSPARENT_BK)

            # Título
            hfont_t  = make_font(-16, FW_BOLD)
            old_font = gdi32.SelectObject(hdc, hfont_t)
            gdi32.SetTextColor(hdc, COLOR_TITLE)
            rc_t = RECT(12, 8, W - 12, 30)
            user32.DrawTextW(hdc, titulo, -1, ctypes.byref(rc_t),
                             DT_SINGLELINE | DT_NOCLIP)
            gdi32.SelectObject(hdc, old_font)
            gdi32.DeleteObject(hfont_t)

            # Mensaje
            hfont_m  = make_font(-13, FW_NORMAL)
            old_font = gdi32.SelectObject(hdc, hfont_m)
            gdi32.SetTextColor(hdc, COLOR_MSG)
            rc_m = RECT(12, 32, W - 12, H - 8)
            user32.DrawTextW(hdc, mensaje, -1, ctypes.byref(rc_m),
                             DT_WORDBREAK | DT_NOCLIP)
            gdi32.SelectObject(hdc, old_font)
            gdi32.DeleteObject(hfont_m)

            user32.EndPaint(hwnd, ctypes.byref(ps))
            return 0

        elif msg in (WM_TIMER, WM_LBUTTONDOWN):
            user32.KillTimer(hwnd, 1)
            user32.DestroyWindow(hwnd)
            return 0

        elif msg == WM_DESTROY:
            user32.PostQuitMessage(0)
            return 0

        return user32.DefWindowProcW(hwnd, msg, wparam, lparam)

    wnd_proc_c = WNDPROCTYPE(wnd_proc)

    class WNDCLASSW(ctypes.Structure):
        _fields_ = [
            ("style",         ctypes.c_uint),
            ("lpfnWndProc",   WNDPROCTYPE),
            ("cbClsExtra",    ctypes.c_int),
            ("cbWndExtra",    ctypes.c_int),
            ("hInstance",     ctypes.c_void_p),
            ("hIcon",         ctypes.c_void_p),
            ("hCursor",       ctypes.c_void_p),
            ("hbrBackground", ctypes.c_void_p),
            ("lpszMenuName",  ctypes.c_wchar_p),
            ("lpszClassName", ctypes.c_wchar_p),
        ]

    hinstance  = kernel32.GetModuleHandleW(None)
    class_name = f"AriaBotOverlay_{id(wnd_proc_c)}"

    wc = WNDCLASSW()
    wc.style         = CS_HREDRAW | CS_VREDRAW
    wc.lpfnWndProc   = wnd_proc_c
    wc.hInstance     = hinstance
    wc.hCursor       = user32.LoadCursorW(None, IDC_ARROW)
    wc.hbrBackground = gdi32.CreateSolidBrush(COLOR_BG)
    wc.lpszClassName = class_name

    user32.RegisterClassW(ctypes.byref(wc))

    hwnd = user32.CreateWindowExW(
        WS_EX_TOPMOST | WS_EX_TOOLWINDOW | WS_EX_LAYERED,
        class_name,
        "AriaBot",
        WS_POPUP | WS_VISIBLE,
        x, y, W, H,
        None, None, hinstance, None
    )

    if not hwnd:
        return

    # ~90% de opacidad
    user32.SetLayeredWindowAttributes(hwnd, 0, 230, LWA_ALPHA)

    # Forzar TOPMOST incluso sobre DirectX fullscreen
    HWND_TOPMOST = ctypes.c_void_p(-1)
    SWP_NOMOVE   = 0x0002
    SWP_NOSIZE   = 0x0001
    user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE)

    user32.ShowWindow(hwnd, 5)
    user32.UpdateWindow(hwnd)
    user32.SetTimer(hwnd, 1, duracion_ms, None)

    class MSG(ctypes.Structure):
        _fields_ = [
            ("hwnd",    ctypes.c_void_p),
            ("message", ctypes.c_uint),
            ("wParam",  ctypes.c_ulonglong),
            ("lParam",  ctypes.c_longlong),
            ("time",    ctypes.c_uint),
            ("pt",      ctypes.c_long * 2),
        ]

    msg = MSG()
    while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) > 0:
        user32.TranslateMessage(ctypes.byref(msg))
        user32.DispatchMessageW(ctypes.byref(msg))

    try:
        user32.UnregisterClassW(class_name, hinstance)
    except Exception:
        pass





# ================= SISTEMA DE REGISTRO (LOG) =================

def _update_log_ui():

    try:

        log_text.configure(state="normal")

        log_text.delete("1.0", "end")

        log_text.insert("end", "\n".join(log_lines))

        log_text.configure(state="disabled")

        log_text.see("end")

    except Exception:

        pass



def log(text):

    timestamp = datetime.now().strftime("%H:%M:%S")

    msg = f"[{timestamp}] {text}"

    log_lines.append(msg)

    if len(log_lines) > 150:

        log_lines.pop(0)

    root.after(0, _update_log_ui)





# ================= INTERFAZ: INDICADORES DE ESTADO =================

def update_status_indicators():

    status_autoclick.configure(

        text="● ACTIVO" if clicking else "○ INACTIVO",

        text_color=ACCENT_GREEN if clicking else "#555566",

    )

    status_seq.configure(

        text="● EN EJECUCIÓN" if sequence_running else "○ EN ESPERA",

        text_color=ACCENT_CYAN if sequence_running else "#555566",

    )

    status_afk.configure(

        text="● ACTIVO" if anti_afk_active else "○ INACTIVO",

        text_color=ACCENT_GREEN if anti_afk_active else "#555566",

    )

    status_levelup.configure(

        text="● VIGILANDO" if levelup_watch_active else "○ INACTIVO",

        text_color="#BB44FF" if levelup_watch_active else "#555566",

    )

    if recording_macro:

        btn_toggle_record.configure(

            text=f"Detener Grabación ({HOTKEYS['grabar'].upper()})",

            fg_color=ACCENT_RED,

            hover_color="#C02020",

        )

    else:

        btn_toggle_record.configure(

            text=f"Iniciar Grabación ({HOTKEYS['grabar'].upper()})",

            fg_color="#2b8a3e",

            hover_color="#236B32",

        )





# ================= MÓDULO DE GRABACIÓN =================

def rec_on_click(x, y, button, pressed):

    if not recording_macro or not pressed:

        return

    p_delay = step_delay_slider.get()

    step_data = {

        "type":   "coordinate",

        "x":      x,

        "y":      y,

        "rel_x":  x / SCREEN_W,

        "rel_y":  y / SCREEN_H,

        "delay":  p_delay,

        "speed":  0.05,

        "target": "",

    }

    master_sequences[current_sequence_key].append(step_data)

    log(f"[INFO] Clic registrado: ({x}, {y})")

    root.after(10, update_timeline_view)



def rec_on_press(key):

    if not recording_macro:

        return



    if hasattr(key, "name") and key.name:

        key_name = key.name

    elif hasattr(key, "char") and key.char:

        key_name = key.char

    else:

        key_name = str(key)



    if isinstance(key_name, str) and key_name.lower() in {

        v.lower() for v in HOTKEYS.values()

    }:

        return



    seq = master_sequences[current_sequence_key]

    if seq and seq[-1]["type"] == "key" and seq[-1]["target"] == key_name:

        return



    p_delay = step_delay_slider.get()

    step_data = {

        "type":   "key",

        "x":      0,

        "y":      0,

        "delay":  p_delay,

        "speed":  0.0,

        "target": key_name,

    }

    master_sequences[current_sequence_key].append(step_data)

    log(f"[INFO] Tecla registrada: [{key_name}]")

    root.after(10, update_timeline_view)



def toggle_macro_recording():

    global recording_macro, mouse_listener, key_listener

    try:

        from pynput import mouse as pynput_mouse, keyboard as pynput_kb

    except ImportError:

        log("[ERROR] Biblioteca 'pynput' no encontrada. Instálela con: pip install pynput")

        return



    if not recording_macro:

        recording_macro = True

        log(f"[INFO] Grabación iniciada en: '{current_sequence_key}'.")

        enviar_burbuja("AriaBot", "Grabación iniciada (F7)")

        mouse_listener = pynput_mouse.Listener(on_click=rec_on_click)

        key_listener   = pynput_kb.Listener(on_press=rec_on_press)

        mouse_listener.start()

        key_listener.start()

    else:

        recording_macro = False

        log("[INFO] Grabación finalizada.")

        enviar_burbuja("AriaBot", "Grabación finalizada")

        if mouse_listener:

            mouse_listener.stop()

        if key_listener:

            key_listener.stop()

        save_data()

    root.after(0, update_status_indicators)



def toggle_macro_recording_hotkey():

    root.after(10, toggle_macro_recording)



def capture_template_region_hotkey():

    root.after(10, capture_template_region)



def toggle_levelup_watch_hotkey():

    root.after(10, toggle_levelup_watch)





# ================= GESTOR DE SECUENCIAS =================

def change_sequence(new_seq):

    global current_sequence_key

    current_sequence_key = new_seq

    log(f"[INFO] Secuencia activa: {new_seq}")

    update_timeline_view()



def add_new_sequence():

    global current_sequence_key

    name = simpledialog.askstring("Nueva Secuencia", "Introduzca el nombre de la secuencia:")

    if not name or not name.strip():

        return

    name_clean = name.strip()

    if name_clean in master_sequences:

        messagebox.showwarning("Advertencia", "El nombre especificado ya existe.")

        return

    master_sequences[name_clean] = []

    current_sequence_key = name_clean

    combo_sequences.configure(values=list(master_sequences.keys()))

    combo_sequences.set(current_sequence_key)

    log(f"[INFO] Secuencia creada: {current_sequence_key}")

    update_timeline_view()

    save_data()



def actualizar_combobox():

    if 'combo_sequences' in globals():

        combo_sequences.configure(values=list(master_sequences.keys()))

        if current_sequence_key in master_sequences:

            combo_sequences.set(current_sequence_key)



def delete_current_sequence():

    global current_sequence_key

    if len(master_sequences) <= 1:

        messagebox.showwarning("No permitido", "No puedes eliminar la única secuencia que queda.")

        return

    if not messagebox.askyesno("Confirmación", f"¿Desea eliminar de forma permanente '{current_sequence_key}'?"):

        return

    del master_sequences[current_sequence_key]

    current_sequence_key = list(master_sequences.keys())[0]

    combo_sequences.configure(values=list(master_sequences.keys()))

    combo_sequences.set(current_sequence_key)

    log("[INFO] Secuencia eliminada del sistema.")

    update_timeline_view()

    save_data()





# ================= GESTOR DE TIMELINE =================

def add_pure_delay_step():

    p_delay = step_delay_slider.get()

    master_sequences[current_sequence_key].append(

        {"type": "delay", "x": 0, "y": 0, "delay": p_delay, "speed": 0.0, "target": ""}

    )

    log(f"[INFO] Pausa insertada: {p_delay}s")

    update_timeline_view()

    save_data()



def move_step_up(index):

    seq = master_sequences[current_sequence_key]

    if index > 0:

        seq[index], seq[index - 1] = seq[index - 1], seq[index]

        update_timeline_view()

        save_data()



def move_step_down(index):

    seq = master_sequences[current_sequence_key]

    if index < len(seq) - 1:

        seq[index], seq[index + 1] = seq[index + 1], seq[index]

        update_timeline_view()

        save_data()



def remove_step_by_index(index):

    seq = master_sequences[current_sequence_key]

    if 0 <= index < len(seq):

        seq.pop(index)

        log(f"[INFO] Paso #{index + 1} eliminado.")

        update_timeline_view()

        save_data()



def change_step_delay(index, val_str):

    try:

        seq = master_sequences.get(current_sequence_key, [])

        if 0 <= index < len(seq):

            seq[index]["delay"] = float(val_str)

            save_data()

    except (ValueError, IndexError):

        pass



def clear_sequence():

    master_sequences[current_sequence_key] = []

    log("[INFO] La secuencia actual ha sido restablecida.")

    update_timeline_view()

    save_data()



def link_image_to_step(template_name, step_idx_str):

    try:

        idx = int(step_idx_str) - 1

        seq = master_sequences[current_sequence_key]

        if 0 <= idx < len(seq):

            seq[idx]["type"]   = "image"

            seq[idx]["target"] = template_name

            log(f"[INFO] Imagen '{template_name}' asignada al paso #{idx + 1}")

            update_timeline_view()

            save_data()

        else:

            messagebox.showwarning("Advertencia", "El número de paso no existe en la secuencia.")

    except ValueError:

        messagebox.showerror("Error", "Introduce un número de paso válido.")



def update_timeline_view():

    for child in timeline_scroll.winfo_children():

        child.destroy()



    timeline_scroll.grid_columnconfigure(0, weight=1)



    seq = master_sequences.get(current_sequence_key, [])

    if not seq:

        ctk.CTkLabel(

            timeline_scroll,

            text="[ Secuencia vacía. Inicie la grabación o inserte una pausa ]",

            text_color="#555566",

            font=("Segoe UI", 12, "italic"),

        ).grid(row=0, column=0, pady=40)

        return



    for index, step in enumerate(seq):

        row_frame = ctk.CTkFrame(

            timeline_scroll,

            fg_color="#141622",

            corner_radius=6,

            border_width=1,

            border_color="#222533",

            height=35,

        )

        row_frame.grid(row=index, column=0, sticky="ew", padx=5, pady=3)

        row_frame.grid_propagate(False)

        row_frame.grid_columnconfigure(1, weight=1)



        ctk.CTkLabel(row_frame, text=f"#{index + 1:02d}",

                     font=("Consolas", 11, "bold"),

                     text_color=ACCENT_CYAN, width=35

                     ).grid(row=0, column=0, padx=5, sticky="w")



        stype = step["type"]

        if stype == "image":

            desc_text = f"Buscar imagen: '{step['target']}'"

        elif stype == "coordinate":

            desc_text = f"Clic en: ({step['x']}, {step['y']})"

        elif stype == "key":

            desc_text = f"Tecla: [{step['target']}]"

        elif stype == "delay":

            desc_text = "Pausa (espera)"

        else:

            desc_text = "Paso desconocido"



        ctk.CTkLabel(row_frame, text=desc_text, font=("Segoe UI", 11), anchor="w"

                     ).grid(row=0, column=1, padx=5, sticky="ew")



        actions_frame = ctk.CTkFrame(row_frame, fg_color="transparent")

        actions_frame.grid(row=0, column=2, padx=5, sticky="e")



        ctk.CTkLabel(actions_frame, text="Pausa (s):", font=("Segoe UI", 10),

                     text_color="#6A6E85").grid(row=0, column=0, padx=2)



        delay_entry = ctk.CTkEntry(

            actions_frame, width=40, height=22,

            font=("Consolas", 10), fg_color=BG_PANEL_INNER, border_color="#333",

        )

        delay_entry.insert(0, str(step["delay"]))

        delay_entry.grid(row=0, column=1, padx=2)

        delay_entry.bind("<FocusOut>",

                         lambda e, idx=index, en=delay_entry: change_step_delay(idx, en.get()))

        delay_entry.bind("<Return>",

                         lambda e, idx=index, en=delay_entry: change_step_delay(idx, en.get()))



        ctk.CTkButton(actions_frame, text="↑", width=24, height=24,

                      fg_color="#1E2230", hover_color=ACCENT_CYAN,

                      command=lambda idx=index: move_step_up(idx)

                      ).grid(row=0, column=2, padx=2)



        ctk.CTkButton(actions_frame, text="↓", width=24, height=24,

                      fg_color="#1E2230", hover_color=ACCENT_CYAN,

                      command=lambda idx=index: move_step_down(idx)

                      ).grid(row=0, column=3, padx=2)



        ctk.CTkButton(actions_frame, text="X", width=24, height=24,

                      fg_color="transparent", hover_color=ACCENT_RED,

                      text_color="#A0A5C0",

                      command=lambda idx=index: remove_step_by_index(idx)

                      ).grid(row=0, column=4, padx=2)





# ================= VISIÓN ARTIFICIAL =================

def capture_template_region():

    global _capture_active

    if _capture_active:

        return

    _capture_active = True

    log("[SISTEMA] Captura de región activada. Selecciona el área en pantalla.")

    enviar_burbuja("AriaBot", "Captura de Región Activada (F8)")

    root.withdraw()

    selector = tk.Toplevel()

    selector.attributes("-fullscreen", True)

    selector.attributes("-alpha", 0.3)

    selector.attributes("-topmost", True)

    selector.configure(bg="black")

    canvas = tk.Canvas(selector, bg="black", highlightthickness=0)

    canvas.pack(fill="both", expand=True)

    start_x = start_y = end_x = end_y = 0

    rect = None



    def on_press(event):

        nonlocal start_x, start_y, rect

        start_x, start_y = event.x, event.y

        rect = canvas.create_rectangle(start_x, start_y, start_x, start_y,

                                       outline=ACCENT_CYAN, width=3)



    def on_drag(event):

        nonlocal end_x, end_y

        end_x, end_y = event.x, event.y

        canvas.coords(rect, start_x, start_y, end_x, end_y)



    def on_release(event):
        global _capture_active
        nonlocal end_x, end_y
        end_x, end_y = event.x, event.y
        selector.destroy()
        root.deiconify()

        if abs(end_x - start_x) < 10 or abs(end_y - start_y) < 10:
            log("[ADVERTENCIA] Selección demasiado pequeña, cancelada.")
            _capture_active = False
            return

        left   = min(start_x, end_x)
        top    = min(start_y, end_y)
        right  = max(start_x, end_x)
        bottom = max(start_y, end_y)

        name = simpledialog.askstring("Guardar Imagen", "Ponle un nombre a esta captura:")
        if not name:
            _capture_active = False
            return
        name_clean = name.strip().replace(" ", "_")
        path = os.path.join(TEMPLATES_DIR, f"{name_clean}.png")

        # Pequeña pausa para que la ventana de AriaBot no aparezca en la captura
        root.withdraw()
        time.sleep(0.15)
        screenshot = ImageGrab.grab()
        root.deiconify()

        screenshot.crop((left, top, right, bottom)).save(path, "PNG")



        meta = {"screen_w": SCREEN_W, "screen_h": SCREEN_H}

        meta_path = os.path.join(TEMPLATES_DIR, f"{name_clean}_meta.json")

        with open(meta_path, "w", encoding="utf-8") as mf:

            json.dump(meta, mf)



        img = cv2.imread(path)

        if img is not None:

            templates[name_clean] = img

            log(f"[ÉXITO] Imagen guardada: {name_clean}.png")

            update_template_scroll_view()

        else:

            log("[ERROR] No se pudo guardar la imagen capturada.")

        _capture_active = False



    canvas.bind("<ButtonPress-1>", on_press)

    canvas.bind("<B1-Motion>", on_drag)

    canvas.bind("<ButtonRelease-1>", on_release)

    def on_escape(e):

        global _capture_active

        selector.destroy()

        root.deiconify()

        log("[INFO] Selección de región cancelada por el usuario.")

        _capture_active = False

    selector.bind("<Escape>", on_escape)



def find_template_and_return_coords(name, conf=0.78):

    if name not in templates:

        return None

    template = templates[name]



    orig_w, orig_h = SCREEN_W, SCREEN_H

    meta_path = os.path.join(TEMPLATES_DIR, f"{name}_meta.json")

    if os.path.exists(meta_path):

        try:

            with open(meta_path, "r", encoding="utf-8") as mf:

                meta = json.load(mf)

                orig_w = meta.get("screen_w", SCREEN_W)

                orig_h = meta.get("screen_h", SCREEN_H)

        except Exception:

            pass



    screenshot = ImageGrab.grab()

    screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    cur_h, cur_w = screen.shape[:2]



    scale_x = cur_w / orig_w

    scale_y = cur_h / orig_h

    scale   = (scale_x + scale_y) / 2



    if abs(scale - 1.0) > 0.05:

        interp = cv2.INTER_AREA if scale < 1.0 else cv2.INTER_CUBIC

        scaled_template = cv2.resize(template, None, fx=scale, fy=scale, interpolation=interp)

    else:

        scaled_template = template



    th, tw = scaled_template.shape[:2]

    if cur_h < th or cur_w < tw:

        log(f"[ADVERTENCIA] La imagen '{name}' es más grande que la pantalla actual.")

        return None



    res = cv2.matchTemplate(screen, scaled_template, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= conf)

    for pt in zip(*loc[::-1]):

        return pt[0] + tw // 2, pt[1] + th // 2

    return None





# ================= NÚCLEO DE EJECUCIÓN =================

def toggle_sequence_execution():

    global sequence_running

    seq = master_sequences.get(current_sequence_key, [])

    if not seq:

        log("[ADVERTENCIA] No hay instrucciones registradas en la secuencia activa.")

        return



    if sequence_running:

        sequence_running = False

        log("[SISTEMA] Ejecución de secuencia detenida.")

        enviar_burbuja("AriaBot", "Secuencia Detenida")

        update_status_indicators()

        return



    sequence_running = True

    update_status_indicators()

    log(f"[SISTEMA] Iniciando procesamiento: {current_sequence_key}")

    enviar_burbuja("AriaBot", f"Secuencia Iniciada: {current_sequence_key}")

    threading.Thread(target=master_sequence_loop, daemon=True).start()



def master_sequence_loop():
    global sequence_running
    seq_key = current_sequence_key   # instantánea al arrancar la ejecución
    while sequence_running:
        cur_w, cur_h = pyautogui.size()
        seq = list(master_sequences.get(seq_key, []))   # copia para evitar mutaciones durante el loop
        if not seq:
            time.sleep(0.2)
            continue
        for step in seq:
            if not sequence_running:
                break
            try:
                stype = step["type"]
                if stype == "delay":
                    time.sleep(step["delay"])

                elif stype == "coordinate":
                    if "rel_x" in step and "rel_y" in step:
                        abs_x = int(step["rel_x"] * cur_w)
                        abs_y = int(step["rel_y"] * cur_h)
                    else:
                        abs_x, abs_y = step["x"], step["y"]
                    pyautogui.moveTo(abs_x, abs_y, duration=step.get("speed", 0.05))
                    pyautogui.click()
                    time.sleep(step["delay"])

                elif stype == "key":
                    kb.press_and_release(step["target"])
                    time.sleep(step["delay"])

                elif stype == "image":
                    coords = find_template_and_return_coords(step["target"], conf=0.78)
                    if coords:
                        pyautogui.moveTo(coords[0], coords[1], duration=0.05)
                        pyautogui.click()
                        time.sleep(step["delay"])
                    else:
                        time.sleep(0.1)

            except Exception as ex:
                log(f"[ERROR] Excepción en paso tipo '{step.get('type','?')}': {ex}")

        time.sleep(0.1)



def toggle_autoclick():

    global clicking, _last_f5_time, _locked_pos, _lock_mouse_stop

    if time.time() - _last_f5_time < 0.5:

        return

    _last_f5_time = time.time()



    if clicking:

        clicking = False

        _lock_mouse_stop.set()

        log("[INFO] Autoclick desactivado.")

        enviar_burbuja("AriaBot", "Autoclick desactivado")

        root.after(0, update_status_indicators)

        return



    # Guardar posición actual si el bloqueo está activado

    if bloquear_raton:

        _locked_pos = pyautogui.position()

        log(f"[INFO] Ratón bloqueado en ({_locked_pos.x}, {_locked_pos.y})")



    clicking = True

    _lock_mouse_stop.clear()

    log("[INFO] Autoclick activado.")

    enviar_burbuja("AriaBot", "Autoclick activado (F5)")

    root.after(0, update_status_indicators)

    threading.Thread(target=autoclick_loop, daemon=True).start()

    if bloquear_raton and _locked_pos:

        threading.Thread(target=_mouse_lock_loop, daemon=True).start()



def autoclick_loop():
    while clicking:
        pyautogui.click()
        # Lee el slider en cada iteración para respetar cambios en tiempo real
        try:
            interval = max(0.01, step_delay_slider.get())
        except Exception:
            interval = 0.05
        time.sleep(interval + random.uniform(-0.005, 0.01))



def _mouse_lock_loop():

    """Mantiene el ratón fijo en la posición guardada mientras autoclick esté activo."""

    while clicking and bloquear_raton and _locked_pos:

        try:

            cur = pyautogui.position()

            if abs(cur.x - _locked_pos.x) > 2 or abs(cur.y - _locked_pos.y) > 2:

                ctypes.windll.user32.SetCursorPos(_locked_pos.x, _locked_pos.y)

        except Exception:

            pass

        _lock_mouse_stop.wait(timeout=0.016)  # ~60 veces por segundo



def toggle_anti_afk():

    global anti_afk_active, _last_f6_time

    if time.time() - _last_f6_time < 0.5:

        return

    _last_f6_time = time.time()



    if anti_afk_active:

        anti_afk_active = False

        log("[INFO] Anti-AFK desactivado.")

        enviar_burbuja("AriaBot", "Anti-AFK desactivado")

        root.after(0, update_status_indicators)

        return

    anti_afk_active = True

    log("[INFO] Anti-AFK activado.")

    enviar_burbuja("AriaBot", "Anti-AFK activado (F6)")

    root.after(0, update_status_indicators)

    threading.Thread(target=afk_loop, daemon=True).start()



def afk_loop():

    while anti_afk_active:

        try:

            cur_w, cur_h = pyautogui.size()

            pyautogui.moveTo(

                random.randint(int(cur_w * 0.15), int(cur_w * 0.85)),

                random.randint(int(cur_h * 0.15), int(cur_h * 0.85)),

                duration=0.3,

            )

            if random.random() < 0.4:

                kb.press_and_release(random.choice(["w", "a", "s", "d", "space"]))

        except Exception:

            pass

        time.sleep(random.randint(40, 80))



def stop_all():
    global clicking, anti_afk_active, sequence_running, recording_macro, _capture_active
    clicking = anti_afk_active = sequence_running = _capture_active = False
    _lock_mouse_stop.set()

    # Detener grabación directamente sin pasar por el toggle
    if recording_macro:
        recording_macro = False
        if mouse_listener:
            try: mouse_listener.stop()
            except Exception: pass
        if key_listener:
            try: key_listener.stop()
            except Exception: pass
        save_data()

    enviar_burbuja("AriaBot", "Todo detenido (F9)")
    root.after(0, update_status_indicators)
    log("[SISTEMA] Todo detenido.")





# ================= VIGILANCIA DE SUBIDA DE NIVEL =================

def toggle_levelup_watch():

    global levelup_watch_active

    levelup_watch_active = not levelup_watch_active

    if levelup_watch_active:

        _levelup_stop_event.clear()

        log("[NIVEL] Guardia Anti-Nivel activada.")

        enviar_burbuja("AriaBot", "Guardia Anti-Nivel activada (F4)")

        threading.Thread(target=_levelup_watch_loop, daemon=True).start()

    else:

        _levelup_stop_event.set()

        log("[NIVEL] Guardia Anti-Nivel desactivada.")

        enviar_burbuja("AriaBot", "Guardia Anti-Nivel desactivada")

    root.after(0, _update_levelup_btn)

    root.after(0, update_status_indicators)



def _update_levelup_btn():

    try:

        if levelup_watch_active:

            btn_levelup_watch.configure(

                text="● VIGILANDO NIVEL  (click para desactivar)",

                fg_color="#7B2FBE",

                hover_color="#5A1E8C",

            )

        else:

            btn_levelup_watch.configure(

                text="Activar Guardia Anti-Nivel",

                fg_color="#1E2230",

                hover_color="#2A3050",

            )

    except Exception:

        pass



def _levelup_watch_loop():
    global levelup_watch_active

    if sct is None:
        root.after(0, lambda: log("[GUARDIA] ERROR: mss no disponible."))
        levelup_watch_active = False
        root.after(0, _update_levelup_btn)
        return

    if not TESSERACT_OK:
        root.after(0, lambda: log(f"[GUARDIA] ERROR: Tesseract no disponible. Ruta buscada: {os.path.join(BASE_DIR, 'Tesseract-OCR', 'tesseract.exe')} — existe: {os.path.isfile(os.path.join(BASE_DIR, 'Tesseract-OCR', 'tesseract.exe'))}"))
        levelup_watch_active = False
        root.after(0, _update_levelup_btn)
        return



    import pytesseract

    import concurrent.futures



    log("[NIVEL] Hilo de vigilancia iniciado. Leyendo chat cada 2 segundos.")



    def _hacer_ocr():

        sw, sh = pyautogui.size()

        left   = int(CHAT_REL["left"]   * sw)

        top    = int(CHAT_REL["top"]    * sh)

        right  = int(CHAT_REL["right"]  * sw)

        bottom = int(CHAT_REL["bottom"] * sh)

        width  = right - left

        height = bottom - top



        monitor = {"top": top, "left": left, "width": width, "height": height}

        screenshot = np.array(sct.grab(monitor))

        img_bgr = screenshot[:, :, :3]



        img_cv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

        lower_yellow = np.array([18,  80, 150])

        upper_yellow = np.array([38, 255, 255])

        mask_yellow  = cv2.inRange(img_cv, lower_yellow, upper_yellow)



        if cv2.countNonZero(mask_yellow) > 30:

            ocr_img = cv2.bitwise_not(mask_yellow)

        else:

            gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

            _, ocr_img = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)



        h, w = ocr_img.shape[:2]

        ocr_img = cv2.resize(ocr_img, (w * 2, h * 2), interpolation=cv2.INTER_CUBIC)

        ocr_pil = Image.fromarray(ocr_img)



        return pytesseract.image_to_string(

            ocr_pil, lang="spa+eng", config="--psm 6"

        ).lower()



    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:

        while levelup_watch_active:

            try:

                future = executor.submit(_hacer_ocr)

                texto  = future.result(timeout=8)



                for keyword in LEVELUP_KEYWORDS:

                    if keyword in texto:

                        root.after(0, lambda k=keyword: log(

                            f"[NIVEL] ⚠ SUBIDA DE NIVEL DETECTADA → '{k}'"

                        ))

                        root.after(50, lambda: log(

                            "[NIVEL] Deteniendo bot y cerrando el juego con Alt+F4..."

                        ))

                        root.after(100, _ejecutar_emergencia_nivel)

                        return



            except concurrent.futures.TimeoutError:

                root.after(0, lambda: log(

                    "[NIVEL] Advertencia: OCR tardó más de 8s, ciclo saltado."

                ))

            except Exception as ex:

                root.after(0, lambda e=ex: log(f"[NIVEL] Error en captura OCR: {e}"))



            _levelup_stop_event.wait(timeout=2)

            if _levelup_stop_event.is_set():

                break



def _ejecutar_emergencia_nivel():
    """Llamada siempre desde root.after() → hilo UI.
    Las operaciones bloqueantes (sleep, subprocess) se delegan a un hilo worker."""

    global clicking, anti_afk_active, sequence_running, levelup_watch_active

    clicking             = False
    anti_afk_active      = False
    sequence_running     = False
    levelup_watch_active = False

    root.after(0, update_status_indicators)
    root.after(0, _update_levelup_btn)

    # Las llamadas bloqueantes van a un hilo separado para no congelar la UI
    def _worker():
        time.sleep(0.5)
        try:
            import subprocess
            subprocess.run(
                ["powershell", "-Command",
                 "$w = Get-Process | Where-Object {$_.MainWindowTitle -like '*Prision*' -or $_.MainWindowTitle -like '*Prison*'} | Select-Object -First 1; "
                 "if ($w) { [void][System.Runtime.InteropServices.RuntimeEnvironment]::GetRuntimeDirectory(); "
                 "Add-Type -AssemblyName Microsoft.VisualBasic; "
                 "[Microsoft.VisualBasic.Interaction]::AppActivate($w.Id) }"],
                capture_output=True, timeout=3
            )
        except Exception:
            pass
        time.sleep(0.3)
        kb.press_and_release("alt+f4")
        root.after(0, lambda: log("[NIVEL] Alt+F4 enviado. Bot detenido por protección de nivel."))
        enviar_burbuja("⚠️ SEGURIDAD", "¡SUBIDA DE NIVEL DETECTADA! Juego cerrado.")

    threading.Thread(target=_worker, daemon=True).start()





# ================= GESTIÓN DE DEPENDENCIAS VISUALES =================

def load_template():

    path = filedialog.askopenfilename(filetypes=[("PNG", "*.png")])

    if not path:

        return

    filename = os.path.splitext(os.path.basename(path))[0]

    img = cv2.imread(path)

    if img is not None:

        templates[filename] = img

        log(f"[ÉXITO] Archivo gráfico importado: {filename}")

        update_template_scroll_view()

    else:

        log(f"[ERROR] No se pudo cargar la imagen: {path}")



def delete_image_file(name):

    if not messagebox.askyesno("Confirmar", f"¿Eliminar la imagen '{name}'?"):

        return

    for ext in [".png", "_meta.json"]:

        fpath = os.path.join(TEMPLATES_DIR, f"{name}{ext}")

        if os.path.exists(fpath):

            try:

                os.remove(fpath)

            except OSError as e:

                log(f"[ERROR] Fallo de escritura en disco: {e}")

    templates.pop(name, None)

    update_template_scroll_view()



def update_template_scroll_view():

    for child in template_scroll.winfo_children():

        child.destroy()



    template_scroll.grid_columnconfigure(0, weight=1)



    for row_idx, t_name in enumerate(templates):

        frame = ctk.CTkFrame(template_scroll, fg_color="#141622", height=42,

                             corner_radius=6, border_width=1, border_color="#222533")

        frame.grid(row=row_idx, column=0, sticky="ew", padx=5, pady=4)

        frame.grid_propagate(False)

        frame.grid_columnconfigure(0, weight=1)



        ctk.CTkLabel(frame, text=t_name, anchor="w",

                     font=("Segoe UI", 11)).grid(row=0, column=0, sticky="ew", padx=10)



        ctk.CTkLabel(frame, text="Paso:", font=("Segoe UI", 11),

                     text_color="#A0A5C0").grid(row=0, column=1, padx=2)



        step_entry = ctk.CTkEntry(frame, width=32, height=22, font=("Consolas", 11))

        step_entry.grid(row=0, column=2, padx=2)



        ctk.CTkButton(frame, text="Asignar", width=50, height=22, fg_color="#1E2230",

                      font=("Segoe UI", 10),

                      command=lambda n=t_name, e=step_entry: link_image_to_step(n, e.get())

                      ).grid(row=0, column=3, padx=2)



        ctk.CTkButton(frame, text="Eliminar", width=50, height=22, fg_color="transparent",

                      font=("Segoe UI", 10), hover_color=ACCENT_RED,

                      border_width=1, border_color="#333",

                      command=lambda n=t_name: delete_image_file(n)

                      ).grid(row=0, column=4, padx=5)





# ================= PERSISTENCIA DE DATOS =================

def save_data():

    try:

        with open(SAVE_FILE, "w", encoding="utf-8") as f:

            json.dump({"sequences": master_sequences}, f,

                      ensure_ascii=False, indent=2)

    except Exception as e:

        log(f"[ERROR] Error al guardar los datos: {e}")



def load_data():

    global master_sequences, current_sequence_key

    try:

        if os.path.exists(SAVE_FILE):

            with open(SAVE_FILE, "r", encoding="utf-8") as f:

                data = json.load(f)

            if "sequences" in data:

                master_sequences = data["sequences"]

            elif "master_sequence" in data:

                master_sequences = {"Secuencia 1": data["master_sequence"]}

            if master_sequences:

                current_sequence_key = list(master_sequences.keys())[0]



        for file in os.listdir(TEMPLATES_DIR):

            if file.endswith(".png"):

                name = os.path.splitext(file)[0]

                img = cv2.imread(os.path.join(TEMPLATES_DIR, file))

                if img is not None:

                    templates[name] = img

    except Exception as e:

        print(f"[ERROR] Error al cargar los datos guardados: {e}")



    if not master_sequences:

        master_sequences = {"Secuencia 1": []}

        current_sequence_key = "Secuencia 1"





# ================= SERVICIOS CLOUD =================

def abrir_ventana_subir():

    seq = master_sequences.get(current_sequence_key, [])

    if not seq:

        messagebox.showwarning("Advertencia", "La secuencia activa está vacía. Graba algunos pasos primero.")

        return



    top = ctk.CTkToplevel(root)

    top.title("Publicación de Contenido")

    top.geometry("400x450")

    top.attributes("-topmost", True)

    _set_icon(top)

    top.grid_columnconfigure(0, weight=1)



    ctk.CTkLabel(top, text="SUBIR SECUENCIA",

                 font=("Segoe UI", 14, "bold"), text_color=ACCENT_CYAN

                 ).grid(row=0, column=0, sticky="ew", padx=30, pady=(20, 10))



    ctk.CTkLabel(top, text="Nombre de la secuencia:", anchor="w"

                 ).grid(row=1, column=0, sticky="w", padx=30)

    ent_nombre = ctk.CTkEntry(top, placeholder_text="Nombre descriptivo")

    ent_nombre.grid(row=2, column=0, sticky="ew", padx=30, pady=(0, 10))



    ctk.CTkLabel(top, text="Autor:", anchor="w"

                 ).grid(row=3, column=0, sticky="w", padx=30)

    ent_autor = ctk.CTkEntry(top, placeholder_text="Tu nombre")

    ent_autor.grid(row=4, column=0, sticky="ew", padx=30, pady=(0, 10))



    ctk.CTkLabel(top, text="Descripción:", anchor="w"

                 ).grid(row=5, column=0, sticky="w", padx=30)

    txt_desc = ctk.CTkTextbox(top, height=80)

    txt_desc.grid(row=6, column=0, sticky="ew", padx=30, pady=(0, 15))



    def confirmar_subida():

        nom = ent_nombre.get().strip()

        aut = ent_autor.get().strip()

        seq = master_sequences[current_sequence_key]



        images_data = {}

        meta_data   = {}

        for step in seq:

            if step["type"] == "image":

                img_path = os.path.join(TEMPLATES_DIR, f"{step['target']}.png")

                if os.path.exists(img_path):

                    with open(img_path, "rb") as f:

                        images_data[step['target']] = base64.b64encode(f.read()).decode('utf-8')

                meta_path = os.path.join(TEMPLATES_DIR, f"{step['target']}_meta.json")

                if os.path.exists(meta_path):

                    with open(meta_path, "r", encoding="utf-8") as mf:

                        meta_data[step['target']] = json.load(mf)



        payload = {

            "name":        nom.replace(" ", "_"),

            "author":      aut,

            "description": txt_desc.get("1.0", "end-1c").strip(),

            "sequence":    seq,

            "images":      images_data,

            "images_meta": meta_data,

        }



        try:

            res = requests.post(f"{SERVER_URL}/upload", json=payload, headers=HEADERS, timeout=10)

            if res.status_code == 200:

                log(f"[ÉXITO] Secuencia '{nom}' subida correctamente al servidor.")

                top.destroy()

            else:

                log(f"[ERROR] El servidor devolvió un error al subir (Código: {res.status_code}).")

        except Exception:

            log("[ERROR] Sin conexión. No se pudo subir la secuencia.")



    ctk.CTkButton(top, text="Subir al servidor", fg_color="#2b8a3e",

                  font=("Segoe UI", 12, "bold"), command=confirmar_subida

                  ).grid(row=7, column=0, pady=10)



def abrir_ventana_descargar():

    top = ctk.CTkToplevel(root)

    top.title("Repositorio de Operaciones")

    top.geometry("500x500")

    top.attributes("-topmost", True)

    _set_icon(top)

    top.grid_columnconfigure(0, weight=1)

    top.grid_rowconfigure(1, weight=1)



    ctk.CTkLabel(top, text="SECUENCIAS DISPONIBLES",

                 font=("Segoe UI", 14, "bold"), text_color=ACCENT_CYAN

                 ).grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))



    scroll = ctk.CTkScrollableFrame(top, fg_color="#11131C")

    scroll.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

    scroll.grid_columnconfigure(0, weight=1)



    def bajar_macro(name):

        log(f"[INFO] Descargando secuencia: {name}")

        try:

            res = requests.get(f"{SERVER_URL}/download/{name}", headers=HEADERS, timeout=10)

            if res.status_code == 200:

                data        = res.json()

                images_data = data.get("images", {})

                images_meta = data.get("images_meta", {})

                master_sequences[name] = data.get("sequence", [])

                for img_name, b64_str in images_data.items():

                    img_path = os.path.join(TEMPLATES_DIR, f"{img_name}.png")

                    with open(img_path, "wb") as f:

                        f.write(base64.b64decode(b64_str))

                    templates[img_name] = cv2.imread(img_path)

                    if img_name in images_meta:

                        meta_path = os.path.join(TEMPLATES_DIR, f"{img_name}_meta.json")

                        with open(meta_path, "w", encoding="utf-8") as mf:

                            json.dump(images_meta[img_name], mf)

                    log(f"[INFO] Imagen descargada: {img_name}")

                save_data()

                actualizar_combobox()

                log(f"[ÉXITO] Secuencia '{name}' descargada correctamente.")

            else:

                log(f"[ERROR] El servidor devolvió un error ({res.status_code}).")

        except Exception:

            log("[ERROR] Error de red al descargar la secuencia.")



    try:

        res = requests.get(f"{SERVER_URL}/list", headers=HEADERS, timeout=5)

        macros_reales = res.json().get("macros", []) if res.status_code == 200 else []

    except Exception:

        log("[ERROR] Sin conexión al servidor.")

        macros_reales = []



    if not macros_reales:

        ctk.CTkLabel(scroll, text="No hay secuencias disponibles en el servidor.",

                     text_color=ACCENT_RED).grid(row=0, column=0, pady=20)

        return



    for card_idx, m in enumerate(macros_reales):

        nombre_macro = m.get("name", "Sin nombre")

        autor_macro  = m.get("author", "Desconocido")

        desc_macro   = m.get("description", "Sin descripción.")



        f_card = ctk.CTkFrame(scroll, fg_color=BG_CARD, corner_radius=8,

                              border_width=1, border_color="#222533")

        f_card.grid(row=card_idx, column=0, sticky="ew", padx=5, pady=5)

        f_card.grid_columnconfigure(0, weight=1)



        info_f = ctk.CTkFrame(f_card, fg_color="transparent")

        info_f.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        info_f.grid_columnconfigure(0, weight=1)



        ctk.CTkLabel(info_f, text=nombre_macro, font=("Segoe UI", 14, "bold"),

                     text_color=ACCENT_GREEN, anchor="w"

                     ).grid(row=0, column=0, sticky="ew")

        ctk.CTkLabel(info_f, text=f"Desarrollador: {autor_macro}",

                     font=("Segoe UI", 10, "italic"), text_color="#A0A5C0", anchor="w"

                     ).grid(row=1, column=0, sticky="ew")

        ctk.CTkLabel(info_f, text=desc_macro, font=("Segoe UI", 12),

                     text_color="#FFF", anchor="w"

                     ).grid(row=2, column=0, sticky="ew")



        ctk.CTkButton(f_card, text="Descargar", width=80, font=("Segoe UI", 12, "bold"),

                      fg_color="#1E2230",

                      command=lambda n=nombre_macro: bajar_macro(n)

                      ).grid(row=0, column=1, padx=10)



def abrir_contacto():

    top = ctk.CTkToplevel(root)

    top.title("Formulario de Asistencia")

    top.geometry("400x450")

    top.attributes("-topmost", True)

    _set_icon(top)

    top.grid_columnconfigure(0, weight=1)



    ctk.CTkLabel(top, text="SOPORTE Y CONTACTO",

                 font=("Segoe UI", 14, "bold"), text_color=ACCENT_CYAN

                 ).grid(row=0, column=0, sticky="ew", padx=30, pady=(20, 10))



    ctk.CTkLabel(top, text="Tu nombre:", anchor="w"

                 ).grid(row=1, column=0, sticky="w", padx=30)

    ent_nombre = ctk.CTkEntry(top)

    ent_nombre.grid(row=2, column=0, sticky="ew", padx=30, pady=(0, 10))



    ctk.CTkLabel(top, text="Tu email:", anchor="w"

                 ).grid(row=3, column=0, sticky="w", padx=30)

    ent_email = ctk.CTkEntry(top)

    ent_email.grid(row=4, column=0, sticky="ew", padx=30, pady=(0, 10))



    ctk.CTkLabel(top, text="Mensaje o problema:", anchor="w"

                 ).grid(row=5, column=0, sticky="w", padx=30)

    txt_msg = ctk.CTkTextbox(top, height=120)

    txt_msg.grid(row=6, column=0, sticky="ew", padx=30, pady=(0, 15))



    def mandar_email():

        n = ent_nombre.get().strip()

        e = ent_email.get().strip()

        m = txt_msg.get("1.0", "end-1c").strip()

        if not n or not e or not m:

            messagebox.showwarning("Formulario incompleto", "Por favor, rellena todos los campos.")

            return

        try:

            res = requests.post(

                "https://formspree.io/f/xbdbkppa",

                json={"name": n, "email": e, "message": f"[{n}] {m}"},

                headers={"Accept": "application/json"},

                timeout=8,

            )

            if res.status_code == 200:

                messagebox.showinfo("¡Enviado!", "Tu mensaje ha sido enviado correctamente.")

                top.destroy()

            elif res.status_code == 422:

                messagebox.showwarning("Email inválido", "El email introducido no tiene un formato correcto.")

            elif res.status_code == 429:

                messagebox.showwarning("Demasiados intentos", "Has enviado demasiados mensajes. Inténtalo más tarde.")

            else:

                messagebox.showerror("Error", f"El servidor devolvió: {res.status_code}")

        except requests.exceptions.RequestException as ex:

            messagebox.showerror("Sin conexión", f"No se pudo conectar al servidor:\n{ex}")



    ctk.CTkButton(top, text="Enviar mensaje", fg_color="#0D47A1",

                  font=("Segoe UI", 12, "bold"), command=mandar_email

                  ).grid(row=7, column=0, pady=10)





# ================= GESTOR DE APLICACIÓN BASE =================

def _set_icon(window):

    try:

        window.iconbitmap(os.path.join(BASE_DIR, "logo.ico"))

    except Exception:

        pass





# ================= CREADOR DE BANDERAS =================

_flag_creator_window = None   # referencia a la ventana Toplevel
status_flag_creator = None    # referencia al label de status (se asigna al construir la UI)


def toggle_flag_creator():
    """Abre o cierra el Creador de Banderas (F9)."""
    global _flag_creator_window

    # Si la ventana existe y está viva, la cerramos
    if _flag_creator_window is not None:
        try:
            if _flag_creator_window.winfo_exists():
                _flag_creator_window.destroy()
                _flag_creator_window = None
                if status_flag_creator: status_flag_creator.configure(text="○ CERRADO", text_color="#555566")
                log("[BANDERAS] Creador de Banderas cerrado.")
                return
        except Exception:
            _flag_creator_window = None

    # Abrir
    if _fg_module is None:
        log("[ERROR] flag_generator.py no encontrado junto a AriaBot.py.")
        messagebox.showerror("Error", "No se encontró flag_generator.py.\nAsegúrate de que está en la misma carpeta que AriaBot.py.")
        return

    try:
        win = tk.Toplevel(root)
        _flag_creator_window = win
        win.title("CREADOR DE BANDERAS — La Prisión 2026")
        win.configure(bg='#08080e')
        win.geometry('1280x920')
        win.resizable(True, True)

        # Al cerrar la ventana manualmente también actualizamos el status
        def _on_close():
            global _flag_creator_window
            _flag_creator_window = None
            if status_flag_creator: status_flag_creator.configure(text="○ CERRADO", text_color="#555566")
            log("[BANDERAS] Creador de Banderas cerrado.")
            win.destroy()

        win.protocol("WM_DELETE_WINDOW", _on_close)

        app = _fg_module.App(win)
        if status_flag_creator: status_flag_creator.configure(text="● ABIERTO", text_color="#00FF88")
        log("[BANDERAS] Creador de Banderas abierto (F9 para cerrar).")

    except Exception as e:
        log(f"[ERROR] No se pudo abrir el Creador de Banderas: {e}")


def _toggle_flag_creator_hotkey():
    root.after(10, toggle_flag_creator)


def _toggle_guia_hotkey():
    root.after(10, toggle_guia_prision)


def toggle_mapa():
    """Abre o cierra el Mapa de La Prisión (F11)."""
    if _mapa_module is None:
        messagebox.showerror(
            "Módulo no encontrado",
            "No se encontró mapa_prision.py.\nAsegúrate de que está en la misma carpeta que AriaBot.py."
        )
        return
    try:
        _mapa_module.toggle_mapa(root, BASE_DIR)
    except Exception as exc:
        messagebox.showerror("Error al abrir el mapa", str(exc))


def _toggle_mapa_hotkey():
    root.after(10, toggle_mapa)


def bind_global_hotkeys():

    """Registra las teclas rápidas globales usando el diccionario HOTKEYS.

    Usa hooks de bajo nivel (LL keyboard hook) para que funcionen

    incluso con un juego en primer plano."""

    try:

        # Limpiamos hotkeys previos para evitar duplicados si se llama varias veces

        try:

            kb.unhook_all_hotkeys()

        except Exception:

            pass



        # suppress=False es esencial: no bloquea la tecla al juego,

        # pero sí la detecta. Se registran con trigger_on_release=False

        # para respuesta inmediata.

        kb.add_hotkey(HOTKEYS["guardia"],   toggle_levelup_watch_hotkey,    suppress=False, trigger_on_release=False)

        kb.add_hotkey(HOTKEYS["autoclick"], toggle_autoclick,                suppress=False, trigger_on_release=False)

        kb.add_hotkey(HOTKEYS["afk"],       toggle_anti_afk,                 suppress=False, trigger_on_release=False)

        kb.add_hotkey(HOTKEYS["grabar"],    toggle_macro_recording_hotkey,   suppress=False, trigger_on_release=False)

        kb.add_hotkey(HOTKEYS["captura"],   capture_template_region_hotkey,  suppress=False, trigger_on_release=False)

        kb.add_hotkey(HOTKEYS["banderas"],  _toggle_flag_creator_hotkey,     suppress=False, trigger_on_release=False)

        kb.add_hotkey(HOTKEYS["guia"],      _toggle_guia_hotkey,             suppress=False, trigger_on_release=False)

        kb.add_hotkey(HOTKEYS["mapa"],      _toggle_mapa_hotkey,             suppress=False, trigger_on_release=False)

        kb.add_hotkey(HOTKEYS["detener"],   stop_all,                        suppress=False, trigger_on_release=False)



        log(f"[SISTEMA] Teclas rápidas registradas correctamente.")

    except Exception as e:

        log(f"[ERROR] Error al registrar las teclas rápidas: {e}")





# ================= INICIALIZACIÓN DE INTERFAZ GRÁFICA =================

# Diccionario de referencias a los labels de tecla en la leyenda (para actualizarlos)
_hotkey_legend_labels = {}

# Referencias a los labels de estado que muestran la tecla activa
_hotkey_status_labels = {}

root = ctk.CTk()

root.title("AriaBot v1.0")

root.geometry("1300x860")

root.minsize(900, 620)

_set_icon(root)

root.configure(fg_color=BG_MAIN)



root.grid_columnconfigure(0, weight=0)

root.grid_columnconfigure(1, weight=1)

root.grid_rowconfigure(0, weight=1)





# ── PANEL LATERAL DE CONTROL ──

sidebar_outer = ctk.CTkFrame(root, width=310, corner_radius=0,

                              fg_color=BG_CARD, border_width=1, border_color="#1E2230")

sidebar_outer.grid(row=0, column=0, sticky="nsew")

sidebar_outer.grid_propagate(False)

sidebar_outer.grid_columnconfigure(0, weight=1)

sidebar_outer.grid_rowconfigure(0, weight=1)

sidebar_outer.grid_rowconfigure(1, weight=0)



sidebar = ctk.CTkScrollableFrame(sidebar_outer, fg_color="transparent", corner_radius=0)

sidebar.grid(row=0, column=0, sticky="nsew")

sidebar.grid_columnconfigure(0, weight=1)



sidebar_bottom = ctk.CTkFrame(sidebar_outer, fg_color="transparent")

sidebar_bottom.grid(row=1, column=0, sticky="ew")

sidebar_bottom.grid_columnconfigure(0, weight=1)



ctk.CTkLabel(sidebar, text="ARIA BOT", font=("Segoe UI", 22, "bold"),

             text_color=ACCENT_RED

             ).grid(row=0, column=0, sticky="w", padx=20, pady=(30, 2))

ctk.CTkLabel(sidebar, text="Build: SMaSeR 2026", font=("Segoe UI", 12),

             text_color="#6A6E85"

             ).grid(row=1, column=0, sticky="w", padx=20, pady=(0, 25))



status_box = ctk.CTkFrame(sidebar, fg_color="#11131C", corner_radius=10,

                          border_width=1, border_color="#222533")

status_box.grid(row=2, column=0, sticky="ew", padx=15, pady=10)

status_box.grid_columnconfigure(0, weight=1)

status_box.grid_columnconfigure(1, weight=0)



ctk.CTkLabel(status_box, text="ESTADO ACTUAL",

             font=("Segoe UI", 10, "bold"), text_color="#555566"

             ).grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")



_lbl_status_autoclick_key = ctk.CTkLabel(status_box, text=f"Autoclick ({HOTKEYS['autoclick'].upper()}):",

             font=("Segoe UI", 12))
_lbl_status_autoclick_key.grid(row=1, column=0, padx=10, pady=2, sticky="w")
_hotkey_status_labels["autoclick"] = _lbl_status_autoclick_key

status_autoclick = ctk.CTkLabel(status_box, text="○ INACTIVO",

                                font=("Segoe UI", 11, "bold"), text_color="#555566")

status_autoclick.grid(row=1, column=1, padx=10, pady=2, sticky="e")



ctk.CTkLabel(status_box, text="Estado Secuencia:",

             font=("Segoe UI", 12)).grid(row=2, column=0, padx=10, pady=2, sticky="w")

status_seq = ctk.CTkLabel(status_box, text="○ EN ESPERA",

                          font=("Segoe UI", 11, "bold"), text_color="#555566")

status_seq.grid(row=2, column=1, padx=10, pady=2, sticky="e")



_lbl_status_afk_key = ctk.CTkLabel(status_box, text=f"Anti-AFK ({HOTKEYS['afk'].upper()}):",

             font=("Segoe UI", 12))
_lbl_status_afk_key.grid(row=3, column=0, padx=10, pady=2, sticky="w")
_hotkey_status_labels["afk"] = _lbl_status_afk_key

status_afk = ctk.CTkLabel(status_box, text="○ INACTIVO",

                          font=("Segoe UI", 11, "bold"), text_color="#555566")

status_afk.grid(row=3, column=1, padx=10, pady=2, sticky="e")



ctk.CTkLabel(status_box, text="Guardia Anti-Nivel:",

             font=("Segoe UI", 12)).grid(row=4, column=0, padx=10, pady=2, sticky="w")

status_levelup = ctk.CTkLabel(status_box, text="○ INACTIVO",

                              font=("Segoe UI", 11, "bold"), text_color="#555566")

status_levelup.grid(row=4, column=1, padx=10, pady=2, sticky="e")



# ── Opción: Bloquear ratón durante Autoclick ──

def _toggle_bloquear_raton():

    global bloquear_raton

    bloquear_raton = chk_lock_var.get() == 1

    estado = "activado" if bloquear_raton else "desactivado"

    log(f"[INFO] Bloqueo de ratón {estado}.")



# ── Fila Banderas (sin hotkey en status, solo indicador) ──
ctk.CTkLabel(status_box, text="Banderas:",
             font=("Segoe UI", 12)).grid(row=5, column=0, padx=10, pady=2, sticky="w")
status_flag_creator = ctk.CTkLabel(status_box, text="○ CERRADO",
                                   font=("Segoe UI", 11, "bold"), text_color="#555566")
status_flag_creator.grid(row=5, column=1, padx=10, pady=2, sticky="e")

# ── Bloqueo ratón va al final del status ──
chk_lock_var = ctk.IntVar(value=0)

chk_lock_mouse = ctk.CTkCheckBox(

    status_box,

    text="Bloquear ratón al hacer Autoclick",

    variable=chk_lock_var,

    font=("Segoe UI", 11),

    text_color="#A0A5C0",

    fg_color=ACCENT_CYAN,

    hover_color="#00B8CC",

    command=_toggle_bloquear_raton,

)

chk_lock_mouse.grid(row=6, column=0, columnspan=2, padx=10, pady=(6, 10), sticky="w")



cloud_box = ctk.CTkFrame(sidebar, fg_color="#11131C", corner_radius=10,

                          border_width=1, border_color="#222533")

cloud_box.grid(row=3, column=0, sticky="ew", padx=15, pady=10)

cloud_box.grid_columnconfigure(0, weight=1)



ctk.CTkLabel(cloud_box, text="PLATAFORMA CLOUD",

             font=("Segoe UI", 10, "bold"), text_color=ACCENT_CYAN

             ).grid(row=0, column=0, sticky="w", padx=10, pady=5)

ctk.CTkButton(cloud_box, text="Publicar Secuencia",

              font=("Segoe UI", 11, "bold"), fg_color="#1E2230",

              command=abrir_ventana_subir

              ).grid(row=1, column=0, sticky="ew", padx=10, pady=5)

ctk.CTkButton(cloud_box, text="Explorar Repositorio",

              font=("Segoe UI", 11, "bold"), fg_color="#1E2230",

              command=abrir_ventana_descargar

              ).grid(row=2, column=0, sticky="ew", padx=10, pady=5)



# ── GUARDIA ANTI-NIVEL ──

levelup_box = ctk.CTkFrame(sidebar, fg_color="#11131C", corner_radius=10,

                             border_width=1, border_color="#3A1E5A")

levelup_box.grid(row=4, column=0, sticky="ew", padx=15, pady=10)

levelup_box.grid_columnconfigure(0, weight=1)



ctk.CTkLabel(levelup_box, text="GUARDIA ANTI-NIVEL",

             font=("Segoe UI", 10, "bold"), text_color="#BB44FF"

             ).grid(row=0, column=0, sticky="w", padx=10, pady=(8, 2))

ctk.CTkLabel(levelup_box,

             text="Detecta subida de nivel por OCR\ny cierra el juego con Alt+F4.",

             font=("Segoe UI", 10), text_color="#6A6E85", justify="left"

             ).grid(row=1, column=0, sticky="w", padx=10, pady=(0, 6))



btn_levelup_watch = ctk.CTkButton(

    levelup_box,

    text="Activar Guardia Anti-Nivel",

    font=("Segoe UI", 11, "bold"),

    fg_color="#1E2230",

    hover_color="#2A3050",

    command=toggle_levelup_watch,

)

btn_levelup_watch.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 10))



hotkey_box = ctk.CTkFrame(sidebar, fg_color="#11131C", corner_radius=10,

                          border_width=1, border_color="#222533")

hotkey_box.grid(row=6, column=0, sticky="ew", padx=15, pady=10)

hotkey_box.grid_columnconfigure(0, weight=1)



ctk.CTkLabel(hotkey_box, text="TECLAS RÁPIDAS",

             font=("Segoe UI", 10, "bold"), text_color=ACCENT_RED

             ).grid(row=0, column=0, sticky="w", padx=10, pady=5)



def _add_hotkey_lbl(parent_row, action_key, txt_desc):
    """Crea una fila en la leyenda. Guarda referencia al label de tecla para actualizarlo."""

    f = ctk.CTkFrame(hotkey_box, fg_color="transparent")

    f.grid(row=parent_row, column=0, sticky="ew", padx=10, pady=2)

    f.grid_columnconfigure(1, weight=1)

    lbl_key = ctk.CTkLabel(f, text=f"[{HOTKEYS[action_key].upper()}]",
                           font=("Consolas", 11, "bold"),
                           text_color=ACCENT_GREEN, width=80, anchor="w")

    lbl_key.grid(row=0, column=0, sticky="w")

    ctk.CTkLabel(f, text=txt_desc, font=("Segoe UI", 11),

                 text_color="#6A6E85"

                 ).grid(row=0, column=1, sticky="w")

    # Guardamos la referencia para actualizarla desde la ventana de Opciones
    _hotkey_legend_labels[action_key] = lbl_key



_add_hotkey_lbl(1, "guardia",   "Activar/Desactivar Guardia")
_add_hotkey_lbl(2, "autoclick", "Autoclick Continuo")
_add_hotkey_lbl(3, "afk",       "Loop Evasión AFK")
_add_hotkey_lbl(4, "grabar",    "Iniciar / Detener Grabación")
_add_hotkey_lbl(5, "captura",   "Capturar Imagen")
_add_hotkey_lbl(6, "banderas",  "Banderas")
_add_hotkey_lbl(7, "guia",      "Guía de La Prisión")
_add_hotkey_lbl(8, "mapa",      "Mapa de La Prisión")
_add_hotkey_lbl(9, "detener",   "DETENER TODO")

btn_banderas = ctk.CTkButton(
    hotkey_box,
    text=f"🏴 Banderas ({HOTKEYS['banderas'].upper()})",
    font=("Segoe UI", 11, "bold"),
    fg_color="#1a2a0a",
    text_color="#66ff66",
    hover_color="#223300",
    command=toggle_flag_creator,
)
btn_banderas.grid(row=10, column=0, sticky="ew", padx=10, pady=(6, 3))
_hotkey_status_labels["banderas_btn"] = btn_banderas


# ── Botón Guía de La Prisión ──
def toggle_guia_prision():
    if _guia_module is None:
        messagebox.showerror(
            "Módulo no encontrado",
            "No se encontró guia_laprision.py.\n"
            "Asegúrate de que está en la misma carpeta que AriaBot.py."
        )
        return
    try:
        _guia_module.abrir_guia()
    except Exception as exc:
        messagebox.showerror("Error al abrir la guía", str(exc))


btn_guia = ctk.CTkButton(
    hotkey_box,
    text=f"⛓ Guía ({HOTKEYS['guia'].upper()})",
    font=("Segoe UI", 11, "bold"),
    fg_color="#0a1a2a",
    text_color="#00F0FF",
    hover_color="#0d2233",
    command=toggle_guia_prision,
)
btn_guia.grid(row=11, column=0, sticky="ew", padx=10, pady=3)
_hotkey_status_labels["guia_btn"] = btn_guia

btn_mapa = ctk.CTkButton(
    hotkey_box,
    text=f"🗺 Mapa ({HOTKEYS['mapa'].upper()})",
    font=("Segoe UI", 11, "bold"),
    fg_color="#0a2a1a",
    text_color="#00FF88",
    hover_color="#0d3322",
    command=toggle_mapa,
)
btn_mapa.grid(row=12, column=0, sticky="ew", padx=10, pady=(3, 8))
_hotkey_status_labels["mapa_btn"] = btn_mapa



ctk.CTkButton(sidebar_bottom, text="DETENER OPERACIONES (F12)", fg_color=ACCENT_RED,

              font=("Segoe UI", 12, "bold"), height=42, command=stop_all

              ).grid(row=0, column=0, sticky="ew", padx=15, pady=(10, 5))

ctk.CTkButton(sidebar_bottom, text="Asistencia Técnica", fg_color="transparent",

              border_width=1, border_color="#333", font=("Segoe UI", 12),

              command=abrir_contacto

              ).grid(row=1, column=0, sticky="ew", padx=15, pady=(0, 10))





# ── ÁREA DE TRABAJO PRINCIPAL ──

content_area = ctk.CTkFrame(root, fg_color="transparent")

content_area.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)

content_area.grid_columnconfigure(0, weight=1)

content_area.grid_columnconfigure(1, weight=1)

content_area.grid_rowconfigure(0, weight=0)

content_area.grid_rowconfigure(1, weight=1)

content_area.grid_rowconfigure(2, weight=0)





# ── CARD CONFIGURACIÓN ──

card_config = ctk.CTkFrame(content_area, fg_color=BG_CARD, corner_radius=12,

                           border_width=1, border_color="#1E2230")

card_config.grid(row=0, column=0, columnspan=2, padx=10, pady=(6,4), sticky="ew")

card_config.grid_columnconfigure(0, weight=1)



ctk.CTkLabel(card_config, text="CONFIGURACIÓN GENERAL",

             font=("Segoe UI", 12, "bold"), text_color=ACCENT_CYAN

             ).grid(row=0, column=0, sticky="w", padx=20, pady=(8, 2))



sliders_frame = ctk.CTkFrame(card_config, fg_color="transparent")

sliders_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=5)

sliders_frame.grid_columnconfigure(0, weight=1)



f_sl1 = ctk.CTkFrame(sliders_frame, fg_color="transparent")

f_sl1.grid(row=0, column=0, sticky="ew", padx=10)

f_sl1.grid_columnconfigure(0, weight=1)



ctk.CTkLabel(f_sl1, text="Intervalo de Espera Estándar (Segundos):",

             font=("Segoe UI", 11), text_color="#A0A5C0"

             ).grid(row=0, column=0, sticky="w")

step_delay_slider = ctk.CTkSlider(f_sl1, from_=0.0, to=5.0, number_of_steps=50,

                                  fg_color="#222533", progress_color=ACCENT_CYAN)

step_delay_slider.set(0.4)

step_delay_slider.grid(row=1, column=0, sticky="ew", pady=4)



record_panel = ctk.CTkFrame(card_config, fg_color="#12131A", corner_radius=8,

                            border_width=1, border_color="#2B2F44")

record_panel.grid(row=2, column=0, sticky="ew", padx=20, pady=(3, 8))

record_panel.grid_columnconfigure(0, weight=1)

record_panel.grid_columnconfigure(1, weight=1)



btn_toggle_record = ctk.CTkButton(record_panel,

                                  text=f"Iniciar Grabación ({HOTKEYS['grabar'].upper()})",

                                  font=("Segoe UI", 12, "bold"), height=35,

                                  command=toggle_macro_recording)

btn_toggle_record.grid(row=0, column=0, sticky="ew", padx=10, pady=8)



ctk.CTkButton(record_panel, text="Añadir Pausa Estática",

              fg_color="#1E293B", font=("Segoe UI", 12), height=35,

              command=add_pure_delay_step

              ).grid(row=0, column=1, sticky="ew", padx=10, pady=8)





# ── CARD RECURSOS VISUALES ──

card_left_repo = ctk.CTkFrame(content_area, fg_color=BG_CARD, corner_radius=12,

                              border_width=1, border_color="#1E2230")

card_left_repo.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

card_left_repo.grid_columnconfigure(0, weight=1)

card_left_repo.grid_rowconfigure(2, weight=1)



ctk.CTkLabel(card_left_repo, text="IMÁGENES GUARDADAS",

             font=("Segoe UI", 12, "bold"), text_color=ACCENT_CYAN

             ).grid(row=0, column=0, sticky="w", padx=20, pady=15)



ctk.CTkButton(card_left_repo, text=f"Capturar Región de Pantalla ({HOTKEYS['captura'].upper()})",

              fg_color="#0D47A1", font=("Segoe UI", 12, "bold"), height=35,

              command=capture_template_region

              ).grid(row=1, column=0, sticky="ew", padx=20, pady=4)



template_scroll = ctk.CTkScrollableFrame(card_left_repo, fg_color="#11131C",

                                         border_width=1, border_color="#1E2230")

template_scroll.grid(row=2, column=0, sticky="nsew", padx=20, pady=15)





# ── CARD TIMELINE ──

card_right_timeline = ctk.CTkFrame(content_area, fg_color=BG_CARD, corner_radius=12,

                                    border_width=1, border_color="#1E2230")

card_right_timeline.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

card_right_timeline.grid_columnconfigure(0, weight=1)

card_right_timeline.grid_rowconfigure(2, weight=1)



header_timeline_frame = ctk.CTkFrame(card_right_timeline, fg_color="transparent")

header_timeline_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=(15, 5))

header_timeline_frame.grid_columnconfigure(0, weight=1)



ctk.CTkLabel(header_timeline_frame, text="SECUENCIAS DE PASOS",

             font=("Segoe UI", 12, "bold"), text_color=ACCENT_CYAN

             ).grid(row=0, column=0, sticky="w")



seq_manager_frame = ctk.CTkFrame(card_right_timeline, fg_color="#11131C",

                                  corner_radius=6, border_width=1, border_color="#222533")

seq_manager_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=5)

seq_manager_frame.grid_columnconfigure(0, weight=1)



combo_sequences = ctk.CTkOptionMenu(seq_manager_frame, font=("Segoe UI", 11),

                                    values=["Secuencia 1"], command=change_sequence)

combo_sequences.grid(row=0, column=0, sticky="ew", padx=10, pady=8)



ctk.CTkButton(seq_manager_frame, text="Crear", width=70, font=("Segoe UI", 11),

              fg_color="#2b8a3e", command=add_new_sequence

              ).grid(row=0, column=1, padx=5)



ctk.CTkButton(seq_manager_frame, text="Eliminar", width=70, font=("Segoe UI", 11),

              fg_color="#8A2B2B", command=delete_current_sequence

              ).grid(row=0, column=2, padx=10)



timeline_scroll = ctk.CTkScrollableFrame(card_right_timeline, fg_color="#11131C",

                                         border_width=1, border_color="#1E2230")

timeline_scroll.grid(row=2, column=0, sticky="nsew", padx=20, pady=5)



control_timeline_frame = ctk.CTkFrame(card_right_timeline, fg_color="transparent")

control_timeline_frame.grid(row=3, column=0, sticky="ew", padx=20, pady=12)

control_timeline_frame.grid_columnconfigure(1, weight=1)



ctk.CTkButton(control_timeline_frame, text="Restablecer Pila",

              font=("Segoe UI", 11, "bold"), fg_color="#3A1C24",

              text_color=ACCENT_RED, width=120, command=clear_sequence

              ).grid(row=0, column=0, sticky="w", padx=5)



ctk.CTkButton(control_timeline_frame, text="EJECUTAR SECUENCIA ACTIVA",

              fg_color="#2563EB", font=("Segoe UI", 12, "bold"), height=36,

              command=toggle_sequence_execution

              ).grid(row=0, column=1, sticky="ew", padx=5)





# ── LOG ──

log_frame = ctk.CTkFrame(content_area, fg_color=BG_CARD, corner_radius=12,

                         border_width=1, border_color="#1E2230")

log_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

log_frame.grid_columnconfigure(0, weight=1)



log_text = ctk.CTkTextbox(log_frame, height=70, font=("Consolas", 11),

                          fg_color="#090A0F", text_color="#A0A5C0",

                          border_width=1, border_color="#1A1D29")

log_text.grid(row=0, column=0, sticky="ew", padx=15, pady=10)



def abrir_opciones():
    """Ventana de configuración de teclas rápidas."""

    top = ctk.CTkToplevel(root)
    top.title("Opciones — Teclas Rápidas")
    top.geometry("480x560")
    top.resizable(False, False)
    top.attributes("-topmost", True)
    _set_icon(top)
    top.grid_columnconfigure(0, weight=1)

    ctk.CTkLabel(top, text="CONFIGURAR TECLAS RÁPIDAS",
                 font=("Segoe UI", 14, "bold"), text_color=ACCENT_CYAN
                 ).grid(row=0, column=0, columnspan=3, sticky="ew", padx=20, pady=(20, 4))

    ctk.CTkLabel(top,
                 text="Haz clic en un botón y luego pulsa la tecla o combinación deseada.",
                 font=("Segoe UI", 10), text_color="#6A6E85"
                 ).grid(row=1, column=0, columnspan=3, sticky="ew", padx=20, pady=(0, 12))

    # Frame scrollable para las filas de hotkeys
    scroll = ctk.CTkScrollableFrame(top, fg_color="#11131C", corner_radius=8,
                                    border_width=1, border_color="#222533")
    scroll.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=20, pady=4)
    scroll.grid_columnconfigure(1, weight=1)
    top.grid_rowconfigure(2, weight=1)

    # Diccionario temporal de edición (copia de HOTKEYS para no modificar hasta Guardar)
    temp_hotkeys = dict(HOTKEYS)

    # Var de estado de captura
    _capturing = {"action": None}

    def _make_row(parent, row_idx, action_key):
        desc = HOTKEY_DESCS.get(action_key, action_key)

        ctk.CTkLabel(parent, text=desc, font=("Segoe UI", 11), anchor="w"
                     ).grid(row=row_idx, column=0, padx=(10, 4), pady=6, sticky="w")

        btn_var = ctk.StringVar(value=temp_hotkeys[action_key].upper())
        btn = ctk.CTkButton(
            parent,
            textvariable=btn_var,
            width=120,
            font=("Consolas", 11, "bold"),
            fg_color="#1E2230",
            hover_color="#2A3050",
            text_color=ACCENT_GREEN,
        )
        btn.grid(row=row_idx, column=1, padx=4, pady=6)

        def _start_capture(ak=action_key, bv=btn_var, b=btn):
            # Deseleccionar cualquier captura anterior
            if _capturing["action"] and _capturing["action"] != ak:
                # Restaurar color del anterior
                pass
            _capturing["action"] = ak
            bv.set("[ Pulsa tecla... ]")
            b.configure(fg_color="#3A3010", text_color="#FFCC00")
            top.focus_force()

        btn.configure(command=lambda ak=action_key: _start_capture(ak))

        return btn_var, btn

    btn_vars = {}
    btn_refs = {}
    for i, action_key in enumerate(HOTKEYS.keys()):
        bv, bt = _make_row(scroll, i, action_key)
        btn_vars[action_key] = bv
        btn_refs[action_key] = bt

    # Rastreo manual de modificadores físicamente pulsados
    # (NO usamos event.state porque incluye bits de Num Lock, Caps Lock, etc.)
    _mods_held = {"ctrl": False, "alt": False, "shift": False}

    _MOD_KEYSYMS = {
        "control_l", "control_r",
        "alt_l", "alt_r", "meta_l", "meta_r",
        "shift_l", "shift_r",
    }

    def _on_mod_press(event):
        ks = event.keysym.lower()
        if "control" in ks: _mods_held["ctrl"]  = True
        if "alt" in ks or "meta" in ks: _mods_held["alt"] = True
        if "shift"   in ks: _mods_held["shift"] = True

    def _on_mod_release(event):
        ks = event.keysym.lower()
        if "control" in ks: _mods_held["ctrl"]  = False
        if "alt" in ks or "meta" in ks: _mods_held["alt"] = False
        if "shift"   in ks: _mods_held["shift"] = False

    # Captura de teclado dentro de la ventana
    def _on_key(event):
        ak = _capturing.get("action")
        if not ak:
            return

        ks = event.keysym.lower()

        # Si es solo un modificador, esperamos la tecla principal
        if ks in _MOD_KEYSYMS:
            return

        # Normalizar keysym: quitar sufijos _l/_r que tkinter añade en algunos sistemas
        ks = ks.replace("_l", "").replace("_r", "")

        # Construir combo SOLO con modificadores físicamente pulsados
        parts = []
        if _mods_held["ctrl"]:  parts.append("ctrl")
        if _mods_held["alt"]:   parts.append("alt")
        if _mods_held["shift"]: parts.append("shift")
        parts.append(ks)
        combo = "+".join(parts)

        # Verificar conflicto con otra acción ya configurada
        conflict = None
        for other_ak, other_val in temp_hotkeys.items():
            if other_ak != ak and other_val.lower() == combo.lower():
                conflict = other_ak
                break

        if conflict:
            messagebox.showwarning(
                "Conflicto de tecla",
                f"La combinación '{combo.upper()}' ya está asignada a:\n\n"
                f"  → {HOTKEY_DESCS.get(conflict, conflict)}\n\n"
                "Elige una combinación diferente.",
                parent=top
            )
            btn_vars[ak].set(temp_hotkeys[ak].upper())
            btn_refs[ak].configure(fg_color="#1E2230", text_color=ACCENT_GREEN)
            _capturing["action"] = None
            return

        temp_hotkeys[ak] = combo
        btn_vars[ak].set(combo.upper())
        btn_refs[ak].configure(fg_color="#1E2230", text_color=ACCENT_GREEN)
        _capturing["action"] = None

    top.bind("<KeyPress>",   _on_key)
    top.bind("<KeyPress>",   _on_mod_press,   add="+")
    top.bind("<KeyRelease>", _on_mod_release)

    # Botones inferiores
    btn_frame = ctk.CTkFrame(top, fg_color="transparent")
    btn_frame.grid(row=3, column=0, columnspan=3, sticky="ew", padx=20, pady=(8, 16))
    btn_frame.grid_columnconfigure(0, weight=1)
    btn_frame.grid_columnconfigure(1, weight=1)

    def _restaurar_defecto():
        defaults = {
            "guardia":   "f4",
            "autoclick": "f5",
            "afk":       "f6",
            "grabar":    "f7",
            "captura":   "f8",
            "banderas":  "f9",
            "guia":      "f10",
            "mapa":      "f11",
            "detener":   "f12",
        }
        for ak, val in defaults.items():
            temp_hotkeys[ak] = val
            btn_vars[ak].set(val.upper())
            btn_refs[ak].configure(fg_color="#1E2230", text_color=ACCENT_GREEN)
        _capturing["action"] = None

    def _guardar():
        global HOTKEYS
        HOTKEYS.update(temp_hotkeys)
        _save_hotkeys()
        # Actualizar leyenda en la ventana principal
        for ak, lbl in _hotkey_legend_labels.items():
            lbl.configure(text=f"[{HOTKEYS[ak].upper()}]")
        # Actualizar labels de estado del sidebar
        if "autoclick" in _hotkey_status_labels:
            _hotkey_status_labels["autoclick"].configure(
                text=f"Autoclick ({HOTKEYS['autoclick'].upper()}):")
        if "afk" in _hotkey_status_labels:
            _hotkey_status_labels["afk"].configure(
                text=f"Anti-AFK ({HOTKEYS['afk'].upper()}):")
        # Actualizar botones con texto de tecla
        if "banderas_btn" in _hotkey_status_labels:
            _hotkey_status_labels["banderas_btn"].configure(
                text=f"🏴 Banderas ({HOTKEYS['banderas'].upper()})")
        if "guia_btn" in _hotkey_status_labels:
            _hotkey_status_labels["guia_btn"].configure(
                text=f"⛓ Guía ({HOTKEYS['guia'].upper()})")
        if "mapa_btn" in _hotkey_status_labels:
            _hotkey_status_labels["mapa_btn"].configure(
                text=f"🗺 Mapa ({HOTKEYS['mapa'].upper()})")
        # Actualizar botón de grabación (texto dinámico según estado)
        update_status_indicators()
        # Re-registrar hotkeys globales con los nuevos valores
        bind_global_hotkeys()
        log(f"[OPCIONES] Teclas rápidas actualizadas y guardadas.")
        top.destroy()

    ctk.CTkButton(btn_frame, text="Restaurar por defecto",
                  font=("Segoe UI", 11), fg_color="#3A1C1C",
                  text_color=ACCENT_RED, hover_color="#5A2020",
                  command=_restaurar_defecto
                  ).grid(row=0, column=0, sticky="ew", padx=(0, 4))

    ctk.CTkButton(btn_frame, text="Guardar y Aplicar",
                  font=("Segoe UI", 11, "bold"), fg_color="#2b8a3e",
                  hover_color="#236B32",
                  command=_guardar
                  ).grid(row=0, column=1, sticky="ew", padx=(4, 0))


ctk.CTkButton(sidebar_bottom, text="⚙ Opciones", fg_color="transparent",

              border_width=1, border_color="#333", font=("Segoe UI", 12),

              command=abrir_opciones

              ).grid(row=2, column=0, sticky="ew", padx=15, pady=(0, 5))


# ================= ARRANQUE DEL SISTEMA =================

load_data()

combo_sequences.configure(values=list(master_sequences.keys()))

combo_sequences.set(current_sequence_key)

update_timeline_view()

update_template_scroll_view()

log("[SISTEMA] AriaBot v1.0 iniciado correctamente.")



root.after(500, bind_global_hotkeys)



root.protocol("WM_DELETE_WINDOW", lambda: [save_data(), root.destroy()])

root.mainloop()