# =====================================================================
# Guía de La Prisión — Módulo para AriaBot
# Basado en el contenido de www.gentelaprision.es
# Developed by: SMaSeR 2026
# =====================================================================

import tkinter as tk
import customtkinter as ctk

# ── Paleta heredada de AriaBot ──
BG_MAIN        = "#0F1015"
BG_CARD        = "#161822"
BG_INNER       = "#0B0C10"
BG_ROW_A       = "#11131C"
BG_ROW_B       = "#0E0F18"
ACCENT_CYAN    = "#00F0FF"
ACCENT_GREEN   = "#00FF88"
ACCENT_RED     = "#FF2A2A"
ACCENT_GOLD    = "#FFB700"
TEXT_DIM       = "#6A6E85"
TEXT_MAIN      = "#C8CBD8"
BORDER         = "#1E2230"

# ══════════════════════════════════════════════════════════════════════
#  DATOS — toda la información de los PDFs
# ══════════════════════════════════════════════════════════════════════

GUIAS = {
    "💣 Municiones": {
        "color": ACCENT_RED,
        "subsecciones": {
            "Munición comprable": [
                ("Piedrecita",            "Traficante/Contrabandista — Patios Veteranos, Áreas descanso  ⚠ Intransferible"),
                ("Grapas",                "Traficante — Área descanso Norte, Área lectura Oeste, Distribuidor, Economato Este"),
                ("Piedrecita roma",       "Traficante/Contrabandista — mismas zonas que Grapas"),
                ("Perdigones",            "Ebbinhaus — Sótanos Norte"),
                ("Clavos",                "Traficante — Patios interiores 1N, 2N, 3S, 4N"),
                ("Clavos reforzados",     "Ebbinhaus — Sótanos Norte"),
                ("Tuercas",               "Traficante — Patios interiores 1N, 2N, 3S, 4N  ⚠ Intransferible"),
                ("Balas calibre 44",      "Traficante — Patios interiores 1N, 2N, 3S, 4N"),
                ("Balas pistola alemana", "Traficante — Distribuidor, WC Gimnasio, Gimnasio Este, Sala visita Sur"),
                ("Balas Walter PPK",      "Bots traficantes — Patios interiores 1N, 2N, 3S, 4N"),
                ("Balas Peacemaker",      "Traficante — Distribuidor, WC Gimnasio, Gimnasio Este, Sala visitas Sur"),
                ("Balas calibre 40",      "Traficante — Patios interiores 1N, 2N, 3S, 4N"),
                ("Balas USP40 (ADCC)",    "Traficante — Patios interiores 1N, 2N, 3S, 4N  (Armas vs Carlito)"),
                ("Balas revólver sureño", "Traficante — Área descanso Norte, Área lectura Oeste, Distribuidor, Economato Este"),
                ("Cartuchos de sal",      "Fabricar en molde calibre 21 ó Traficante — Área guardias Suroeste"),
                ("Cartuchos del 12",      "Traficante — Área descanso Norte, Área lectura Oeste, Distribuidor, Economato Este"),
                ("Cartuchos del 10",      "Traficante/Contrabandista — Patios interiores 1N, 2N, 3S, 4N"),
                ("Cartuchos Benelli",     "Traficante — Distribuidor, WC Gimnasio, Gimnasio Este, Sala visita Sur"),
                ("Balas calibre 5,45",    "Traficante — Área descanso Norte, Área lectura Oeste, Distribuidor, Economato Este"),
                ("Bombeta química",       "Traficante — Distribuidor, WC Gimnasio, Gimnasio Este, Sala visita Sur"),
                ("Carga gas butano",      "Traficante — Patios interiores 1N, 2N, 3S, 4N"),
                ("Balas fusil de asalto", "Traficante — Distribuidor, WC Gimnasio, Gimnasio Este, Sala visita Sur"),
                ("Carga química débil",   "ATS Subcontratado — Área enfermería Norte/Sur/Este/Oeste, Sala lectura y TV Sur"),
                ("Carga revit. débil",    "Médico de guardia — Enfermerías"),
                ("Cargas vacías Híperspray", "Derrotar: Jack Muerte / Capitán RedDevil / Capitana Creppled/Dragon/Scar-face\n→ Entregar en Locutorio (excepto Hall 1) a Amigo de Martín/Andrés/Rafael → 3 cargas Hiperspray"),
            ],
            "Fabricar munición": [
                ("MOLDES",             "Monitor/Auxiliar de Mecánica — Patio 1W, Área descanso Oeste, Distribuidor,\nSala TV Oeste, Patio 4E, Área cocina Oeste, Patio 3S, Área enfermería Sur"),
                ("Proyectil de bala",  "Talleres → Tornillo de banco: Soplete de precisión + Trozo de acero  |  Dif: 20 pts Mecánica"),
                ("Casquillo de bala",  "Traficante Pata Palo  ó  Lámina hierro + Soplete + Martillo planchado  |  Dif: 10 pts"),
                ("Pólvora negra",      "50 pts Mecánica: Trozo carbón + Puñado salitre + Lata de azufre\n  · Carbón: Caja metales — Azoteas / Patio basuras\n  · Salitre: Alcantarillas/Tapas — Azoteas / Entrada principal\n  · Lata azufre: Trapo limpio + 2 Cristales azufre + Lata vacía  |  Dif: 20 pts"),
                ("Pólvora refinada",   "2 Latas pólvora negra + Bote ácido sulfúrico  |  Dif: 75 pts Mecánica\n  · Ácido sulfúrico: Batería de coche (sótanos): Cristal azufre + Pila petaca + Frasco cristal"),
                ("Molde calibre 9",    "Balas 9mm (10)  |  Dif: 30 pts"),
                ("Molde calibre 12",   "Balas 12mm (10) Dif 35  /  Balas 12 Especial (10) Dif 40 — usa pólvora refinada"),
                ("Molde calibre 15",   "Balas 15mm (10)  |  Dif: 45 pts"),
                ("Molde calibre 21",   "Balas 21mm Dif 55 / Cartuchos sal Dif 60 / Balas Mercurio Dif 90 / Cartuchos perforador Dif 100"),
            ],
            "Granada Enola Gay": [
                ("⚠ Mínimo",           "230 puntos de Mecánica — con menos, los fallos son continuos"),
                ("Combinación final",  "Mesa de trabajo Talleres:\n  5 envoltorios + 5 cargas explosivas + 1 carga explosiva especial\n  + 3 detonadores + 1 granada electrónica desarmada"),
                ("Carga explosiva",    "Mesa: Rollo estaño + Destornillador + Pólvora refinada + Nitroglicerina + Cartuchos carga  |  Dif: 75"),
                ("Carga esp. especial","Mesa: Destornillador + Rollo platino + Trozo U-235 + Cartuchos carga  |  Dif: 150"),
                ("U-235",              "Visitar comedor 2S llevando brebajes"),
                ("Granada desarmada",  "Se puede robar en Sótanos 3S"),
                ("Entrega a Vitto",    "Don Vitto Corleone — Colector Este (llevar personaje que abra puertas)\n  → ~30% Enolas + resto bombas de ataque corto"),
            ],
            "Cargas de Spray": [
                ("Cargas Químicas normales (3)",    "Kit Química: 4 Cargas débiles + Carcasa + Vaporizador  |  Dif: 55"),
                ("Cargas Químicas fuertes (2)",     "Kit Química: 3 Cargas normales + Carcasa + Vaporizador  |  Dif: 60"),
                ("Carga Química Ultrafuerte (1)",   "Kit Química: 2 Cargas fuertes + Carcasa + Vaporizador  |  Dif: 65"),
                ("Cargas Revit. normales (2)",      "Kit Química: 4 Cargas débiles + Carcasa + Vaporizador  |  Dif: 65"),
                ("Cargas Revit. fuertes (2)",       "Kit Química: 3 Cargas normales + Carcasa + Vaporizador  |  Dif: 70"),
                ("Carga Revit. Ultrafuerte (1)",    "Kit Química: 2 Cargas fuertes + Carcasa + Vaporizador  |  Dif: 75"),
            ],
        },
    },

    "🍳 Cocina": {
        "color": ACCENT_GOLD,
        "subsecciones": {
            "Recetas en Olla": [
                ("Huevo Duro",              "Huevo + Vaso agua  |  +9 Sal"),
                ("Sopa de Fideos",          "Cuenco + Sobre fideos + 3 vasos agua  |  +26"),
                ("Arroz Blanco",            "Cuenco + Sobre arroz + 4 vasos agua + Sal  |  +18"),
                ("Patatas Cocidas",         "Cuenco patatas peladas + 4 vasos agua + Sal  |  +28"),
                ("Sopa de Ajo",             "Cuenco + Pimentón + Barra pan + 4 vasos agua + Ajos + Aceite  |  +30"),
                ("Estofado Carne Ave",      "Carne ave + Aceite + Sal + Zanahorias + Patatas + 4 vasos agua  |  +46"),
                ("Hervido",                 "4 cuencos peladuras (patatas/zanahorias/cebollas/judías) + Sal + 4 vasos  |  +48  Dom 86"),
                ("Macarrones",              "Leche + Sobre macarrones + Harina + Salchichas + Queso + Tomate frito  |  +57"),
                ("Guiso de Alubias",        "Saco alubias + 4 vasos + Pimentón + Chorizo + Tocino + Carne ave + Aceite + Sal  |  +54"),
                ("Spaguetti al Huevo",      "Spaguettis + Plato + Huevo + Bacon + Mantequilla + 4 vasos + Sal + Queso + Pimentón  |  +80"),
                ("Spaguetti Bolognesa",     "Spaguettis + Plato + 4 vasos + Mantequilla + Carne ave + Tomate frito + Aceite + Sal + Pimienta + Queso  |  +110"),
            ],
            "Frituras (Fogones)": [
                ("Tostada con Mantequilla", "Rebanada pan + Mantequilla + Sartén  |  +12"),
                ("Huevo Frito",             "Huevo + Plato + Aceite + Sal + Sartén  |  +12"),
                ("Huevos Fritos con Bacon", "2 Huevos + Plato + Aceite + Sal + Bacon + Sartén  |  +29"),
                ("Tomate Frito",            "Cuenco tomates + Aceite + Sal + Azúcar + Sartén  |  +11"),
                ("Salchichas al Licor",     "Salchichas + Licor suave + Vaso agua + Aceite + Sartén  |  +61"),
                ("Migas",                   "Barra pan + Cuenco + Leche + Tocino + Aceite + Ajo + Pimentón + Cuchillo + Sartén  |  +70"),
                ("Tortitas de Chocolate",   "Plato + Harina + Azúcar + Leche + Sartén + Sirope chocolate + Aceite  |  +67"),
                ("Tortitas de Vainilla",    "Plato + Harina + Azúcar + Leche + Sartén + Sirope vainilla + Aceite  |  +65"),
                ("Arroz a la Cubana",       "Cuenco arroz blanco + Cuenco tomate frito + Huevo frito + Sartén  |  +75"),
                ("Nuggets de Pollo",        "Mesa: Pollo + Harina + Agua + Sal + Pimienta + Huevos batidos\nFogones: Sartén + Pollo rebozado + Plato  |  +64"),
                ("6 Hot Dogs",              "6 Panecillos + Plato salchichas + Ketchup + Mostaza + 6 servilletas  (en mesa)"),
            ],
            "Ensaladas y Horno": [
                ("Salsa Alioli",         "Cuenco + Aceite + Ajos + Huevo + Tenedor largo  |  +19"),
                ("Ensalada Mixta",       "Cuenco tomates + Cuenco cebollas + Lechuga + Huevo duro + Atún + Aceite + Vinagre + Sal  |  +60"),
                ("Patatas Alioli",       "Cuenco salsa alioli + Cuenco patatas cocidas"),
                ("Compota de Manzana",   "Cuenco manzanas + Azúcar + Licor suave  [Horno]  |  +20"),
                ("Patatas Asadas",       "Cuenco patatas + Mantequilla + Sal  [Horno]  |  +35"),
                ("Bizcocho Casero",      "Harina + Levadura + 4 Huevos + 3 vasos agua + Azúcar + Plato  [Horno]  |  +70  Dom 158"),
                ("Tarta de Manzana",     "Cuenco de masa + Azúcar + 5 manzanas grandes + Plato  [Horno]  |  +42"),
                ("Cookies Caseras",      "Cuenco de masa + Sirope de chocolate  [Horno]  |  +50"),
            ],
            "Recetas Especiales": [
                ("Paella",        "Fogones: Sartén + Plato + Aceite + Carne ave + Judías + Tomate frito\n  + 6 vasos agua + Sal + Pimentón + Arroz  |  +165  Dom 188"),
                ("Fingers Queso", "Mesa: Cuchillo + Queso rallado + Huevos batidos + Harina + Pan rallado\nFogones: Sartén + Fingers rebozados + Plato + Aceite  |  +190  Dom 188"),
                ("Fondue",        "Olla: Queso Monterey Jack + Queso Cheddar + Queso Suizo + Queso + Aceite\n  + Ajos + Carne ave + Patatas + Sal + Tenedor largo  |  +250  Dom 215"),
                ("Pizza",         "Masa en mesa → Tortilla francesa con chorizo en fogones\n  Horno: base + tortilla + tomate frito + atún + salchichas\n  + queso Cheddar + sal + 2 huevos duros + bacon  |  +350  Dom 230"),
            ],
        },
    },

    "⚗️ Química": {
        "color": "#A855F7",
        "subsecciones": {
            "Primeros pasos": [
                ("Kit de Química",      "Dar 6 cuencos de gelatina a Schwarkoff — WC Enfermería 2N"),
                ("Ácido Acético",       "= Vinagre — comprar al Cocinero de Cocina Este"),
                ("Ácido Nítrico",       "Batería de coche (sótanos): Frasco Cristal Duro + Trapo Limpio + Cristal Azulado"),
                ("Ácido Sulfúrico",     "Batería de coche (sótanos): Frasco Cristal Duro + Trapo Limpio + Cristal de Azufre"),
                ("Carcasas de Spray",   "Armarios de cristal de las enfermerías"),
                ("Frascos Riboflavina", "Armarios de cristal de las enfermerías"),
                ("Pieza sucia Látex",   "Cubos de basura de las enfermerías"),
                ("Goma Quirúrgica",     "Cubos de basura de las enfermerías"),
                ("Frascos Sucios",      "Estanterías de Economatos, comedores o almacenes"),
                ("Frascos Limpios",     "Limpiar frascos sucios en cualquier grifo"),
                ("Kit Montaje Sprays",  "1500$ a la enfermera de guardia"),
            ],
            "Kit de Química — Recetas": [
                ("Golosina revitalizante  Dif 9",   "Cuenco gelatina + Ginseng + Riboflavina"),
                ("Cataplasma  Dif 15",               "Vaso agua + Tela algodón remendada + Tiamina + Riboflavina"),
                ("Brebaje vitamínico  Dif 19",       "Agua + Ginseng + Piridoxina + Frasco limpio"),
                ("Brebaje adrenalínico  Dif 26",     "Agua + Retinol + Riboflavina + Frasco limpio"),
                ("Brebaje de fortificante  Dif 32",  "Agua + Tiamina + Piridoxina + Frasco limpio"),
                ("Polvos nandralona  Dif 50",        "Agua + Vinagre + Frasco limpio + Sobre nandralona"),
                ("Lata pólvora negra  Dif 50",       "Trozo carbón + Puñado salitre + Lata azufre"),
                ("2 Cargas revit. normales  Dif 55", "Carcasa + Vaporizador + 4 Cargas revitalizantes débiles"),
                ("Poción Velocidad +5  Dif 60",      "Agua + Frasco limpio + Polvos nandralona"),
                ("Analgésico  Dif 62",               "Ginseng + Retinol + Tiamina + Piridoxina + Riboflavina + Cápsulas vacías + Colecalciferol"),
                ("3 Cargas químicas norm.  Dif 65",  "Carcasa + 4 Cargas químicas débiles + Vaporizador"),
                ("Brebaje revitalizante  Dif 71",    "Ginseng + Retinol + Tiamina + 2 Piridoxina + 2 Riboflavina + Colecalciferol + Frasco cristal"),
                ("Lata pólvora refinada  Dif 75",    "2 Latas pólvora negra + Ácido sulfúrico"),
                ("Calmantes de glicerina  Dif 79",   "2 Piridoxina + Magnesio + Cápsulas + 2 Colecalciferol + Famotidina"),
                ("Lata de glicerina  Dif 80",        "Calmantes de glicerina + Lata vacía"),
                ("Analgésicos Potentes  Dif 87",     "Calmantes glicerina + 2 Riboflavina + 2 Magnesio + Cápsulas + Famotidina"),
                ("Sulfamidas  Dif 99",               "Ginseng + Retinol + Tiamina + Riboflavina + Magnesio + 2 Colecalciferol + Frasco cristal"),
                ("Lata nitroglicerina  Dif 100",     "2 Latas glicerina + Ácido sulfúrico + Ácido nítrico"),
                ("Antiséptico  Dif 130",             "Retinol + Brebaje revitalizante + Analgésicos potentes + Famotidina"),
                ("Antibióticos  Dif 145",            "Sulfamidas + Antiséptico + Colecalciferol"),
                ("Antibióticos clínicos  Dif 150",   "Sulfamidas + Antiséptico clínico + Colecalciferol"),
                ("Megacomplejo nutritivo  Dif 230",  "Famotidina + 5 Raciones de Paella Valenciana"),
            ],
            "Sprays avanzados": [
                ("Spray curativo +10/+14/+15  Dif 95",   "Difusor + Canuto + Carcasa + Globo Seda Revit. ZH7/ZH4/ZH6"),
                ("Spray Fuerza +3/+4/+6  Dif 105",       "Difusor + Canuto + Carcasa + Globo Seda/Látex Fortif. NH3/NH2/NH8"),
                ("Spray Agilidad +3/+4/+6  Dif 105",     "Difusor + Canuto + Carcasa + Globo Seda/Látex Adrenal. TO2/TO9/TO8"),
                ("Spray Destreza +3/+4/+6  Dif 105",     "Difusor + Canuto + Carcasa + Globo Seda/Látex Vitam. FG2/FG8/FG1"),
                ("Spray curativo +20/+25/+35  Dif 110",  "Difusor + Canuto + Carcasa + Globo Seda Revit. NM9/NM1/NM3"),
                ("Spray tóxico Fuerza/Agil/Dest -3  Dif 123", "Difusor + Canuto + Carcasa + Globo Látex correspondiente"),
                ("Spray super revit. +30  Dif 130",      "Difusor + Canuto + Carcasa + Globo Seda Revit. THX"),
                ("Spray curativo +45  Dif 135",          "Difusor + Canuto + Carcasa + Globo Seda Revit. CO7"),
                ("Spray curativo +70  Dif 155",          "Difusor + Canuto + Carcasa + Globo Seda Revit. CO3"),
                ("Spray curativo +85  Dif 170",          "Difusor + Canuto + Carcasa + Globo Seda Revit. CH3"),
                ("Spray curativo +95  Dif 180",          "Difusor + Canuto + Carcasa + Globo Seda Revit. CH6"),
            ],
        },
    },

    "💎 Joyería": {
        "color": "#22D3EE",
        "subsecciones": {
            "Proceso completo": [
                ("Paso 1 — Roca",        "Joyero en 3E Azotea 'Sala Aljibes Sur'\n  → Entregar Roca del Yacimiento → Fragmento Cristalizado (1 Verde ó 1 Rojo)"),
                ("Paso 2 — Fragmento",   "Joyero en 3S Enfermería 'Sala Rehabilitación Sur'\n  → Rojo = 2 joyas desconocidas / Verde = 1 joya desconocida"),
                ("Paso 3 — Identificar", "Joyero en Cine Sur (3W) — Entregar joya + dinero → Joya conocida\n  (3 tipos: Reconstruida, Vidriosa, Orbicular)"),
                ("Mechero Bunsen",       "Solo lo da Comandante Esperanza (Bosque Sur/Norte)\n  Solo se puede matar con 1 LEÑO (misión Novato Prisionero, Bosque Sur/Norte)"),
            ],
            "Precio de identificación": [
                ("Zafiro",    "64.000$  →  Ira, Absorción bombas, Doble turno, Anti-Bombas"),
                ("Topacio",   "41.000$  →  Golpe Rejuvenecedor, Barrido, Aturdir"),
                ("Ámbar",     "36.000$  →  P.A., Furia Sanguinaria, Corte Profundo"),
                ("Camafeo",   "22.500$  →  Agilidad, Daño, Golpe a Traición"),
                ("Azurita",   "17.000$  →  Habilidades armas (Distancia, Contundentes, Marciales)"),
                ("Rubí",      "12.500$  →  Tiro Certero, Ráfaga, Herida Sangrante"),
                ("Esmeralda", " 9.500$  →  Destreza, Fuerza, Bonus contra armas (solo protecciones)"),
            ],
            "Fragmentos según atributos": [
                ("Rodio",    "Prenda con 1 atributo"),
                ("Paladio",  "Prenda con 2 atributos"),
                ("Iridio",   "Prenda con 3 atributos"),
                ("Rutenio",  "Prenda con 4 atributos"),
                ("Osmio",    "Prenda con 5 atributos"),
            ],
        },
    },

    "⚡ Habilidades": {
        "color": ACCENT_GREEN,
        "subsecciones": {
            "Entrenadores": [
                ("Ratter",         "Aturdir, Golpe a Traición, Tiro Certero, Furia Sanguinaria  |  Distribuidor interior (2S)"),
                ("McNamara",       "Doble Ataque, Contraataque  |  Patio interior (3S)"),
                ("Clemente",       "Esquivar, Desarmar  |  Aseos (4W)"),
                ("Dr. Eclipse",    "Herida Sangrante, Corte Profundo  |  Patio Interior (1N)"),
                ("Maestro Armero", "Regeneración, Torbellino, Barrido, Uchimata, Golpe Rejuvenecedor, Ráfaga\n  |  Bosque Exterior Sur o Norte  —  Nivel mínimo: 120"),
            ],
            "McNamara": [
                ("Doble Ataque MER Nv10",   "Ensalada Mixta + Botella Vermouth + 8 Rebanadas pan + Sopa ajo\n  + Compota manzana + Estofado carne ave + Escalpelo Dr. Fausto\n  → Peto del Mossad"),
                ("Doble Ataque ASU/MAF/NAR Nv20", "Gafas Freak + Casco/Calzones/Peto/Botas Kevlar + Sopa de Queso  → Peto Spec Op"),
                ("Doble Ataque ATR Nv30",   "Escalpelo Dr. Vicious + Mazo Júpiter + Cuchillo Norman B. + Cinturón Roger  → Botas Schindler"),
                ("Contraataque NAR Nv9",    "Zapatos Crazy Bat + Bufanda Cartón + Jersey Algodón\n  + Pantalones Seda + Collar orejas Crazy Bat  → Medallón Zinc"),
                ("Contraataque ASU Nv13",   "Rodilleras Piel + Calzones Piel + Botas Piel\n  + Casco Nylon/Acero + Pantalones Tela Acolchada  → Medallón Carbono"),
                ("Contraataque MER Nv17",   "10 Collares Crazy Bat + 10 Anillos Wall Broker\n  + 10 Botas Black Sister + 10 Guantes Clown  → Medallón Cobre"),
            ],
            "Ratter": [
                ("Aturdir POL/ASU/MAF Nv5",  "10 Hot Dog + 2 Frascos sal + 8 Rebanadas pan + 10 Botellas aceite  → Maza Vulcano"),
                ("Aturdir HAC Nv7",          "2 Collares orejas Black Widow + Roca Volcánica + Guantes Algodón  → Maza Neptuno"),
                ("Aturdir TIM Nv9",          "Peto/Pantalones Nylon y Corcho + 3 Zapatos Crazy Bat  → Maza Odín"),
                ("Aturdir LAD Nv11",         "5 Cristales Azulados + 2 Juegos Póker de Clown  → Mazo Thor"),
                ("Aturdir ATR/NAR Nv13",     "5 Orejas Radical + Botella Whisky + Ginebra + Cuenco Sangre Carne  → Mazo Júpiter"),
                ("Aturdir MER/ASU Nv20",     "10 Gafas Freak + 10 Camisetas Plateadas + 10 Gorros Algodón + 10 Pistolas Glock  → Maza Zeus"),
                ("Furia Sanguinaria ASE Nv30","5 Tablas Clavos Infectados + 5 Hachas Excaliboor + 15 Tartas Manzana\n  + 10 Pañuelos Red Devil + Coquilla Reforzada"),
            ],
            "Clemente y Dr. Eclipse": [
                ("Esquivar TIM/POL Nv3",    "Plato Salchichas + Patatas Fritas  → Cinturón Hunter"),
                ("Esquivar ATR Nv7",        "2 Comics Manga + 2 Revistas Eróticas + 2 Comics Superhéroes  → Cinturón Roger"),
                ("Esquivar LAD/HAC Nv8",    "1000$ + 2 Collares orejas Crazy Bat + Medallón Brick Head  → Cinturón Langley"),
                ("Desarmar LAD Nv25",       "Cuchillo Carnicero + 2 Aspas Ventilador + 3 Tijeras Podar\n  + 2 Escalpelos Infectados + 3 Bisturís infectados  → Porra Carabinieri"),
                ("Corte Profundo HAC Nv3",  "Medallón Brick Head + Collar orejas Crazy Bat + Collar orejas Cyber Angel  → Cuchillo Jack Ripper"),
                ("Corte Profundo NAR/MAF Nv10", "Bufanda Seda + Chaleco Seda + Pantalones Seda + Sandalias Piel  → Cuchillo Lexter"),
                ("Herida Sangrante MER Nv5","Collar Crazy Bat + Medallón Brick Head + Collar Cyber Angel + Collar Black Window  → Escalpelo Dr. Fausto"),
                ("Herida Sangrante TIM/LAD Nv7","Roca Verde  → Escalpelo Dr. Franky"),
                ("Herida Sangrante ATR/ASU Nv10","Botas Black Sisters + Bufanda Seda + Cristales Azulados + 2 Jarrones Pledgiki  → Escalpelo Dr. Vicious"),
            ],
            "Maestro Armero Nv120": [
                ("Regeneración TIM/POL",  "10 Globos Látex Adrenalínicos TO5 + 10 Globos Látex Fortificantes NHS\n  + 10 Globos Látex Vitamínicos FG9"),
                ("Torbellino ASE/ASU",    "50 Antibióticos Clínicos"),
                ("Barrido TIM/LAD/ATR",   "Lanza Zinc + Lanza Carbono + Lanza Acero + Lanza Oro + Lanza Titanio"),
                ("Uchimata MER",          "Sierra Mecánica: Pissline + Pingwood + Tochiba + Boss + Philslap + Gump + Frioneer"),
                ("Ráfaga ASU/MAF/NAR",    "Clavadora: Gump + Boss + Philslap + Frioneer + Pingwood + Pissline + Tochiba"),
                ("Golpe Rejuvenecedor",   "Datos desconocidos — consultar www.gentelaprision.es"),
            ],
        },
    },

    "👗 Prendas Esencia": {
        "color": "#F472B6",
        "subsecciones": {
            "Esencia 50  (Linda la Divina — Calabozos Noreste 1S)": [
                ("Casco   → 2 Sabiduría",      "Wild Dog (Nv 50–75), Creppled Corpse (Nv 50–75)"),
                ("Mangas  → 3 Agilidad",        "Wild Boar (Nv 65–75), God's Rage (Nv 75)"),
                ("Cinturón → 3 Elegancia",      "Evil Witch Nv50, Creepy, Creppled Corpse, Dragon (varios niveles 50–75)"),
                ("Botas   → 4 Resistencia",     "Creepy (Nv 50–54), Wild Dog (Nv 54–75)"),
                ("Zapatillas → 4 Resistencia",  "Robber Baron, Wild Dog, Creppled Corpse, Wild Boar (Nv 50–73)"),
                ("Peto    → 6 Fuerza",          "Robber Baron Nv52, Wild Dog Nv50–52, Guardias Especiales/Cabo/Sargento/Oficial MER"),
                ("Guantes → 2 Habilidad",       "Wolf Chest, Robber Baron, Wild Dog, Creppled Corpse, Dragon (Nv 50–75)"),
                ("Pantalones → 5 Protección",   "Evil Witch, Wolf Chest, Creepy, Robber Baron, Guardias Asalto (Nv 50–80)"),
            ],
            "Esencia 70  (Linda la Divina — Calabozos Noreste 1S)": [
                ("Casco   → 2 Sabiduría",    "God's Rage (Nv 71–85)"),
                ("Mangas  → 3 Agilidad",     "God's Rage (Nv 78–85)"),
                ("Cinturón → 3 Elegancia",   "Wild Boar (Nv 72–79)"),
                ("Botas   → 4 Resistencia",  "Wild Boar (Nv 70–78)"),
                ("Zapatillas → 4 Resistencia","Wild Boar: Vigilante TIM 70, Devastador MER 77"),
                ("Peto    → 6 Fuerza",       "Dragon (Nv 76–85)"),
                ("Guantes → 2 Habilidad",    "God's Rage (Nv 75–84)"),
                ("Pantalones → 5 Protección","Mad Gang (Nv 81–90), Black Cat (Nv 81–90)"),
            ],
            "Esencia Divina 100  (Linda la Divina — Calabozos Noreste 1S)": [
                ("Casco   → 4 Sabiduría",    "Vigilante: Asesina ASU 100"),
                ("Mangas  → 6 Agilidad",     "Strangler (Nv 85–100)"),
                ("Cinturón → 6 Elegancia",   "Dragon (Nv 75–84)"),
                ("Botas   → 8 Resistencia",  "Black Cat (Nv 81–100)"),
                ("Zapatillas → 8 Resistencia","Strangler (Nv 85–100)"),
                ("Peto    → 12 Fuerza",      "Italianos: Fredo, Andolini, Mancini, Lumberto, Vincent (MAF 82–83)"),
                ("Guantes → 4 Habilidad",    "Scar-Face (Nv 90–99)"),
                ("Pantalones → 10 Protección","Mad Gang (Nv 81–99)"),
            ],
            "Maese  (Arcanos de tu delito Nv 120)": [
                ("Casco Maese → 3 Sabiduría",    "Clown Aprendiz-Arcano/GuíaDeLuz/ARCANO (TIM 120)"),
                ("Brazalete → 3 Agilidad",        "Strangler, Brick Head, Wall Brocker Arcanos (MER/MAF/ASU 120)"),
                ("Cinturón → 3 Elegancia",        "Freak, Black Sister Arcanos (ASE/LAD 120)"),
                ("Botas → 3 Resistencia",         "Red Devil, Undead Horse, Black Cat Arcanos (HAC/POL/NAR 120)"),
                ("Zapatillas → 3 Resistencia",    "Dragon, Radical, Black Widow Arcanos (MER/ASU/ATR 120)"),
                ("Peto → 3 Fuerza",               "Crazy Bat Arcanos (ASE 120)"),
                ("Guantes → 3 Habilidad",         "Pinky Killer Arcanos (MAF 120)"),
                ("Pantalones → 3 Protección",     "Cyber Angel Arcanos (MER 120)"),
            ],
        },
    },

    "🔧 Mecánica": {
        "color": "#FB923C",
        "subsecciones": {
            "Proveedores y materiales": [
                ("Monitor de Mecánica",      "Sala TV Oeste, Patio 4E, Área Cocina Oeste, Patio 3S, Enfermería Sur\n  → Lata vacía, Pila petaca, Destornillador, Lima, Cartuchos carga, Moldes, Envoltorio explosivo"),
                ("Auxiliar de Mecánica",     "Patio 1W, Área Descanso Oeste, Distribuidor\n  → Válvula, Soplete de precisión, Papel de impresora"),
                ("Informática Empedernida",  "Cualquier Economato  → Esquemas Alpha/Beta/Gamma, Chipsets"),
                ("Ebbinhaus",                "Sótanos Norte  → Botella cristal, Esparadrapo especial, Acero, Plata"),
                ("Champman/Dianne",          "Sala Máquinas Sur/Oeste  → Chipsets, Oro, Cordón, Equipo soldadura"),
                ("Arena",                    "Paredes de los distribuidores"),
                ("Azufre",                   "Estanterías de los almacenes"),
                ("Carbón/Zinc/Hierro",       "Caja de metales — Patios de basuras"),
                ("Chipsets",                 "Will Board — botín al matarlos"),
                ("Estaño",                   "Wall Brockers en Biblioteca 3N"),
                ("Platino",                  "Clown, Freak, Evil Witch, Wolf Chest, Robber Baron — botín"),
                ("Salitre",                  "Tapas de alcantarillas (patios de azotea)"),
                ("Termómetro",               "Creepys — botín en calabozo este"),
                ("Hierro rojo",              "Tuberías de calabozos y pasillos lavanderías"),
            ],
            "Horno de Alfarería — Láminas": [
                ("Lámina hierro    Dif 10",   "Martillo planchado + Trozo de hierro"),
                ("Lámina zinc      Dif 30",   "Martillo planchado + Trozo de zinc"),
                ("Lámina acero     Dif 50",   "Martillo planchado + Trozo de acero"),
                ("Lámina titanio   Dif 85",   "Rollo estaño + Soplete + Martillo planchado + Trozo de titanio"),
                ("Lámina plata     Dif 90",   "Lata lubricante + Soplete + Martillo planchado + Trozo de plata"),
                ("Lámina oro       Dif 110",  "Lata lubricante + Soplete + Martillo planchado + Trozo de oro"),
                ("Lámina carbono   Dif 130",  "Lata azufre + Soplete + Martillo planchado + Trozo de carbono"),
                ("Cócktail explosivo Dif 100","Botella cristal + Lata barniz + Carga explosiva"),
                ("Cócktail Molotov  Dif 140", "Botella cristal + Lata barniz + Carga incendiaria"),
                ("Cócktail Molotov terrible 160","Botella cristal + Lata barniz + Carga explosiva especial"),
            ],
            "Tornillo de Banco — Armas": [
                ("Rifle perdigones   Dif 40",  "Tornillo + Lámina zinc + Destornillador + Esquema + Pieza rifle"),
                ("Escopeta de sal    Dif 40",  "Tornillo + Lámina zinc + Destornillador + Esquema + Pieza escopeta"),
                ("Tirachinas látex   Dif 40",  "Astilla madera + Pieza látex + Cordón + Goma quirúrgica + Esquema tirachinas"),
                ("Rifle 9mm          Dif 60",  "Tornillos + Lámina acero + Destornillador + Esquema + Pieza"),
                ("Escopeta paralela  Dif 60",  "Tornillo + Lámina acero + Destornillador + Esquema + Pieza"),
                ("Rifle 17mm         Dif 100", "Rollo estaño + Tornillo + Soplete + Destornillador + Lámina plata + Esquema + Pieza"),
                ("Escopeta precisión Dif 100", "Rollo estaño + Tornillo + Soplete + Destornillador + Lámina plata + Esquema + Pieza"),
                ("Rifle 21mm         Dif 120", "Rollo estaño + Tornillo + Soplete + Lámina oro + Esquema + Pieza"),
                ("Escopeta 12        Dif 120", "Rollo estaño + Tornillo + Soplete + Lámina oro + Esquema + Pieza"),
                ("Rifle francotirador Dif 140","Tornillo + Soplete + Destornillador + Lámina carbono + Rollo platino + Esquema + Pieza"),
                ("Rifle franc. especial 140",  "Ídem + 2 Láminas carbono + Trozo U-235"),
            ],
            "Mesa de Trabajo — Explosivos": [
                ("Carga explosiva        Dif 75",  "Rollo estaño + Destornillador + Pólvora refinada + Nitroglicerina + Cartuchos carga"),
                ("Carga bioquímica       Dif 90",  "Rollo estaño + Destornillador + Compuestos bioquímicos + Cartuchos carga"),
                ("Carga incendiaria      Dif 110", "Rollo estaño + Gas butano + Gasolina + Queroseno + Destornillador + Cartucho tinta"),
                ("Carga explosiva esp.   Dif 150", "Destornillador + Rollo platino + Trozo U-235 + Cartuchos carga"),
                ("Cartucho de dinamita   Dif 200", "Envoltorio explosivo + Carga explosiva + Detonador"),
                ("Explosivo Goma-2       Dif 210", "3 Envoltorios + 3 Cargas explosivas + 2 Detonadores"),
                ("Explosivo TNT          Dif 230", "5 Envoltorios + 5 Cargas explosivas + 3 Detonadores"),
                ("Explosivo TNT especial Dif 230", "5 Envoltorios + 5 Cargas + Carga especial + 3 Detonadores"),
                ("Granada Electrónica    Dif 230", "Ídem TNT especial + Granada electrónica desarmada"),
            ],
            "Fabricación de Munición": [
                ("Balas 9mm (10)",         "Molde Calibre 9  |  Pólvora Negra + 10 Casquillos + 10 Proyectiles"),
                ("Balas 12mm (10)",        "Molde Calibre 12  |  Pólvora Negra + 10 Casquillos + 10 Proyectiles"),
                ("Balas 12 Especial (10)", "Molde Calibre 12  |  Pólvora Refinada + 10 Casquillos + 10 Proyectiles"),
                ("Balas 15mm (10)",        "Molde Calibre 15  |  Pólvora Negra + 10 Casquillos + 10 Proyectiles"),
                ("Balas 21mm (10)",        "Molde Calibre 21  |  Pólvora Negra + 10 Casquillos + 10 Proyectiles"),
                ("Balas Mercurio (25)",    "Molde Calibre 21  |  Pólvora Refinada + 25 Casquillos + 25 Proyectiles + 1 Termómetro"),
                ("Cartucho Perforador (25)","Molde Calibre 21  |  Pólvora Refinada + 25 Casquillos + 1 Refuerzo Carbono"),
            ],
        },
    },

    "🧵 Costura": {
        "color": "#A3E635",
        "subsecciones": {
            "Conseguir las Tijeras": [
                ("#1  Sniper  (Azotea Oeste)",           "Huevos fritos con bacon + 4 Tostadas con mantequilla + 1 Queso Cheddar\n  → Diploma Sniper"),
                ("#2  Demetrius  (Taller Alfarería Oeste)","Entregar Diploma Sniper → pide Diploma + 3000$"),
                ("#3  Demetrius  (Taller Alfarería Oeste)","Diploma Sniper + 3000$  → Diploma de Costura Falsificado"),
                ("#4  Brooks Haddon  (Biblioteca Oeste)", "Diploma de Costura Falsificado  → Tijeras de Costura + Libro de Haddon ✓"),
            ],
            "Costurero — Prendas básicas": [
                ("Pieza gruesa nylon   Dif 1",    "Tijeras costura + 10 Mantas gruesas lavadas"),
                ("Pieza cartón trab.   Dif 4",    "Tijeras costura + Trozo de cartón arrancado"),
                ("Pieza de seda        Dif 6",    "Hilo de coser + Jiro de seda"),
                ("Prendas Cartón       Dif 70",   "Patrón + Piezas cartón trabajado + Hilo  (bufanda/gorro/casco/chaleco/jersey/peto/calzones/pantalones/botas/mangas/guantes/sandalias)"),
                ("Prendas Algodón      Dif 113",  "Patrón + Tela algodón remendada + Hilo"),
                ("Prendas Seda         Dif 123",  "Patrón + Hilo + Piezas de seda (2–5 según prenda)"),
                ("Prendas Nylon        Dif 134",  "Patrón + Hilo + Piezas gruesas nylon (cantidad varía)"),
            ],
            "Costurero Profesional": [
                ("Globo vacío seda    Dif 145",   "Hilo + Pieza de seda + Tijeras de costura"),
                ("Globo vacío látex   Dif 145",   "Hilo + Pieza de látex limpia + Tijeras de costura"),
                ("Prendas Piel        Dif 163",   "Patrón + Hilo + Piezas de tela refinada"),
                ("Prendas Piel Ref.   Dif 176",   "Patrón + Hilo + Piezas tela refinada + Refuerzos de acero"),
                ("Prendas Kevlar      Dif 187",   "Patrón + Piezas kevlar + Hilo"),
                ("Prendas Maese       Dif 230",   "Tijeras de Brooks + Baño especial arcano\n  + Trozos tela bota élite (2–8 según prenda) + Prenda maese inacabada"),
            ],
            "Refuerzos": [
                ("Refuerzo espuma  Dif 1",    "Trozo espuma + Astilla madera + Hilo de coser"),
                ("Refuerzo corcho  Dif 1",    "Astilla madera + Trozo corcho + Tubito pegamento"),
                ("Refuerzo Zinc    Dif 100",  "2 Clavos pequeños acero + Astilla madera + Lámina zinc"),
                ("Refuerzo titanio Dif 140",  "2 Clavos + Astilla madera + Lámina titanio"),
                ("Refuerzo plata   Dif 160",  "2 Clavos + Astilla madera + Lámina plata"),
                ("Refuerzo oro     Dif 180",  "2 Clavos + Astilla madera + Lámina oro"),
                ("Refuerzo carbono Dif 200",  "2 Clavos + Astilla madera + Lámina carbono"),
            ],
        },
    },

    "🏆 Carlito-Coraza": {
        "color": ACCENT_RED,
        "subsecciones": {
            "Resumen y objetivo": [
                ("Objetivo final",   "Combinar en el Altar de Capilla:\n  Anillo de la compañía del testículo\n  + Martillo de la Luz  +  Testículo Único de Poder\n  → CARLITO-CORAZA"),
                ("Los 6 elementos",  "1. Planos del arma definitiva\n2. Calavera del Rey Ghoul\n3. Maza de guerra de Cassandra\n4. Escrituras perdidas de Kaifas (6 escrituras)\n5. Miembro de Héctor el Zombi\n6. Polvo rojo"),
                ("Tras entregar",    "Kaifas entrega: 10 ADCC + Anillo de la compañía del testículo\n  → Matar Carlito Brygante → Testículo Único de Poder\n  → Entregar a Kaifas → Martillo de la Luz"),
            ],
            "Elementos 1–3": [
                ("1  Planos",         "Hablar con WongLong — Aseos pabellón oeste (4N)  [sin entregar nada]"),
                ("2  Calavera Ghoul", "Matar con ARMA A DISTANCIA al Rey Ghoul lvl 120\n  — Guarida frente a zombis de 1S"),
                ("3  Maza Cassandra", "Matar con ARMA CONTUNDENTE a Cassandra Femme lvl 120\n  — Guarida frente a mineros de 2S"),
            ],
            "Escrituras (Elemento 4)": [
                ("Escritura 1", "Robar al Sargento Ghoul (zombis 1S) la escritura manchada → entregarla a Kaifas"),
                ("Escritura 2", "Entregar Peto Arcano de tu delito a DonVitto\n  — Colector sótanos 2N (Creepy)"),
                ("Escritura 3", "Entregar a tu Arcano las bombillas Nº1/2/3/4\n  — Matando Ancianos Arcanos lvl 120 en cada módulo de celdas con arma a distancia"),
                ("Escritura 4", "Entregar al Dr. Skull (escalera sótano 4S):\n  4 manos + 12 pies + 5 dedos + 20 orejas de zombis"),
                ("Escritura 5", "Entregar al Coronel de Élite (1E/4W):\n  5 sellos de cada tipo + 3 móviles de cada tipo (5 clases)\n  — Matando psicópatas en 1N y 2N lvl 115-120"),
                ("Escritura 6", "MISIÓN COMEDORES — ver subsección 'Misión Comedores'"),
                ("Entrega final","Los 6 trozos a Gumaro — Capilla 1N → Escrituras Perdidas"),
            ],
            "Misión Comedores (Escritura 6)": [
                ("Inicio",         "Cuchara de pala bendecida → Alcalde Butcher Norton\n  (bendecir: Kaifas + prendas maese de tu delito → te devuelve las protecciones + cuchara bendecida)"),
                ("Comedor Central","120 Paellas valencianas, 10 Macarrones, 25 Huevos bacon,\n  50 Patatas fritas, 12 Ensaladas mixtas, 60 Hot Dog, 12 Huevos duros, 6 Tortillas francesas"),
                ("Comedor Este",   "25 Fondues, 12 Sopas queso Cheddar, 6 Cuencos cereales,\n  50 Cookies caseras, 10 Spaguetti al huevo, 12 Sopas fideos, 100 Palomitas, 12 Salchichas al licor"),
                ("Comedor Oeste",  "20 Fingers rebozados, 80 Hamburguesas dobles especiales,\n  10 Mazorcas maíz gratinadas, 5 Tartas manzana, 30 Pizzas, 7 Tortitas vainilla, 7 Tortitas chocolate, 50 Ensaladas americanas"),
                ("Fin",            "Cada cocinero devuelve la nota + su nota específica\n  → Las 3 notas al Alcalde Butcher Norton → Escritura 6"),
            ],
            "Polvo Rojo (Elemento 6)": [
                ("Ingredientes",    "Combinar en combinador (planta junto al alcaide):\n  A. Semillas de la desgracia\n  B. Láminas del testículo\n  C. Sangre de Carlito\n  D. Cuchara de pala bendecida\n  E. Orín de Carlito"),
                ("A — Semillas",   "Dr. Skull → nota → doctores en morgues:\n  Bertran 1N: 10 calaveras resecas + 10 sin dientes\n  Ivanovic 2N: 10 calaveras frescas + 10 semipodridas\n  Smithers 3S: 10 calaveras relucientes + 10 sonrientes\n  Barreda 4N: 10 calaveras con vida + 10 completas\n  → 4 notas al Dr. Skull (sótanos oeste) → Semillas"),
                ("C — Sangre",     "Matar Hanibal Trinchacarnes lvl 120 — Cine patio descanso sur (3N)"),
                ("E — Orín",       "Misión de las Sobrinas:\n  4 chicas en locutorio norte 1N: Verónica, Noelia, Sandra, Aida\n  3 chicos: Andrés (loc. este 2N), Rafael (loc. sur 3E), Martín (loc. oeste 4E)\n  → Cadena de cartas (puede fallar, reintentar) → 4 anillos\n  → Anillo de Aida a Kaifas → vaso para el orín\n  → Vaso + 3 anillos a Barrabás/Juliani (capillas) → Orín de Carlito"),
            ],
        },
    },

    "📈 Subir de Nivel": {
        "color": ACCENT_CYAN,
        "subsecciones": {
            "Tabla de Bots por nivel": [
                ("Escala de poder",        "Novato → Pardillo → Paria → Chivato → Esbirro → Secuaz → Compinche\n  → Rompehuesos → Negociador → Medico → Cabecilla → Guardaespaldas → Devastador → Vengador → Jefe → Líder"),
                ("Crazy Bats",             "Niveles 1–40"),
                ("Brick Heads",            "Niveles 1–40"),
                ("Black Widows",           "Niveles 1–40"),
                ("Cyberangels",            "Niveles 1–40"),
                ("Black Sisters",          "Niveles 1–50"),
                ("Undead Horses",          "Niveles 1–35"),
                ("Wall Brokers",           "Niveles 1–25"),
                ("Radicals",               "Niveles 1–40"),
                ("Red Devils",             "Niveles 1–40"),
                ("Wolf Chest",             "Niveles 1–50"),
                ("Evil Witchs",            "Niveles 1–50"),
                ("Creppled Corpses",       "Niveles 1–65"),
                ("Robber Barons",          "Niveles 1–35"),
                ("Wild Dogs",              "Niveles 1–65"),
                ("Wild Boars",             "Niveles 1–40"),
                ("GodsRages",              "Niveles 1–55"),
                ("Mad Gang",               "Niveles 1–55"),
                ("Stranglers",             "Niveles 1–40"),
                ("Black Cats",             "Niveles 1–55"),
                ("Dragons",                "Niveles 1–25"),
                ("Scar-faces",             "Niveles 1–25"),
                ("Guardias Vigilancia",    "Niveles 1–20"),
                ("Guardias Seguridad",     "Niveles 1–35"),
                ("Guardias Especiales",    "Niveles 1–35"),
                ("Guardias Asalto",        "Niveles 1–40"),
                ("Guardias Antidisturbios","Niveles 1–40"),
            ],
            "Misiones sin pelear": [
                ("Nv 1  — Orejas",           "El Padrino de La Familia\n  Dar: 1 oreja de cualquier tipo\n  Ubicación: Patio 1W/4E, Azotea Norte, Área descanso O/S/E, Duchas módulo 2, Azotea Sur"),
                ("Nv 2  — Cucharas",         "El Padrino de La Familia\n  Dar: 1 Cuchara Afilada  |  Mismas ubicaciones"),
                ("Nv 15 — Llaves",           "Tiffany — Recepción Reclusos Noreste\n  Dar: 1 llave niquelada + 1 llave plata + 1 llave esmeralda"),
                ("Nv 15 — Licores",          "Bill / Negociador BrickHead — Área Enfermería Oeste / Duchas Módulo 2\n  Dar: Botella Ron + Coñac + Ginebra"),
                ("Nv 20 — Láminas y Toallas","Freak Carter — Azotea Sur (3E)\n  Dar: 1 Toalla Bordada Freak + 3 Láminas de Titanio"),
                ("Nv 20 — Roscos",           "Dake Dewell — Sala Rehabilitación Norte\n  Dar: 1 Rosco vino tinto + 1 Rosco vino blanco"),
                ("Nv 30 — Anillos y Llaves", "Dr. Smithers — Morgue Sur (3S)\n  Dar: 5 Anillos Esmeralda + 5 Llaves Esmeralda\n  → Anillo de oro macizo + Toalla Wong Long + Exp."),
                ("Nv 37 — Mantequillas",     "Billy Heyes — Biblioteca Oeste (4W)\n  Dar: 5 Mantequillas Deluxe + 5 Chóped Artesano + 5 Zumos Naranja  → 10 de tréboles + Exp."),
                ("Nv 40 — Fusiles",          "Slyboot — Oficina Seguridad Este\n  Dar: 2 Fusiles Coleccionista + Perla Mallorca + Bala 1ª Guerra\n  → Jarrón Slyboot + Dinero + Exp."),
                ("Nv 45 — Doblones",         "Janice — Locutorio Norte\n  Dar: Doblón Cobre + Doblón Plata + Doblón Oro"),
                ("Nv 65 — Calcetines",       "Sommerville — Recepción Reclusos Suroeste\n  Dar: 5 Medallones Will Board + 3 Calcetines Wild Board"),
                ("Nv 65 — Diamantes",        "Guardia Cabreadísimo — Patio Descanso Norte\n  Dar: Diamante puro + Diamante rojizo + Diamante verdoso"),
                ("Nv 70 — Chapas",           "Kitt — Comedor Oeste\n  Dar: 2 Dados God Rage + 2 Chapas de cada tipo de guardia (6 tipos)"),
                ("Nv 80 — Pelotas",          "Durango — Recepción Reclusos Noreste (1E)\n  Dar: Pelota de tenis + Pelota de béisbol"),
            ],
        },
    },
}


