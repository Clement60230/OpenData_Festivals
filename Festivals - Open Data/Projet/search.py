import datetime

# Algorithme de recherche
def search_by(self, place, domaine, start_date, end_date):
    """
    le résultat de la recherche est stocké dans une liste.
    Il sera vide à chaque fois pour s'assurer que les données ne s'ajoutent pas aux dernières données.
    """
    self.result = []
    # Prendre chaque ligne de manifestation du fichier csv chargé après filtrage
    for manifestation in self.manifestations_list:
        # Si tous les champs de résultat sont vides, afficher toutes les données
        if place == "" and domaine == "" and start_date == "" and end_date == "":
            self.result.append(manifestation)
        # Si tous les champs de résultat ont une donnée
        elif place != "" and domaine != "" and start_date != "" and end_date != "":
            # Try/Except Block, en cas d'erreur sur les données, rien est fait
            try:
                """
                Convertir le format de données du m/j/a au format du module datetime,
                ce qui nous permettra de calculer les dates.
                """
                input_start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y').date()
                input_end_date = datetime.datetime.strptime(end_date, '%m/%d/%Y').date()
                database_start_date = datetime.datetime.strptime(manifestation['Date de début'], '%m/%d/%Y').date()
                database_end_date = datetime.datetime.strptime(manifestation['Date de fin'], '%m/%d/%Y').date()
            except:
                continue
            # Le caractère "\" signifie casser la ligne, pour casser le code python long en plusieurs lignes.
            if manifestation['Commune principale'] == place \
            and manifestation['Domaine'] == domaine \
            and (input_start_date - database_start_date).days == 0 \
            and (input_end_date - database_end_date).days == 0:
                self.result.append(manifestation)
        # Pour rechercher uniquement par nom de commune
        elif place != "" and domaine == "" and start_date == "" and end_date == "":
            if manifestation['Commune principale'] == place:
                self.result.append(manifestation)
        # Pour rechercher uniquement par nom de domaine
        elif place == "" and domaine != "" and start_date == "" and end_date == "":
            if manifestation['Domaine'] == domaine:
                self.result.append(manifestation)
        # Pour rechercher par nom de commune et par nom de domaine
        elif place != "" and domaine != "" and start_date == "" and end_date == "":
            if manifestation['Commune principale'] == place and manifestation['Domaine'] == domaine:
                self.result.append(manifestation)
        # Pour rechercher par la date de début et la date de fin
        elif place == "" and domaine == "" and start_date != "" and end_date != "":
            try:
                input_start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y').date()
                input_end_date = datetime.datetime.strptime(end_date, '%m/%d/%Y').date()
                database_start_date = datetime.datetime.strptime(manifestation['Date de début'], '%m/%d/%Y').date()
                database_end_date = datetime.datetime.strptime(manifestation['Date de fin'], '%m/%d/%Y').date()
            except:
                continue
            # Le résultat affichera toutes les données souhaitées
            if (input_start_date - database_start_date).days == 0 and (input_end_date - database_end_date).days == 0:
                self.result.append(manifestation)
        # Pour rechercher uniquement par date de début
        elif place == "" and domaine == "" and start_date != "" and end_date == "":
            try:
                input_start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y').date()
                database_start_date = datetime.datetime.strptime(manifestation['Date de début'], '%m/%d/%Y').date()
            except:
                continue
            # Le résultat affichera toutes les données souhaitées
            if (input_start_date - database_start_date).days == 0:
                self.result.append(manifestation)
        # Pour rechercher par date de début et Commune principale
        elif place != "" and domaine == "" and start_date != "" and end_date == "":
            try:
                input_start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y').date()
                database_start_date = datetime.datetime.strptime(manifestation['Date de début'], '%m/%d/%Y').date()
            except:
                continue
            # Le résultat affichera toutes les données souhaitées
            if (input_start_date - database_start_date).days == 0 and manifestation['Commune principale'] == place:
                self.result.append(manifestation)
        # Pour rechercher par date de début et Domaine
        elif place == "" and domaine != "" and start_date != "" and end_date == "":
            try:
                input_start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y').date()
                database_start_date = datetime.datetime.strptime(manifestation['Date de début'], '%m/%d/%Y').date()
            except:
                continue
            # Le résultat affichera toutes les données souhaitées
            if (input_start_date - database_start_date).days == 0 and manifestation['Domaine'] == domaine:
                self.result.append(manifestation)
        # Pour rechercher uniquement par date de fin
        elif place == "" and domaine == "" and start_date == "" and end_date != "":
            try:
                input_end_date = datetime.datetime.strptime(end_date, '%m/%d/%Y').date()
                database_end_date = datetime.datetime.strptime(manifestation['Date de fin'], '%m/%d/%Y').date()
            except:
                continue
            # Le résultat affichera toutes les données souhaitées
            if (input_end_date - database_end_date).days == 0:
                self.result.append(manifestation)
        # Pour rechercher par date de fin et domaine
        elif place == "" and domaine != "" and start_date == "" and end_date != "":
            try:
                input_end_date = datetime.datetime.strptime(end_date, '%m/%d/%Y').date()
                database_end_date = datetime.datetime.strptime(manifestation['Date de fin'], '%m/%d/%Y').date()
            except:
                continue
            # Le résultat affichera toutes les données souhaitées
            if (input_end_date - database_end_date).days == 0 and manifestation['Domaine'] == domaine:
                self.result.append(manifestation)
        # Pour rechercher par date de fin et Commune principale.
        elif place != "" and domaine == "" and start_date == "" and end_date != "":
            try:
                input_end_date = datetime.datetime.strptime(end_date, '%m/%d/%Y').date()
                database_end_date = datetime.datetime.strptime(manifestation['Date de fin'], '%m/%d/%Y').date()
            except:
                continue
            # Le résultat affichera toutes les données souhaitées
            if (input_end_date - database_end_date).days == 0 and manifestation['Commune principale'] == place:
                self.result.append(manifestation)
        # Pour rechercher par le nom de la commune et la date de début + date de fin
        elif place != "" and domaine == "" and start_date != "" and end_date != "":
            try:
                input_start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y').date()
                input_end_date = datetime.datetime.strptime(end_date, '%m/%d/%Y').date()
                database_start_date = datetime.datetime.strptime(manifestation['Date de début'], '%m/%d/%Y').date()
                database_end_date = datetime.datetime.strptime(manifestation['Date de fin'], '%m/%d/%Y').date()
            except:
                continue
            if manifestation['Commune principale'] == place \
            and (input_start_date - database_start_date).days == 0 \
            and (input_end_date - database_end_date).days == 0:
                self.result.append(manifestation)  
        # Pour rechercher par le domaine et la date de début + date de fin
        elif place == "" and domaine != "" and start_date != "" and end_date != "":
            try:
                input_start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y').date()
                input_end_date = datetime.datetime.strptime(end_date, '%m/%d/%Y').date()
                database_start_date = datetime.datetime.strptime(manifestation['Date de début'], '%m/%d/%Y').date()
                database_end_date = datetime.datetime.strptime(manifestation['Date de fin'], '%m/%d/%Y').date()
            except:
                continue
            if manifestation['Domaine'] == domaine and (input_start_date - database_start_date).days == 0 and (input_end_date - database_end_date).days == 0:
                self.result.append(manifestation)  
