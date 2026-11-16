import streamlit as st
from metrics import REGIONS, kpis, by_month
st.title("Net revenue")
st.caption("Excludes refunds. Amounts in EUR.")
with st.container(horizontal=True):
    region = st.selectbox("Region", REGIONS)
    quarter = st.segmented_control(
        "Quarter", ["Q1", "Q2", "Q3", "Q4"],
        default="Q3", required=True,
    )
k = kpis(region, quarter)
grid = st.grid(3, border=True)
grid.metric("Revenue", k.revenue, k.revenue_delta)
grid.metric("Orders", k.orders, k.orders_delta)
grid.metric("Avg. order", k.aov, k.aov_delta)
st.bar_chart(by_month(region), x="month"
