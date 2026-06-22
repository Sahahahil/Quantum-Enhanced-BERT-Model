import json
import pandas as pd

json_file = "dataset.json"
csv_file = "dataset.csv"

# Load JSON
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv(csv_file, index=False, encoding="utf-8-sig")

print(f"Saved CSV to: {csv_file}")
print(f"Rows: {len(df)}")
