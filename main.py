"""---------Simple program to add and store recipes---------------------
   ---------Calulates calories based on serving size and weight---------"""



#Ingredient class that stores information about each ingredient
class Ingredient:
    def __init__(self, name, weight, calories):
        self.name = name
        self.weight = weight
        self.calories = calories

    def printIngredient(Ingredient):
        print("Ingredient Name: " + Ingredient.name + "\n" + "Ingredient weight: " + Ingredient.weight + " " + "grams\n" + "Ingredient calories: " + Ingredient.calories + "\n")
        return

#Entire recipe including a list of ingredients
class Recipe:
    def __init__(self, name, ingList, instructions):
        self.name = name
        self.instructions = instructions
        self.ingList = []  
    

    #prints the entire recipe
    def printRecipes():
        for i in range(len(RecipeList)):
            print("Recipe name: " + RecipeList[i].name + "\n")
            for k in range(len(RecipeList[i].ingList)):
                Ingredient.printIngredient(RecipeList[i].ingList[k])
          

    #adds the recipe to the recipe list
    def addRecipe():
        tempRecipe  = Recipe("temp", "temp", "temp")
        tempRecipe.name = input("Recipe name: ")
        count = 0
        num = int(input("List Number of Ingredients: "))
        currentList = []
        while count < num:
            tempIng = Ingredient("temp", "temp", "temp")
            tempIng.name = input("Ingredient name: ")
            tempIng.weight = input("Weight of Ingredient: ")
            tempIng.calories = input("Calories of Ingredient: ")
            currentList.append(tempIng)
            count = count + 1
        tempRecipe.ingList = currentList
        tempRecipe.instructions = "Do Something"
        return tempRecipe
        

    #calculate total weight
    def calcTotalWeight(self, Recipe):
        totalweight = 0.0
        for i in range(len(Recipe.ingList)):
            totalweight += float(Recipe.ingList[i].weight)
        return totalweight

    #calculate total calories
    def calcTotalCalories(self, Recipe):
        totalcalories = 0.0
        for i in range(len(Recipe.ingList)):
                totalcalories += float(Recipe.ingList[i].calories)   
        return totalcalories
       
        
def calcCaloriesServ(Recipe):
    print("How many servings? 1, 2, or 4?")
    serving = input()
    totalCal = Recipe.calcTotalCalories(Recipe)
    servingCal = totalCal / float(serving)
    print("Calories per " + str(serving) + " serving size " + str(servingCal) + "\n")
    

def calcWeightServ(Recipe):
    print("How much does your serving weigh in grams? ")
    weight = input()
    totalWeight = Recipe.calcTotalWeight(Recipe)
    totalCalories = Recipe.calcTotalCalories(Recipe)
    calorieServing = float((totalWeight / totalCalories) * float(weight))
    print("Calories for this serving " + str(calorieServing))

#shows the main menu
def showMenu():
    print("Choose an option below: ")
    print("1.View Recipes \n2.Add Recipe\n3.Calculate Recipe Info")
    choice = input()
    print(choice)
    if choice == "1":
        Recipe.printRecipes()
    elif choice == "2":
        newRecipe = Recipe.addRecipe()
        RecipeList.append(newRecipe)
    elif choice == "3":
        print("Which Recipe to Calculate? ")
        findRecipe = input()
        for i in range(len(RecipeList)):
            if findRecipe == RecipeList[i].name:
                print("Calculate 1.Calories or 2.Weight? ")
                choice2 = input()
                if choice2 == "1":
                    calcCaloriesServ(RecipeList[i])
                    break
                elif choice2 == "2":
                    calcWeightServ(RecipeList[i])    
    else:
        running = False
        
        
#main stuff
running = True
RecipeList = []
print("Welcome to Recipe Calculator!")
while (running):
    
    showMenu()
