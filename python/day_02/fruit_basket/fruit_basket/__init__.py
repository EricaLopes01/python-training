class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class FruitBasket:
    def __init__(self):
        self.fruits = []

    def add_fruit(self, fruit):
        self.fruits.append(fruit)

    def remove_fruit(self, fruit):
        if fruit in self.fruits:
            self.fruits.remove(fruit)

    def print_basket(self):
        for fruit in self.fruits:
            print(f"- {fruit.name} ({fruit.color})")

def main():

    basket = FruitBasket()

    while True:
        fruit_name = input("What is the fruit name? ")
        fruit_color = input("What is the fruit color? ")
        fruit = Fruit(fruit_name, fruit_color)
        basket.add_fruit(fruit)

        more = input("Do you want to add another fruit? (yes/no) ")
        if more.lower() != 'yes':
            break

    basket.print_basket()

    if basket.fruits:
        basket.remove_fruit(basket.fruits[0])
        basket.print_basket()
        
if __name__ == "__main__":
    main()
