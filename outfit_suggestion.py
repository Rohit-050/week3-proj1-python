import random

mood_to_color = {
    "happy": "Yellow",
    "sad": "Blue",
    "relaxed": "Green",
    "angry": "Red",
    "stressed": "Blue",
    "calm": "Green",
    "energetic": "Red",
    "professional": "Black",
    "caring": "Pink"
}

color_to_outfits = {
    "Red": ["Red hoodie", "Red blouse", "Red sneakers"],
    "Blue": ["Blue jeans", "Blue cardigan", "Blue shirt"],
    "Yellow": ["Yellow sundress", "Yellow polo", "Yellow flats"],
    "Green": ["Green t-shirt", "Green jacket", "Green pants"],
    "Black": ["Black blazer", "Black slacks", "Black dress"],
    "Pink": ["Pink top", "Pink skirt", "Pink sneakers"],
    "Default": ["Gray hoodie", "White tee", "Neutral trousers"]
}


seasonal_colors = {
    "summer": ["Yellow", "Pink", "White"],
    "winter": ["Black", "Blue", "Green"],
    "spring": ["Green", "Pink", "Yellow"],
    "fall": ["Red", "Orange", "Brown"]
}

def get_user_input():
    print(" ")
    print("==================================================")
    print("          Mood-Based Outfit Recommender")
    print("==================================================")
    print(" ")
    mood = input("→ What's your current mood? (e.g., happy, stressed) : ").strip().lower()
    detail = input("→ Any additional feelings? (Optional) : ").strip().lower()
    style = input("→ Do you prefer casual or formal wear? (casual/formal) : ").strip().lower()
    season = input("→ What season is it currently? (summer/fall/winter/spring) : ").strip().lower()
    return mood, detail, style, season

def choose_color(mood, detail, season):
    color = mood_to_color.get(mood)

    if not color and detail:
        for word in reversed(detail.split()):
            if word in mood_to_color:
                color = mood_to_color[word]
                break

    if not color:
        color = "Default"

    # Modify based on season
    if season in seasonal_colors and color != "Default":
        if color not in seasonal_colors[season]:
            color = random.choice(seasonal_colors[season])

    return color

def choose_outfit(color, style):
    items = color_to_outfits.get(color, color_to_outfits["Default"])
    if style == "formal":
        formal_items = [i for i in items if any(keyword in i.lower() for keyword in ["blazer", "dress", "slacks", "blouse"])]
        if formal_items:
            return random.choice(formal_items)
    return random.choice(items)

def recommend():
    mood, detail, style, season = get_user_input()
    color = choose_color(mood, detail, season)
    outfit = choose_outfit(color, style)
    print(" ")
    print("--------------------------------------------------")
    print("         Your Personalized Recommendation         ")
    print("--------------------------------------------------")
    print(f"• Mood detected: {mood.capitalize() or 'Unknown'}")
    print(f"• Season considered: {season.capitalize() or 'Unknown'}")
    print(f"• Suggested color: {color}")
    print(f"• Recommended outfit: {outfit}")
    print("--------------------------------------------------")

    if mood not in mood_to_color:
        print("Note: The mood you entered is not in the list of recognized moods. Try using a simpler term next time.")
    print(" ")

if __name__ == "__main__":
    while True:
        recommend()
        again = input("Would you like another recommendation? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nThanks for using the Mood-Based Outfit Recommender!")
            print("Stay stylish and have a great day!")
            print(" ")
            break