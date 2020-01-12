import pandas as pd
import collections
import numpy as np

"""
Ouvrir le fichier CSV
encoding='latin1'               => pour lire des caractères français
replace(np.nan, '', regex=True) => cela remplacera la valeur 'NaN' des pandas à None, car 'NaN' est un peu compliqué.
"""
data_frame = pd.read_csv("data.csv", encoding='latin1').replace(np.nan, '', regex=True)


class Domaine:
    def __init__(self):
        # Créer des domaines et les convertir en liste
        self.domains_list = data_frame['Domaine'].values.tolist()
        # Obtenir uniquement les domaines principaux sans répétition
        self.main_domains = [item for item, count in collections.Counter(self.domains_list).items() if count > 1]
        # Trier les données de A à Z
        self.main_domains.sort()
        # Convertir les données en paire (clé, valeur)
        """
        enumerate example : ["a","b","c"] sera <enumerate object>
        dict : <enumerate object> sera {0:"a", 1:"b", 2:"c"}
        """
        self.domaine = dict(enumerate(self.main_domains))

    """
    'Property decorator' pour rendre cette méthode utilisée comme variable,
     ce qui signifie que vous pouvez y accéder sans parenthèses
    """
    @property
    def all_domaines(self):
        # Imprimer tous les domaines disponibles, y compris la valeur nulle
        for key in self.domaine:
            print(key, self.domaine[key])

    # obtenir le domaine par son identifiant (id)
    def get_domaine(self, id):
        return self.domaine[id]

    # obtenir toutes les valeurs d'en-tête
    def get_header(self, columns_id=[0,2,7,9,12,13,23]):
        header = []
        for head in columns_id:
            header.append(data_frame.columns.values[head])
        return header
