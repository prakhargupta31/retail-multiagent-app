import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "inventory_monitoring_cleaned.csv")

try:
    inventory_data = pd.read_csv(file_path)
except FileNotFoundError:
    inventory_data = None

def suggest_instore_action(product_id):
    if inventory_data is None:
        return "⚠️ Inventory data file not found."

    product_data = inventory_data[inventory_data["Product ID"] == int(product_id)]

    if product_data.empty:
        return f"No inventory data found for Product ID {product_id}."

    stock_level = product_data["Stock Levels"].values[0]
    expiry_date = product_data["Expiry Date"].values[0]

    if stock_level < 10:
        return f"⚠️ Low stock for Product {product_id}. Consider restocking."
    elif stock_level > 100:
        return f"📢 Overstock detected for Product {product_id}. Promote sales!"
    else:
        return f"✅ Stock level for Product {product_id} is optimal. Expiry: {expiry_date}"
