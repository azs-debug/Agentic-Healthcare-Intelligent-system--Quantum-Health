import streamlit as st

def render_glassbox(hospital):

    st.subheader("🔍 Glass Box AI")

    st.info("🧠 Reasoning Trace")
    st.write(hospital["recommendation"])

    st.warning("⚖️ Truth Gap")
    st.write(hospital["truth_gap_notes"])