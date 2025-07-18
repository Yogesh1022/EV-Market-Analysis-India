import pandas as pd

# Load the two CSV files
df1 = pd.read_csv(r'EV_India_2014-2025_MarketData.csv')
df2 = pd.read_csv(r'EV_Maker_by_Place.csv')

# Merge them by stacking (one below the other)
merged_df = pd.concat([df1, df2], ignore_index=True)

# Save to a new CSV file
merged_df.to_csv('geographical_data.csv', index=False)

print("CSV files merged successfully!")
