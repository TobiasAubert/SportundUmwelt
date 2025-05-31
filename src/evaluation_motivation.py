import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Load and clean
df = pd.read_csv("src/results_motivation.csv")
df.columns = df.columns.str.strip().str.replace('"', '')
df['Arithmetic mean'] = df['Arithmetic mean'].astype(float)
df['Standard deviation'] = df['Standard deviation'].astype(float)

# Sort by mean descending
df = df.sort_values('Arithmetic mean', ascending=False).reset_index(drop=True)
x_vals = range(len(df))

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# 1. Bars (background)
ax.bar(
    x_vals,
    df['Arithmetic mean'],
    color='lightgray',
    edgecolor='black',
    width=0.6,
    label='Mittelwert'
)

# 2. Overlay: Points with standard deviation (error bars)
ax.errorbar(
    x_vals,
    df['Arithmetic mean'],
    yerr=df['Standard deviation'],
    fmt='o',
    color='tab:blue',
    capsize=5,
    label='± Standardabweichung'
)

# Formatting
ax.set_xticks(x_vals)
ax.set_xticklabels(df['Motivation'], rotation=45, ha='right')
ax.set_ylabel("Mittelwert\n(1 = nicht wichtig, 5 = sehr wichtig)")
ax.set_ylim(1, 5.5)
ax.set_title("Motivationsfaktoren: Mittelwerte mit Standardabweichung")
ax.grid(True, axis='y')
ax.legend()

plt.tight_layout()
# plt.show()

#------------- obstacles ----------------
df_obstacles = pd.read_csv("src/results_obstacles.csv")

print(df_obstacles.columns)

# Sortieren nach Anzahl Nennungen (optional, für bessere Übersicht)
df_obstacles = df_obstacles.sort_values("Nennungen")

# Balkendiagramm erstellen
plt.figure(figsize=(10, 6))
plt.barh(df_obstacles["Hindernis"], df_obstacles["Nennungen"], color="skyblue")
plt.xlabel("Anzahl Nennungen")
plt.title("Häufigkeit der genannten Hindernisse für nachhaltige Mobilität")
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()