import pydeck as pdk


# -------------------------
# COLOR LOGIC
# -------------------------
def compute_color(trust_score, is_medical_desert, rank):

    # 🟢 Best hospital (rank 1)
    if rank == 1:
        return [0, 255, 0]

    # 🔴 Medical desert
    if is_medical_desert:
        return [255, 0, 0]

    # 🟢 High trust
    if trust_score >= 0.7:
        return [0, 200, 0]

    # 🟡 Moderate
    return [255, 165, 0]


# -------------------------
# MAP RENDER FUNCTION
# -------------------------
def render_map(df):

    # -------------------------
    # SAFETY FIXES (NO ERRORS)
    # -------------------------
    if df.empty:
        return pdk.Deck()

    if "latitude" not in df.columns or "longitude" not in df.columns:
        return pdk.Deck()

    if "trust_score" not in df.columns:
        df["trust_score"] = 0.5

    if "is_medical_desert" not in df.columns:
        df["is_medical_desert"] = False

    if "rank" not in df.columns:
        df["rank"] = range(1, len(df) + 1)

    if "name" not in df.columns:
        df["name"] = "Unknown"

    if "crisis_ratio" not in df.columns:
        df["crisis_ratio"] = 0

    if "recommendation" not in df.columns:
        df["recommendation"] = ""

    # -------------------------
    # APPLY COLORS
    # -------------------------
    df["color"] = df.apply(
        lambda x: compute_color(
            x["trust_score"],
            x["is_medical_desert"],
            x["rank"]
        ),
        axis=1
    )

    # -------------------------
    # MAP LAYER
    # -------------------------
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df,
        get_position='[longitude, latitude]',
        get_fill_color='color',
        get_radius=7000,
        pickable=True,
    )

    # -------------------------
    # VIEW STATE
    # -------------------------
    view_state = pdk.ViewState(
        latitude=df["latitude"].mean(),
        longitude=df["longitude"].mean(),
        zoom=6,
        pitch=0,
    )

    # -------------------------
    # TOOLTIP (VERY IMPORTANT)
    # -------------------------
    tooltip = {
        "html": """
        <b>{name}</b><br/>
        ⭐ Trust Score: {trust_score}<br/>
        ⚠ Crisis Score: {crisis_ratio}<br/>
        📌 {recommendation}
        """,
        "style": {
            "backgroundColor": "black",
            "color": "white"
        }
    }

    # -------------------------
    # RETURN MAP
    # -------------------------
    return pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip=tooltip
    )