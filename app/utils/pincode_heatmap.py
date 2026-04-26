import pydeck as pdk

def render_pincode_heatmap(pincode_df):

    layer = pdk.Layer(
        "HeatmapLayer",
        data=pincode_df,
        get_position='[avg_lon, avg_lat]',
        get_weight='crisis_ratio',
        radiusPixels=80
    )

    view_state = pdk.ViewState(
        latitude=pincode_df["avg_lat"].mean(),
        longitude=pincode_df["avg_lon"].mean(),
        zoom=6
    )

    return pdk.Deck(
        layers=[layer],
        initial_view_state=view_state
    )