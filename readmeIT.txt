=====================================================================
  AriaBot v1.5 — Guida per l'utente
  Sviluppato da SMaSeR · 2026
=====================================================================


COS'È ARIABOT?
───────────────
AriaBot è un assistente di automazione progettato specificamente per
La Prisión. Permette di registrare e riprodurre sequenze di azioni,
eseguire autoclick, evitare la disconnessione per inattività (AFK),
monitorare i passaggi di livello e accedere alle guide e alle mappe
del gioco senza lasciare la schermata.


RACCOMANDAZIONI PRIMA DI INIZIARE
───────────────────────────────────
► Avvia il gioco a SCHERMO INTERO per prestazioni ottimali.
  AriaBot ha bisogno di vedere lo schermo correttamente per rilevare
  le immagini ed eseguire le azioni nella posizione corretta.

► Se lasci il bot funzionare senza sorveglianza, IGNORA la chat di
  gioco. I messaggi di altri giocatori possono spostare il mouse o
  la tastiera e desincronizzare le sequenze.

► Avvia AriaBot come Amministratore (l'installer lo fa automatica-
  mente). Se i tasti rapidi non rispondono, verifica di avere i
  permessi di amministratore.


INSTALLAZIONE
──────────────
1. Avvia AriaBot_Setup.exe e segui la procedura guidata.
2. Scegli la cartella di installazione (predefinita in Programmi).
3. Opzionale: crea un collegamento sul Desktop e/o nel menu Start.
4. Al termine puoi avviare il programma direttamente dall'installer.

Il programma crea automaticamente nella sua cartella di installazione:
  · Secuencias.json  → le tue sequenze registrate
  · hotkeys.json     → la tua configurazione dei tasti rapidi
  · settings.json    → la tua impostazione della lingua
  · templates\       → immagini catturate per la verifica delle sequenze
  · changelog.txt    → cronologia delle modifiche (scaricata agli aggiornamenti)
  · _update.bat      → file temporaneo che appare e scompare durante
                       gli aggiornamenti automatici (normale, non eliminare)


INTERFACCIA PRINCIPALE
────────────────────────
La finestra è divisa in due aree:

  PANNELLO SINISTRO (sidebar)
  · Stato in tempo reale di ogni funzione attiva.
  · Legenda dei tasti rapidi configurati.
  · Accesso rapido a Bandiere, Guida e Mappa.
  · Pulsante ⚙ Opzioni per configurare i tasti e la lingua.

  PANNELLO DESTRO
  · Configurazione generale (intervallo autoclick, velocità del mouse,
    modalità one loop, registrazione).
  · Immagini salvate → gestione dei modelli di riconoscimento.
  · Sequenze di passi → registrare, modificare ed eseguire macro.
  · Registro in tempo reale → storico di tutte le azioni del programma.


FUNZIONALITÀ
─────────────

1. GUARDIA ANTI-LIVELLO (F4 per impostazione predefinita)
   Monitora la chat di gioco tramite OCR. Quando rileva il messaggio
   "HAS SUBIDO DE NIVEL" (salita di livello) in giallo, ferma tutte
   le funzioni attive e chiude il gioco automaticamente con Alt+F4.
   Questo impedisce al personaggio di salire di livello senza applicare
   i punti costituzione, il che ridurrebbe i punti vita massimi.
   Ideale per il farming senza sorveglianza.

2. AUTOCLICK CONTINUO (F5 per impostazione predefinita)
   Esegue clic in modo continuo mentre è attivo. Configura l'intervallo
   nel campo "Intervallo Autoclick (s)" nel pannello superiore.
   Premi di nuovo il tasto per fermarlo.

   BLOCCA IL MOUSE DURANTE L'AUTOCLICK:
   Attiva la casella "Blocca il mouse durante l'Autoclick" nel pannello
   di stato per fissare il cursore nella posizione registrata mentre
   l'autoclick è in esecuzione. Utile quando altre azioni di sistema
   potrebbero spostare il puntatore.

3. LOOP EVASIONE AFK (F6 per impostazione predefinita)
   Muove il personaggio in modo casuale e periodico per evitare che
   il gioco ti disconnetta per inattività. Attiva e dimentica.

