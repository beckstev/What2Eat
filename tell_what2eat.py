import w2e.classifier
import w2e.scrapper
import w2e.output

import sys


conditons = {'cooking_time': 30, 'difficulty': 'medium'}

user_info = w2e.classifier.get_infos()
dish_type = w2e.classifier.compare(user_info)
print('\n---------------------\n')

if dish_type == 'bestellen':
    print('Bestell dir lieber was. Du bist nicht in der Stimmung zu kochen.')
    print('Hier der passende Link: \n')
    print('https://www.lieferando.de/en/?gclid=EAIaIQobChMIvcb2tdLE5gIVhLHtCh2wWw_cEAAYASAAEgLUwvD_BwE&gclsrc=aw.ds')
    sys.exit()

# --- Get Recipe
print('Suche nach einem passenden Gericht!')
print('Damit wir dir einen individuellen Vorschlag machen können, benötigen wir etwas Zeit.')
URL = w2e.scrapper.generate_url(dish_type, user_info.ausrichtung, conditons)
recipe = w2e.scrapper.get_recipe(dish_type, URL)
print('Hier gehts zu deinem Rezept:')
print(URL)
w2e.output.display_suggestion(recipe)
