# app/utils/helpers.py

def get_color(score):
    if score >= 0.7:
        return [0, 200, 0]   # Green
    elif score >= 0.4:
        return [255, 165, 0] # Orange
    else:
        return [200, 0, 0]   # Red