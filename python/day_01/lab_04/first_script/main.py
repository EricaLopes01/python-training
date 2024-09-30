def main():
    nome = input("Hello, what is your name?\n")

   
    fruits = []


    fruits_input = input(f"Welcome, {nome}! Type your favourite fruits, separated by commas, please:\n").strip()

    
    fruits = [fruit.strip() for fruit in fruits_input.split(',')]

    
    print_fruits(fruits)

    
    fruit_to_remove = input("Which fruit would you like to remove from the list? ").strip()

    
    for stored_fruit in fruits:
        if stored_fruit.lower() == fruit_to_remove.lower():
            fruits.remove(stored_fruit)
            print(f"\n'{stored_fruit}' removed from the list.\n")
            break
    else:
        print(f"\n'{fruit_to_remove}' is not in the list.\n")

    
    print("Updated list of your favorite fruits:")
    print_fruits(fruits)

def print_fruits(fruits):
    """Função para imprimir as frutas favoritas formatadas."""
    if not fruits:
        print("No fruits in the list.")
    else:
        print("Here's your favourite fruits:")
        for fruit in fruits:
            print(f"- {fruit}")  
    print()  

if __name__ == "__main__":
    main()
