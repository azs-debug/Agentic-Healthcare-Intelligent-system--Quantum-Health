import requests

def get_route(user_lat, user_lon, hosp_lat, hosp_lon):

    try:
        url = f"http://router.project-osrm.org/route/v1/driving/{user_lon},{user_lat};{hosp_lon},{hosp_lat}?overview=full&geometries=geojson"

        res = requests.get(url, timeout=10).json()

        # -------------------------
        # SAFETY CHECK 1
        # -------------------------
        if "routes" not in res:
            return []

        if len(res["routes"]) == 0:
            return []

        # -------------------------
        # RETURN ROUTE COORDINATES
        # -------------------------
        return res["routes"][0]["geometry"]["coordinates"]

    except Exception as e:
        print("Routing error:", e)
        return []