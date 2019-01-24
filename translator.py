
# Spanish Dictionary

#This program works as a dictionary that translates english words into spanish.
#get word from the user to get translate into spanish
def translate(a):
    print("The tanslation of " +a, " in spanish is ", spanish.get(a))
    
    
#function to draw the turtle graph(cover of the dictionary)
def turtlegraph():
    import turtle


    turtle.begin_fill()
    turtle.width(10)
    for i in range(4):
       
        turtle.forward(300)
        turtle.right(90)
    turtle.color("yellow")    
    turtle.end_fill()

    turtle.penup()
    turtle.goto(70,-60)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.circle(25)

    turtle.penup()
    turtle.goto(90,-60)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.circle(25)


    turtle.penup()
    turtle.goto(160,-285)
    turtle.pendown()
    turtle.color("blue")
    turtle.begin_fill()
    turtle.circle(100, extent=720, steps=5)
    turtle.end_fill()

#This is the list of the english and spanish words in the dictionary.
#constant
spanish = {"hello": "hola",
           "bye": "adios",
           "good": "bien",
           "bad" : "malo",
           "how" : "como",
           "angry" : "enojado(a)",
           "animal": "animal",
           "ant" : "hormiga",
           "here" : "aqui",
           "far" : "lejos",
           "between" : "entre",
           "awareness" : "conciencia,alerta",
           "baby" : "bebé",
           "back": "espalda",
           "bee" : "abeja",
           "beef" : "carne de res/vaca",
           "bite" : "morder",
           "cake": "pastel",
           "cabbage" : "col, repollo",
           "cell" : "célula",
           "cheese" : "queso",
           "chicken" : "pollo"
           
           }

#set true for the menu in the program
program = True

#Display The dictionary at the beginning of the program
for key,val in sorted(spanish.items()):
            print (key,"=", val)


#Loop of the program
try:
    while True:
        #main menu
        print("\nWelcome to the translator!")
        answer = int(input("""
                       0 = Quit
                       1 = Look Up a term
                       2 = Add a term
                       3 = Redefine a term
                       4 = Delete a term
                       5 = Display the Dictionary
                       6 = Display Dictionary cover\n
                       """))


        #if input is 0 or 6 display the cover of the dictionary
        if (answer == 0 or answer ==6):
            print("BYE, thank you for using the translator!")
            turtlegraph()
            break
          
        #if input is 1. get word that user wants to translate in spanish.
        elif (answer == 1):
            a = input("What would you like to have translated? ")
            translate(a)
            #print("The tanslation of " +a, " in spanish is ", spanish.get(a))
            
            
        #gets a word that user wants to add into the dictionary with the translation in spanish.
        elif (answer == 2):
            b = input("Enter the term you woul like to add: ")
            b1 = input("Meaning in Spanish: ")
            spanish[b]=b1
            #for key,val in sorted(spanish.items()):
                #print (key,"=", val)

            
        # gets the word that the user wants to redefine: change the meaning or add
        # more definitions. 
    
        elif (answer == 3):
            c = input(" Enter the term you would like to redefine: ")
            c1 = input("New meaning: ")
            spanish[c] = c1
            #for key,val in sorted(spanish.items()):
                #print (key,"=", val)

            
        #Get the term that the user wants to delete from the dictionary
        elif (answer == 4):
            d = input("Enter the term you would like to delete: ")
            del spanish[d]
            print("The word "+ d, " has been deleted form the dictionary. ")
            print("New dictionary: \n")
            #for key,val in sorted(spanish.items()):
                #print (key,"=", val)
    
        #Display the dictionary into the screen. 
        elif (answer == 5):
            for key,val in sorted(spanish.items()):
                print (key,"=", val)
        
            
#return false to the main program. 
except:
    program = False
