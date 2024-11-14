import ezodf  # pip install ezodf # pip install lxml

# Načtení .ods souboru
def nacti_ods_soubor(cesta_k_souboru):
    # Otevře .ods soubor
    dokument = ezodf.opendoc(cesta_k_souboru)
    return dokument


def vypis_obsah_listu(dokument):
    #prepneme na1. list a vypiseme jeho jmeno
    list = dokument.sheets[0]
    print(f"List: {list.name}")

    # projde bunky
    for radek in list.rows():
        hodnoty = [bunka.value for bunka in radek]
        print(hodnoty)

# prace s daty
def zpracuj_data(dokument):
    list = dokument.sheets[0]
    celkovy_soucet = 0
    neprazdne_bunky = 0

    for radek in list.rows():
        for bunka in radek:
            if isinstance(bunka.value, (int, float)):  # Kontrola, zda je hodnota číselná
                celkovy_soucet += bunka.value
                neprazdne_bunky += 1

    # Vypočítáme průměr
    prumer = celkovy_soucet / neprazdne_bunky if neprazdne_bunky else 0
    print(f"Celkový součet: {celkovy_soucet}")
    print(f"Průměr: {prumer}")


cesta_k_souboru = "data.ods"  
dokument = nacti_ods_soubor(cesta_k_souboru)

# Výpis dat ze souboru
vypis_obsah_listu(dokument)
#zpracovani dat
zpracuj_data(dokument)
