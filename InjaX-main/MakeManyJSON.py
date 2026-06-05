import pandas as pd
import json
import os


df = pd.read_csv("Student_Mental_health.csv")
df.columns = ["Timestamp","Genero","Edad","Carrera",
              "Ano_Estudio","CGPA","Estado_Civil",
              "Depresion","Ansiedad","Panico","Tratamiento"]
df["CGPA"]       = df["CGPA"].str.strip()
df["Ano_Estudio"] = df["Ano_Estudio"].str.lower().str.strip()

os.makedirs("data", exist_ok=True)

cgpa_order  = ["0 - 1.99","2.00 - 2.49","2.50 - 2.99","3.00 - 3.49","3.50 - 4.00"]
colors_u2   = ["#F1B972","#FED8B1","#FDAE44","#E77D22","#D16002"]
cgpa_num    = {"0 - 1.99":1,"2.00 - 2.49":2,"2.50 - 2.99":3,"3.00 - 3.49":4,"3.50 - 4.00":5}
years       = [("year 1","Año 1"),("year 2","Año 2"),("year 3","Año 3"),("year 4","Año 4")]
total       = len(df)

# ------ U1: Distribución de Depresión ------
u1 = {"data": [
    {
        "Depresion": "No",
        "Cantidad":  int((df["Depresion"] == "No").sum()),
        "Etiqueta":  f'{round((df["Depresion"] == "No").mean() * 100, 1)}%'
    },
    {
        "Depresion": "Si",
        "Cantidad":  int((df["Depresion"] == "Yes").sum()),
        "Etiqueta":  f'{round((df["Depresion"] == "Yes").mean() * 100, 1)}%'
    }
]}
with open("data/u1_depresion.json", "w", encoding="utf-8") as f:
    json.dump(u1, f, indent=2, ensure_ascii=False)
print("[OK] data/u1_depresion.json")

# ------ U2: Distribución por CGPA ------
u2 = {"data": [
    {"CGPA": c, "Cantidad": int((df["CGPA"] == c).sum()), "Color": colors_u2[i]}
    for i, c in enumerate(cgpa_order)
]}
with open("data/u2_cgpa.json", "w", encoding="utf-8") as f:
    json.dump(u2, f, indent=2, ensure_ascii=False)
print("[OK] data/u2_cgpa.json")

# ------ U3: Distribución por Género (pie) ------
u3 = {"data": [
    {
        "Genero":     g,
        "Cantidad":   int((df["Genero"] == g).sum()),
        "Porcentaje": round((df["Genero"] == g).mean() * 100, 1),
        "Color":      "#DC9DDD" if g == "Female" else "#4682B4"
    }
    for g in ["Female", "Male"]
]}
with open("data/u3_genero.json", "w", encoding="utf-8") as f:
    json.dump(u3, f, indent=2, ensure_ascii=False)
print("[OK] data/u3_genero.json")

# ------ Bi1: CGPA vs Depresión (barras agrupadas) ------
bi1 = {"data": []}
for c in cgpa_order:
    sub = df[df["CGPA"] == c]
    bi1["data"].append({
        "CGPA":    c,
        "CantNo":  int((sub["Depresion"] == "No").sum()),
        "CantYes": int((sub["Depresion"] == "Yes").sum())
    })
with open("data/bi1_cgpa_dep.json", "w", encoding="utf-8") as f:
    json.dump(bi1, f, indent=2, ensure_ascii=False)
print("[OK] data/bi1_cgpa_dep.json")

# ------ Bi2: Ansiedad vs Año de Estudio (barras agrupadas) ------
bi2 = {"data": []}
for yr, label in years:
    sub = df[df["Ano_Estudio"] == yr]
    bi2["data"].append({
        "Anio":    label,
        "CantNo":  int((sub["Ansiedad"] == "No").sum()),
        "CantYes": int((sub["Ansiedad"] == "Yes").sum())
    })
with open("data/bi2_ansiedad_anio.json", "w", encoding="utf-8") as f:
    json.dump(bi2, f, indent=2, ensure_ascii=False)
print("[OK] data/bi2_ansiedad_anio.json")

# ------ Bi3: Depresión por Género (apilado 100%) ------
bi3 = {"data": []}
for g in ["Female", "Male"]:
    sub = df[df["Genero"] == g]
    t = len(sub)
    bi3["data"].append({
        "Genero": g,
        "PctYes": round((sub["Depresion"] == "Yes").sum() / t * 100, 1),
        "PctNo":  round((sub["Depresion"] == "No").sum()  / t * 100, 1)
    })
with open("data/bi3_dep_genero.json", "w", encoding="utf-8") as f:
    json.dump(bi3, f, indent=2, ensure_ascii=False)
print("[OK] data/bi3_dep_genero.json")

# ------ Multi: Coordenadas paralelas (un registro por estudiante) ------
multi = {"data": []}
for _, row in df.iterrows():
    edad = int(row["Edad"]) if pd.notna(row["Edad"]) else 20
    multi["data"].append({
        "Edad":        edad,
        "CGPA_val":    cgpa_num.get(row["CGPA"], 3),
        "Depresion":   1 if row["Depresion"]   == "Yes" else 0,
        "Ansiedad":    1 if row["Ansiedad"]    == "Yes" else 0,
        "Panico":      1 if row["Panico"]      == "Yes" else 0,
        "Tratamiento": 1 if row["Tratamiento"] == "Yes" else 0,
        "Color":       "#2D68C4" if row["Depresion"] == "Yes" else "#F4C430",
        "Opacity":     "0.7"    if row["Depresion"] == "Yes" else "0.4"
    })
with open("data/multi_paralelas.json", "w", encoding="utf-8") as f:
    json.dump(multi, f, indent=2, ensure_ascii=False)
print("[OK] data/multi_paralelas.json")

# ------ Facetas: Condiciones por Género (apilado 100%) ------
facets = {"data": []}
for g, label in [("Female", "Mujeres"), ("Male", "Hombres")]:
    sub = df[df["Genero"] == g]
    t = len(sub)
    for cond in ["Ansiedad", "Depresion", "Panico"]:
        facets["data"].append({
            "Genero":    label,
            "Condicion": cond,
            "PctYes":    round((sub[cond] == "Yes").sum() / t * 100, 1),
            "PctNo":     round((sub[cond] == "No").sum()  / t * 100, 1)
        })
with open("data/facets_genero.json", "w", encoding="utf-8") as f:
    json.dump(facets, f, indent=2, ensure_ascii=False)
print("[OK] data/facets_genero.json")

print("\nListo. Todos los JSON generados en ./data/")