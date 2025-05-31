import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("src/results-survey926142.csv")

# -------------- Clean the DataFrame --------------
#removing unnecessary columns
df.drop(columns=[
    "Antwort ID",
    "Letzte Seite", 
    "Start-Sprache", 
    "Zufallsstartwert", 
    "Bitte fülle diese Umfrage nur aus, wenn du Sport studierst und eine Sportart regelmässig (mind. 1x pro Woche) ausübst.",
    "An welcher Hochschule studierst du Sportwissenschaft?  [Sonstiges]",
    ], inplace=True)

# Remove invalite entries
df_cleaned = df[df['Datum Abgeschickt'].notna()]
df_cleaned.drop(columns=["Datum Abgeschickt"], inplace=True)


# Vereinheitlichung Kategorien
column_sports = "Bitte gibt deine Hauptsportart an, welche du regelmässig ausübst. "
df_cleaned[column_sports] = df_cleaned[column_sports].str.rstrip() # Remove trailing spaces in the column values
df_cleaned[column_sports] = df_cleaned[column_sports].replace("Gym", "Fitnesssport")
df_cleaned[column_sports] = df_cleaned[column_sports].replace("Fitness", "Fitnesssport")
df_cleaned[column_sports] = df_cleaned[column_sports].replace("Krafttraining", "Fitnesssport")
df_cleaned[column_sports] = df_cleaned[column_sports].replace("Vereinsgeräteturnen", "Geräteturnen")
df_cleaned[column_sports] = df_cleaned[column_sports].replace("Vereinsturnen", "Geräteturnen")
df_cleaned[column_sports] = df_cleaned[column_sports].replace("Schuttä", "Fussball")
df_cleaned[column_sports] = df_cleaned[column_sports].replace("Fusball", "Fussball")



# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Optional: to show full content in each cell (no truncation)
pd.set_option('display.max_colwidth', None)
print(df_cleaned)


## ----------- Plotting -----------
# ---------Plot different sports--------------
# Count the number of occurrences of each sport (excluding NaN)
sport_counts = df_cleaned[column_sports].dropna().value_counts()

total = sport_counts.sum()

plt.figure(figsize=(10, 6))
bars = plt.barh(sport_counts.index, sport_counts.values, color='#1f77b4', edgecolor='black')

# Add data labels: number + percentage
for bar in bars:
    count = int(bar.get_width())
    percent = (count / total) * 100
    label = f'{count} ({percent:.1f}%)'
    plt.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
             label, va='center', fontsize=12)

plt.xlabel("Anzahl", fontsize=12)
plt.ylabel("Sportart", fontsize=12)
plt.title("Häufigkeit der Hauptsportarten", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.gca().invert_yaxis()  # Show most frequent sport at the top
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ---------Plot Modalsplit--------------
# Spaltennamen (genau wie in deinem DataFrame)
columns_transport = [
    "Wie häufig nutzt du die folgenden Verkehrsmittel durchschnittlich pro Woche für den Weg zu deiner Hauptsportart?   [Zu Fuss]",
    "Wie häufig nutzt du die folgenden Verkehrsmittel durchschnittlich pro Woche für den Weg zu deiner Hauptsportart?   [Mit dem Fahrrad]",
    "Wie häufig nutzt du die folgenden Verkehrsmittel durchschnittlich pro Woche für den Weg zu deiner Hauptsportart?   [Öffentliche Verkehrsmittel]",
    "Wie häufig nutzt du die folgenden Verkehrsmittel durchschnittlich pro Woche für den Weg zu deiner Hauptsportart?   [Motorrad/Roller]",
    "Wie häufig nutzt du die folgenden Verkehrsmittel durchschnittlich pro Woche für den Weg zu deiner Hauptsportart?   [Auto (Fahrgemeinschaft)]",
    "Wie häufig nutzt du die folgenden Verkehrsmittel durchschnittlich pro Woche für den Weg zu deiner Hauptsportart?   [Auto (allein)]",

]

df_cleaned.loc[24, "Wie häufig nutzt du die folgenden Verkehrsmittel durchschnittlich pro Woche für den Weg zu deiner Hauptsportart?   [Zu Fuss]"] = 2.0
# Gesamthäufigkeit für jedes Verkehrsmittel berechnen (NaN werden ignoriert)
# Einheitliche Farben – abgestuft nach Umweltfreundlichkeit
custom_colors = {
    'Zu Fuß': '#a1d99b',                # sehr hellgrün
    'Fahrrad': '#31a354',               # grün
    'Öffentliche Verkehrsmittel': "#7ec6f0",  # mittelblau
    'Motorrad/Roller':"#857ecc" ,       # violett (auch hoch)
    'Auto (Fahrgemeinschaft)': "#5645b6",  # etwas heller
    'Auto (allein)': "#460a6b",         # dunkelviolett (hohe Emissionen)
}


# Optional: schöner formatierte Labels
labels = list(custom_colors.keys())



## Modalsplit nach Häufigkeit der Verwendung

transport_sums = df_cleaned[columns_transport].sum()

# Durchschnittliche Nutzung pro Person berechnen
avg_use_per_person = transport_sums / len(df_cleaned)

# Prozentanteile für das Kreisdiagramm
percentages = transport_sums / transport_sums.sum() * 100
chart_labels = [f"{p:.1f}%" for p in percentages]

# Plot
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts = ax.pie(
    transport_sums, 
    labels=chart_labels, 
    startangle=140, 
    colors=[custom_colors[label] for label in labels]
)
ax.axis('equal')
plt.title("Modal Split zur Hauptsportart (nach Häufigkeit)")

# Legende mit durchschnittlicher Nutzung pro Person
legend_labels = [f"{label}: {val:.1f}x/Woche" for label, val in zip(labels, avg_use_per_person)]
ax.legend(wedges, legend_labels, title="Ø Nutzung pro Person und Woche", loc="center left", bbox_to_anchor=(1, 0.5))

plt.tight_layout()
# plt.show()


##Modalsplit nach Kilometern
# Name der Spalte mit der Distanz zum Trainingsort
distance_column = "Wie lang ist dein durchschnittlicher Weg (in Kilometer) zum Trainingsort deiner Hauptsportart? "

# Sicherstellen, dass keine NaNs in den relevanten Spalten stören
df_cleaned[columns_transport] = df_cleaned[columns_transport].fillna(0)
df_cleaned[distance_column] = df_cleaned[distance_column].fillna(0)

# Multipliziere jede Transportnutzung mit der Distanz → ergibt Kilometer je Verkehrsmittel
km_per_transport = df_cleaned[columns_transport].multiply(df_cleaned[distance_column], axis=0)

# Summiere die Kilometer je Verkehrsmittel
transport_km_sums = km_per_transport.sum()

# Prozentberechnung für Anzeige
total_km = transport_km_sums.sum()
percentages = transport_km_sums / total_km * 100
agv_km_per_person = transport_km_sums / df_cleaned[distance_column].gt(0).sum()

# Labels im Chart: nur Prozent
chart_labels = [f"{p:.1f}%" for p in percentages]

# Plot
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts = ax.pie(
    transport_km_sums, 
    labels=chart_labels, 
    startangle=140, 
    colors=[custom_colors[label] for label in labels]
)
ax.axis('equal')
plt.title("Modal Split zur Hauptsportart (nach Kilometern)")

# Legende mit absoluten Werten
legend_labels = [f"{label}: {km:.1f} km" for label, km in zip(labels, agv_km_per_person)]
ax.legend(wedges, legend_labels, title="Ø zurückgelegte Kilometer pro Person und Woche", loc="center left", bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.show()

