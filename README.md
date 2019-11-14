# PsychoPyTutorial
In diesem Repository findet ihr alles in meinem PsychoPy Tutorial am 15.11.19 verwendete Material. Neben der Präsentation auch alle 6 Versionen des Beispielprojekts. 

Zum Lernen von PsychoPy empfehle ich zusätzlich die ausgesprochen lehrreichen PsychoPy Demos. Fragen beantwortet und Unterstützung bekommt man auch im PsychoPy Forum.  
> Demos: https://www.psychopy.org/builder/concepts.html
> Forum: https://discourse.psychopy.org/

# Beispielprojekt
Wir implementieren einen beispielhaften Go/NoGo - Task in PsychoPy. Die Probanden sollen die Leertaste drücken wenn der Stimulus rot ist und sonst keine Taste drücken.

Das Projekt ist in 6 Versionen implentiert, die aufeinander aufbauen. In jeder Version kommen ein oder mehrere neue Elemente dazu. Zum Ausprobieren kann man dieses Repository (über den grünen Button Download/Clone) herunterladen und dann die einzelnen .psyexp Dateien in PsychoPy laden.

Eine Beschreibung was in den einzelnen Versionen umgesetzt wurde findet sich auch in der Präsentation.

# Version 1
In dieser Version erstellen wir nur eine Routine (ein Teil des Experiments das anschließend öfter wiederholt wird). Sie enthält drei Komponenten, die nacheinander angezeigt werden (Namen der Komponenten in Klammern):
- Ein Fixationspunkt (fixation)
- Der Stimulus (go_item)
- Ein Keyboard Component (key_resp)

Dabei das Verhalten des Keyboards (mittels des Parameters "Force end of routine") so angepasst, dass die Routine dann beendet wird wenn die Leertaste gedrückt wird.

Über die Parameter der einzelnen Komponenten kann man in der PsychoPy - Dokumentation mehr erfahren z.B.:

> Fixationspunkt: https://www.psychopy.org/builder/components/grating.html
> Keyboard: https://www.psychopy.org/builder/components/keyboard.html

# Version 2
In dieser Version sollte unsere Routine fünf mal wiederholt werden und der Stimulus in unterschiedlichen Farben angezeigt werden.
Hier haben wir eine Schleife (Loop) hinzugefügt, damit die Routine 5x wiederholt wird. Durch einen Klick auf die Schleife (fuenfMal) kann man sich Details dazu anschauen. In dieser Schleife wird die Datei 02loop.xlsx eingelesen. In dieser Datei haben wir 5 Bedingungen definiert, die jeweils 1x (nRep) zufällig wiederholt werden. Dabei wird in jeder Bedingung die Variable go_color auf einen bestimmten Wert gesetzt (z.B. Red oder Green). 

Damit diese Variable auch eine Auswirkung hat, haben wir zusätzlich die Parameter von go_item angepasst. Unter dem Reiter Advanced, sehen wir, dass das Attribut 'Fill color' jetzt auf den Wert $go_color gesetzt wurde, und diese Zuweisung bei jeder Wiederholung geschieht (set every repeat). Damit wird in jedem Durchgang die Füllfarbe unseres Polygons auf den Wert der Variablen go_color gesetzt. So wird der Stimulus in unseren fünf Wiederholungen einmal rot, grün, schwarz, weiß und lachsfarben angezeigt.

> Mehr Informationen zu verschiedenen Schleifentypen etc.: https://www.psychopy.org/builder/flow.html

# Version 3
In dieser Version sollte erst ein Instruktionsbildschirm angezeigt werden und Antworten als richtig oder falsch klassifiziert werden.
Hier wurde (zu sehen im 'Flow' Teil des Builders), eine weitere Routine 'instruction' hinzugefügt, die vor den jeweiligen Stimuluspräsentationen angezeigt wird.
Zusätzlich wurde unsere Schleife angepasst (importiert jetzt 03loop.xlsx) und definiert jetzt 2 Variablen. Neben der Farbe wird jetzt auch die richtige Taste definiert. Wenn ein roter Stimulus erscheint wäre die richtige Antwort die 'space'-Taste zu drücken. Erscheint ein andersfarbener Stimulus, ist die richtige Antwort keine Taste zu drücken (None). Die Keyboard Komponente greift auf diese Varible zu, um zu klassifizieren welche Antworten der Versuchsperson richtig und welche falsch sind.

