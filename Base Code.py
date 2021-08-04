import requests
def recipe_search(user_input_string):
    app_id = "8ef86872"
    app_key = "a1760510c7cf9aba12e231b19aec1da3"
    results = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(user_input_string, app_id, app_key)
                           )
    data = [section['recipe'] for section in results.json()['hits']]
    return data
# in the API section 'hits' the search is returning results from the 'recipes' dictionary

def print_results(results):
 for i,recipe in enumerate(results):
     print(i,recipe['label'])
     print(recipe['uri'])
     print(recipe['ingredientLines'])
     print()
# Enumerate is the function that numbers each item on the list of results
# - i is the standard letter given to the numbers so the first print statement is calling it to print the number and the recipe name

# def calorie_sort():
#     Adding a function to sort the list by calories in the recipes

if __name__=='__main__':
    # Apparently it's good python to define all function at the beginning of code, and the put this statement in and start the rest you want to run
    # It makes the code only run after this statement so we don't accidentally run any code that is included in the file you imported
    # Main means 'is the code directly in the file you are running, the main code'
    print("Hello! Let's find you something delicious to cook")
    print("You can search by a main ingredient, cuisine, or dietary requirement")
    search_item = input("What do you fancy? ")
    results = recipe_search(search_item)
    # Calorie Sort function could go here
    print_results(results)
    print("Do you want to add these ingredients to your shopping list")
    recipe_nums = []
    while True:
        try:
            recipe_num = int(input("Enter the number of the recipe, pick as many as you like!"))
        except ValueError:
            break
        # This currently asks the question as many times as you enter a number, and ends when you press enter as 'no answer' is a valueerror
        # We could change this into a for loop that runs the question a certain number of times rather than indefinitely
        # Then we could change the question to 'pick 3 recipes to save to your shopping list'
        recipe_nums.append(recipe_num)
    print(recipe_nums)
    ingredients_list =  []
    for recipe_num in recipe_nums:
        ingredients_dict = results[recipe_num]['ingredients']
        ingredients_list += [ingredient_dict['text'] for ingredient_dict in ingredients_dict]
    with open('shopping_list.txt','a+') as text_file:
        for ingredient in ingredients_list:
            text_file.write(ingredient + "\n")
# \n makes each ingredient be saved on a new line of the list rather than in a chunk
# Maybe we could add in so it saves the 'label' recipe name linked to the ingredients as well