4. REGISTRAZIONE SEQUENZE (F7 per impostazione predefinita)
   · Premi F7 per avviare la registrazione.
   · Esegui le azioni che vuoi automatizzare (clic, tasti,
     attese, movimenti del mouse).
   · Premi di nuovo F7 per fermare la registrazione.
   · La sequenza viene salvata ed è pronta per essere eseguita.
   · Puoi avere più sequenze e passare da una all'altra tramite
     il menu a tendina in alto.
   · Ogni passo può essere modificato: cambiare il tempo di attesa,
     assegnare un'immagine di verifica, riordinare o eliminare passi.
   · Puoi aggiungere pause statiche tra i passi con il pulsante
     "Aggiungi Pausa Statica" situato accanto al pulsante di esecuzione.

5. CATTURA IMMAGINE (F8 per impostazione predefinita)
   Seleziona una regione dello schermo per salvarla come modello.
   Queste immagini vengono usate come condizioni di verifica nei passi
   delle sequenze: il bot verifica che l'immagine sia sullo schermo
   prima di eseguire quel passo. Se non la rileva, può riprovare o
   saltare il passo in base alla configurazione.
   · Premi Escape per annullare la cattura senza selezionare nulla.
   · Puoi anche importare immagini PNG esterne direttamente dal pannello
     delle immagini salvate, senza catturare lo schermo.

6. BANDIERE (F9 per impostazione predefinita)
   Apre il Generatore Principale di Bandiere v6 integrato. Permette di
   creare e personalizzare bandiere del gioco con oltre 500 varianti,
   editor di colori carattere per carattere, assemblatore nick+cornice
   ed esportazione diretta del codice per il file .inf del gioco.

7. GUIDA DELLA PRIGIONE (F10 per impostazione predefinita)
   Apre la guida completa del gioco direttamente all'interno di AriaBot,
   senza dover cambiare finestra. Include le categorie Munizioni, Cucina,
   Chimica, Gioielleria, Abilità, Abbigliamento, Meccanica, Cucito,
   Carlito-Corazza e Salita di Livello.
   Crediti: www.gentelaprision.es

8. MAPPA DELLA PRIGIONE (F11 per impostazione predefinita)
   Apre la mappa interattiva del gioco all'interno di AriaBot con:
   · Zoom con la rotella del mouse o i pulsanti +/−
   · Trascinamento per navigare nella mappa
   · Legenda con toggle per mostrare/nascondere i livelli di icone
   · Pulsante CENTRA per tornare alla vista iniziale (120% centrato)
   · Clic destro sulla mappa → mostra le coordinate del punto
     (utile per la calibrazione)

   RICERCA STANZA:
   · Digita il nome di qualsiasi stanza nella barra di ricerca
   · La ricerca è in tempo reale e insensibile agli accenti
     (sotano = sótano)
   · La mappa fa zoom automatico e si centra sulla stanza trovata
   · Se ci sono più risultati, naviga con i pulsanti ‹ ›
   · Il contatore mostra quanti risultati ci sono (es: 1 / 3)
   · Cancella il testo per tornare alla vista normale

   Crediti: www.gentelaprision.es

9. FERMA TUTTO (F12 per impostazione predefinita)
   Ferma immediatamente tutte le funzioni attive: autoclick, AFK,
   guardia, sequenze in esecuzione. Pulsante di emergenza.


CONFIGURAZIONE GENERALE
────────────────────────
Nel pannello superiore destro troverai tre controlli indipendenti:

  INTERVALLO AUTOCLICK (s)
  Digita direttamente il numero di secondi tra ogni clic dell'autoclick.
  Applicato in tempo reale senza riavviare.

  VELOCITÀ DI SPOSTAMENTO DEL MOUSE NELLE SEQUENZE
  Cursore che controlla la velocità di movimento del mouse durante
  l'esecuzione delle sequenze. Centrato per impostazione predefinita
  (velocità standard). Sposta a sinistra per andare più lento, a destra
  per andare più veloce.

  SEQUENZA ONE LOOP
  Se selezionato, la sequenza attiva eseguirà un unico ciclo completo e
  si fermerà automaticamente al termine. Se deselezionato, la sequenza
  si ripete in loop continuo fino a quando non la fermi manualmente.


CONFIGURARE I TASTI RAPIDI (⚙ Opzioni)
────────────────────────────────────────
Puoi cambiare qualsiasi tasto rapido con la combinazione che preferisci:

1. Clicca il pulsante ⚙ Opzioni nel pannello sinistro.
2. Clicca il pulsante dell'azione che vuoi modificare.
3. Premi il tasto o la combinazione desiderata (Ctrl+J, Alt+F, F2…).
4. Se c'è un conflitto con un'altra azione, il programma ti avviserà.
5. Clicca "Salva e Applica" — le modifiche sono immediate.
6. "Ripristina predefiniti" riporta tutto a F4–F12.

