import tkinter as tk
from tkinter import ttk, messagebox
import random


mood_to_color = {
    "happy": "Yellow", "sad": "Blue", "relaxed": "Green",
    "angry": "Red", "stressed": "Blue", "calm": "Green",
    "energetic": "Red", "professional": "Black", "caring": "Pink"
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
    "Summer": ["Yellow", "Pink", "White"],
    "Winter": ["Black", "Blue", "Green"],
    "Spring": ["Green", "Pink", "Yellow"],
    "Fall": ["Red", "Orange", "Brown"]
}


def recommend_outfit():
    mood = mood_var.get().strip().lower()
    extra = extra_var.get().strip().lower()
    style = style_var.get()
    season = season_var.get()

    color = mood_to_color.get(mood)
    if not color and extra:
        for word in reversed(extra.split()):
            if word in mood_to_color:
                color = mood_to_color[word]
                break
    if not color:
        color = "Default"

    if season in seasonal_colors and color != "Default":
        if color not in seasonal_colors[season]:
            color = random.choice(seasonal_colors[season])

    items = color_to_outfits.get(color, color_to_outfits["Default"])
    if style == "Formal":
        Formal_items = [i for i in items if any(k in i.lower() for k in ["blazer", "dress", "slacks", "blouse"])]
        outfit = random.choice(Formal_items if Formal_items else items)
    else:
        outfit = random.choice(items)

    output.set(f"Suggested color: {color}\nRecommended outfit: {outfit}")
    if mood not in mood_to_color:
        messagebox.showinfo("Tip", "Try a simpler mood like 'happy', 'calm', or 'stressed'.")

# GUI 
root = tk.Tk()
root.title("Mood-Based Outfit Recommender")
root.geometry("460x400")
root.resizable(False, False)
root.configure(bg="#f9f9f9")

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

ttk.Label(main_frame, text="Mood-Based Outfit Recommender", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)


def create_labeled_input(row, text, variable, is_combo=False, options=None):
    ttk.Label(main_frame, text=text, font=("Helvetica", 10, "bold")).grid(row=row, column=0, sticky="w", padx=(0, 10), pady=5)
    if is_combo:
        entry = ttk.Combobox(main_frame, textvariable=variable, values=options, state="readonly", width=30)
    else:
        entry = ttk.Entry(main_frame, textvariable=variable, width=32)
    entry.grid(row=row, column=1, pady=5)
    return entry


mood_var = tk.StringVar()
extra_var = tk.StringVar()
style_var = tk.StringVar(value="Casual")
season_var = tk.StringVar(value="Summer")


create_labeled_input(1, "Your Current Mood:", mood_var)
create_labeled_input(2, "Additional Feelings (Optional):", extra_var)
create_labeled_input(3, "Style Preference:", style_var, is_combo=True, options=["Casual", "Formal"])
create_labeled_input(4, "Current Season:", season_var, is_combo=True, options=["Summer", "Fall", "Winter", "Spring"])


ttk.Button(main_frame, text="Show Outfit Suggestion", command=recommend_outfit).grid(row=5, column=0, columnspan=2, pady=20)


output = tk.StringVar()
ttk.Label(main_frame, textvariable=output, background="#e6e6e6", padding=10, relief="groove", anchor="center", wraplength=400, justify="center").grid(row=6, column=0, columnspan=2, pady=(0, 10), sticky="we")

root.mainloop()