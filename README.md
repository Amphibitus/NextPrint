# 🗺️ QGIS-Plugin: NextPrint

![QGIS Version](https://img.shields.io/badge/QGIS-3.x-green.svg)
![Plugin Version](https://img.shields.io/badge/Version-2.7-blue.svg)

**NextPrint** ist ein leistungsstarkes QGIS-Plugin, das den Workflow im Drucklayout (Print-Composer) radikal vereinfacht. Es ermöglicht die schnelle Eingabe von Textdaten, das Handling zahlreicher Layouts und die einfache Rotation von Karten.

---

## 📖 Scope & Historie

Dieses Plugin basiert auf dem ursprünglichen "Instant Print" von SOURCEPOLE und wurde über "Easy Template Print" stetig weiterentwickelt.

### Entwickler-Historie:
* **Version 2.7+ (NextPrint):** Gerd Dreier (geoplaning GmbH)
* **Bis Version 2.6 (Easy Template Print):** Jesper Jøker Eg (GISkonsulenten)
* **Ursprung (Instant Print):** SOURCEPOLE, Zürich

---

## ✨ Hauptfunktionen

Das Plugin erweitert die Standard-Druckfunktionen von QGIS um folgende Features:

### Automatisierung beim Start:
* **Composer-Liste:** Lädt alle aktiven Layouts des Projekts alphabetisch sortiert.
* **Skalierung:** Synchronisiert den Maßstab automatisch mit dem aktuellen Kartenfenster.
* **Label-Erkennung:** Findet automatisch bis zu 5 Ausdrücke/Labels im Layout und erstellt dafür Eingabefelder im Dialog.
* **Export-Formate:** Erstellt eine Liste aller verfügbaren Export-Optionen.

### Benutzerfunktionen im Dialog:
* **Layout-Wechsel:** Einfache Auswahl verschiedener Composer.
* **Flexibler Maßstab:** Maßstab aus Liste wählen, manuell tippen oder vom Map-Canvas übernehmen.
* **Format & Ausrichtung:** Dynamische Auswahl von Papiergröße sowie Hoch- oder Querformat.
* **Rotation:** Anpassung der Rotation für alle an die Karte gekoppelten Elemente.
* **Druck entlang einer Linie:** Spezialfunktion für lineare Projekte.
* **Multi-Print:** Festlegung einer Überlappungsgröße für Seriendrucke.
* **Sichtbarkeit:** Legende ein- oder ausblenden per Klick.
* **Direkt-Export:** Export in Datei, Öffnen des Layouts im Composer oder automatisches Öffnen der generierten PDF.

---

## 🛠 Technische Details & Bindings

Damit das Plugin die Textfelder im Layout erkennt, müssen die Variablen korrekt formatiert sein.

> [!IMPORTANT]
> **Syntax für Label-Variablen:** > Die Variable muss exakt so geschrieben werden: `[% @Region %]` (bitte auf die Leerzeichen achten!).

* Das Plugin durchsucht alle Label-Items im Composer nach dem String `[% @]`.
* Gefundene Variablen werden als Eingabefeld im Dialog angezeigt.
* Eingabedaten werden in den Projektvariablen gespeichert und stehen somit auch für andere Composer zur Verfügung.
* **Hinweis:** Template-Variablen dürfen nicht denselben Namen wie Label-Variablen tragen.

---

## 📐 Dynamische Layouts (Papierformat)

Um die Funktion zur Änderung der Papiergröße optimal zu nutzen, müssen die Elemente (Karte, Legende, Texte) im QGIS-Composer **dynamisch definiert** sein, damit sie sich automatisch anpassen.

* Beispiele finden sich im `Layout`-Ordner des Plugins.
* Weitere Informationen findest du im [QGIS Training Manual: Dynamic Layout](https://docs.qgis.org/3.34/en/docs/training_manual/map_composer/dynamic_layout.html).

---

## 📂 Extras & Vorlagen

Im Verzeichnis des Plugins befindet sich ein **`Help`-Ordner**. Dieser enthält:
* Vorbereitete Composer-Templates.
* Beispiel-Projektdateien für ein schnelles Setup.

---
*Entwickelt für effizientes Arbeiten mit QGIS Drucklayouts.*
