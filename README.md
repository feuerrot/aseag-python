# Aseag, Python?
Die ASEAG bietet für Smartphones eine Anwendung an, die auf eine API
zugreift, die Echtzeitdaten liefert. Da man das natürlich auch gerne in
eigenen Anwendungen nutzen will, um Dinge™ anzuzeigen - ein eigener
Abfahrtsmonitor wird so z.B. möglich.

## Technische Details
### Allgemein
`http://ivu.aseag.de/interfaces/ura/` ist die Basis, unter der dann alle
Endpunkte erreichbar sind. Es scheint so, als wären dort dann zwei
generelle Typen unterscheidbar.

### {instant,stream}_V{1,2}
Diese vier Endpunkte geben die aktuellen Informationen aus (instant) bzw.
streamen sie (stream). Wo genau der Unterschied zwischen _V1 und _V2 ist,
ist nicht bekannt. Transport for London hat eine
[API-Dokumentation](http://content.tfl.gov.uk/tfl-live-bus-river-bus-arrivals-api-documentation.pdf),
die ganz gut die Verwendung beschreibt.

Die Endpunkte eignen sich wahrscheinlich für Echtzeitdaten für Haltestellen
und einzelne Busläufe.

### {location,journey,journeyUpdate}
Diese drei Endpunkte geben jeweils nicht-kaputtes JSON aus (yay), aus denen
man insbesondere recht einfach die Bedeutung von Werten rauslesen kann und
dienen dazu, Haltestellen zu finden (location), Routing zu planen (journey)
und Informationen zum Routing aktuell zu halten (journeyUpdate).

`location?searchString=NAME` findet Haltestellen mit passendem Name. Der
Parameter `maxResults` kann dazu verwendet werden, das ganze weiter
einzuschränken oder auch in Kombination mit * als Name, um alle
Haltestellen auszugeben. Der Defaultwert scheint 10 zu sein.
Der Parameter `searchTypes` kennt mindestens den Wert `STOPPOINT`, was auch
der Defaultwert ist.

`journey?startStopId=A&endStopId=B&departureTime=C` gibt
Routinginformationen aus. Die HaltestellenIDs A und B ergeben sich aus dem
location-Endpunkt, `departureTime` ist ein Unix Timestamp in Millisekunden.
Anstatt `departureTime` ist auch die Angabe von `arrivalTime` möglich(?).

`journeyUpdate` tut komische Dinge mit einem Parameter, der aus `journey`
rausfällt und weiteren Parametern. Keine Ahnung, hab ich bisher noch nicht
verwendet.

## Benutzung
`./main [StopID] [BusIDs]` macht Echtzeitinformationen zur Haltestelle. Als
StopID funktionieren sowohl Haltestellennamen als auch die numerischen IDs.

`./main [StartID] [StopID]` macht Routing vom Start zum Stop. Für die IDs
gilt das gleiche wie bei den Echtzeitinformationen.

## Todo
Der Code ist scheiße. Über die Ausgabe von `instant_V{1,2}` kann man
wahrscheinlich deutlich schöner iterieren und ich habe beim Einbauen des
Routing viel Code aus der vorherigen Version übernommen. Man müsste also
den ganzen Code mal wegwerfen und alles sauber neu schreiben - das wird
in $(date +%Y) natürlich nicht passieren. Was ggf. in $(date +%Y) passiert:
- [ ] Weniger magisches Argumentparsing
- [ ] Sinnvolleres Iterieren über die Ausgabe von `instant_V{1,2}`
- [ ] Nutzung von `stream_V{1,2}` für eigene Echtzeitanzeigen
