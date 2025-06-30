import pandas as pd

csv_path = "Photo_Metadata_Log.csv"
df = pd.read_csv(csv_path)

df["Viewpoint"] = df["Viewpoint"].replace("Front View", "Front")
df.to_csv(csv_path, index=False)

print("✔️ Replaced 'Front View' with 'Front'")
