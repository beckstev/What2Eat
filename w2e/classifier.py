import sys

import w2e.classes


def get_infos():
    #  Eingabeoptionen
    Ja = ['Ja', 'ja', 'j', 'y']
    Nein = ['Nein', 'nein', 'n']
    sehr = ['sehr', 's']
    mittel = ['mittel', 'm']

    print('Bist du vegan?\nWähle zwischen den folgenden Optionen aus:\n\"Ja\", \"Nein\"\n')
    while True:
        ausrichtung = input()
        if ausrichtung in Ja:
            ausrichtung = 'vegan'
            break
        elif ausrichtung in Nein:
            ausrichtung = 'vegan'
            break
        else:
            print('Bitte wähle eine der angegebenen Optionen aus.\n')

    if ausrichtung == 'vegan':
        pass
    else:
        print('Bist du vegetarisch?\nWähle zwischen den folgenden Optionen aus:\n\"Ja\", \"Nein\"\n')
        while True:
            ausrichtung = input()
            if ausrichtung in Ja:
                ausrichtung = 'vegetarisch'
                break
            elif ausrichtung in Nein:
                ausrichtung = 'vegetarisch'
                break
            else:
                print('Bitte wähle eine der angegebenen Optionen aus.\n')

    if ausrichtung == 'vegan' or ausrichtung == 'vegetarisch':
        pass
    else:
        ausrichtung = ''

    print('Wie hungrig fühlst du dich?\nWähle zwischen den folgenden Optionen aus:\n\"sehr\", \"mittel\"\n')
    while True:
        hunger = input()
        if hunger in sehr:
            hunger = True
            break
        elif hunger in mittel:
            hunger = False
            break
        else:
            print('Bitte wähle eine der angegebenen Optionen aus.\n')

    print('Möchtest du gesund essen?\nWähle zwischen den folgenden Optionen aus:\n\"Ja\", \"Nein\"\n')
    while True:
        gesundheit = input()
        if gesundheit in Ja:
            gesundheit = True
            break
        elif gesundheit in Nein:
            gesundheit = False
            break
        else:
            print('Bitte wähle eine der angegebenen Optionen aus.\n')

    print('Möchtest du gerne die gesamte Zeit beim kochen präsent sein?\nWähle zwischen den folgenden Optionen aus:\n\"Ja\", \"Nein\"\n')
    while True:
        praesenz = input()
        if praesenz in Ja:
            praesenz = True
            break
        elif praesenz in Nein:
            praesenz = False
            break
        else:
            print('Bitte wähle eine der angegebenen Optionen aus.\n')


    return w2e.classes.user_info(ausrichtung, hunger, gesundheit, praesenz)

def compare_clean(feature, list_, user_feature_info):
    for n in range(len(list_)):
        if not user_feature_info == list_[n][feature]:
            list_[n] = 0
    for n in range(list_.count(0)):
        list_.remove(0)
    return list_

def compare(user_info):
    user_hunger = user_info.hunger
    user_gesundheit = user_info.gesundheit
    user_praesenz = user_info.praesenz

    gerichts_klassen = w2e.classes.gerichts_klassen
    gerichts_klassen = compare_clean('hunger', gerichts_klassen, user_hunger)
    gerichts_klassen = compare_clean('gesundheit', gerichts_klassen, user_gesundheit)
    gerichts_klassen = compare_clean('praesenz', gerichts_klassen, user_praesenz)

    if len(gerichts_klassen) == 1:
        return gerichts_klassen[0]['name']
    else:
        return 'bestellen'






if __name__ == '__main__':
    #  pipeline
    try:
        user_info = get_infos()
        ausrichtung = user_info.ausrichtung
        user_choice = compare(user_info)

    except:
        e = sys.exc_info()[0]
        print(f'Error: {e}')
        print('Ein Fehler ist aufgetreten. Bitte versuche es erneut.')
