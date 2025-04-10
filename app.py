import streamlit as st

from agents.pricing_agent import suggest_discount
from agents.warehouse_agent import prioritize_store_fulfillment
from agents.supplier_agent import decide_restock
from agents.store_agent import suggest_instore_action
from agents.customer_agent import simulate_feedback

st.title("🧠 Retail Multi-Agent System Dashboard")

store_id = st.text_input("Enter Store ID", "")
product_id = st.text_input("Enter Product ID", "")

if store_id and product_id:
    store_id = int(store_id)
    product_id = int(product_id)

    st.subheader("🟡 Pricing Agent")
    st.text(suggest_discount(product_id))

    st.subheader("🔵 Warehouse Agent")
    st.text(prioritize_store_fulfillment(store_id, product_id))

    st.subheader("🟣 Supplier Agent")
    st.text(decide_restock(product_id))

    st.subheader("🟠 Store Agent")
    st.text(suggest_instore_action(product_id))

    st.subheader("🟢 Customer Agent")
    st.text(simulate_feedback(product_id))
