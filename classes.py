import random

############### Fruit classes ###############

class Fruit():
    def __init__(self):
        self.flavour, self.colour = random.choice(self.varieties)
    
    def __repr__(self):
        return f"<{self.flavour}, {self.colour}, {self.__class__.__name__}>"
    
    def __str__(self):
        return f"{self.__class__.__name__.lower()}"

class Apple(Fruit):
    varieties = [("sour", "green"), ("sweet", "red")]

class Pear(Fruit):
    varieties = [("mellow", "yellow"), ("sharp", "green")]

############## Tree classes #################

class Tree():
    def __init__(self):
        self.fruits = []
    
    def __repr__(self):
        return f"{self.fruit_type.__name__} tree"

    def blossom(self):
        for i in range(self.fecundity):
            self.fruits.append(self.fruit_type())

    def harvest(self):
        crop = self.fruits
        self.fruits = []
        return crop

class AppleTree(Tree):
    fecundity = 3
    fruit_type = Apple

class PearTree(Tree):
    fecundity = 5
    fruit_type = Pear

############## Cider Class #################

class Cider():
    def __init__(self, fruitlist):
        self.type = fruitlist[0]
        self.flavour = {
            "sweet": 0,
            "sour": 0,
            "mellow": 0,
            "sharp": 0
        }
        for fruit in fruitlist:
            self.flavour[fruit.flavour] += 1
    
    def __repr__(self):
        return f"a barrel of {max(self.flavour, key=lambda key: self.flavour[key])} {self.type} cider"

############## Farm Class #################

class Farm():
    def __init__(self, orchard={}) -> None:
        if not orchard:
            print("Welcome")
            apple = int(input("How many apple trees would you like to plant? "))
            pear = int(input("How many pear trees would you like to plant? "))
            self.orchard = {"apples":apple, "pears":pear}
        else:
            self.orchard = orchard
        self.plant_trees()
        self.spring()
        apple_crop, pear_crop = self.autumn_harvest()
        self.brew_cider(apple_crop)
        self.brew_cider(pear_crop)

    def __repr__(self) -> str:
        return f"{self.orchard}"

    def plant_trees(self):
        self.apple_trees = [AppleTree() for tree in range(self.orchard["apples"])]
        self.pear_trees = [PearTree() for tree in range(self.orchard["pears"])]
        print("All apple trees and pear trees have been planted")

    def spring(self):
        for tree in self.apple_trees:
            tree.blossom()

        print("All apple trees have blossomed, yay 🍎")        
        for tree in self.apple_trees:
            print(tree.fruits)
        
        for tree in self.pear_trees:
            tree.blossom()

        print("All pear trees have blossomed, yay 🍐")        
        # for tree in self.pear_trees:
        #     print(tree.fruits)

    def autumn_harvest(self):
        apple_crop = []
        for tree in self.apple_trees:
            apple_crop.extend(tree.harvest())

        pear_crop = []
        for tree in self.pear_trees:
            pear_crop.extend(tree.harvest())

        # print("Apple Harvest", apple_crop)
        # print("Pear Harvest", pear_crop)
        return (apple_crop, pear_crop)
    
    def brew_cider(self, fruitlist):
        new_barrel = Cider(fruitlist)
        print(new_barrel)