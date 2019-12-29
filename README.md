# egn Abfallkalender

Das für mich zuständige Abfallunternehmen, die EGN Entsorgungsgesellschaft Niederrhein mbH, bietet mir die Möglichkeit, dass ich mir im Browser meinen Abfallkalender unter [www.egn-abfallkalender.de](https://www.egn-abfallkalender.de/) anzeigen lassen kann, allerdings kann ich den Kalender dort nicht herunterladen, um ihn in Google Kalender oder einer anderen Kalender-App zu importieren.

Für das Tool __egn.py__ kopiere ich mir im Browser nach Erzeugen meines Abfallkalenders das json-Objekt aus der Entwicklerkonsole und füge es in meinem Tool ein. Ich muss dort dann noch das Jahr in der Variable _year_ setzen und das Tool starten, das im Verzeichnis dann eine csv-Datei erzeugt.

Die Anfrage für das json-Objekt richtet sich an die URL _https://www.egn-abfallkalender.de/kalender_ (POST) mit den folgenden Parametern city=[Name der Stadt]&district=[Name des Stadtteils]&street=[Name der Hausnummer]&street_number=[Hausnummer].

Google bietet eine [Anleitung](https://support.google.com/calendar/answer/37118), wie man csv- oder ics-Dateien in Google Kalender importieren kann und welches Format erforderlich ist.

Stand: Dezember 2019
