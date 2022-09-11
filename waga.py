
print("Welcome to the average calculator. You can choose to calculate arithmetic or weighted average. If you want to calculate the arithmetic average type: arithmetic if it is to be weighted, type: weighted\n")

####### V ######
type = input("What type of average do you want to count?\n")
ratings = []
weights = []
maxlenghtlist = range(1,40)

####### FUNKCJE ######
def entry():
    while len(ratings) != maxlenghtlist:
        try:
            rating = input("Enter a rating:\n")
            ratings.append(int(rating))
        except:
            while rating == "stop":
                arithmetic()
                break
            break
def arithmetic ():
    x = sum(ratings)
    y= len(ratings)
    print("Your arithmetic average is:", x/y)
    # print(x/y)
def entry_weighted():
    while len(ratings) != maxlenghtlist:
        try:
            rating = input("Enter a rating:\n")
            weight = input("Enter a weight:\n")
            weights.append(int(weight))
            suma = int(rating)*int(weight)
            ratings.append(int(suma))
        except:
            while rating  == "stop":
                weighted()
                break
            break

def weighted():
    x = sum(ratings)
    y = sum(weights)
    print("Your weighted average is:")
    print(x / y)

#### program ####
if type == str("arithmetic"):
    entry ()
elif type == str("weighted"):
    entry_weighted()
else:
    print("Enter weighted or arithmetic")

