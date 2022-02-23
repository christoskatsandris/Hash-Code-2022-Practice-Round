class Client:
    def __init__(self):
        self.likedIngredients = []
        self.dislikedIngredients = []
        self.points = 0
    
    def addLikedIngredient(self, ingredient):
        self.likedIngredients.append(ingredient)
    
    def addDislikedIngredient(self, ingredient):
        self.dislikedIngredients.append(ingredient)

    def calcPoints(self):
        self.points = len(self.likedIngredients) - len(self.dislikedIngredients)
    
class Pizza:
    def __init__(self):
        self.ingredients = []
        self.likes = 0

    def addIngredient(self, ingredient):
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)
            return True
        else:
            return False

    def removeIngredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            return True
        else:
            return False


class Ingredient:
    def __init__(self, name):
        self.name = name
        self.likedBy = 0
        self.dislikedBy = 0
        self.points = 0

    def addLike(self):
        self.likedBy += 1

    def addDislike(self):
        self.dislikedBy += 1

    def calcPoints(self):
        self.points = self.likedBy - self.dislikedBy

clients = []
ingredients = []

def main():
    filenames = ["a_an_example", "b_basic", "c_coarse", "d_difficult", "e_elaborate"]
    for filename in filenames:
        clients.clear()
        ingredients.clear()

        readData(f"Inputs\\{filename}.in.txt")
        sortClientsByPoints()
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

def sortClientsByPoints():
    for client in clients:
        client.calcPoints()
    clients.sort(key = lambda client: client.points, reverse=True)

def makePizza():
    newPizza = Pizza()

    for client in clients:
        if client.points < 0:
            break
        for likedIngredient in client.likedIngredients:
            newPizza.addIngredient(likedIngredient)
        for dislikedIngredient in client.dislikedIngredients:
            newPizza.removeIngredient(dislikedIngredient)

    return newPizza

def logData(filename, pizza):
    with open(filename, "wt") as log:
        print(f"{len(pizza.ingredients)}", file=log, end='')
        for ingredient in pizza.ingredients:
            print(f" {ingredient.name}", file=log, end='')

if __name__ == "__main__":
    main()