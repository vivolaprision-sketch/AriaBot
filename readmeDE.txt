=====================================================================
  AriaBot v1.5 — Benutzerhandbuch
  Entwickelt von SMaSeR · 2026
=====================================================================


WAS IST ARIABOT?
─────────────────
AriaBot ist ein Automatisierungs-Assistent, der speziell für 
La Prisión entwickelt wurde. Er ermöglicht das Aufzeichnen und 
Wiedergeben von Aktionssequenzen, Autoklick, AFK-Schutz (verhindert 
Inaktivität), Level-Überwachung sowie den Zugriff auf Guides und 
Karten des Spiels, ohne das Spiel verlassen zu müssen.


EMPFOHLENE VORAUSSETZUNGEN
─────────────────────────────────
► Führen Sie das Spiel im VOLLBILDMODUS aus, um eine optimale Funktion 
  zu gewährleisten. AriaBot muss den Bildschirm korrekt erfassen 
  können, um Bilder zu erkennen und Aktionen an der richtigen Position 
  auszuführen.

► Wenn der Bot autonom läuft, IGNORIEREN Sie den Spiel-Chat. 
  Nachrichten anderer Spieler können dazu führen, dass Maus oder 
  Tastatur ihre Position verlieren und die Sequenzen desynchronisiert 
  werden.

► Führen Sie AriaBot als Administrator aus (das Installationsprogramm 
  erledigt dies automatisch). Wenn die Hotkeys nicht reagieren, prüfen 
  Sie bitte, ob Sie über Administratorrechte verfügen.


INSTALLATION
────────────
1. Führen Sie AriaBot_Setup.exe aus und folgen Sie dem Installationsassistenten.
2. Wählen Sie den Installationsordner (standardmäßig unter Programme).
3. Optional: Erstellen Sie eine Verknüpfung auf dem Desktop oder im Startmenü.
4. Nach Abschluss können Sie das Programm direkt über das Installationsprogramm starten.

Das Programm erstellt automatisch in seinem Installationsordner:
  · Secuencias.json  → speichert Ihre aufgezeichneten Sequenzen
  · hotkeys.json     → speichert Ihre Hotkey-Konfiguration
  · settings.json    → speichert Ihre Spracheinstellungen
  · templates\       → Ordner mit Bildern, die für Sequenzen erfasst wurden
  · changelog.txt    → Änderungsprotokoll (wird beim Update heruntergeladen)
  · _update.bat      → temporäre Datei, die während automatischer Updates 
                       erscheint und wieder verschwindet (normal, nicht löschen)


HAUPTOBERFLÄCHE
───────────────────
Das Fenster ist in zwei Bereiche unterteilt:

  LINKES PANEL (Seitenleiste)
  · Echtzeitstatus jeder aktiven Funktion.
  · Legende der konfigurierten Hotkeys.
  · Schnellzugriff auf Flaggen, Guides und Karten.
  · ⚙ Optionen-Button zum Konfigurieren von Tasten und Sprache.

  RECHTES PANEL
  · Allgemeine Einstellungen (Autoklick-Intervall, Mausgeschwindigkeit, 
    One-Loop-Modus, Aufnahme).
  · Gespeicherte Bilder → Verwaltung von Erkennungsvorlagen.
  · Sequenzschritte → Aufnehmen, Bearbeiten und Ausführen von Makros.
  · Echtzeit-Log → Protokoll aller Programmaktionen.


FUNKTIONALITÄTEN
────────────────

1. LEVEL-ÜBERWACHUNG (standardmäßig F4)
   Überwacht den Spiel-Chat mittels OCR. Wenn die Meldung 
   "HAS SUBIDO DE NIVEL" (Du bist ein Level aufgestiegen) in Gelb 
   erkannt wird, stoppt es alle aktiven Funktionen und schließt 
   das Spiel automatisch. Dies verhindert, dass der Charakter weiter 
   aufsteigt, ohne Konstitutionspunkte zu vergeben, was die maximale 
   Lebensenergie reduzieren würde. Ideal für unbeaufsichtigtes Farming.

