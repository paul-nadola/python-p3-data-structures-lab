spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        for key in food.keys():
            if key == 'name':
                names.append(food[key])
    # breakpoint()
    return names



def get_spiciest_foods(spicy_foods):
    spiciest  = []
    for food in spicy_foods:
        for key in food.keys():
            if key == 'heat_level' and food[key] > 5:
                spiciest.append(food)
    # breakpoint()
    return spiciest

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_emojis = "🌶" * heat_level
        if heat_level > 5 :
            print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num_foods = len(spicy_foods)
    
    for food in spicy_foods:
        heat_level = food["heat_level"]
        total_heat_level += heat_level
    return total_heat_level / num_foods
    # if num_foods > 0:
    #     average = total_heat_level / num_foods
    #     return int(average)
    # else:
    #     return 0



def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
