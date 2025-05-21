import random

print("Üdvözlet a blackjackben!")

# Kezdőpontok generálása a játékosnak és a dealernek
jatekos_pont = random.randint(2, 11) + random.randint(2, 11)
dealer_pont = random.randint(2, 11) + random.randint(2, 11)

print(f"A játékos kezdőpontja: {jatekos_pont}")
print(f"A dealer kezdőpontja: {dealer_pont}")

# Játékos köre – addig húzhat, amíg 21-nél kevesebb a pontszáma
while jatekos_pont < 21:
    dontes = input("Húzol fel? (húzok/nem): ").lower()
    if dontes == 'húzok':
        uj_lap = random.randint(2, 11)
        jatekos_pont += uj_lap
        print(f"Új lap értéke: {uj_lap}, összpont: {jatekos_pont}")
    elif dontes == 'nem':
        break
    else:
        print("Érvénytelen válasz, kérlek írd be pontosan: húzok vagy nem")

# Ha a játékos túlmegy 21-en
if jatekos_pont > 21:
    print("Túlmentél, vesztettél!")
else:
    print(f"\nA dealer kezdőpontja: {dealer_pont}")

    # Dealer köre – húz, amíg el nem éri a 17 pontot
    while dealer_pont < 17:
        lap = random.randint(2, 11)
        dealer_pont += lap
        print(f"Gép húzott: {lap}, gép összpont: {dealer_pont}")

    # Végső eredmények kiírása
    print(f"\nVégeredmény — Játékos: {jatekos_pont}, Gép: {dealer_pont}")

    # Eredmény kiértékelése
    if dealer_pont > 21 or jatekos_pont > dealer_pont:
        print("Nyertél!")
    elif dealer_pont > jatekos_pont:
        print("Vesztettél!")
    else:
        print("Döntetlen!")