2. KONTINUIERLICHER AUTOKLICK (standardmäßig F5)
   Führt kontinuierlich Klicks aus, solange die Funktion aktiv ist. 
   Konfigurieren Sie das Intervall im Feld "Autoklick-Intervall (s)" 
   im oberen Panel. Drücken Sie die Taste erneut, um es zu stoppen.

   MAUS BEI AUTOKLICK SPERREN:
   Aktivieren Sie das Kontrollkästchen "Maus bei Autoklick sperren" im 
   Statuspanel, um den Cursor an der Aufnahmeposition zu fixieren, 
   während der Autoklick läuft. Nützlich, wenn andere Systemaktionen 
   den Zeiger verschieben könnten.

3. AFK-AUSWEICHSCHLEIFE (standardmäßig F6)
   Bewegt den Charakter zufällig und periodisch, um zu verhindern, dass 
   das Spiel Sie aufgrund von Inaktivität trennt. Aktivieren und vergessen.

4. SEQUENZAUFNAHME (standardmäßig F7)
   · Drücken Sie F7, um die Aufnahme zu starten.
   · Führen Sie die Aktionen aus, die Sie automatisieren möchten 
     (Klicks, Tasten, Wartezeiten, Mausbewegungen).
   · Drücken Sie erneut F7, um die Aufnahme zu stoppen.
   · Die Sequenz wird gespeichert und ist ausführbereit.
   · Sie können mehrere Sequenzen haben und über das obere Dropdown-Menü 
     zwischen ihnen wechseln.
   · Jeder Schritt der Sequenz kann bearbeitet werden: Wartezeit ändern, 
     ein Verifizierungsbild zuweisen, Schritte neu anordnen oder löschen.
   · Sie können mit dem Button "Statische Pause hinzufügen" neben dem 
     Ausführungs-Button statische Pausen zwischen den Schritten einfügen.

5. BILDERFASSUNG (standardmäßig F8)
   Wählen Sie einen Bereich des Bildschirms aus, um ihn als Vorlage zu 
   speichern. Diese Bilder werden als Verifizierungsbedingung in den 
   Sequenzschritten verwendet: Der Bot prüft, ob das Bild auf dem 
   Bildschirm sichtbar ist, bevor er diesen Schritt ausführt. Wenn er 
   es nicht erkennt, kann er je nach Konfiguration wiederholen oder den 
   Schritt überspringen.
   · Drücken Sie Escape, um die Erfassung ohne Auswahl abzubrechen.
   · Sie können externe PNG-Bilder auch direkt über das Panel für 
     gespeicherte Bilder importieren, ohne den Bildschirm zu erfassen.

6. FLAGGEN (standardmäßig F9)
   Öffnet den integrierten "Generador Maestro de Banderas v6" (Meister-
   Flaggen-Generator). Ermöglicht das Erstellen und Anpassen von 
   Spielflaggen mit über 500 Varianten, zeichenweisem Farbeditor, 
   Nick+Rahmen-Assembler und direktem Export des Codes für die .inf 
   des Spiels.

7. LA PRISIÓN GUIDE (standardmäßig F10)
   Öffnet den kompletten Spiel-Guide direkt in AriaBot, ohne das Fenster 
   wechseln zu müssen. Beinhaltet Kategorien für Munition, Kochen, 
   Chemie, Schmuck, Fertigkeiten, Kleidung, Mechanik, Nähen, 
   Carlito-Coraza und Level-Aufstieg.
   Credits: www.gentelaprision.es

