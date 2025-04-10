import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "inventory_monitoring_cleaned.csv")

try:
    inventory_data = pd.read_csv(file_path)
except FileNotFoundError:
    inventory_data = None


def decide_restock(product_id):
    if inventory_data is None:
        return "⚠️ Inventory data file not found."

    product_data = inventory_data[inventory_data["Product ID"] == int(product_id)]

    if product_data.empty:
        return f"No inventory data found for Product ID {product_id}."

    stock_level = product_data["Stock Levels"].values[0]
    reorder_point = product_data["Reorder Point"].values[0]
    supplier_lead_time = product_data["Supplier Lead Time (days)"].values[0]

    if stock_level < reorder_point:
        return (f"Restock needed for Product {product_id}. "
                f"Lead time is {supplier_lead_time} days.")
    else:
        return f"No restock needed for Product {product_id} (stock level: {stock_level})."
