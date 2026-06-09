=====================================================================
  AriaBot v1.4 — Guía de Usuario
  Desarrollado por SMaSeR · 2026
=====================================================================


¿QUÉ ES ARIABOT?
─────────────────
AriaBot es un asistente de automatización diseñado específicamente
para La Prisión. Permite grabar y reproducir secuencias de acciones,
hacer autoclick, evitar la desconexión por inactividad (AFK), vigilar
subidas de nivel y acceder a guías y mapas del juego sin salir de la
pantalla.


RECOMENDACIONES ANTES DE EMPEZAR
─────────────────────────────────
► Ejecuta el juego en PANTALLA COMPLETA para un funcionamiento óptimo.
  AriaBot necesita ver la pantalla correctamente para detectar imágenes
  y ejecutar acciones en la posición adecuada.

► Si dejas el bot funcionando de forma autónoma, IGNORA el chat del
  juego. Mensajes de otros jugadores pueden provocar que el ratón o
  el teclado queden fuera de posición y desincronicen las secuencias.

► Ejecuta AriaBot como Administrador (el instalador lo hace automáti-
  camente). Si las teclas rápidas no responden, comprueba que tienes
  permisos de administrador.


INSTALACIÓN
────────────
1. Ejecuta AriaBot_Setup.exe y sigue el asistente.
2. Elige la carpeta de instalación (por defecto en Archivos de programa).
3. Opcional: crea acceso directo en el Escritorio y/o en el Menú de Inicio.
4. Al finalizar puedes arrancar el programa directamente desde el instalador.

El programa crea automáticamente en su carpeta de instalación:
  · Secuencias.json  → guarda tus secuencias grabadas
  · hotkeys.json     → guarda tu configuración de teclas rápidas
  · settings.json    → guarda tu configuración de idioma
  · templates\       → carpeta con las imágenes capturadas para secuencias
  · changelog.txt    → historial de cambios (se descarga al actualizar)
  · _update.bat      → archivo temporal que aparece y desaparece durante
                       las actualizaciones automáticas (es normal, no borrarlo)


INTERFAZ PRINCIPAL
───────────────────
La ventana se divide en dos zonas:

  PANEL IZQUIERDO (sidebar)
  · Estado en tiempo real de cada función activa.
  · Leyenda de teclas rápidas configuradas.
  · Acceso rápido a Banderas, Guía y Mapa.
  · Botón ⚙ Opciones para configurar las teclas y el idioma.

  PANEL DERECHO
  · Configuración general (intervalo de autoclick, velocidad del ratón,
    modo one loop, grabación).
  · Imágenes guardadas → gestión de plantillas de reconocimiento.
  · Secuencias de pasos → grabar, editar y ejecutar macros.
  · Log en tiempo real → registro de todas las acciones del programa.


FUNCIONALIDADES
────────────────

1. GUARDIA ANTI-NIVEL (F4 por defecto)
   Monitoriza el chat del juego con OCR. Cuando detecta el mensaje
   "HAS SUBIDO DE NIVEL" en amarillo, detiene todas las funciones
   activas y cierra el juego automáticamente. Esto evita que el
   personaje siga subiendo niveles sin aplicar puntos de constitución,
   lo que reduciría su vida máxima. Ideal para farming desatendido.

2. AUTOCLICK CONTINUO (F5 por defecto)
   Realiza clics de forma continua mientras está activo. Configura el
   intervalo en la casilla "Intervalo Autoclick (s)" del panel superior.
   Pulsa de nuevo la tecla para detenerlo.

   BLOQUEAR RATÓN DURANTE AUTOCLICK:
   Activa la casilla "Bloquear ratón al hacer Autoclick" en el panel
   de estado para fijar el cursor en la posición de grabación mientras
   el autoclick está en marcha. Útil cuando otras acciones del sistema
   puedan desplazar el puntero.

3. LOOP EVASIÓN AFK (F6 por defecto)
   Mueve el personaje de forma aleatoria y periódica para evitar que
   el juego te desconecte por inactividad. Actívalo y olvídate.