8. LA PRISIÓN KARTE (standardmäßig F11)
   Öffnet die interaktive Karte des Spiels in AriaBot mit:
   · Zoom mit Mausrad oder +/− Buttons
   · Ziehen zur Navigation auf der Karte
   · Icon-Legende mit Toggles zum Ein-/Ausblenden von Ebenen
   · ZENTRIEREN-Button zur Rückkehr zur Anfangsansicht (120% zentriert)
   · Rechtsklick auf die Karte → zeigt die Koordinaten des Punktes 
     (nützlich zur Kalibrierung)

   RAUMSUCHE:
   · Geben Sie den Namen eines Raums in die Suchleiste ein.
   · Die Suche erfolgt in Echtzeit, ohne Umlaute (sotano = sótano).
   · Die Karte zoomt automatisch auf den gefundenen Raum und zentriert ihn.
   · Wenn es mehrere Ergebnisse gibt, navigieren Sie mit den Buttons ‹ ›.
   · Der Zähler zeigt die Anzahl der Ergebnisse an (z. B. 1 / 3).
   · Löschen Sie den Text, um zur normalen Ansicht zurückzukehren.

   Credits: www.gentelaprision.es

9. ALLES ANHALTEN (standardmäßig F12)
   Stoppt sofort alle aktiven Funktionen: Autoklick, AFK, Wache, laufende 
   Sequenzen. Notfall-Button.


ALLGEMEINE EINSTELLUNGEN
──────────────────────
Im oberen rechten Panel finden Sie drei unabhängige Steuerelemente:

  AUTOKLICK-INTERVALL (s)
  Geben Sie direkt die Anzahl der Sekunden zwischen jedem Klick 
  ein. Wird in Echtzeit angewendet, ohne Neustart.

  MAUSBEWEGUNGSGESCHWINDIGKEIT IN SEQUENZEN
  Schieberegler, der die Mausbewegungsgeschwindigkeit während der 
  Ausführung von Sequenzen steuert. Standardmäßig zentriert (Standard-
  geschwindigkeit). Bewegen Sie ihn nach links für langsamere, nach 
  rechts für schnellere Bewegung.

  ONE-LOOP-SEQUENZ
  Wenn aktiviert, führt die aktive Sequenz einen einzigen vollständigen 
  Zyklus aus und stoppt von selbst. Wenn deaktiviert, wird die Sequenz 
  in einer Endlosschleife wiederholt, bis Sie sie manuell stoppen.


HOTKEYS KONFIGURIEREN (⚙ Optionen)
────────────────────────────────────────
Sie können jeden Hotkey durch die gewünschte Kombination ersetzen:

1. Klicken Sie auf den ⚙ Optionen-Button im linken Panel.
2. Klicken Sie auf den Button der Aktion, die Sie ändern möchten.
3. Drücken Sie die gewünschte Taste oder Kombination (Strg+J, Alt+F, F2 usw.).
4. Wenn ein Konflikt mit einer anderen Aktion besteht, warnt Sie das Programm.
5. Klicken Sie auf "Speichern und Anwenden" — die Änderungen sind sofort aktiv.
6. Mit "Standard wiederherstellen" setzen Sie auf F4–F12 zurück.

Die konfigurierten Tasten werden in hotkeys.json gespeichert und bei 
jedem Start des Programms automatisch geladen.

WICHTIG: Die AriaBot-Aktionen zugewiesenen Tasten werden nicht in den 
Sequenzen aufgezeichnet, damit sie die Automatisierung nicht stören.


SPRACHE ÄNDERN (⚙ Optionen)
─────────────────────────────
AriaBot ist in Spanisch, Englisch, Französisch und Italienisch verfügbar.
Um die Sprache zu ändern:

1. Klicken Sie auf den ⚙ Optionen-Button im linken Panel.
2. Wählen Sie im Bereich SPRACHE / LANGUAGE die Option ES, EN, FR oder IT.
3. Klicken Sie auf "Speichern und Anwenden".
4. Ein Hinweis erscheint, dass ein Neustart erforderlich ist.
5. Drücken Sie "Jetzt neu starten", um die Änderung sofort anzuwenden, 
   oder "Später neu starten", um dies beim nächsten Start zu tun.

