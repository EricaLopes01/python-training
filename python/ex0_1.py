diogo_basket = ["Apple", "Watermelon", "Grapes"]
henrique_basket = []

while len(henrique_basket) < 10: 
    possible_fruit = input("Qual é a fruta que devo levar? ")

    if possible_fruit.lower() == 'sair':
        break

    if possible_fruit in diogo_basket:
        print(f"A fruta {possible_fruit} não é permitida, pois já está na cesta do Diogo.")
    else:
        henrique_basket.append(possible_fruit)
        print(f"A fruta {possible_fruit} foi adicionada à cesta do Henrique.")

if len(henrique_basket) == 0:
    print("Henrique não pegou em nenhuma fruta.")
else:
    print(f"A cesta do Henrique contém: {', '.join(henrique_basket)}.")
