import os
import pandas as pd
csv_path = 'notebook/data/stud.csv'

if not os.path.exists(csv_path):
    print(f"Error: File not found at {csv_path}")
else:
    df = pd.read_csv(csv_path)
    print("CSV file loaded successfully!")