Die gewählte Sprache wird in settings.json gespeichert und bei jedem 
Start des Programms automatisch angewendet.


TECHNISCHER SUPPORT
───────────────────
AriaBot enthält ein integriertes Kontaktformular, das über den Button 
"Asistencia Técnica" (Technischer Support) unten im linken Panel 
zugänglich ist. Geben Sie Ihren Namen, Ihre E-Mail-Adresse und eine 
Beschreibung des Problems ein; die Nachricht wird direkt an den 
Entwickler gesendet.


CLOUD-PLATTFORM
─────────────────
AriaBot bietet Integration mit einem Server zum Teilen und Herunterladen 
von Sequenzen mit anderen Spielern:

· Sequenz veröffentlichen → lädt die aktive Sequenz auf den Server hoch, 
  damit andere Spieler sie herunterladen können.
· Repository durchsuchen → lädt von anderen Benutzern veröffentlichte 
  Sequenzen herunter und importiert sie direkt in Ihre Sammlung.


SEQUENZEN — ERWEITERTE NUTZUNG
──────────────────────────
· Sie können mit dem "+"-Button so viele Sequenzen erstellen, wie Sie benötigen.
· Jede Sequenz wird beim Schließen des Programms automatisch gespeichert.
· Schritte unterstützen: Linksklick, Rechtsklick, Doppelklick, 
  Tastenanschlag, Texteingabe und zeitgesteuerte Wartezeiten.
· Die Zuweisung eines Bildes zu einem Schritt bewirkt, dass der Bot 
  prüft, ob das Bild auf dem Bildschirm sichtbar ist, bevor er ihn 
  ausführt.
· Sequenzen können in einer Endlosschleife oder in einem einzigen 
  Zyklus ausgeführt werden, indem die Option "One-Loop-Sequenz" aktiviert wird.
· Sie können mit dem Button neben dem Ausführungs-Button statische 
  Pausen zwischen den Schritten hinzufügen.
· Sie können externe PNG-Bilder in das Vorlagenpanel importieren, ohne 
  sie vom Bildschirm erfassen zu müssen.


GENERIERTE DATEIEN UND ORDNER
───────────────────────────────
Alle Dateien werden im selben Ordner erstellt, in dem sich die .exe befindet:

  Secuencias.json   → aufgezeichnete Sequenzen (Backup empfohlen)
  hotkeys.json      → Hotkey-Konfiguration
  settings.json     → Spracheinstellungen
  templates\        → Bilder für Sequenz-Verifizierungen
  Mapa.png          → Kartenbild (wird automatisch aktualisiert)
  changelog.txt     → wird beim Update erstellt/aktualisiert
  readme.txt        → dieses Handbuch (wird automatisch aktualisiert)
  _update.bat       → temporäre Datei während Updates (wird automatisch gelöscht)
  AriaBot.new       → temporäre Datei während des Downloads eines Updates
                      (wird nach Abschluss zu AriaBot.exe)


AUTOMATISCHE UPDATES
─────────────────────────────
AriaBot prüft beim Start, ob eine neue Version verfügbar ist.
Wenn ja, werden Sie gefragt, ob Sie aktualisieren möchten. Nach der Bestätigung:
  1. Wird die neue Version im Hintergrund heruntergeladen (Fortschritt im Log sichtbar).
  2. Werden Changelog, Readme und Mapa.png aktualisiert.
  3. Beendet sich das Programm automatisch.
  4. Die ausführbare Datei wird durch die neue Version ersetzt.
  5. Der changelog.txt wird im Editor geöffnet, damit Sie die Änderungen sehen.
Sie müssen nichts weiter tun. Ihre Sequenzen und Einstellungen bleiben erhalten.

CREDITS
─────────
Guides und Spielressourcen bereitgestellt von:
  www.gentelaprision.es
  — Die spanische Referenz für alles rund um La Prisión.

=====================================================================