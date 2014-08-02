# Aseag, Python?
Die ASEAG bietet für Smartphones eine Anwendung an, die auf eine API
zugreift, die Echtzeitdaten liefert. Da man das natürlich auch gerne in
eigenen Anwendungen nutzen will, um Dinge™ anzuzeigen - ein eigener
Abfahrtsmonitor wird so z.B. möglich.

## Technische Details
[Hier](http://ivu.aseag.de/interfaces/ura/instant_V1) fällt JSON raus. Wenn
man einfach die API-Dokumentation von [Transport for
London](http://www.tfl.gov.uk/cdn/static/cms/documents/tfl-live-bus-and-river-bus-arrivals-api-documentation.pdf)
nimmt, hat man eine ganz gute Anleitung, was man mit so einer
URA-Schnittstelle anfangen kann.

## Wann gibt es interessantes?
Niemals. Höchstens zurechtgebasteltes, was hauptsächlich meinen
Anforderungen entspricht. Immerhin gibt es sogar eine Anleitung, wenn man
das Script ohne Argumente aufruft:
```
Usage: ./main [Stop] [Bus IDs]
```
Dazu kommt dann noch die Ausgabe von der Defaulthaltestelle - aber das wird
noch.

## Mitmachen
Ja, tu es! Ich sehe auch gerne noch andere Anwendungen hierfür - so ein
selbstgebautes Abfahrtsdisplay wäre doch ganz schick!

## Aktueller Status
Zuckt tatsächlich noch, wurde in den letzten paar Stunden leicht
überarbeitet (aka: Code in Fenster 1 offen, alles in Fenster 2 neu
schreiben) und könnte schon etwas besser als vorher sein.

## Zukunft
FPGA + Ethernet + VGA wäre zwar echt nett, aber ich bleibe wahrscheinlich
bei 'nem Raspberry oder dergleichen mit einem Monitor dazu, das kann ich
wenigstens. Frühestens zu sehen in zu langer Zeit…
