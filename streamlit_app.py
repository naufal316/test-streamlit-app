import streamlit as st
from metrics import REGIONS, kpis, by_month

REGIONS = ["London", "Manchester", "Birmingham", "Oxford", "Cambridge", "Grimsby"]


st.title("Net revenue")
st.caption("Excludes refunds. Amounts in EUR.")
with st.container(horizontal=True):
    region = st.selectbox("Region", REGIONS)
    quarter = st.segmented_control(
        "Quarter", ["Q1", "Q2", "Q3", "Q4"],
        default="Q3", required=True,
    )
