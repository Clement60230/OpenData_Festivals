# import pdfkit
from tkinter import messagebox

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter, landscape, A2
from reportlab.lib import colors
from reportlab.lib.units import inch

"""
Il y a beaucoup de méthodes pour générer des pages HTML,
La méthode ci-dessous a été utilisée dans le but de limiter le nombre de modules utilisés.
La table sera créée en utilisant bootstrap4.
"""
def generate_html(header, rows):
    # Obtenir le code html à partir de "template/section/section1.html"
    with open("template/section/section1.html", "r") as html_section_1:
        initilize = html_section_1.read()
    # Fin de la section 1, le résultat final avec ces deux sections est un fichier html vide.
    with open("template/section/section2.html", "r") as html_section_2:
        ending = html_section_2.read()
    # Ici, nous allons créer le fichier html principal avec nos données de sortie
    with open("output/main.html", "w", encoding="latin1") as main:
        """
        nous allons insérer un tableau dans le fichier html à l'intérieur de <body> tag.
        """
        main.write(initilize+"\n")
        # Insérer l'en-tête du tableau
        main.write("<thead>\n") # \n => signifie revenir à une nouvelle ligne
        main.write("\t<tr>\n")  # \t => signifie créer un espace de tabulation.
        for head in header:
            main.write("\t\t<th>{}<th>".format(head))
        main.write("\t</tr>\n")
        main.write("</thead>\n")
        # Insérer le contenu du tableau
        main.write("<tbody>\n")
        for e in range(len(rows)):
            main.write("\t<tr>\n")
            for t in rows[e]:
                if t == "Site web":
                    main.write("\t\t<td style='width: 25%'>{}</td>\n".format(rows[e][t]))
                else:
                    main.write("\t\t<td>{}</td>\n".format(rows[e][t]))
                main.write("\t\t<td></td>\n")
            main.write("\t</tr>\n")
        main.write("</tbody>\n")
        # Fin du fichier
        main.write(ending+"\n")
    messagebox.showinfo("IHM Exportateur", "Les données ont été exportées avec succès:\n{}".format('output/main.html'))

"""
La création d'un fichier pdf est compliquée.
Nous allons donc simplement convertir le résultat html en fichier pdf.
"""

def generate_pdf(header, filename = 'output/main.pdf', table_content_dict=[]):
    # Créer une instance de fichier
    output_pdf = SimpleDocTemplate(filename)
    output_pdf.pagesize = landscape(A2)
    # Convertir les données en liste
    table_content_list = []
    # Ajouter l'en-tête
    table_content_list.append(header)
    # Ajouter le contenu
    for e in range(len(table_content_dict)):
        temp = []
        for k, i in table_content_dict[e].items():
            if k == 'Nom de la manifestation':
                temp.append((i.replace('\x92',"'")).replace('\x96',""))
            else:
                temp.append(i)
        table_content_list.append(temp)
    # Créer la table
    table = Table(table_content_list)
    # Styliser la table
    style = TableStyle(
        [
            ('BACKGROUND', (0,0), (-1,0), colors.green), # Header background
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke), # Header text
            ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke), # Content background
            ('TEXTCOLOR', (0,1), (-1,-1), colors.black), # Content text
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),    # Align text to center
        ]   
    )
    # Appliquer le style à la table
    table.setStyle(style)
    # Ajoutez les données à la table
    elements = []
    elements.append(table)
    # Générer un pdf
    output_pdf.build(elements)
    # Confirmation
    messagebox.showinfo("IHM Exportateur", "Les données ont été exportées avec succès:\n{}".format('output/main.pdf'))