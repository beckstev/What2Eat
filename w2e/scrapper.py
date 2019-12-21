import os
import requests
from pprint import pprint
from bs4 import BeautifulSoup
import numpy as np
import w2e.output
import sys

def get_recipe(dish_type, URL):
    page = requests.get(url=URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    recipes = soup.find_all("a", {"class":'ds-mb ds-mb-row ds-card rsel-recipe bi-recipe-item'})
    assert len(recipes) > 0
    random_recipe_index = np.random.randint(low=0, high=len(recipes))
    recipe_suggestion = extract_information(recipes[random_recipe_index])
    return recipe_suggestion


def extract_information(recipe):
    recipe_information = dict()
    recipe_information['title'] = recipe['data-vars-recipe-title']
    recipe_information['link'] = recipe['href']
    linktoimg = recipe.find('amp-img')['srcset'].split('\n')[-1].split(' ')[-2]
    recipe_information['img_link'] = linktoimg
    return recipe_information


def generate_url(dish_type, type_of_eating, conditons):

    page = np.random.choice([0, 30, 60])
    if conditons['cooking_time']:
        filter = f'{page}e1n1z1b0i0m{conditons["cooking_time"]}d1,2,3'

    else:
        filter = page

    URL = f'https://www.chefkoch.de/rs/s{filter}/{dish_type}+{type_of_eating}/Rezepte.html'
    return URL



if __name__ == '__main__':
    type_of_eating = ''
    dish_type = 'auflauf'

    if dish_type == 'bestellen':
        print(
            'https://www.lieferando.de/en/?gclid=EAIaIQobChMIvcb2tdLE5gIVhLHtCh2wWw_cEAAYASAAEgLUwvD_BwE&gclsrc=aw.ds')
        sys.exit()
    URL = generate_url(dish_type, type_of_eating, conditons)
    test = get_recipe(dish_type, URL)
    w2e.output.display_suggestion(test)
