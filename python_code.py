"""
Seasonal Crop Advisor - Single File Module

This script provides crop suggestions based on the season provided by the user.
It consolidates the data, utility, and main application logic into one file
for simplified execution, while maintaining clear functional separation internally.
"""

import sys

# --- Data Module (Replaces data.py) ---
def get_default_crop_data():
    """
    Defines the core dataset of crops organized by season. 
    Returns:
        dict: A dictionary mapping season names (lowercase) to lists of suggested crops.
    """
    # Note: These suggestions are general and may vary based on specific climate and region.
    return {
        "spring": [
            "Lettuce (Leafy Greens)",
            "Peas",
            "Radishes",
            "Spinach",
            "Broccoli (starting indoors)",
            "Potatoes",
        ],
        "summer": [
            "Tomatoes",
            "Peppers (Bell and Chili)",
            "Zucchini and Squash",
            "Corn",
            "Cucumbers",
            "Beans (Pole and Bush)",
            "Eggplant",
        ],
        "autumn": [
            "Kale",
            "Carrots",
            "Garlic (for overwintering)",
            "Pumpkins and Winter Squash",
            "Cabbage",
            "Beets",
        ],
        "winter": [
            "Brussels Sprouts",
            "Leeks",
            "Hardier varieties of Kale and Spinach (Under cover)",
            "Harvesting overwintered Garlic",
            "Cover Crops (e.g., Rye)",
        ]
    }

# --- Utility Module (Replaces utils.py) ---
def suggest_crops(season, crop_data):
    """
    Looks up and prints crop suggestions for the given season.

    Args:
        season (str): The season entered by the user.
        crop_data (dict): The dictionary containing seasonal crop mappings.
    """
    # Convert input to lowercase for case-insensitive matching and lookup
    season_key = season.lower()
    
    if season_key in crop_data:
        print(f"\n---  Crop Suggestions for {season.capitalize()}  ---")
        suggestions = crop_data[season_key]
        for i, crop in enumerate(suggestions, 1):
            print(f"  {i}. {crop}")
        print("-" * 45)
    else:
        # Error handling for invalid season input
        print(f"\n Error: '{season}' is not a recognized season.")
        print("Please ensure you enter one of the following: Spring, Summer, Autumn, or Winter.")

# --- Main Application Logic (Replaces main.py) ---
def main():
    """
    Main entry point for the Seasonal Crop Advisor application.
    Loads data and runs the suggestion loop.
    """
    try:
        # 1. Load the data structure
        crop_data = get_default_crop_data()
        
        print(" Welcome to the Single-File Seasonal Crop Advisor! ")
        print("Available seasons: Spring, Summer, Autumn, Winter.")
        
        # 2. Continuous loop for user interaction
        while True:
            # Use sys.stdin.readline for robust input handling in different environments
            user_input = input("\nEnter the current season (or type 'exit'): ").strip()
            
            if user_input.lower() == 'exit':
                print("Thank you for using the Crop Advisor. Happy gardening!")
                break
            
            if not user_input:
                print("Please enter a season or 'exit'.")
                continue
                
            # 3. Process and display suggestions
            suggest_crops(user_input, crop_data)
            
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
