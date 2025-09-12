favoriteNumbers = ()
print("========================================")
print("========================================")
print("========================================")
print("========================================")
print("Welcome to the favrotie Number tracker!!")
print("========================================")
print("========================================")
print("========================================")
print("========================================")

def shownum(num):
    Counter = 0
    for e in num:
                print(Counter, ":", e)
                Counter += 1



def show_menu():
    print("if you want to add → to add a number type 1 ")
    print("if you want to show → to show all  numbers type 2 ")
    print("if you want to remove → to remove a number type 3 ")
    print(" type 4 to show the biggest number")
    print("type 5 if you want to see the smallest number ")
    print("if you want to quit → to quit  type 6 ")
    print("if you want to sum → to add all of the numbers type 7 ")
    print("if you want to product → to * all the numbers  type 8 ")



def add_number():
    choice = input("pick one: ")
    if choice == '1':
       number = int(input("what number: "))
       favoriteNumbers.append(number)
       print("you number has been added")

def show_number():
    if len(favoriteNumbers) == 0:
            print("There are no numbers to show you")
    else:
        shownum(num=favoriteNumbers)

def remove_number():
    if len(favoriteNumbers) == 0:
            print("There are no numbers to remove")
    else:
        shownum(num=favoriteNumbers)
def biggest_numbers(big):
    if len(favoriteNumbers) == 0:
          print("no numbers to compare")
    else:
         
            
        

def smallest_numbers():
    if len(favoriteNumbers) == 0:
          print("no numbers to compare")
    else:
         