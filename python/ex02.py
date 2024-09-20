diogo_basket = ["Apple", "Watermelon", "Grapes"]
henrique_basket = []

while len(henrique_basket) < 10: 
    possible_fruit = input("Qual é a fruta que devo levar? ")

    if not possible_fruit:
        print("Hemrique não quer adicionar mais itens.")
        break

    if possible_fruit in diogo_basket:
        print("A fruta n é permitida pois já está na cesta")
        continue


    henrique_basket.append(possible_fruit)
    print(f"A fruta {possible_fruit} foi adicionada à cesta do Henrique.")

if not henrique_basket:
    print("Henrique não pegou em nenhuma fruta.")
