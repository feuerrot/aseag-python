# Aseag, Python?
Die ASEAG bietet für Smartphones eine Anwendung an, die auf eine API
zugreift, die Echtzeitdaten liefert. Da man das natürlich auch gerne in
eigenen Anwendungen nutzen will, um Dinge™ anzuzeigen - ein eigener
Abfahrtsmonitor wird so z.B. möglich.

## Technische Details
[Hier](http://ivu.aseag.de/interfaces/ura/instant_V2) fällt JSON raus. Wenn
man einfach die API-Dokumentation von [Transport for
London](http://www.tfl.gov.uk/cdn/static/cms/documents/tfl-live-bus-and-river-bus-arrivals-api-documentation.pdf)
nimmt, hat man eine ganz gute Anleitung, was man mit so einer
URA-Schnittstelle anfangen kann.

Außerdem existieren noch Schnittstellen für das Routing und die Suche nach
Haltestellen. Muss noch inspiziert werden, Ergebnisse werden folgen.

## Wann gibt es interessantes?
Jetzt! Der Code ist zwar ranzig, kann aber zur Abfrage einzelner
Haltestellen bereits verwendet werden. Dazu wirft man einfach die
gewünschten Argumente in beliebiger Reihenfolge gegen das Script:
```
Usage: ./main [StopID/StopName] [BusID] ([BusID]…) +[MaxWait]
```
### [StopID/StopName]
* StopID: Haltestellennummer, 6 Ziffern
* StopName: Haltestellenname, eindeutiger Teilstring, case insensitive

### [BusID]
* 1-3 Ziffern für die Busnummer
 * Todo: {,1}3{A,B} sollte auch funktionieren
* Beliebig viele angebbar

### +[MaxWait]
* + gefolgt von einer Zahl: maximal Busse bis in n Minuten anzeigen

## Mitmachen
Ja, tu es! Ich sehe auch gerne noch andere Anwendungen hierfür - so ein
selbstgebautes Abfahrtsdisplay wäre doch ganz schick!

## Aktueller Status
Zuckt tatsächlich noch und könnte wieder etwas besser als vorher sein. Muss
allerdings noch mindestens drei Mal genau so neu geschrieben werden, bis es
schön aussieht.

## Zukunft
Routing und die Suche nach Haltestellennamen/IDs wäre fein, ggf. auch die
Anzeige der Routeninformation eines einzelnen Busses.
