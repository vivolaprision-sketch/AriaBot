=====================================================================
  AriaBot v1.4 — User Guide
  Developed by SMaSeR · 2026
=====================================================================


WHAT IS ARIABOT?
─────────────────
AriaBot is an automation assistant designed specifically for
La Prisión. It allows you to record and replay action sequences,
perform autoclicking, avoid disconnection due to inactivity (AFK),
watch for level-ups, and access in-game guides and maps without
leaving the screen.


RECOMMENDATIONS BEFORE YOU START
──────────────────────────────────
► Run the game in FULL SCREEN for optimal performance.
  AriaBot needs a clear view of the screen to detect images
  and execute actions at the correct position.

► If you leave the bot running unattended, IGNORE the in-game chat.
  Messages from other players can move the mouse or keyboard out of
  position and desync your sequences.

► Run AriaBot as Administrator (the installer does this automatically).
  If hotkeys are not responding, check that you have admin privileges.


INSTALLATION
─────────────
1. Run AriaBot_Setup.exe and follow the wizard.
2. Choose the installation folder (default is Program Files).
3. Optional: create a shortcut on the Desktop and/or Start Menu.
4. When finished you can launch the program directly from the installer.

The program automatically creates the following in its installation folder:
  · Secuencias.json  → your recorded sequences
  · hotkeys.json     → your hotkey configuration
  · settings.json    → your language setting
  · templates\       → images captured for sequence verification
  · changelog.txt    → change history (downloaded on update)
  · _update.bat      → temporary file that appears and disappears
                       during automatic updates (normal, do not delete)


MAIN INTERFACE
───────────────
The window is split into two areas:

  LEFT PANEL (sidebar)
  · Real-time status of each active function.
  · Hotkey legend showing configured keys.
  · Quick access to Flags, Guide and Map.
  · ⚙ Options button to configure hotkeys and language.

  RIGHT PANEL
  · General configuration (autoclick interval, mouse speed,
    one loop mode, recording).
  · Saved images → template management for image recognition.
  · Step sequences → record, edit and run macros.
  · Real-time log → record of all program actions.


FEATURES
─────────

1. LEVEL GUARD (F4 by default)
   Monitors the in-game chat using OCR. When it detects the message
   "HAS SUBIDO DE NIVEL" (level up) in yellow, it stops all active
   functions and closes the game automatically with Alt+F4. This
   prevents the character from levelling up without applying
   constitution points, which would reduce maximum health.
   Ideal for unattended farming.

2. CONTINUOUS AUTOCLICK (F5 by default)
   Performs continuous clicks while active. Configure the interval
   in the "Autoclick Interval (s)" field in the top panel.
   Press the key again to stop.

   LOCK MOUSE DURING AUTOCLICK:
   Enable the "Lock mouse during Autoclick" checkbox in the status
   panel to fix the cursor at the recorded position while autoclick
   is running. Useful when other system actions might move the pointer.

3. AFK EVASION LOOP (F6 by default)
   Moves the character randomly and periodically to prevent the game
   from disconnecting you due to inactivity. Enable and forget.

4. SEQUENCE RECORDING (F7 by default)
   · Press F7 to start recording.
   · Perform the actions you want to automate (clicks, keys,
     waits, mouse movements).
   · Press F7 again to stop recording.
   · The sequence is saved and ready to run.
   · You can have multiple sequences and switch between them
     using the dropdown at the top.
   · Each step can be edited: change the wait time, assign a
     verification image, reorder or delete steps.
   · You can add static pauses between steps using the
     "Add Static Pause" button next to the run button.

5. IMAGE CAPTURE (F8 by default)
   Select a region of the screen to save as a template.
   These images are used as verification conditions in sequence
   steps: the bot checks that the image is on screen before
   executing that step. If not detected, it can retry or skip
   the step depending on configuration.
   · Press Escape to cancel the capture without selecting anything.
   · You can also import external PNG images directly from the
     saved images panel, without capturing the screen.

6. FLAGS (F9 by default)
   Opens the integrated Master Flag Generator v6. Allows you to
   create and customise in-game flags with over 500 variants,
   character-by-character colour editor, nick+frame assembler and
   direct code export for the game's .inf file.

7. THE PRISON GUIDE (F10 by default)
   Opens the complete in-game guide directly inside AriaBot,
   without needing to switch windows. Includes categories for
   Ammo, Cooking, Chemistry, Jewellery, Skills, Clothing,
   Mechanics, Sewing, Carlito-Armor and Levelling Up.
   Credits: www.gentelaprision.es

