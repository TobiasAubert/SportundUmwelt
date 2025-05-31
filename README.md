# 📊 Modal Split & Motivation – Seminarprojekt *Sport und Umwelt*

## Überblick

Dieses Projekt analysiert die Mobilitätsgewohnheiten und Motivationsfaktoren von Sportstudierenden im Rahmen des Seminars **„Sport und Umwelt“**. Ziel ist es, den **Modal Split** (Verteilung der genutzten Verkehrsmittel) und relevante **Einflussfaktoren** auf nachhaltige Mobilität zu erfassen und visuell darzustellen.

---

## 📁 Struktur

### `evaluation.py`
- Liest und bereinigt die Umfragedaten (`results-survey926142.csv`)
- Vereinheitlicht Sportarten zur besseren Gruppierung
- Visualisiert:
  - Die **Häufigkeit der Hauptsportarten**
  - Den **Modal Split** zur Hauptsportart:
    - Nach Nutzungshäufigkeit (Fahrten pro Woche)
    - Nach zurückgelegten Kilometern pro Verkehrsmittel

### `evaluation_motivation.py`
- Analysiert Daten zu:
  - **Motivationsfaktoren** für nachhaltige Mobilität (`results_motivation.csv`)
  - **Hindernissen** für nachhaltige Mobilität (`results_obstacles.csv`)
- Darstellung:
  - Balkendiagramm mit **Mittelwerten und Standardabweichungen** der Motivation
  - Häufigkeit der Nennungen von **Barrieren**

---

## 📊 Datengrundlage

Die Analyse basiert auf drei Umfrage-Datensätzen:
- `results-survey926142.csv`: Hauptumfrage mit Sportarten und Verkehrsmitteln
- `results_motivation.csv`: Einschätzung verschiedener Motivationsfaktoren
- `results_obstacles.csv`: Offene Nennungen von Hindernissen

---

## 🛠 Anforderungen

- Python 3.x
- Pakete:
  - `pandas`
  - `matplotlib`
  - `numpy`
  - `mpl_toolkits` (für `inset_axes`)

Installiere ggf. fehlende Pakete mit:

```bash
pip install pandas matplotlib numpy
