class Basket:
    def __init__(self, owner, size):
        self.owner=owner
        self.size=size
        self.content= []

        print("fNova cesta iniciada para o {owner}!")


    def add_content(self, content):
        if not len(self.content) < self.size:
            print("Cesta cheia!")
            return
        

        self.content.append(content)


if __name__ == "__main__":
    basket_a= Basket(owner="Diogo", size=10)
    basket_b= Basket(owner="Henrique", size=10)

    basket_a.add_content("apple")

    print(basket_a.content)