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

Da Schnittstellen für Haltestellenechtzeitdaten, Haltestellensuche und
Routing existieren, nutze ich die hier auch.

## Benutzung
`./main [StopID] [BusIDs]` macht Echtzeitinformationen zur Haltestelle. Als
StopID funktionieren sowohl Haltestellennamen als auch die numerischen IDs.

`./main [StartID] [StopID]` macht Routing vom Start zum Stop. Für die IDs
gilt das gleiche wie bei den Echtzeitinformationen.
