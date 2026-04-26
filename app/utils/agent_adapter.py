import pandas as pd

def agent_output_to_df(agent_results):

    rows = []

    for item in agent_results:

        rows.append({
            "name": item["facility"],
            "latitude": item["coords"]["lat"],
            "longitude": item["coords"]["long"],
            "trust_score": item["trust_score"] / 10,  # normalize (0–1)
            "crisis_ratio": item["crisis_score"],
            "recommendation": item["recommendation"],
            "is_medical_desert": "*** MEDICAL DESERT ***" in item.get("label", ""),
            "truth_gap_notes": item["truth_gap_notes"],
            "rank": item["rank_in_results"]
        })

    return pd.DataFrame(rows)