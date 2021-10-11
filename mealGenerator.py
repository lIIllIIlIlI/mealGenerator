import random

meals = {
    "sandwich": [
        ["Vollkornbroetchen", "Vollkorntoast", "Dinkelbrot"],
        ["Mayonnaise", "Senf", "Tomatenmark", "Olivenoel", "BBQ soße", "Frischkäse", "Ziegenkäse", "Sambal oleg
k"],
        ["Tomaten", "Gurken", "Ruccola", "Paprika", "Avocado", "Zwiebeln"],
        ["Putenbrust", "Scheibenkäse", "Schinken", "Thunfisch", "Mozarella", "Gernelen"],
        ["Salz"],
        ["Pfeffer"],
        ["Zitrone"]
        ],
    "Smoothie_Gruen": [
        ["Spinat", "Gurke", "Ruccola", "Avocado", "Basilikum"],
        ["Apfel", "Kiwi", "Birne", "Blaubeeren"],
        ["Bannane", "Datteln"],
        ["Chia Samen", "Makadamia Nüsse", "Wallnüsse", "Ingwer", "Kresse"],
        ["Süßstoff"],
        ["Wasser", "Milch", "Kokosmilch"],
        ["Zitrone"],
        ["Eiswuerfel"]
        ],
    "Smoothie_Rot": [
        ["Himbeeren", "Blaubeeren", "Beerenmischung", "Orange", "Granatapfel", "Brombeeren", "Erdbeeren"],
        ["Bannane", "Apfel", "Rote beete", "Karotte", "Pflaume", "Papaya", "Rettich"],
        ["Chia Samen", "Makadamia Nüsse", "Wallnüsse", "Ingwer", "Minze", "Kokosnuss raspeln", "kurkuma"],
        ["Süßstoff"],
        ["Wasser", "Milch", "Kokosmilch"],
        ["Zitrone"],
        ["Eiswuerfel"]
        ],
    "Bowl": [
        ["Hähnchen", "Tofu", "Steak", "Fisch", "Entenbrust"],
        ["Gegrillte Zucchini", "Gegrillte Paprika", "Gegrillte Karotten", "Gebratener Spargel", "Gegrillte Pilze"],
        ["Vollkorn Nudeln", "Reis", "Süßkartoffeln", "Quinoa"],
        ["Mango", "Erdbeeren", "Blaubeeren", "Papaya", "Apfel"],
        ["Tomaten", "Avocado", "Eier", "Garnelen", "Gurke", "Brokkoli", "Radieschen", "Mais", "Kaiserschoten"],
        ["Koriander", "Basilikum", "Kresse", "Chia Samen", "Sesam", "Erdnüsse"],
        ["Senfsoße", "Thini soße", "Dairy soße", "Vinaigrette soße", "Pesto soße", "Fruchtige soße"],
        ],
    "Salat": [
        ["Vollkornbrötchen", "Nudeln", "Quinoa", "Reis"],
        ["Ruccola", "Salatblaetter", "Rettich"],
        ["Karotten", "Kresse", "Gurke", "Croutons", "Zucchini", "Paprika", "Apfel", "Kresse"],
        ["Mozarella", "Avocado", "Tomaten", "Reis", "Nudeln", "Oliven"],
        ["Wassermelone", "Cottage cheese", "Bacon", "Eingelegte Gurken", "Himbeeren", "Orange"],
        ["Eier", "Thunisch", "Chicken", "Steak", "Tofu"],
        ["Senfsoße", "Thini soße", "Dairy soße", "Vinaigrette soße", "Pesto soße", "Fruchtige soße"],
        ],
    "Risotto": [
        [],
    ],
    "Muesli": [
        [],
    ],
    "Wok": [
        [],
    ],
    "Wraps": [
        [],
    ],
}

generatedMeals = {}

for meal in meals:
    generatedMeal = []
    for ingredientType in meals[meal]:
        if ingredientType:
            selectedIngredient = random.choice(ingredientType)
            generatedMeal.append(selectedIngredient)
    generatedMeals.update({meal: generatedMeal})

print("\n\n             *** Generated meals ***")
for name, ingredients in generatedMeals.items():
    print("{} : {}".format(name, ingredients))
print("\n\n")