# Version 4
In dieser Version sollte der Stimulus nicht mehr in der Mitte des Bildschirms, sondern zufällig entweder links oder rechts präsentiert werden. Dafür sollte eine Code Komponente verwendet werden.

In der neuen Komponente (code) wurden ein paar Zeilen Python code eingefügt. Code Komponenten sind ein guter Weg um flexibel Teile des Experiments anpassen zu können ohne den Coder verwenden zu müssen. Es wurde Python code in den 2 Bereichen (über Reiter der Komponente code zu erreichen) 'Begin Routine' und 'End Routine' hinzugefügt. Am Anfang jeder Durchführung der Routine soll die Stimulus position zufällig bestimmt werden (entweder rechts oder links). Dafür generieren wir einen zufälligen Wert zwischen 0 und 1. Ist dieser kleiner als 0.5 (das passiert in 50% der Fälle), wird eine neue Varible stim_pos auf einen Koordinatenwert links der Bildschirmmitte gesetzt. Ist der zufällige Wert größer als 0.5, auf einen Wert rechts der Bildschirmmitte. Am Ende jeder Routine soll noch gespeichert werden wo der Stimulus präsentiert wurde, um das später bei Auswertung der Ergebnisse berücksichtigen zu können. Dafür wird unter dem 'End Routine' Reiter definiert, dass in unsere Datei mit allen Daten des Experiments (im Anschluss an die Durchführung im Ordner data/ zu finden), zusätzlich eine Spalte stimulusPosition geschrieben wird.

Damit der Stimulus auch an der richtigen Position angezeigt wird, wurde zusätzlich das Attribut Position von unserem Stimulus (go_item) mit der neuen Variable $stim_pos belegt.

> Mehr Information zu Code Komponenten: https://www.psychopy.org/builder/components/code.html
> Mehr Information zu den verwendeten Python Code Befehlen: https://www.w3schools.com/python/python_conditions.asp

# Version 4b
Veränderte Code Komponente um zu zeigen wie man Objekte während einer Routine in eine zufällige Richtung bewegen kann.

# Version 5
In dieser Version sollte nach der Instruktion ein paar Mal die spätere Routine mit Feedback als Übungsrunde implementiert werden.

Wir haben 2 weitere Routinen sowie eine neue Schleife (practiceLoop) hinzugefügt. Neu und interessant ist vor allem die neue Routine feedback. Hier gibt es eine Text Komponente die lediglich die Variable $msg als Text anzeigt. Dieser Variable wird von der Code Komponente code_2 ein bestimmter Wert zugewiesen. Die Feedback Routine soll der Versuchsperson zeigen ob ihre letzte Antwort richtig oder falsch war und entsprechend einen anderen Text anzeigen. Dafür wird in code_2 am Anfang des Experiments einmal die Varible msg definiert. Anschließend wird (mittels der Keyboard Komponente key_resp aus der trial Routine) überprüft ob die letzte Antwort richtig war oder nicht. Entsprechend wird die $msg Variable auf eine unterschiedlichen Wert gesetzt.

# Version 6
In dieser letzten Version wollten wir die Übungsrunden optional machen und Veränderungen mit dem Coder vornehmen. 

Wir haben zuerst die 'Experiment Settings' mit einem Klick auf den entsprechenden Button im Builder verändert und eine weitere Zeile 'practice' mit Defaultwert True eingefügt. Anschließend haben wir die bei Ausführung von PsychoPy automatisch generierte python-Datei 06version_lastrun.py im Coder geöffnet und in Zeile 244 drei Zeilen Code eingefügt. Diese überprüfen, ob bei Start des Experiments das Häkchen bei practice gesetzt ist. Falls nicht, wird durch den Befehl 'break' die komplette Schleife practiceLoop übersprungen. Das Experiment springt also direkt in das Hauptexperiment. 
Damit die Datei nicht überschrieben wird, haben wir Sie anschließend in 06version.py umbenannt. Um diese Änderungen auszuprobieren, muss man die Datei 06version.py im Coder öffnen und starten.

Diese Änderung sollte zeigen wie der Coder funktioniert. Außerdem sollte klarwerden, dass es in einigen Fällen praktisch sein kann kleinere Anpassungen im Coder vorzunehmen.