I tasti configurati vengono salvati in hotkeys.json e caricati
automaticamente ad ogni avvio del programma.

IMPORTANTE: i tasti assegnati alle azioni di AriaBot sono esclusi
dalla registrazione nelle sequenze, in modo da non interferire con
l'automazione.


CAMBIARE LINGUA (⚙ Opzioni)
─────────────────────────────
AriaBot è disponibile in Spagnolo, Inglese, Francese e Italiano.
Per cambiare lingua:

1. Clicca il pulsante ⚙ Opzioni nel pannello sinistro.
2. Nella sezione LINGUA / LANGUAGE, seleziona ES, EN, FR o IT.
3. Clicca "Salva e Applica".
4. Apparirà un avviso che indica che è necessario riavviare.
5. Clicca "Riavvia ora" per applicare il cambiamento immediatamente,
   o "Riavvia più tardi" per farlo al prossimo avvio.

La lingua scelta viene salvata in settings.json e applicata
automaticamente ad ogni avvio del programma.


ASSISTENZA TECNICA
───────────────────
AriaBot include un modulo di contatto integrato accessibile dal pulsante
"Assistenza Tecnica" in fondo al pannello sinistro. Compila il tuo nome,
email e una descrizione del problema e il messaggio verrà inviato
direttamente allo sviluppatore.


PIATTAFORMA CLOUD
──────────────────
AriaBot include l'integrazione con un server per condividere e scaricare
sequenze con altri giocatori:

· Pubblica Sequenza → carica la sequenza attiva sul server in modo che
  altri giocatori possano scaricarla.
· Esplora Repository → scarica le sequenze pubblicate da altri utenti
  e le importa direttamente nella tua collezione.


SEQUENZE — USO AVANZATO
─────────────────────────
· Puoi creare quante sequenze vuoi con il pulsante "+".
· Ogni sequenza viene salvata automaticamente alla chiusura del programma.
· I passi supportano: clic sinistro, clic destro, doppio clic, pressione
  di tasto, digitazione di testo e attese temporizzate.
· Assegnare un'immagine a un passo fa sì che il bot verifichi che
  l'immagine sia visibile sullo schermo prima di eseguirlo.
· Le sequenze possono essere eseguite in loop continuo o in un unico
  ciclo attivando l'opzione Sequenza one loop.
· Puoi aggiungere pause statiche tra i passi dal pulsante situato
  accanto al pulsante di esecuzione.
· Puoi importare immagini PNG esterne nel pannello dei modelli senza
  doverle catturare dallo schermo.


FILE E CARTELLE CREATI
────────────────────────
Tutti i file vengono creati nella stessa cartella del .exe:

  Secuencias.json   → sequenze registrate (backup consigliato)
  hotkeys.json      → configurazione dei tasti rapidi
  settings.json     → configurazione della lingua
  templates\        → immagini catturate per la verifica nelle sequenze
  Mapa.png          → immagine della mappa (aggiornata automaticamente)
  changelog.txt     → creato/aggiornato quando si riceve un aggiornamento
  readme.txt        → guida in spagnolo (aggiornata automaticamente)
  readmeIT.txt      → questa guida (aggiornata automaticamente)
  _update.bat       → file temporaneo durante gli aggiornamenti
                      (si elimina da solo)
  AriaBot.new       → file temporaneo durante il download di un aggiornamento
                      (diventa AriaBot.exe al termine)


AGGIORNAMENTI AUTOMATICI
──────────────────────────
AriaBot verifica all'avvio se è disponibile una nuova versione.
Se lo è, ti chiederà se vuoi aggiornare. Accettando:
  1. Scarica la nuova versione in background (il progresso è visibile
     nel registro).
  2. Scarica il changelog, il readme e Mapa.png aggiornati.
  3. Si chiude automaticamente.
  4. Sostituisce l'eseguibile con la nuova versione.
  5. Apre changelog.txt nel Blocco note per mostrarti le modifiche.
Non devi fare altro. Le tue sequenze e la tua configurazione vengono
conservate.


CREDITI
────────
Guide e risorse del gioco fornite da:
  www.gentelaprision.es
  — Il riferimento in spagnolo per tutto ciò che riguarda La Prisión.

=====================================================================
