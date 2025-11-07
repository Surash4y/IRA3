#contenu des trains 
trains = {
    'TUN-PAR': {'places_total': 5, 'places_restantes': 5, 'passagers': set()},
    'TUN-ROM': {'places_total': 3, 'places_restantes': 3, 'passagers': set()},
    'TUN-MAD': {'places_total': 4, 'places_restantes': 4, 'passagers': set()},
}

#liste des tickets
tickets = []

def afficher_titre(titre):
    print(f"{titre}")

#fonction pour afficher les trains disponibles
def afficher_trains():
    afficher_titre("Trains disponibles")
    
    
    for trajet, info in trains.items():
        places_occupees = info['places_total'] - info['places_restantes']
        statut = " complet" if info['places_restantes'] == 0 else " Disponible"
        
        print(f"\n {trajet}")
        print(f"{info['places_restantes']} places restantes / {info['places_total']}")
        print(f"{places_occupees} places occupées")
        print(f"Statut : {statut}")

#fonction pour réserver une place
def reserver_place():
    afficher_titre("Réservez un billet")
    
    nom = input("\n Entrez votre nom ").strip().upper()

    
    print("\n Trajets disponibles :")
    trajets_disponibles = []
    for trajet, info in trains.items():
        if info['places_restantes'] > 0:
            print(f"{trajet} ({info['places_restantes']} places)")
            trajets_disponibles.append(trajet)
        else:
            print(f"  {trajet} (COMPLET)")

    
    trajet = input("\n Choisissez votre trajet").strip().upper()
    


    trains[trajet]['passagers'].add(nom)
    trains[trajet]['places_restantes'] -= 1
    
    numero_place = trains[trajet]['places_total'] - trains[trajet]['places_restantes']
    ticket = (nom, trajet, numero_place)
    tickets.append(ticket)
    




    print(f"Passager  : {nom}")
    print(f"Trajet    : {trajet}")
    print(f"Numéro de place  : {numero_place}")
    print(f"Ticket ID : {len(tickets)}")


#fonction pour annuler une reservation
def annuler_reservation():

    afficher_titre("annuler une reservation")
    
    nom = input("\n Nom du passager : ").strip().upper()

    trajet = input("Code du trajet : ").strip().upper()

    trains[trajet]['passagers'].remove(nom)
    trains[trajet]['places_restantes'] += 1
    
    print("\n Réservation annulée")

#fonction pour afficher les passagers d'un train

def afficher_passagers():
    afficher_titre("Liste des passagers")
    
    trajet = input("\n Code du trajet : ").strip().upper()
    
    if trajet not in trains:
        print(f"'{trajet}' n'existe pas.")
        return
    
    passagers = trains[trajet]['passagers']
    
    
    print(f"\n Train {trajet}")
    print(f"il y a  {len(passagers)} passagers")
    print(f" Places occupées : {trains[trajet]['places_total'] - trains[trajet]['places_restantes']}/{trains[trajet]['places_total']}")
    print("\n Liste des passagers :")
    
    for i, passager in enumerate(sorted(passagers), 1):
        print(f"{i} {passager}")

#fonction pour afficher les trains complets
def afficher_trains_complets():

    afficher_titre("trains complets")
    
    trains_complets = [
        trajet for trajet, info in trains.items()
        if info['places_restantes'] == 0
    ]
    

    
    print(f"\n {len(trains_complets)} train complet :\n")
    
    for trajet in trains_complets:
        info = trains[trajet]
        print(f"{trajet}")
        print(f"{info['places_total']} places ")
        print(f"{len(info['passagers'])} passagers")

#fonction pour afficher les tickets

def afficher_tickets():

    afficher_titre("tickets trouvés")
    

    print(f"\n{len(tickets)} ticket trouvés :\n")
    
    for i, (nom, trajet, place) in enumerate(tickets, 1):
        print(f"Ticket #{i}")
        print(f"Passager : {nom}")
        print(f"Trajet   : {trajet}")
        print(f"Place    : {place}")
        print()

#fonction pour afficher le menu
def afficher_menu():
    print("1. Trains disponibles")
    print("2. Réserver un billet")
    print("3. Annuler une réservation")
    print("4. Afficher le nombre de passagers dans un train")
    print("5. Voir les trains complets")
    print("0. Quitter")



def main():

    
    while True:
        afficher_menu()
        choix = input("\n entrez votre choix : ").strip()
        
        if choix == '1':
            afficher_trains()
        
        elif choix == '2':
            reserver_place()
        
        elif choix == '3':
            annuler_reservation()
        
        elif choix == '4':
            afficher_passagers()
        
        elif choix == '5':
            afficher_trains_complets()
        
        elif choix == '6':
            afficher_tickets()
        
        input("\n Entrée pour continuer")


if __name__ == "__main__":
    main()