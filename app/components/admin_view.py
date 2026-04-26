# app/components/admin_view.py

import streamlit as st

from utils.pincode_analytics import compute_pincode_crisis
from utils.pincode_heatmap import render_pincode_heatmap


def render_admin(df):

    st.subheader("📊 Medical Desert (PIN Code Crisis Map)")

    # ---------------------------
    # SAFETY CHECK
    # ---------------------------
    if df.empty:
        st.warning("No data available for admin view.")
        return

    # ---------------------------
    # COMPUTE PINCODE ANALYTICS
    # ---------------------------
    pincode_df = compute_pincode_crisis(df)

    if pincode_df.empty:
        st.warning("No PIN code aggregation available.")
        return

    # ---------------------------
    # HEATMAP VISUALIZATION
    # ---------------------------
    st.pydeck_chart(render_pincode_heatmap(pincode_df))

    # ---------------------------
    # HIGH RISK AREAS TABLE
    # ---------------------------
    st.subheader("🚨 High Risk PIN Codes")

    if "crisis_ratio" not in pincode_df.columns:
        st.error("crisis_ratio missing in dataset")
        return

    high_risk = (
        pincode_df
        .sort_values("crisis_ratio", ascending=False)
        .head(10)
    )

    st.dataframe(high_risk)