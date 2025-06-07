# Color Psychology Outfit Recommender

def get_user_mood():
    print("Welcome to the Color Psychology Outfit Recommender!")
    print("How are you feeling today? Choose from the moods below:")
    print("Options: happy, sad, angry, stressed, relaxed, energetic, calm, serious, caring")
    mood = input("Enter your mood: ").strip().lower()
    return mood

def recommend_color_and_outfit(mood):
    mood_dict = {
        "happy": {"color": "Yellow", "outfit": "yellow sundress or yellow t-shirt"},
        "sad": {"color": "Green", "outfit": "green hoodie or green sweater"},
        "angry": {"color": "Black", "outfit": "black jacket or black boots"},
        "stressed": {"color": "Blue", "outfit": "blue cardigan or blue jeans"},
        "relaxed": {"color": "Green", "outfit": "green t-shirt or linen shirt"},
        "energetic": {"color": "Red", "outfit": "red sportswear or red sneakers"},
        "calm": {"color": "Blue", "outfit": "blue blouse or blue scarf"},
        "serious": {"color": "Black", "outfit": "black blazer or black dress pants"},
        "caring": {"color": "Pink", "outfit": "pink top or pink sweater"},
    }

    if mood in mood_dict:
        color = mood_dict[mood]["color"]
        outfit = mood_dict[mood]["outfit"]
        print(f"\nYour mood: {mood.capitalize()}")
        print(f"Recommended color: {color}")
        print(f"Suggested outfit: {outfit}")
    else:
        print("\nSorry, we couldn't recognize that mood.")
        print("Please choose a mood from the given options.")

def main():
    mood = get_user_mood()
    recommend_color_and_outfit(mood)

if __name__ == "__main__":
    main()
