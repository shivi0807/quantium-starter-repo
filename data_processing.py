import pandas as pd
import os

data_dir = 'data/'
files = [file for file in os.listdir(data_dir) if file.endswith('.csv')]

combined_df = pd.concat([pd.read_csv(os.path.join(data_dir, file)) for file in files])

# Keep only Pink Morsel data
filtered_df = combined_df[combined_df['product'].str.lower() == 'pink morsel'].copy()

# Clean price and convert to numeric
filtered_df['price'] = filtered_df['price'].replace('[\$,]', '', regex=True).astype(float)

# Calculate sales
filtered_df['sales'] = filtered_df['quantity'] * filtered_df['price']

# Keep only relevant fields
final_df = filtered_df[['sales', 'date', 'region']]

# Save correctly formatted data inside data folder
final_df.to_csv('data/formatted_sales_data.csv', index=False)

print("Correctly formatted file created at: data/formatted_sales_data.csv")
