import requests

app_id = "174ef8f2"
app_key = "c0b5c225723a0a0f6f79031b601de218"
ingredient = input('Enter an ingredient: ')
mealType = input('Choose a meal (breakfast, lunch or dinner): ')
print('\n')

def recipe_search(ingredient, mealType):
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}&mealType={mealType}'
    response = requests.get(url)

#parse response to get the info you need

    data = response.json()
    hits = data ['hits'] #a hit means a single recipe that has matched the search query parameters

    if 'hits' not in data:
        print('No recipe found.')
        return[]

#now get the recipe info

    recipes = []    #empty list to store recipe info

    for hit in hits:    #iterate through each dict in hits list (a dict contains a key and value)
        recipe = hit['recipe'] #extract the dict of recipe info from current hit
        title = recipe['label'] #extract recipe title from the recipe dict above
        image_url = recipe['image']
        recipe_url = recipe['url']
        ingredients = recipe['ingredientLines'] #extract list of recipe ingredients from the recipe dict
        mealType = recipe['mealType']

    #now create a new dictionary that stores the extracted recipe info

        recipe_data = {
            'title': title, #use : because it is a dict
            'image_url': image_url,
            'recipe_url': recipe_url,
            'ingredients': ingredients,
            'mealType': mealType
        }

        recipes.append(recipe_data) #adding this new dictionary to the recipes list

    return recipes

recipes = recipe_search(ingredient, mealType)

for recipe in recipes:
    print (recipe['title'])
    print(recipe['ingredients'])
    print(recipe['mealType'])
    print('\n')