8. THE PRISON MAP (F11 by default)
   Opens the interactive in-game map inside AriaBot with:
   · Zoom with mouse wheel or +/− buttons
   · Drag to navigate the map
   · Legend with toggles to show/hide icon layers
   · CENTER button to return to the initial view (120% centered)
   · Right-click on the map → shows coordinates of the point
     (useful for calibration)

   ROOM SEARCH:
   · Type any room name in the search bar
   · Search is real-time and accent-insensitive (sotano = sótano)
   · The map auto-zooms and centres on the found room
   · If there are multiple results, navigate with the ‹ › buttons
   · The counter shows how many results there are (e.g. 1 / 3)
   · Clear the text to return to the normal view

   Credits: www.gentelaprision.es

9. STOP ALL (F12 by default)
   Immediately stops all active functions: autoclick, AFK, level
   guard, running sequences. Emergency button.


GENERAL CONFIGURATION
──────────────────────
In the top right panel you will find three independent controls:

  AUTOCLICK INTERVAL (s)
  Type the number of seconds between each autoclick directly in the
  field. Applied in real time without restarting.

  MOUSE MOVEMENT SPEED IN SEQUENCES
  Slider that controls how fast the mouse moves during sequence
  execution. Centred by default (standard speed). Move left for
  slower, right for faster.

  SEQUENCE ONE LOOP
  If checked, the active sequence will run one complete cycle and
  stop automatically when finished. If unchecked, the sequence
  repeats in a continuous loop until stopped manually.


CONFIGURE HOTKEYS (⚙ Options)
───────────────────────────────
You can change any hotkey to the combination you prefer:

1. Click the ⚙ Options button in the left panel.
2. Click the button for the action you want to change.
3. Press the desired key or combination (Ctrl+J, Alt+F, F2, etc.).
4. If there is a conflict with another action the program will warn you.
5. Click "Save and Apply" — changes take effect immediately.
6. "Restore Defaults" resets everything back to F4–F12.

Configured keys are saved in hotkeys.json and loaded automatically
every time you start the program.

IMPORTANT: keys assigned to AriaBot actions are excluded from being
recorded in sequences, so they do not interfere with automation.


CHANGE LANGUAGE (⚙ Options)
─────────────────────────────
AriaBot is available in Spanish, English, French and Italian.
To change the language:

1. Click the ⚙ Options button in the left panel.
2. In the LANGUAGE / IDIOMA section, select ES, EN, FR or IT.
3. Click "Save and Apply".
4. A notice will appear indicating that a restart is required.
5. Click "Restart Now" to apply the change immediately,
   or "Restart Later" to do so on the next launch.

The chosen language is saved in settings.json and applied
automatically every time you start the program.


TECHNICAL SUPPORT
──────────────────
AriaBot includes a built-in contact form accessible from the
"Technical Support" button at the bottom of the left panel.
Fill in your name, email and a description of the problem and
the message will be sent directly to the developer.


CLOUD PLATFORM
───────────────
AriaBot includes integration with a server to share and download
sequences with other players:

· Publish Sequence → uploads the active sequence to the server so
  other players can download it.
· Browse Repository → downloads sequences published by other users
  and imports them directly into your collection.


SEQUENCES — ADVANCED USE
──────────────────────────
· You can create as many sequences as you need with the "+" button.
· Each sequence is saved automatically when the program closes.
· Steps support: left click, right click, double click, key press,
  text input and timed waits.
· Assigning an image to a step makes the bot verify that the image
  is visible on screen before executing it.
· Sequences can be run in a continuous loop or a single cycle by
  enabling the Sequence one loop option.
· You can add static pauses between steps using the button next to
  the run button.
· You can import external PNG images into the template panel without
  capturing them from the screen.


FILES AND FOLDERS CREATED
───────────────────────────
All files are created in the same folder as the .exe:

  Secuencias.json   → recorded sequences (backup recommended)
  hotkeys.json      → hotkey configuration
  settings.json     → language configuration
  templates\        → captured images for sequence verification
  Mapa.png          → map image (updated automatically)
  changelog.txt     → created/updated when an update is received
  readme.txt        → Spanish guide (updated automatically)
  readmeENG.txt     → this guide (updated automatically)
  _update.bat       → temporary file during updates (self-deletes)
  AriaBot.new       → temporary file during update download
                      (becomes AriaBot.exe when complete)


AUTOMATIC UPDATES
──────────────────
AriaBot checks for a new version on startup.
If one is available, it will ask if you want to update. When accepted:
  1. Downloads the new version in the background (progress shown in log).
  2. Downloads the updated changelog, readme and Mapa.png.
  3. Closes automatically.
  4. Replaces the executable with the new version.
  5. Opens changelog.txt in Notepad so you can see the changes.
You don't need to do anything else. Your sequences and configuration
are preserved.


CREDITS
────────
Game guides and resources provided by:
  www.gentelaprision.es
  — The Spanish reference for everything related to La Prisión.

=====================================================================
