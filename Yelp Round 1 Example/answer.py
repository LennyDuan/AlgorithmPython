# <-- EXPAND to see the data classes
import fileinput


class Meal(object):
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients


def get_unique_meal_count(meals):
    res = set()
    for meal in meals:
        ingredients_sort_arr = sorted(meal.ingredients)
        ingredients_str = ''.join(ingredients_sort_arr)
        res.add(ingredients_str)

    return len(res)


if __name__ == "__main__":