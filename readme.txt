=====================================================================
  AriaBot — Guía de Usuario
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
  · Configuración general (intervalo de autoclick, grabación).
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
   intervalo desde el panel de estado. Pulsa de nuevo la tecla para
   detenerlo.

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
   · Las secuencias se pueden ejecutar en bucle.

5. CAPTURA DE IMAGEN (F8 por defecto)
   Selecciona una región de la pantalla para guardarla como plantilla.
   Estas imágenes se usan como condición de verificación en los pasos
   de las secuencias: el bot comprobará que la imagen está en pantalla
   antes de ejecutar ese paso. Si no la detecta, puede reintentar o
   saltar el paso según configuración.
   · Pulsa Escape para cancelar la captura sin seleccionar nada.

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
AriaBot está disponible en Español e Inglés. Para cambiar el idioma:

1. Haz clic en el botón ⚙ Opciones del panel izquierdo.
2. En la sección IDIOMA / LANGUAGE, selecciona ES o EN.
3. Haz clic en "Guardar y Aplicar".
4. Aparecerá un aviso indicando que es necesario reiniciar.
5. Pulsa "Reiniciar ahora" para aplicar el cambio inmediatamente,
   o "Reiniciar más tarde" para hacerlo en el próximo arranque.

El idioma elegido queda guardado en settings.json y se aplica
automáticamente cada vez que arrancas el programa.


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
· Las secuencias se pueden ejecutar en bucle.
· Puedes añadir pausas estáticas entre pasos desde el panel superior.


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


PREGUNTAS FRECUENTES
─────────────────────
P: Las teclas rápidas no responden mientras juego.
R: Asegúrate de ejecutar AriaBot como Administrador. El juego en
   pantalla completa exclusiva puede bloquear los hooks de teclado;
   prueba con modo ventana sin bordes.

P: El autoclick hace clic en el sitio equivocado.
R: Las coordenadas se graban en base a la resolución y posición de
   la ventana del juego en el momento de la grabación. Si cambias
   la resolución o mueves la ventana, vuelve a grabar la secuencia.

P: El bot no detecta la imagen capturada.
R: Asegúrate de que el juego está en la misma resolución que cuando
   capturaste la imagen. Si la imagen es muy pequeña o cambia mucho
   de aspecto puede no detectarse.

P: La Guardia no detecta la subida de nivel.
R: Asegúrate de que el chat del juego es visible en pantalla y de
   que los mensajes de sistema (en amarillo) no están desactivados.
   La detección usa OCR sobre una zona del chat, por lo que necesita
   visibilidad directa.

P: Al actualizar aparece un error de DLL y luego el programa funciona.
R: Es normal en la primera actualización. El nuevo ejecutable ya
   incluye la corrección y las siguientes actualizaciones no darán
   ese aviso.

P: El buscador del mapa no encuentra una sala.
R: Prueba escribiendo solo parte del nombre (ej: "comedor" en vez de
   "Comedor Central"). La búsqueda no distingue tildes ni mayúsculas.

P: ¿Dónde se guardan mis secuencias?
R: En el archivo Secuencias.json dentro de la carpeta de instalación.
   Puedes hacer copia de seguridad de ese archivo para no perderlas.

P: ¿Puedo cambiar la carpeta de instalación?
R: Sí, durante la instalación con AriaBot_Setup.exe puedes elegir
   cualquier carpeta. El programa funcionará igual en cualquier ruta.

P: ¿Cómo cambio el idioma?
R: En el botón ⚙ Opciones del panel izquierdo, sección IDIOMA /
   LANGUAGE. Selecciona ES o EN, guarda y reinicia cuando te lo pida.


CRÉDITOS
─────────
Guías y recursos del juego proporcionados por:
  www.gentelaprision.es
  — La referencia en español para todo lo relacionado con La Prisión.

Desarrollado por SMaSeR · 2026

=====================================================================
