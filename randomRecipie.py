import random

# Define dictionaries of recipes for each dish
recipes = {
    "spaghetti carbonara": {
        "ingredients": ["spaghetti", "bacon", "eggs", "parmesan cheese", "black pepper"],
        "instructions": [
            "Cook spaghetti according to package instructions until al dente.",
            "In a skillet, cook bacon until crispy. Remove bacon from skillet and drain on paper towels, reserving some of the fat.",
            "In a bowl, whisk together eggs, parmesan cheese, and black pepper.",
            "Add cooked spaghetti to the skillet with the reserved bacon fat. Pour egg mixture over spaghetti and toss until well combined and eggs are cooked.",
            "Crumble cooked bacon over the top and serve immediately."
        ]
    },
    "chicken alfredo": {
        "ingredients": ["chicken breast", "fettuccine", "heavy cream", "butter", "garlic", "parmesan cheese", "salt", "black pepper"],
        "instructions": [
            "Season chicken breast with salt and black pepper. Cook chicken in a skillet over medium heat until golden brown and cooked through. Remove from skillet and slice into strips.",
            "In the same skillet, melt butter and sauté minced garlic until fragrant.",
            "Add heavy cream to the skillet and bring to a simmer. Stir in grated parmesan cheese until melted and sauce is smooth.",
            "Cook fettuccine according to package instructions until al dente. Drain pasta and toss with the alfredo sauce.",
            "Top pasta with sliced chicken breast and serve hot."
        ]
    },
    # Add recipes for other dishes here
}

# Additional recipes
additional_recipes = {
    "beef bourguignon": {
        "ingredients": ["beef chuck roast", "bacon", "red wine", "beef broth", "carrots", "onions", "garlic", "mushrooms", "pearl onions", "parsley", "thyme", "bay leaves"],
        "instructions": [
            "Preheat oven to 300°F (150°C).",
            "In a large Dutch oven or oven-safe pot, brown the beef chuck roast in bacon fat over medium-high heat.",
            "Remove the beef from the pot and set aside.",
            "Add the bacon, carrots, onions, and garlic to the pot and cook until softened.",
            "Add the mushrooms and pearl onions and cook until softened.",
            "Add the red wine, beef broth, parsley, thyme, and bay leaves to the pot and bring to a simmer.",
            "Return the beef to the pot and nestle it in the vegetables and liquid.",
            "Cover the pot and braise in the oven for 2-3 hours, or until the beef is fall-apart tender.",
            "Serve over mashed potatoes or egg noodles."
        ]
    },
    "Indian chicken tikka masala": {
        "ingredients": ["boneless, skinless chicken breasts", "plain yogurt", "garam masala", "ground cumin", "ground coriander", "paprika", "cayenne pepper", "ginger-garlic paste", "lemon juice", "vegetable oil", "onions", "bell peppers", "tomatoes", "heavy cream"],
        "instructions": [
            "In a large bowl, combine the chicken breasts, yogurt, garam masala, cumin, coriander, paprika, cayenne pepper, ginger-garlic paste, and lemon juice.",
            "Cover and refrigerate for at least 30 minutes, or up to overnight.",
            "Heat the oil in a large skillet or Dutch oven over medium-high heat.",
            "Add the chicken and cook until browned on all sides.",
            "Remove the chicken from the skillet and set aside.",
            "Add the onions and bell peppers to the skillet and cook until softened.",
            "Add the tomatoes and cook until they start to break down.",
            "Add the chicken back to the skillet and stir to combine.",
            "Add the heavy cream and bring to a simmer.",
            "Serve over rice or naan bread."
        ]
    },
    "pad thai": {
        "ingredients": ["flat rice noodles", "chicken breasts", "shrimp", "eggs", "bean sprouts", "green onions", "cilantro", "peanuts", "fish sauce", "tamarind paste", "red chili peppers", "lime wedges"],
        "instructions": [
            "Soak the rice noodles in warm water for 10 minutes, or until softened.",
            "In a large skillet or wok, heat the oil over medium-high heat.",
            "Add the chicken and shrimp and cook until browned on all sides.",
            "Remove the chicken and shrimp from the skillet and set aside.",
            "Add the eggs to the skillet and cook, stirring constantly, until scrambled.",
            "Add the noodles, bean sprouts, green onions, cilantro, peanuts, fish sauce, tamarind paste, and red chili peppers to the skillet and stir to combine.",
            "Add the chicken and shrimp back to the skillet and stir to combine.",
            "Serve immediately, with lime wedges on the side."
        ]
    },
    # Add more recipes here
}

# Merge additional recipes into the main recipes dictionary
recipes.update(additional_recipes)

def generate_recipe():
    # Choose a random dish
    dish = random.choice(list(recipes.keys()))
    
    print(f"Recipe for {dish.capitalize()}:\n")
    
    # Print ingredients
    print("Ingredients:")
    for ingredient in recipes[dish]["ingredients"]:
        print("- " + ingredient)
    print()
    
    # Print instructions
    print("Instructions:")
    for i, instruction in enumerate(recipes[dish]["instructions"], 1):
        print(f"{i}. {instruction}")
    print()

def ask_user_preference():
    print("Welcome to the Recipe Generator!")
    print("What type of cuisine would you like? (Italian, French, Indian, Thai, etc.)")
    cuisine = input("Enter cuisine type: ").lower()
    
    # Split the cuisine input into individual words
    cuisine_words = cuisine.split()
    
    # Filter recipes based on the presence of cuisine-related keywords in recipe names
    filtered_recipes = {key: value for key, value in recipes.items() if any(word in key.lower() for word in cuisine_words)}
    
    if not filtered_recipes:
        print("Sorry, no recipes found for that cuisine.")
        return
    
    print("\nHere's a random recipe for you:\n")
    generate_recipe()

ask_user_preference()
