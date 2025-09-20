favoritenumbers = []
print("================================================")
print("================================================")
print("Welcome to the favorte number Tracker!!!!!      ")
print("================================================")
print("================================================")

def shownum(num):
    shownumber = 0
    for item in num:
          print(shownumber ,":", item)
          shownumber =+ 1


def showmenu():
    print("MENU     : ↓ ")
    print("Add      : 'add'")
    print("Show     : 'show'")
    print("Remove   : 'remove'")
    print("Biggest  : 'biggest'")
    print("Smallest : 'smallest'")
    print("Sum      : 'sum'")
    print("Product  : 'product'")
    print("Quit     : 'quit'")


def add_num():
    choice = int(input("Give me a number: "))
    favoritenumbers.append(choice)

def show_number():
    if len(favoritenumbers) == 0:
            print("There are no numbers to show you")
    else:
        shownum(num=favoritenumbers)

def remove_num():
    if len(favoritenumbers) == 0:
        print("no numbers to remove")
    else:
        remove = int(input("give me a number to remove"))
        shownum(num=favoritenumbers)
        favoritenumbers.pop(remove)


def biggest():
    if len(favoritenumbers) == 0:
          print("there is no number to compare")
    else:
        biggest =  favoritenumbers[0]
        for b in favoritenumbers:
            if b > biggest:
                biggest =  b
        print(f"the biggest number is {biggest}")
                

    
def smallest():
    if len(favoritenumbers) == 0:
          print("there is no numbeer to compare")
    else:
        smallest =  favoritenumbers[0]
        for b in favoritenumbers:
            if b < smallest:
                smallest =  b
        print(f"the smallest number is {smallest}")

def add_all_num():
    if  len(favoritenumbers) == 0:
        print("no num to add")
    else:
        total = 0 
        for a in favoritenumbers:
            total += a 
        print(f"the sum is {total}")


def mult_all_num():
    if  len(favoritenumbers) == 0:
        print("no num to add")
    else:
        product = 1 
        for a in favoritenumbers:
               product *= a
        print(f"the product is {product}")

while True:
    showmenu()
    question = input("pick one: ")
    if question == "add":
        add_num()
    elif question == "show":
        show_number()
    elif question == "remove":
        remove_num()
    elif question == "biggest":
        biggest()
    elif question == "smallest":
        smallest()
    elif question == "sum":
        add_all_num()
    elif question == "product":
        mult_all_num()
    elif question == "quit":
        break