# ══════════════════════════════════════════════════════════════════════
#  VENTANA PRINCIPAL
# ══════════════════════════════════════════════════════════════════════

def abrir_guia():
    """Punto de entrada: crea y muestra la ventana de guías."""
    win = ctk.CTkToplevel()
    win.title("Guía — La Prisión Online  |  www.gentelaprision.es")
    win.geometry("1200x780")
    win.minsize(900, 600)
    win.configure(fg_color=BG_MAIN)
    win.grab_set()          # bloquea la ventana padre mientras está abierta
    win.focus_force()

    # ── Estado interno ──
    _state = {"guia": None, "sub": None}

    # ══════ LAYOUT RAÍZ ══════
    win.grid_columnconfigure(0, weight=0)   # panel izq guías
    win.grid_columnconfigure(1, weight=0)   # panel central subsecciones
    win.grid_columnconfigure(2, weight=1)   # contenido
    win.grid_rowconfigure(0, weight=0)      # header
    win.grid_rowconfigure(1, weight=1)      # cuerpo
    win.grid_rowconfigure(2, weight=0)      # footer

    # ══════ HEADER ══════
    header = ctk.CTkFrame(win, fg_color=BG_CARD, corner_radius=0,
                          border_width=0, height=56)
    header.grid(row=0, column=0, columnspan=3, sticky="ew")
    header.grid_propagate(False)
    header.grid_columnconfigure(1, weight=1)

    ctk.CTkLabel(header, text="⛓  GUÍA DE LA PRISIÓN",
                 font=("Segoe UI", 18, "bold"),
                 text_color=ACCENT_CYAN).grid(row=0, column=0, padx=20, pady=14, sticky="w")

    lbl_breadcrumb = ctk.CTkLabel(header, text="",
                                  font=("Segoe UI", 11), text_color=TEXT_DIM)
    lbl_breadcrumb.grid(row=0, column=1, padx=10, sticky="w")

    ctk.CTkLabel(header,
                 text="Fuente: www.gentelaprision.es",
                 font=("Segoe UI", 9), text_color="#333650"
                 ).grid(row=0, column=2, padx=20, sticky="e")

    # ══════ PANEL IZQUIERDO — guías ══════
    panel_left = ctk.CTkFrame(win, fg_color=BG_INNER, corner_radius=0,
                               border_width=0, width=180)
    panel_left.grid(row=1, column=0, sticky="nsew")
    panel_left.grid_propagate(False)
    panel_left.grid_rowconfigure(1, weight=1)
    panel_left.grid_columnconfigure(0, weight=1)

    ctk.CTkLabel(panel_left, text="CATEGORÍAS",
                 font=("Segoe UI", 9, "bold"), text_color=TEXT_DIM
                 ).grid(row=0, column=0, padx=12, pady=(12, 4), sticky="w")

    scroll_left = ctk.CTkScrollableFrame(panel_left, fg_color=BG_INNER,
                                         scrollbar_button_color="#222533")
    scroll_left.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)
    scroll_left.grid_columnconfigure(0, weight=1)

    # ══════ PANEL CENTRAL — subsecciones ══════
    panel_mid = ctk.CTkFrame(win, fg_color="#0E0F18", corner_radius=0,
                              border_width=0, width=220)
    panel_mid.grid(row=1, column=1, sticky="nsew")
    panel_mid.grid_propagate(False)
    panel_mid.grid_rowconfigure(1, weight=1)
    panel_mid.grid_columnconfigure(0, weight=1)

    ctk.CTkLabel(panel_mid, text="SECCIONES",
                 font=("Segoe UI", 9, "bold"), text_color=TEXT_DIM
                 ).grid(row=0, column=0, padx=12, pady=(12, 4), sticky="w")

    scroll_mid = ctk.CTkScrollableFrame(panel_mid, fg_color="#0E0F18",
                                         scrollbar_button_color="#222533")
    scroll_mid.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)
    scroll_mid.grid_columnconfigure(0, weight=1)

    # ══════ PANEL DERECHO — contenido ══════
    panel_right = ctk.CTkFrame(win, fg_color=BG_CARD, corner_radius=0, border_width=0)
    panel_right.grid(row=1, column=2, sticky="nsew", padx=0)
    panel_right.grid_rowconfigure(1, weight=1)
    panel_right.grid_columnconfigure(0, weight=1)

    # Búsqueda
    search_frame = ctk.CTkFrame(panel_right, fg_color=BG_INNER,
                                 corner_radius=8, border_width=1, border_color=BORDER)
    search_frame.grid(row=0, column=0, sticky="ew", padx=16, pady=(12, 6))
    search_frame.grid_columnconfigure(1, weight=1)

    ctk.CTkLabel(search_frame, text="🔍", font=("Segoe UI", 13),
                 text_color=TEXT_DIM).grid(row=0, column=0, padx=(10, 4), pady=6)

    search_var = tk.StringVar()
    search_entry = ctk.CTkEntry(search_frame, textvariable=search_var,
                                placeholder_text="Buscar en todas las guías...",
                                font=("Segoe UI", 12), fg_color=BG_INNER,
                                border_width=0, text_color=TEXT_MAIN)
    search_entry.grid(row=0, column=1, sticky="ew", pady=6, padx=(0, 10))

    # Área de contenido — canvas+scrollbar para filas
    content_scroll = ctk.CTkScrollableFrame(panel_right, fg_color=BG_CARD,
                                             scrollbar_button_color="#222533")
    content_scroll.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
    content_scroll.grid_columnconfigure(0, weight=1)

    # ══════ FOOTER ══════
    footer = ctk.CTkFrame(win, fg_color=BG_INNER, corner_radius=0, height=28)
    footer.grid(row=2, column=0, columnspan=3, sticky="ew")
    footer.grid_propagate(False)
    ctk.CTkLabel(footer,
                 text="⛓  Contenido basado en las guías de www.gentelaprision.es  —  La Prisión Online · Prisonserver · GenteLaPrision 2001–2020",
                 font=("Segoe UI", 9), text_color="#2A2D40"
                 ).pack(side="left", padx=16)

    # ══════════════════════════════════════
    #  FUNCIONES DE RENDERIZADO
    # ══════════════════════════════════════

    btn_guia_refs = {}    # nombre_guia → botón
    btn_sub_refs  = {}    # nombre_sub  → botón

    def _clear_frame(f):
        for w in f.winfo_children():
            w.destroy()

    def _render_rows(filas, accent_color=ACCENT_CYAN):
        """Dibuja las filas nombre/valor en el panel derecho."""
        _clear_frame(content_scroll)
        if not filas:
            ctk.CTkLabel(content_scroll, text="Sin resultados.",
                         font=("Segoe UI", 12), text_color=TEXT_DIM
                         ).grid(row=0, column=0, padx=20, pady=20, sticky="w")
            return
        for i, (nombre, valor) in enumerate(filas):
            bg = BG_ROW_A if i % 2 == 0 else BG_ROW_B
            row_frame = ctk.CTkFrame(content_scroll, fg_color=bg, corner_radius=6,
                                      border_width=0)
            row_frame.grid(row=i, column=0, sticky="ew", padx=8, pady=2)
            row_frame.grid_columnconfigure(1, weight=1)

            ctk.CTkLabel(row_frame, text=nombre,
                         font=("Segoe UI", 11, "bold"),
                         text_color=accent_color,
                         anchor="nw", justify="left",
                         wraplength=220, width=230
                         ).grid(row=0, column=0, padx=(12, 8), pady=8, sticky="nw")

            ctk.CTkLabel(row_frame, text=valor,
                         font=("Segoe UI", 11),
                         text_color=TEXT_MAIN,
                         anchor="nw", justify="left",
                         wraplength=700
                         ).grid(row=0, column=1, padx=(0, 12), pady=8, sticky="nw")

    def _render_intro(guia_nombre):
        """Muestra intro al seleccionar una guía."""
        _clear_frame(content_scroll)
        guia = GUIAS[guia_nombre]
        color = guia["color"]

        ctk.CTkLabel(content_scroll, text=guia_nombre,
                     font=("Segoe UI", 22, "bold"),
                     text_color=color
                     ).grid(row=0, column=0, padx=20, pady=(20, 4), sticky="w")

        ctk.CTkLabel(content_scroll,
                     text=f"  {len(guia['subsecciones'])} secciones disponibles — selecciona una en el panel lateral.",
                     font=("Segoe UI", 12), text_color=TEXT_DIM
                     ).grid(row=1, column=0, padx=20, pady=(0, 16), sticky="w")

        # Preview: primera subsección
        primera_key = next(iter(guia["subsecciones"]))
        primera_filas = guia["subsecciones"][primera_key]
        ctk.CTkLabel(content_scroll,
                     text=f"Vista previa: {primera_key}",
                     font=("Segoe UI", 11, "bold"),
                     text_color=TEXT_DIM
                     ).grid(row=2, column=0, padx=20, pady=(0, 6), sticky="w")

        for i, (nombre, valor) in enumerate(primera_filas[:5]):
            bg = BG_ROW_A if i % 2 == 0 else BG_ROW_B
            rf = ctk.CTkFrame(content_scroll, fg_color=bg, corner_radius=6)
            rf.grid(row=3+i, column=0, sticky="ew", padx=8, pady=2)
            rf.grid_columnconfigure(1, weight=1)
            ctk.CTkLabel(rf, text=nombre, font=("Segoe UI", 11, "bold"),
                         text_color=color, anchor="nw", width=230, wraplength=220
                         ).grid(row=0, column=0, padx=(12, 8), pady=6, sticky="nw")
            ctk.CTkLabel(rf, text=valor, font=("Segoe UI", 11),
                         text_color=TEXT_MAIN, anchor="nw", justify="left", wraplength=700
                         ).grid(row=0, column=1, padx=(0, 12), pady=6, sticky="nw")

        if len(primera_filas) > 5:
            ctk.CTkLabel(content_scroll,
                         text=f"  … y {len(primera_filas)-5} entradas más en esta sección.",
                         font=("Segoe UI", 10), text_color=TEXT_DIM
                         ).grid(row=3+5, column=0, padx=20, pady=4, sticky="w")

    def _select_guia(nombre):
        _state["guia"] = nombre
        _state["sub"]  = None
        guia = GUIAS[nombre]
        color = guia["color"]

        # Resaltar botón seleccionado
        for n, b in btn_guia_refs.items():
            b.configure(fg_color=BG_CARD if n != nombre else "#1A1E2F",
                        text_color=ACCENT_CYAN if n == nombre else TEXT_MAIN,
                        border_width=1 if n == nombre else 0,
                        border_color=color if n == nombre else BG_CARD)

        # Poblar panel de subsecciones
        _clear_frame(scroll_mid)
        btn_sub_refs.clear()
        for idx, sub_nombre in enumerate(guia["subsecciones"]):
            b = ctk.CTkButton(scroll_mid,
                              text=sub_nombre,
                              font=("Segoe UI", 10),
                              fg_color=BG_INNER,
                              text_color=TEXT_MAIN,
                              hover_color="#1A1E2F",
                              anchor="w",
                              corner_radius=6,
                              border_width=0,
                              command=lambda s=sub_nombre: _select_sub(s))
            b.grid(row=idx, column=0, sticky="ew", padx=4, pady=2)
            btn_sub_refs[sub_nombre] = b

        lbl_breadcrumb.configure(text=f"›  {nombre}")
        _render_intro(nombre)

    def _select_sub(sub_nombre):
        _state["sub"] = sub_nombre
        guia_nombre   = _state["guia"]
        guia          = GUIAS[guia_nombre]
        color         = guia["color"]
        filas         = guia["subsecciones"][sub_nombre]

        # Resaltar subsección
        for n, b in btn_sub_refs.items():
            b.configure(fg_color="#1A1E2F" if n == sub_nombre else BG_INNER,
                        text_color=color if n == sub_nombre else TEXT_MAIN,
                        border_width=1 if n == sub_nombre else 0,
                        border_color=color if n == sub_nombre else BG_INNER)

        lbl_breadcrumb.configure(text=f"›  {guia_nombre}  ›  {sub_nombre}")
        _render_rows(filas, color)

    def _on_search(*_):
        q = search_var.get().strip().lower()
        if not q:
            if _state["guia"] and _state["sub"]:
                _select_sub(_state["sub"])
            elif _state["guia"]:
                _render_intro(_state["guia"])
            return

        resultados = []
        for guia_nombre, guia_data in GUIAS.items():
            for sub_nombre, filas in guia_data["subsecciones"].items():
                for nombre, valor in filas:
                    if q in nombre.lower() or q in valor.lower():
                        resultados.append((f"[{guia_nombre}  ›  {sub_nombre}]  {nombre}", valor))

        lbl_breadcrumb.configure(text=f"›  Búsqueda: \"{q}\"  —  {len(resultados)} resultado(s)")
        _render_rows(resultados, ACCENT_CYAN)

    search_var.trace_add("write", _on_search)

    # ══════════════════════════════════════
    #  POBLAR PANEL IZQUIERDO
    # ══════════════════════════════════════
    for idx, (guia_nombre, guia_data) in enumerate(GUIAS.items()):
        color = guia_data["color"]
        b = ctk.CTkButton(scroll_left,
                          text=guia_nombre,
                          font=("Segoe UI", 11, "bold"),
                          fg_color=BG_CARD,
                          text_color=TEXT_MAIN,
                          hover_color="#1A1E2F",
                          anchor="w",
                          corner_radius=8,
                          border_width=0,
                          height=38,
                          command=lambda n=guia_nombre: _select_guia(n))
        b.grid(row=idx, column=0, sticky="ew", padx=4, pady=3)
        btn_guia_refs[guia_nombre] = b

    # Seleccionar la primera guía por defecto
    primera = list(GUIAS.keys())[0]
    _select_guia(primera)

    return win


# ══════════════════════════════════════════════════════════════════════
#  EJECUCIÓN STANDALONE (prueba sin AriaBot)
# ══════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    root.withdraw()
    w = abrir_guia()
    w.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()
