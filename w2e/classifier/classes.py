#  features: hunger, gesundheit, praesenz
#  hunger: deftig = True, leicht = False
#  gesundheit: gesund = True, egal = False
#  praesenz: anwesend = True, großteils abwesen = False
class user_info():
    def __init__(self, ausrichtung, hunger, gesundheit, praesenz):
        self.ausrichtung = ausrichtung
        self.hunger = hunger
        self.gesundheit = gesundheit
        self.praesenz = praesenz


pfannengericht = {
    'name': 'pfannengericht',
    'hunger': True,
    'gesundheit': False,
    'praesenz': True
    }
low_carb = {
    'name': 'low+carb',
    'hunger': False,
    'gesundheit': True,
    'praesenz': True
    }
pampe = {
    'name': 'pampe',
    'hunger': True,
    'gesundheit': True,
    'praesenz': True
    }
auflauf = {
    'name': 'auflauf',
    'hunger': True,
    'gesundheit': False,
    'praesenz': False
    }
eintopf = {
    'name': 'eintopf',
    'hunger': False,
    'gesundheit': True,
    'praesenz': False
    }

gerichts_klassen = [pfannengericht, low_carb, pampe, auflauf, eintopf]
