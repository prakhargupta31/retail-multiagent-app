import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "pricing_optimization_cleaned.csv")

try:
    pricing_data = pd.read_csv(file_path)
except FileNotFoundError:
    pricing_data = None

def simulate_feedback(product_id):
    if pricing_data is None:
        return "⚠️ Pricing data file not found."

    product_data = pricing_data[pricing_data["Product ID"] == int(product_id)]

    if product_data.empty:
        return f"No pricing data found for Product ID {product_id}."

    review_score = product_data["Customer Reviews"].values[0]
    return_rate = product_data["Return Rate (%)"].values[0]

    if review_score < 3.0:
        return f"❌ Negative feedback detected (Rating: {review_score}). Investigate quality."
    elif return_rate > 20:
        return f"⚠️ High return rate ({return_rate}%). Consider product improvements."
    else:
        return f"✅ Positive customer feedback (Rating: {review_score}). Low returns."
