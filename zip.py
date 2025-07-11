import pandas as pd
import os

folder = "archive"  # folder where your extracted files are

# Loop through files and convert JSON/XLSX to CSV
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    if filename.endswith(".json"):
        df = pd.read_json(file_path)
        df.to_csv(file_path.replace(".json", ".csv"), index=False)
        print(f"Converted {filename} to CSV.")

    elif filename.endswith(".xlsx"):
        df = pd.read_excel(file_path)
        df.to_csv(file_path.replace(".xlsx", ".csv"), index=False)
        print(f"Converted {filename} to CSV.")

    elif filename.endswith(".csv"):
        print(f"{filename} is already a CSV.")

    else:
        print(f"Unsupported file type: {filename}")
