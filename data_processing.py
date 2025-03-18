import pandas as pd
import glob

# Step 1: Read CSV files from data folder
file_paths = glob.glob("data/*.csv")

# Create an empty DataFrame to hold merged data
final_data = pd.DataFrame()

# Step 2: Loop through each file and perform processing
for file_path in file_paths:
    df = pd.read_csv(file_path)

    # Step 3: Filter rows where product is 'pink morsel'
    df = df[df["product"] == "pink morsel"]

    # Step 4: Create new column "sales" by multiplying quantity and price
    df["sales"] = df["quantity"] * df["price"]

    # Step 5: Select only the required columns: sales, date, region
    df = df[["sales", "date", "region"]]

    # Step 6: Append this processed data into final_data
    final_data = pd.concat([final_data, df])

# Step 7: Write the combined data to a single CSV
final_data.to_csv("formatted_sales_data.csv", index=False)

# Confirm completion
print("CSV files successfully combined and processed!")
