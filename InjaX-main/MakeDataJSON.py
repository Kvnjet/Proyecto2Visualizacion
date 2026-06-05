import pandas as pd, json

df = pd.read_csv("Student_Mental_health.csv")
df.columns = ["Timestamp","Genero","Edad","Carrera",
              "Ano_Estudio","CGPA","Estado_Civil",
              "Depresion","Ansiedad","Panico","Tratamiento"]
df["CGPA"] = df["CGPA"].str.strip()
df["Ano_Estudio"] = df["Ano_Estudio"].str.lower().str.strip()

print(json.dumps({"data": df.to_dict(orient="records")}, indent=2))