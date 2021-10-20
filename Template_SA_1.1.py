import turtle

turtle.showturtle()
turtle.shape('turtle')

side = int(input("Enter the side value"))

#For Student 1

#Hint 1: Write an "if" condition to obtain side value greater than 0 and less than or equal to 100.

    for x in range(20):
        turtle.fillcolor("")#Hint 2: Fill the color as "yellow".
        turtle.begin_fill()
        turtle.forward(side)
        
        #Hint 3: Write an "if" condition, "if x%2==0", inside the "for" loop.
            turtle.left(175)
            turtle.pencolor("")#Hint 4: Make the pencolor as "red"
            
        #Hint 5: Write an "else" condition.
            turtle.left(225)
            turtle.pencolor("")#Hint 6: Make the pencolor as "green".

    turtle.end_fill()

#For Student 2

#Hint 1: Write an "elif" condition to obtain side values greater than 100 and less than equal to 200.

    for x in range(20):
        turtle.fillcolor("") #Hint 2: Fill the color as "cyan"
        turtle.begin_fill()
        turtle.forward(side)
        
        #Hint 3: Write an "if" condition, "if x%2==0".
            turtle.left(175)
            turtle.pencolor("") #Hint 4: Make the pencolor as "yellow"
            
        #Hint 5: Write an "else" condition.
            turtle.left(225)
            turtle.pencolor("") #Hint 6: Make the pencolor as "blue"

    turtle.end_fill()

else:
    
        for x in range(20):
            turtle.fillcolor("red")
            turtle.begin_fill()
            turtle.forward(side)
            if x % 2 == 0:
                turtle.left(175)
                turtle.pencolor('orange')
            else:
                turtle.left(225)
                turtle.pencolor('cyan')

        turtle.end_fill()   

        turtle.end_fill()    

turtle.ht()
