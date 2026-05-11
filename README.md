# 🗺️ QGIS-Plugin: NextPrint

![QGIS Version](https://img.shields.io/badge/QGIS-3.x-green.svg)
![Plugin Version](https://img.shields.io/badge/Version-2.7-blue.svg)
![Category](https://img.shields.io/badge/Category-Printing-orange.svg)

**NextPrint** optimiert den Workflow im QGIS-Drucklayout (Print-Composer). Es ermöglicht eine schnelle Texteingabe über Dialogfelder, unterstützt die Rotation von Karten und das Handling zahlreicher Layouts in einem Schritt.

---

## 📖 Hintergrund & Historie

Das Plugin ist eine konsequente Weiterentwicklung bewährter Tools und vereint deren Stärken mit neuen Funktionen.

### Entwickler-Historie:
* **Seit Version 2.7 (NextPrint):** Gerd Dreier (geoplaning GmbH)
* **Bis Version 2.6 (Easy Template Print):** Jesper Jøker Eg (GISkonsulenten)
* **Ursprung (Instant Print):** SOURCEPOLE, Zürich

---

## ✨ Features & Funktionen

### Automatisierung beim Start
* **Intelligente Liste:** Erkennt alle Composer im Projekt und sortiert sie alphabetisch.
* **Maßstabs-Sync:** Übernimmt automatisch den aktuellen Maßstab des Kartenfensters.
* **Label-Erkennung:** Findet bis zu 5 Ausdrücke im Layout und generiert sofort passende Eingabefelder.

### Benutzerfunktionen im Dialog
* **Flexibles Layout:** Wechsel von Papierformaten sowie Hoch- und Querformat direkt im Tool.
* **Präzise Rotation:** Anpassung der Rotation für die Karte und alle damit verknüpften Layout-Elemente.
* **Druck-Extras:** * Unterstützung für "Drucken entlang einer Linie".
    * Definition von Überlappungen für den Multi-Print.
    * Legende per Checkbox ein- oder ausblenden.
* **Workflow-Boost:** Export-Vorschau, direktes Öffnen der PDF nach der Generierung oder Bearbeiten des Layouts im Composer.

---

## 🛠 Konfiguration der Labels (Bindings)

Damit NextPrint die Eingabefelder automatisch erkennt, müssen die Variablen im Drucklayout einem bestimmten Schema folgen:

> [!IMPORTANT]
> **Syntax:** Die Variable muss exakt als `[% @Region %]` formatiert sein.
> Das Plugin sucht gezielt nach dem Präfix `[% @]`.

* **Speicherung:** Eingegebene Daten werden als Projektvariablen gespeichert und sind somit über verschiedene Composer hinweg verfügbar.
* **Einschränkung:** Standard-Templatevariablen dürfen nicht denselben Namen wie Label-Variablen tragen.

---

## 📂 Vorlagen & Hilfe

Das Plugin wird mit fertigen Ressourcen ausgeliefert, um den Einstieg zu erleichtern:

* **Templates:** Beispiel-Layouts findest du direkt im Ordner `Layout` innerhalb des Plugin-Verzeichnisses.
* **Projektdateien:** Im `Help`-Ordner befinden sich vorkonfigurierte QGIS-Projekte.

### Dynamische Layouts
Wenn du das Papierformat im laufenden Betrieb ändern möchtest, müssen die Elemente (Karte, Legende, Titel) im Composer **dynamisch** definiert sein.
* Anleitungen dazu findest du in der [QGIS Dokumentation zu dynamischen Layouts](https://docs.qgis.org/3.34/en/docs/training_manual/map_composer/dynamic_layout.html).

---
*Made for GIS-Pros – Effizientes Drucken leicht gemacht.*
