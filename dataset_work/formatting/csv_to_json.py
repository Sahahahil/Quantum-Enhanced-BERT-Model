import pandas as pd
import json

csv_file = "dataset.csv"
json_file = "dataset.json"

# Read CSV
df = pd.read_csv(csv_file)

# Convert to list of dictionaries
data = df.to_dict(orient="records")

# Save JSON
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Saved JSON to: {json_file}")
print(f"Rows: {len(data)}")
