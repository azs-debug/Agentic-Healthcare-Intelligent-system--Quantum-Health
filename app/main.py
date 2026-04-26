# app/main.py

import streamlit as st
import pydeck as pdk

from utils.data_loader import load_data
from utils.location import get_user_location

from utils.agent_runner import run_agent
from utils.agent_adapter import agent_output_to_df

from components.map_view import render_map
from components.routing import get_route
from components.glassbox import render_glassbox
from components.admin_view import render_admin

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(layout="wide")

# -------------------------
# LOAD DATA (for admin view)
# -------------------------
df_raw = load_data()

mode = st.sidebar.radio("Mode", ["Patient View", "Admin View"])

# =========================================================
# PATIENT VIEW
# =========================================================
if mode == "Patient View":

    st.title("🏥 Geospatial Truth Healthcare System")

    # -------------------------
    # AUTO LOCATION
    # -------------------------
    user_lat, user_lon = get_user_location()
    st.success(f"📍 Location detected: {user_lat:.4f}, {user_lon:.4f}")

    # -------------------------
    # NATURAL LANGUAGE INPUT
    # -------------------------
    query = st.text_input(
        "Describe your condition (e.g., 'ICU bed with ventilator urgently needed')"
    )

    if query:

        # -------------------------
        # RUN AGENT
        # -------------------------
        agent_results = run_agent(query)
        df = agent_output_to_df(agent_results)

        if df.empty:
            st.error("No hospitals found for this query.")
            st.stop()

        # -------------------------
        # SAFETY FIXES
        # -------------------------
        if "rank" not in df.columns:
            df["rank"] = range(1, len(df) + 1)

        if "trust_score" not in df.columns:
            df["trust_score"] = 0.5

        if "crisis_ratio" not in df.columns:
            df["crisis_ratio"] = 0

        if "is_medical_desert" not in df.columns:
            df["is_medical_desert"] = False

        # -------------------------
        # MAP
        # -------------------------
        st.subheader("🗺️ Geospatial Truth Map")
        st.pydeck_chart(render_map(df))

        # -------------------------
        # SELECT HOSPITAL
        # -------------------------
        hospital_name = st.selectbox("Select Hospital", df["name"])
        hospital = df[df["name"] == hospital_name].iloc[0]

        st.markdown("### 🏥 Hospital Details")

        st.write("⭐ Trust Score:", f"{hospital['trust_score']*10:.1f}/10")
        st.write("⚠ Crisis Score:", hospital["crisis_ratio"])
        st.write("📌 Recommendation:", hospital["recommendation"])

        # =====================================================
        # ROUTING (SAFE IMPLEMENTATION)
        # =====================================================
        if hospital["rank"] == 1:

            st.success("🚑 Best Match Hospital (Routing Enabled)")

            if st.button("Show Shortest Route"):

                route = get_route(
                    user_lat,
                    user_lon,
                    hospital["latitude"],
                    hospital["longitude"]
                )

                if not route:
                    st.warning("⚠ Route not available for this hospital.")
                else:
                    route_layer = pdk.Layer(
                        "PathLayer",
                        data=[{"path": route}],
                        get_path="path",
                        get_width=5,
                        get_color=[0, 0, 255],
                    )

                    st.pydeck_chart(
                        pdk.Deck(
                            layers=[route_layer],
                            initial_view_state=pdk.ViewState(
                                latitude=user_lat,
                                longitude=user_lon,
                                zoom=7
                            )
                        )
                    )

        # -------------------------
        # GLASS BOX (EXPLANATION)
        # -------------------------
        render_glassbox(hospital)

        # -------------------------
        # RANKED LIST
        # -------------------------
        st.subheader("🚑 Recommended Hospitals (Ranked)")

        for _, row in df.sort_values("rank").iterrows():

            if row["trust_score"] >= 0.7:
                st.success(f"🟢 {row['name']} — GOLDEN HOUR FACILITY")

            elif row["is_medical_desert"]:
                st.error(f"🔴 {row['name']} — MEDICAL DESERT")

            else:
                st.warning(f"🟡 {row['name']} — Moderate Reliability")

            st.write(f"⭐ Trust Score: {row['trust_score']*10:.1f}/10")
            st.write(f"⚠ Crisis Score: {row['crisis_ratio']}")
            st.write(f"📌 Recommendation: {row['recommendation']}")
            st.markdown("---")

# =========================================================
# ADMIN VIEW
# =========================================================
else:
    st.title("📊 Admin Dashboard — Medical Desert Analytics")

    render_admin(df_raw)