# TKG · Geldwerter Vorteil

Firmenwagen-Rechner für den Nettovergleich einer Gehaltsabrechnung mit und ohne Firmenwagen.

Live: https://flathack.github.io/tkg-geldwerter-vorteil/

## Nutzung

`index.html` im Browser öffnen oder lokal mit `python -m http.server 8080` bereitstellen. Abrechnungswerte können manuell eingegeben oder aus einer PDF übernommen werden. Die Verarbeitung der Abrechnung erfolgt lokal im Browser. PDF.js wird extern geladen; für die PDF-Funktion ist eine Internetverbindung erforderlich.

`firmenwagenrechner-standalone.html` ist der Download mit eingebetteter Gestaltung und Rechnerlogik. Auch hier lädt die PDF-Funktion PDF.js extern.

Der Rechner liefert eine überschlägige Netto-Differenzrechnung; die bestehenden Berechnungen wurden beim Umzug unverändert übernommen.

## Veröffentlichung

GitHub Pages veröffentlicht den Branch `main` aus dem Repository-Stammverzeichnis. Nach einem Push den Pages-Build unter Actions prüfen.

## Herkunft

Übernommen aus `flathack/flathack.github.io`, ehemaliger Pfad `guides/firmenwagenrechner/`. Eigenständige TKG-Oberfläche auf Basis lokal eingebundener Flathack-Design-Tokens. Zehn wählbare Themes, standardmäßig Cloud, einschließlich Matrix und Guild Wars 2. Die Auswahl wird lokal gespeichert; Animationen lassen sich abschalten und respektieren reduzierte Bewegung. TKG-Branding und Rechnerlogik bleiben eigenständig.

## Standalone aktualisieren

Nach Änderungen an Oberfläche oder Gestaltung `python scripts/build-standalone.py` ausführen. Der Generator bettet CSS, Fonts, Texturen und Theme-Scripts ein; nur PDF.js benötigt weiterhin eine Internetverbindung.
