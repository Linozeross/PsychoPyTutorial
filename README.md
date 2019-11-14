# PsychoPyTutorial
In diesem Repository findet ihr alles in meinem PsychoPy Tutorial am 15.11.19 verwendete Material. Neben der Präsentation auch alle 6 Versionen des Beispielprojekts. 

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
Fixationspunkt: https://www.psychopy.org/builder/components/grating.html
Keyboard: https://www.psychopy.org/builder/components/keyboard.html

# Version 2
In dieser Version sollte unsere Routine fünf mal wiederholt werden und der Stimulus in unterschiedlichen Farben angezeigt werden.
Hier haben wir eine Schleife (Loop) hinzugefügt, damit die Routine 5x wiederholt wird. Durch einen Klick auf die Schleife (fuenfMal) kann man sich Details dazu anschauen. In dieser Schleife wird die Datei 02loop.xlsx eingelesen. In dieser Datei haben wir 5 Bedingungen definiert, die jeweils 1x (nRep) zufällig wiederholt werden. Dabei wird in jeder Bedingung die Variable go_color auf einen bestimmten Wert gesetzt (z.B. Red oder Green). 

Damit diese Variable auch eine Auswirkung hat, haben wir zusätzlich die Parameter von go_item angepasst. Unter dem Reiter Advanced, sehen wir, dass das Attribut 'Fill color' jetzt auf den Wert $go_color gesetzt wurde, und diese Zuweisung bei jeder Wiederholung geschieht (set every repeat). Damit wird in jedem Durchgang die Füllfarbe unseres Polygons auf den Wert der Variablen go_color gesetzt. So wird der Stimulus in unseren fünf Wiederholungen einmal rot, grün, schwarz, weiß und lachsfarben angezeigt.

# Version 3
In dieser Version sollte erst ein Instruktionsbildschirm angezeigt werden und Antworten als richtig oder falsch klassifiziert werden.
Hier wurde (zu sehen im 'Flow' Teil des Builders), eine weitere Routine 'instruction' hinzugefügt, die vor den jeweiligen Stimuluspräsentationen angezeigt wird.
Zusätzlich wurde unsere Schleife angepasst (importiert jetzt 03loop.xlsx) und definiert jetzt 2 Variablen













