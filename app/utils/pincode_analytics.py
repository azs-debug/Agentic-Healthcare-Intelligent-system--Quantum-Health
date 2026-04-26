import pandas as pd

def compute_pincode_crisis(df):

    # -------------------------
    # SAFETY: unify column name
    # -------------------------
    if "pin_code" not in df.columns:

        if "address_zipOrPostcode" in df.columns:
            df["pin_code"] = df["address_zipOrPostcode"]
        else:
            df["pin_code"] = "UNKNOWN"

    # -------------------------
    # SAFETY: required fields
    # -------------------------
    if "latitude" not in df.columns:
        df["latitude"] = 0

    if "longitude" not in df.columns:
        df["longitude"] = 0

    if "crisis_ratio" not in df.columns:
        df["crisis_ratio"] = 0

    # -------------------------
    # GROUP BY PIN CODE
    # -------------------------
    grouped = df.groupby("pin_code").agg(
        avg_lat=("latitude", "mean"),
        avg_lon=("longitude", "mean"),
        crisis_ratio=("crisis_ratio", "mean"),
        facility_count=("pin_code", "count")
    ).reset_index()

    return grouped