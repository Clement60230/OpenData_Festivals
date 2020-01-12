from domaine import Domaine, data_frame
from search import search_by

class Manifestation:
    def __init__(self):
        # Instance de classe Domaine
        self.domaine = Domaine()
        # Obtenir toutes les valeurs d'en-tête
        self.columns = self.domaine.get_header()
        # Obtenir toutes les données nécessaires et les convertir en liste
        self.manifestations_list = data_frame[self.columns].values.tolist()
        # Obtenir chaque manifestation et l'organiser sous forme de dictionnaire
        for each in range(len(self.manifestations_list)):
            self.manifestations_list[each] = dict(zip(self.columns, self.manifestations_list[each]))

    # Les valeurs nulles afficheront toutes les données sur l'interface graphique
    def search_by_fields(self, place="", domaine="", start_date="", end_date=""):
        search_by(self, place, domaine, start_date, end_date)

