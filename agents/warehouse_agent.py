import pandas as pd
import os

def prioritize_store_fulfillment(store_id, product_id):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'inventory_monitoring_cleaned.csv')

    try:
        inventory_data = pd.read_csv(file_path)
    except FileNotFoundError:
        return "⚠️ Inventory data file not found."

    match = inventory_data[
        (inventory_data['Store ID'] == store_id) &
        (inventory_data['Product ID'] == product_id)
    ]

    if not match.empty:
        stock = match.iloc[0]['Stock Levels']
        reorder_point = match.iloc[0]['Reorder Point']
        supplier_lead_time = match.iloc[0]['Supplier Lead Time (days)']
        if stock < reorder_point:
            return f"🛒 Prioritize Store {store_id}: Reorder Product {product_id} (Stock low: {stock})"
        else:
            return f"✅ Store {store_id} has sufficient stock for Product {product_id} (Stock: {stock})"
    else:
        return "ℹ️ Product not found in inventory for this store."
