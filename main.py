"""
main.py: čtvrtý projekt do Engeto Online Tester with Python Akademie

author: Anna Waldhansová
email: annaw@email.cz
"""


seznam_ukolu = []

def pridat_ukol():
    while True:
        nazev_ukolu = input("Zadejte název úkolu: ")
        if nazev_ukolu.strip():
            break
        print("Název úkolu nesmí být prázdný. Zkuste to znovu.")
    
    while True:
        popis_ukolu = input("Zadejte popis úkolu: ")
        if popis_ukolu.strip():
            break
        print("Popis úkolu nesmí být prázdný. Zkuste to znovu.")
    seznam_ukolu.append({nazev_ukolu: popis_ukolu})
    
    
def zobrazit_vsechny_ukoly():
    if not seznam_ukolu:
        print("Žádné úkoly nejsou k dispozici.")
    else:
        print("\nSeznam úkolů:")
        for index, ukol in enumerate(seznam_ukolu, start=1):
            nazev_ukolu = list(ukol.keys())[0]
            popis_ukolu = ukol[nazev_ukolu]
            print(f"{index}. {nazev_ukolu} - {popis_ukolu}")
            
def odstranit_ukol():
    if not seznam_ukolu:
        print("Žádné úkoly nejsou k dispozici.")
        return
    
    zobrazit_vsechny_ukoly()
    
    while True:
        try:
            index = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            if 1 <= index <= len(seznam_ukolu):
                del seznam_ukolu[index - 1]
                print("Úkol byl úspěšně odstraněn.")
                break
            else:
                print("Neplatné číslo úkolu. Zkuste to znovu.")
        except ValueError:
            print("Zadejte platné číslo.")
            

def hlavni_menu():
    nabidka = (
        "\nSprávce úkolů - Hlavní menu\n"
        "1. Přidat nový úkol\n"
        "2. Zobrazit všechny úkoly\n"
        "3. Odstranit úkol\n"
        "4. Konec programu"
)
    while True:
        print(nabidka)
        volba = input("\nZadejte číslo volby: ")
        
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_vsechny_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("\nDěkujeme za použití programu!")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


if __name__ == "__main__":            
    hlavni_menu()

