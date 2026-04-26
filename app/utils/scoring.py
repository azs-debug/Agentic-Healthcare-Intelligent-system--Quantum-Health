def compute_color(trust_score, truth_gap):
    """
    Green = high trust, low gap
    Red = low trust, high gap
    """

    if trust_score >= 0.7 and truth_gap < 3:
        return [0, 200, 0]   # GREEN (verified)
    elif trust_score >= 0.4:
        return [255, 165, 0] # ORANGE (moderate)
    else:
        return [200, 0, 0]   # RED (risk)