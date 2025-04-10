import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "pricing_optimization_cleaned.csv")

try:
    pricing_data = pd.read_csv(file_path)
except FileNotFoundError:
    pricing_data = None


def suggest_discount(store_id):
    if pricing_data is None:
        return "⚠️ Pricing data file not found."

    store_data = pricing_data[pricing_data["Store ID"] == int(store_id)]

    if store_data.empty:
        return f"No pricing data found for Store ID {store_id}. column not present in csv file"

    avg_elasticity = store_data["Elasticity Index"].mean()

    if avg_elasticity > 1.2:
        return f"High elasticity detected. Suggested discount: 15%"
    elif avg_elasticity > 0.8:
        return f"Moderate elasticity detected. Suggested discount: 10%"
    else:
        return f"Low elasticity detected. Suggested discount: 5%"
