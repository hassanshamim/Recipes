import json
import os


class Recipe:
    def __init__(self,
                 name,
                 servings=0,
                 total_time='',
                 ingredients=None,
                 directions=None,
                 starred=False):
        self.name = name
        self.servings = servings
        self.total_time = total_time
        self.ingredients = ingredients  # list of ingredients, i.e.: ['soy sauce', 2, 'tablespoon']
        self.directions = directions
        self.starred = is_starred # added by Alex for tracking if a recipe is starred.

    def __iter__(self):
        '''
        Special method to allow us to convert our Recipe instances to a dictionary
        by calling dict(recipe_object)
        '''
        keys = ['name', 'servings', 'total_time', 'ingredients', 'directions']
        for key in keys:
            yield key, getattr(self, key)

    @classmethod
    def load_recipes(cls):
        """
        Returns a list of recipe objects saved in the recipe.json file.abs
        If the file does not exist, returns an empty list.
        """
        fname = 'recipes.json'
        if not os.path.exists(fname):
            return []
        file = open(fname, 'r')
        recipes_data = json.load(file)
        file.close()
        recipes = [cls(**data) for data in recipes_data]
        return recipes

    @classmethod
    def save_recipes(cls, recipes):
        """
        Takes a list of recipe object, converts them to json,
        and saves them to a file called 'recipes.json'.abs

        If recipes.json already exists, it replaces the file with the contents of
        the recipes parameter.
        """
        recipes = [dict(recipe) for recipe in recipes]
        file = open('recipes.json', 'w')
        json.dump(recipes, file, indent=4)
        file.close()

    @classmethod
    def from_input(cls):
        """
        Creates a new Recipe object from gathered input from the user
        """
        print('Creating a new Recipe')
        recipe_name = input("What is your recipe's name?  ")
        servings = int(input(' many does it serve?  '))
        total_time = input("How long does it take?  i.e: 40 minutes  ")

        print('Please follow the prompt to list your ingredients')
        print('When you are done, leave the name prompt blank and hit enter\n')
        ingredients = []
        while True:
            name = input('Name of ingredient:  ')
            if not name:
                break
            amount = float(input('How much?  Just a number please:  '))
            unit = input('And what is the unit of measurement?  I.e. cups  ')
            ingredients.append([name, amount, unit])

        print('\n\nNow list your directions')
        print('Enter a blank line when you are done')
        directions = []
        while True:
            line = input()
            if not line:
                break
            directions.append(line)

        """
        These are the "starred" recipe additions Alex made
        """
        print('Do you want to star this recipe? Enter "Y" ("Yes") or "N" ("No")')
        star_answer = input()
        star_answer = star_answer.upper
            correct_answers = ['Y','N']
            if star_answer is not in correct_answers:
                print('Try again, I need "Y" or "N"')
            elif star_answer == 'Y'
                is_starred = TRUE
            elif star_answer == 'N'
                is_starred = FALSE



        return cls(
            recipe_name,
            is_starred = is_starred,
            servings=servings,
            total_time=total_time,
            ingredients=ingredients,
            directions=directions)

    def display(self):
        print(self.name)
        print('Starred: ', self.starred) # Adding in a display for the "starred" status (Alex again).
        print('Servings:', self.servings)
        print('Cooking time:', self.total_time)
        print('Ingredients:'.center(40))
        for ingredient in self.ingredients:
            name, amount, unit = ingredient
            name = name.ljust(25)
            amounts = str(amount).ljust(10) + unit.ljust(15)
            print(name + amounts)

        print()
        print('DIRECTIONS'.center(70))

        for direction in self.directions:
            print(direction)
            print()


def list_recipes(recipes):
    print('your recipes are:')
    for i, recipe in enumerate(recipes):
        print(f"{i} - {recipe.name}")

def display_recipe(recipes):
    command = input()
    try:
        i = int(command)
        recipes[i].display()
    except ValueError:
        pass


if __name__ == '__main__':
    all_recipes = Recipe.load_recipes()
    command = None
    print('Hello and welcome to Recipe App')


    while command != 'q':
    # # display actions
        print('Your options:')
        print('q - exit this program')
        print('1 - list recipes')
        print('2 - add a recipe')

        # prompt user for action
        command = input('Choose an action\n')

        if command == '1':
            list_recipes(all_recipes)

            print("Input a Recipes number to display it, or leave blank to return to the menu\n")
            display_recipe(all_recipes)


        elif command == '2': # add new recipe
            new_recipe = Recipe.from_input()
            all_recipes.append(new_recipe)
            Recipe.save_recipes(all_recipes)
