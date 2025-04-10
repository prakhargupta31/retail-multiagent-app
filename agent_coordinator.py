from agents.pricing_agent import suggest_discount
from agents.warehouse_agent import prioritize_store_fulfillment
from agents.supplier_agent import decide_restock
from agents.store_agent import suggest_instore_action
from agents.customer_agent import simulate_feedback

def simulate_system():
    print("🧠 Starting LLM-enhanced Retail Agent Simulation\n")

    # --------- Pricing Agent ---------
    print("🟡 Pricing Agent:")
    pricing_output = suggest_discount(store_id=77, product_id=2068)
    print(pricing_output)

    # --------- Warehouse Agent ---------
    print("\n🔵 Warehouse Agent:")
    warehouse_output = prioritize_store_fulfillment(product_id=2605)
    print(warehouse_output)

    # --------- Supplier Agent ---------
    print("\n🟣 Supplier Agent:")
    supplier_output = decide_restock(product_id=2605, warehouse_id=999)  # Replace 999 with actual warehouse ID if needed
    print(supplier_output)

    # --------- Store Agent ---------
    print("\n🟠 Store Agent:")
    store_output = suggest_instore_action(store_id=60, product_id=2605)
    print(store_output)

    # --------- Customer Agent ---------
    print("\n🟢 Customer Agent:")
    customer_output = simulate_feedback(store_id=77, product_id=2068)
    print(customer_output)

    print("\n✅ Simulation Complete.")

if __name__ == "__main__":
    simulate_system()
