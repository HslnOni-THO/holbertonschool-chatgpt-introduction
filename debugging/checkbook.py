class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Dépôt de ${:.2f}".format(amount))
        print("Solde actuel : ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Fonds insuffisants pour effectuer le retrait.")
        else:
            self.balance -= amount
            print("Retrait de ${:.2f}".format(amount))
            print("Solde actuel : ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Solde actuel : ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("Que souhaitez-vous faire ? (dépôt, retrait, solde, quitter) : ")
        if action.lower() == 'quitter':
            break
        elif action.lower() == 'dépôt':
            try:
                amount = float(input("Veuillez entrer le montant à déposer : $"))
                if amount < 0:
                    print("Le montant ne peut pas être négatif. Veuillez réessayer.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre valide pour le dépôt.")
        elif action.lower() == 'retrait':
            try:
                amount = float(input("Veuillez entrer le montant à retirer : $"))
                if amount < 0:
                    print("Le montant ne peut pas être négatif. Veuillez réessayer.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre valide pour le retrait.")
        elif action.lower() == 'solde':
            cb.get_balance()
        else:
            print("Commande invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()