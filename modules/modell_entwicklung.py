# modell_entwicklung.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt

# 1. CSV-Datei einlesen (Pfad ggf. anpassen)
df = pd.read_csv("ml_daten/ml_daten_cab9d20a.csv")
print("Daten geladen:")
print(df.head())

# 2. One-Hot-Encoding für 'landuse_typ' durchführen
if "landuse_typ" in df.columns:
    encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
    landuse_encoded = encoder.fit_transform(df[["landuse_typ"]])
    landuse_df = pd.DataFrame(landuse_encoded, columns=encoder.get_feature_names_out(["landuse_typ"]))
    df = pd.concat([df.drop(columns=["landuse_typ"]), landuse_df], axis=1)

# 3. Features und Ziel trennen
feature_columns = [col for col in df.columns if col != "label"]
X = df[feature_columns]
y = df["label"]

# 4. Trainings- und Testdaten aufteilen
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Modell erstellen und trainieren
modell = DecisionTreeClassifier(random_state=42)
modell.fit(X_train, y_train)

# 6. Vorhersage & Bewertung
y_pred = modell.predict(X_test)

print("\nGenauigkeit:", accuracy_score(y_test, y_pred))
print("\nDetailauswertung:")
print(classification_report(y_test, y_pred))

# 7. Wichtigkeit der Features anzeigen
importances = modell.feature_importances_
features = X.columns

importance_df = pd.DataFrame({"Feature": features, "Wichtigkeit": importances})
importance_df = importance_df.sort_values(by="Wichtigkeit", ascending=False)

print("\nFeature-Wichtigkeiten:")
print(importance_df)

# 8. Visualisierung (optional)
plt.figure(figsize=(10, 6))
plt.barh(importance_df["Feature"], importance_df["Wichtigkeit"])
plt.xlabel("Wichtigkeit")
plt.title("Feature Importance im Decision Tree")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()



