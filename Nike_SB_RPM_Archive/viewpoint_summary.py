import csv
from collections import Counter

# Step 1: Load the metadata CSV
with open("Photo_Metadata_Log.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    # Step 2: Extract viewpoint values from the file
    viewpoints = [row["Viewpoint"] for row in reader]

# Step 3: Count frequency of each viewpoint
counts = Counter(viewpoints)

# Step 4: Print results
print("📊 Viewpoint Summary:\n")
for viewpoint, count in counts.items():
    print(f"{viewpoint}: {count}")
