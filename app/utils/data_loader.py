import pandas as pd
import os

def load_data():

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(base_dir, "data", "engineered_data.csv")

    df = pd.read_csv(file_path)

    # -----------------------------
    # TRUST SCORE
    # -----------------------------
    if "trust_score" not in df.columns:
        df["trust_score"] = 0.5

    # -----------------------------
    # TRUTH GAP
    # -----------------------------
    df["truth_gap"] = (1 - df["trust_score"]) * 10

    # -----------------------------
    # POPULATION DENSITY (fallback)
    # -----------------------------
    if "population_density" not in df.columns:
        df["population_density"] = 50000

    # -----------------------------
    # FACILITY CAPABILITY
    # -----------------------------
    df["facility_capability"] = df["trust_score"] * 100 + 1

    # -----------------------------
    # CRISIS RATIO (ADMIN VIEW)
    # -----------------------------
    df["crisis_ratio"] = df["population_density"] / df["facility_capability"]

    return df