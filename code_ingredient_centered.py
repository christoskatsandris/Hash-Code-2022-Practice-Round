class Client:
    def __init__(self):
        self.likedIngredients = []
        self.dislikedIngredients = []
    
    def addLikedIngredient(self, ingredient):
        self.likedIngredients.append(ingredient)
    
    def addDislikedIngredient(self, ingredient):
        self.dislikedIngredients.append(ingredient)
    
class Pizza:
    def __init__(self):
        self.ingredients = []
        self.likes = 0

    def addIngredient(self, ingredient):
        self.ingredients.append(ingredient)
    
    def updateLikes(self):
        pass

class Ingredient:
    def __init__(self, name):
        self.name = name
        self.likedBy = 0
        self.dislikedBy = 0
        self.likedByPercentage = 0
        self.dislikedByPercentage = 0
        self.score = 0

    def addLike(self):
        self.likedBy += 1
        self.calcPercentages()

    def addDislike(self):
        self.dislikedBy += 1
        self.calcPercentages()

    def calcPercentages(self):
        self.likedByPercentage = self.likedBy / (self.likedBy + self.dislikedBy)
        self.dislikedByPercentage = self.dislikedBy / (self.likedBy + self.dislikedBy)
        self.score = self.likedByPercentage - self.dislikedByPercentage

clients = []
ingredients = []

def main():
    filenames = ["a_an_example", "b_basic", "c_coarse", "d_difficult", "e_elaborate"]
    for filename in filenames:
        clients.clear()
        ingredients.clear()

        readData(f"Inputs\\{filename}.in.txt")
        sortIngredientsByPoints()
        pizza = makePizza()
        logData(f"Outputs\\{filename}.out.txt", pizza)
        print(f"{filename} done.")

def readData(filename):
    with open(filename, "rt") as data:
        howManyClients = int(data.readline())
        
        for clientIterator in range(howManyClients):
            newClient = Client()
            clients.append(newClient)
            likedIngredientsInput = data.readline().split(' ')
            dislikedIngredientsInput = data.readline().split(' ')
            
            for ingredientIterator in range(1, int(likedIngredientsInput[0])+1):
                currentIngredient = getIngredient(likedIngredientsInput[ingredientIterator].rstrip())
                newClient.addLikedIngredient(currentIngredient)
                currentIngredient.addLike()
            for ingredientIterator in range(1, int(dislikedIngredientsInput[0])+1):
                currentIngredient = getIngredient(dislikedIngredientsInput[ingredientIterator].rstrip())
                newClient.addDislikedIngredient(currentIngredient)
                currentIngredient.addDislike()
    
def getIngredient(ingredient):
    for savedIngredient in ingredients:
        if savedIngredient.name == ingredient:
            return savedIngredient

    newIngredient = Ingredient(ingredient)
    ingredients.append(newIngredient)
    return newIngredient

def sortIngredientsByPoints():
    ingredients.sort(key = lambda ingredient: ingredient.score, reverse = True)

def makePizza():
    newPizza = Pizza()

    for ingredient in ingredients:
        if (ingredient.score < 0.1):
            break
        newPizza.addIngredient(ingredient)

    return newPizza

def logData(filename, pizza):
    with open(filename, "wt") as log:
        print(f"{len(pizza.ingredients)}", file=log, end='')
        for ingredient in pizza.ingredients:
            print(f" {ingredient.name}", file=log, end='')

if __name__ == "__main__":
    main()