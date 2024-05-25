import requests
import json
headrs={"Content-Type":"application/json"}
searchfor=input("What would you like to search for?: ")
url=f"https://www.themealdb.com/api/json/v1/1/search.php?s={searchfor}"
response=requests.get(url, headers=headrs).json()
if response['meals']:
    meal=response['meals'][0]
    print('-'*10,meal['strMeal'], '-'*10)
    print("\n")
    print('-'*5,'Ingredients', '-'*5)
    for i in range(1,20):
        if meal[f'strIngredient{str(i)}']!="":
            print(meal[f'strIngredient{str(i)}']," | ", end="", flush=True)
            if meal[f'strMeasure{str(i)}']!="":
                print(meal[f'strMeasure{str(i)}'])
    print('\n','-'*5, 'Instructions', '-'*5,'\n')
    print(meal['strInstructions'])
input()
    


