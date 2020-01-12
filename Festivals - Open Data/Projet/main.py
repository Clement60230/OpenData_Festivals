import tkinter as tk
from tkinter import ttk
from manifestation import Manifestation
from exporter import generate_html, generate_pdf

"""
Nous avons utilisé les widgets suivants:
Frame => pour diviser notre fenêtre principale en sections, nous pouvons facilement organiser les widgets internes.
Button => Pour générer des boutons.
Label => pour afficher le titre des widgets comme étiquette.
Scrollbar => pour rendre la barre de défilement horizontale et verticale.
Combobox => pour générer la liste des éléments.
Entry => champ de saisie de texte.
Treeview => pour représenter nos données sous forme de tableau.
"""

# Initialiser l'instance de manifestation
Manifestations = Manifestation()

# La fonction s'exécute lorsque vous cliquez sur le bouton 'rafraîchir'
def show_data():
    dataview.delete(*dataview.get_children())
    Manifestations.search_by_fields(
        place=manifestation_entry.get(),
        domaine=domaine_entry.get(),
        start_date=start_date_entry.get(),
        end_date=end_date_entry.get()
        )
    for e in range(len(Manifestations.result)):
        dataview.insert('', 'end', text="Item_"+str(e),
                                values=(
                                    Manifestations.result[e]['Nom de la manifestation'],
                                    Manifestations.result[e]['Domaine'],
                                    Manifestations.result[e]['Site web'],
                                    Manifestations.result[e]['Commune principale'],
                                    Manifestations.result[e]['Date de début'],
                                    Manifestations.result[e]['Date de fin'],
                                    Manifestations.result[e]['Code postal'],
                                        )
                        )


# Générer la fenêtre principale
root = tk.Tk()
root.title("IHM")
root.resizable(False,False)
# Divisions principales
row1 = tk.Frame(root, width=500, height=50)
row2 = tk.Frame(root, width=500, height=200)
row3 = tk.Frame(root, width=500, height=50)
row1.pack() # nous pouvons utiliser 'pack' ou 'grid' pour afficher le widget sur la fenêtre.
row2.pack()
row3.pack(pady=10)
# Divisions intérieures
row1col1 = tk.Frame(row1, width=500, height=50)
row1col2 = tk.Frame(row1, width=200, height=50)
row2col1 = tk.Frame(row2, width=500, height=200)
row2col2 = tk.Frame(row2, width=200, height=250)
row3col1 = tk.Frame(row3, width=500, height=50)
row3col2 = tk.Frame(row3, width=200, height=50)
row1col1.grid(row=0,column=0)
row1col2.grid(row=0,column=1)
row2col1.grid(row=0,column=0)
row2col2.grid(row=0,column=1, padx=10)
row3col1.grid(row=0,column=0)
row3col2.grid(row=0,column=1)
# Division imbriquée
row2col1col1 = tk.Frame(row2col1, width=480, height=180)
row2col1col1.grid(row=0,column=0)
row2col1col1row1 = tk.Frame(row2col1col1, width=480, height=180)
row2col1col1row1.pack()
# Frame supplémentaire
dataview_frame = tk.Frame(row2col1col1row1)
dataview_frame.pack(fill='x', side=tk.LEFT)
# Widgets
main_title = tk.Label(row1col1, text='IHM', anchor='w', width=50, font=("Helvetica", 16))
dataview = ttk.Treeview(dataview_frame)
h_scrollbar = tk.Scrollbar(dataview_frame, orient=tk.HORIZONTAL)
v_scrollbar = tk.Scrollbar(row2col1col1row1, orient=tk.VERTICAL)
load_data = tk.Button(row3col2, text="rafraîchir", command=show_data)
export_html = tk.Button(row3col1, text="exporter HTML", command=lambda: generate_html(Manifestations.columns, Manifestations.result))
export_html.grid(row=0,column=0, padx=115)
export_pdf = tk.Button(row3col1, text="exporter PDF", command=lambda: generate_pdf(header=Manifestations.columns, table_content_dict=Manifestations.result))
export_pdf.grid(row=0,column=1, padx=115) 
search_label = tk.Label(row2col2, text="Chercher:", font=("Helvetica", 14), anchor='w')
commune_label = tk.Label(row2col2, text="Commune:")
manifestation_entry = tk.Entry(row2col2, width=30)
domaine_label = tk.Label(row2col2, text="Domaine:")
domaine_entry = ttk.Combobox(row2col2,width=27, values=Manifestations.domaine.main_domains)
start_date_label = tk.Label(row2col2, text="Date de début:")
start_date_entry = tk.Entry(row2col2, width=30)
end_date_label = tk.Label(row2col2, text="Date de fin:")
end_date_entry = tk.Entry(row2col2, width=30)
main_title.pack()
dataview.pack(fill='x')
h_scrollbar.pack(fill=tk.X)
v_scrollbar.pack(fill='y', side=tk.LEFT)
load_data.pack(padx=70)
search_label.pack(padx=(5,100))
commune_label.pack()
manifestation_entry.pack()
domaine_label.pack()
domaine_entry.pack()
start_date_label.pack()
start_date_entry.pack()
end_date_label.pack()
end_date_entry.pack()
# Configurer la barre de défilement pour la faire fonctionner
v_scrollbar.configure(command=dataview.yview)
dataview.configure(yscrollcommand=v_scrollbar.set)
h_scrollbar.configure(command=dataview.xview)
dataview.configure(xscrollcommand=h_scrollbar.set)
# Ajouter l'en-tête des données à 'TreeView'
dataview["columns"] = Manifestations.columns
dataview["show"] = "headings"
for col in Manifestations.columns:
    dataview.heading(col, text=col)
dataview.column("#1",minwidth=10,width=140, stretch=tk.NO)
dataview.column("#2",minwidth=10,width=60, stretch=tk.NO)
dataview.column("#3",minwidth=10,width=52, stretch=tk.NO)
dataview.column("#4",minwidth=10,width=120, stretch=tk.NO)
dataview.column("#5",minwidth=10,width=85, stretch=tk.NO)
dataview.column("#6",minwidth=10,width=65, stretch=tk.NO)
dataview.column("#7",minwidth=10,width=73, stretch=tk.NO)

# Code important pour s'assurer que les fenêtres ne se ferment pas tant qu'on ne clique pas sur le bouton x.
root.mainloop()