4. GRABACIÓN DE SECUENCIAS (F7 por defecto)
   · Pulsa F7 para iniciar la grabación.
   · Realiza las acciones que quieras automatizar (clics, teclas,
     esperas, movimientos de ratón).
   · Pulsa F7 de nuevo para detener la grabación.
   · La secuencia queda guardada y lista para ejecutarse.
   · Puedes tener múltiples secuencias y cambiar entre ellas desde
     el desplegable superior.
   · Cada paso de la secuencia se puede editar: cambiar el tiempo
     de espera, asignarle una imagen de verificación, reordenar o
     eliminar pasos.
   · Puedes añadir pausas estáticas entre pasos con el botón
     "Añadir Pausa Estática" situado junto al botón de ejecución.

5. CAPTURA DE IMAGEN (F8 por defecto)
   Selecciona una región de la pantalla para guardarla como plantilla.
   Estas imágenes se usan como condición de verificación en los pasos
   de las secuencias: el bot comprobará que la imagen está en pantalla
   antes de ejecutar ese paso. Si no la detecta, puede reintentar o
   saltar el paso según configuración.
   · Pulsa Escape para cancelar la captura sin seleccionar nada.
   · También puedes importar imágenes PNG externas directamente desde
     el panel de imágenes guardadas, sin necesidad de capturar pantalla.

6. BANDERAS (F9 por defecto)
   Abre el Generador Maestro de Banderas v6 integrado. Permite crear
   y personalizar banderas del juego con más de 500 variantes, editor
   de colores carácter a carácter, ensamblador de nick+marco y
   exportación directa del código para el .inf del juego.

7. GUÍA DE LA PRISIÓN (F10 por defecto)
   Abre la guía completa del juego directamente dentro de AriaBot,
   sin necesidad de salir ni cambiar de ventana. Incluye categorías
   de Municiones, Cocina, Química, Joyería, Habilidades, Prendas,
   Mecánica, Costura, Carlito-Coraza y Subir de Nivel.
   Créditos: www.gentelaprision.es

8. MAPA DE LA PRISIÓN (F11 por defecto)
   Abre el mapa interactivo del juego dentro de AriaBot con:
   · Zoom con rueda del ratón o botones +/−
   · Arrastre para navegar por el mapa
   · Leyenda de iconos con toggles para mostrar/ocultar capas
   · Botón CENTRAR para volver a la vista inicial (120% centrado)
   · Clic derecho sobre el mapa → muestra las coordenadas del punto
     (útil para calibración)

   BUSCADOR DE SALAS:
   · Escribe el nombre de cualquier sala en la barra de búsqueda
   · La búsqueda es en tiempo real, sin tildes (sotano = sótano)
   · El mapa hace zoom automático y centra en la sala encontrada
   · Si hay varios resultados navega entre ellos con los botones ‹ ›
   · El contador muestra cuántos resultados hay (ej: 1 / 3)
   · Borra el texto para volver a la vista normal

   Créditos: www.gentelaprision.es

9. DETENER TODO (F12 por defecto)
   Para inmediatamente todas las funciones activas: autoclick, AFK,
   guardia, secuencias en ejecución. Botón de emergencia.


CONFIGURACIÓN GENERAL
──────────────────────
En el panel superior derecho encontrarás tres controles independientes:

  INTERVALO AUTOCLICK (s)
  Escribe directamente el número de segundos entre cada clic del
  autoclick. Se aplica en tiempo real sin necesidad de reiniciar.

  VELOCIDAD DE DESPLAZAMIENTO DEL MOUSE EN SECUENCIAS
  Barra deslizante que controla la velocidad de movimiento del ratón
  durante la ejecución de secuencias. Centrada por defecto (velocidad
  estándar). Desplaza hacia la izquierda para ir más lento, hacia la
  derecha para ir más rápido.

  SECUENCIA ONE LOOP
  Si está marcada, la secuencia activa ejecutará un único ciclo
  completo y se detendrá sola al terminar. Sin marcar, la secuencia
  se repite en bucle continuo hasta que la pares manualmente.


CONFIGURAR TECLAS RÁPIDAS (⚙ Opciones)
────────────────────────────────────────
Puedes cambiar cualquier tecla rápida por la combinación que prefieras:

1. Haz clic en el botón ⚙ Opciones del panel izquierdo.
2. Haz clic en el botón de la acción que quieras cambiar.
3. Pulsa la tecla o combinación deseada (Ctrl+J, Alt+F, F2, etc.).
4. Si hay conflicto con otra acción el programa te avisará.
5. Haz clic en "Guardar y Aplicar" — los cambios son inmediatos.
6. Con "Restaurar por defecto" vuelves a F4–F12.

