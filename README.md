# Abfallkalender-Downloader

> [!WARNING]  
> Ich pflege dieses Repository nicht mehr, da ich den Abfallkalender eines anderen Anbieters benötige. Das Repository bleibt online, falls jemand anderes den Quelltext benötigen kann (2023-12-31).

Die EGN Entsorgungsgesellschaft Niederrhein mbH bietet die Möglichkeit, dass man sich im Browser seinen Abfallkalender unter [www.egn-abfallkalender.de](https://www.egn-abfallkalender.de/) anzeigen lassen kann, allerdings kann man den Kalender dort nicht herunterladen, um ihn in Google Kalender oder einer anderen Kalender-App zu importieren.

Hier setzt das Tool an und erlaubt die Daten aus dem Online-Kalender zu beziehen.

Im Tool __egn.py__ setzt man folgende Parameter

```python
year = 2020
city = "Brüggen"
district = "Bracht"
street = "Agrisstrasse"
house_number = "1"
```

und führt es dann aus. Das Tool erzeugt dann eine csv-Datei, die man z. B. in Google Kalender importieren kann.

Google bietet eine [Anleitung](https://support.google.com/calendar/answer/37118), wie man csv- oder ics-Dateien in Google Kalender importieren kann und welches Format erforderlich ist.

Stand: Dezember 2019

## ChangeLog

### [1.0.0] - 2019-12-29
### Added
- Grundsätzliche Funktionalität
- eng.py kann json-Daten aus dem Browser verarbeiten und eine csv-Datei schreiben, die in Google Kalender importiert werden kann
