import requests

# Your HERE API key
HERE_API_KEY = "0c1Ca68_mhEPNQzRVgDMhu5AqmCry1ytvGdmv3YCwzA"

def print_full_route(current_lat, current_lng, dest_lat, dest_lng):
    """Fetch and print all directions from HERE API."""
    
    # Construct API URL
    url = (
        f"https://router.hereapi.com/v8/routes?"
        f"transportMode=scooter"
        f"&origin={current_lat},{current_lng}"
        f"&destination={dest_lat},{dest_lng}"
        f"&return=polyline,actions,instructions"
        f"&apiKey={HERE_API_KEY}"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "routes" in data and len(data["routes"]) > 0:
            sections = data["routes"][0]["sections"]
            print("? Full Route Directions:\n")
            step_num = 1
            for section in sections:
                if "actions" in section:
                    for action in section["actions"]:
                        instruction = action.get("instruction", "Continue")
                        street = action.get("roadName", "")
                        full_text = f"?? Step {step_num}: {instruction}"
                        if street:
                            full_text += f" on {street}"
                        print(full_text)
                        step_num += 1
        else:
            print("? No route found.")
    else:
        print("? Failed to fetch directions:", response.status_code)


# === Example Usage ===
current_lat = 22.3674523
current_lng = 70.7974323
dest_lat = 22.3089935
dest_lng = 70.8007054

print_full_route(current_lat, current_lng, dest_lat, dest_lng)