Las teclas configuradas quedan guardadas en hotkeys.json y se cargan
automáticamente cada vez que arrancas el programa.

IMPORTANTE: las teclas asignadas a acciones de AriaBot quedan exentas
de grabarse en las secuencias, así no interfieren con la automatización.


CAMBIAR IDIOMA (⚙ Opciones)
─────────────────────────────
AriaBot está disponible en Español, Inglés, Francés e Italiano.
Para cambiar el idioma:

1. Haz clic en el botón ⚙ Opciones del panel izquierdo.
2. En la sección IDIOMA / LANGUAGE, selecciona ES, EN, FR o IT.
3. Haz clic en "Guardar y Aplicar".
4. Aparecerá un aviso indicando que es necesario reiniciar.
5. Pulsa "Reiniciar ahora" para aplicar el cambio inmediatamente,
   o "Reiniciar más tarde" para hacerlo en el próximo arranque.

El idioma elegido queda guardado en settings.json y se aplica
automáticamente cada vez que arrancas el programa.


ASISTENCIA TÉCNICA
───────────────────
AriaBot incluye un formulario de contacto integrado accesible desde
el botón "Asistencia Técnica" en la parte inferior del panel izquierdo.
Rellena tu nombre, email y descripción del problema y el mensaje se
enviará directamente al desarrollador.


PLATAFORMA CLOUD
─────────────────
AriaBot incluye integración con un servidor para compartir y descargar
secuencias con otros jugadores:

· Publicar Secuencia → sube la secuencia activa al servidor para que
  otros jugadores puedan descargarla.
· Explorar Repositorio → descarga secuencias publicadas por otros
  usuarios y las importa directamente en tu colección.


SECUENCIAS — USO AVANZADO
──────────────────────────
· Puedes crear tantas secuencias como necesites con el botón "+".
· Cada secuencia se guarda automáticamente al cerrar el programa.
· Los pasos soportan: clic izquierdo, clic derecho, doble clic,
  pulsación de tecla, escritura de texto y esperas temporizadas.
· Asignar una imagen a un paso hace que el bot verifique que esa
  imagen está visible en pantalla antes de ejecutarlo.
· Las secuencias se pueden ejecutar en bucle continuo o en un único
  ciclo activando la opción Secuencia one loop.
· Puedes añadir pausas estáticas entre pasos desde el botón situado
  junto al botón de ejecución.
· Puedes importar imágenes PNG externas al panel de plantillas sin
  necesidad de capturarlas desde pantalla.


ARCHIVOS Y CARPETAS GENERADOS
───────────────────────────────
Todos los archivos se crean en la misma carpeta donde está el .exe:

  Secuencias.json   → secuencias grabadas (copia de seguridad recomendada)
  hotkeys.json      → configuración de teclas rápidas
  settings.json     → configuración de idioma
  templates\        → imágenes capturadas para verificación en secuencias
  Mapa.png          → imagen del mapa (se actualiza automáticamente)
  changelog.txt     → se crea/actualiza al recibir una actualización
  readme.txt        → esta guía (se actualiza automáticamente)
  _update.bat       → archivo temporal durante actualizaciones (se borra solo)
  AriaBot.new       → archivo temporal durante la descarga de una actualización
                      (se convierte en AriaBot.exe al finalizar)


ACTUALIZACIONES AUTOMÁTICAS
─────────────────────────────
AriaBot comprueba al arrancar si hay una versión nueva disponible.
Si la hay, te preguntará si deseas actualizar. Al aceptar:
  1. Descarga la nueva versión en segundo plano (se ve el progreso en el log).
  2. Descarga el changelog, readme y Mapa.png actualizados.
  3. Se cierra automáticamente.
  4. Reemplaza el ejecutable con la nueva versión.
  5. Abre el changelog.txt en el Bloc de notas para que veas los cambios.
No necesitas hacer nada más. Tus secuencias y configuración se conservan.

CRÉDITOS
─────────
Guías y recursos del juego proporcionados por:
  www.gentelaprision.es
  — La referencia en español para todo lo relacionado con La Prisión.

=====================================================================
