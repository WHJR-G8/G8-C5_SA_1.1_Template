import turtle

turtle.showturtle()
turtle.shape('turtle')

side = int(input("Enter the side value"))

#For Student 1

#write the code for if block over here

    for x in range(20):
        turtle.fillcolor("")#Fill the color as "yellow"
        #Start the color filling
        turtle.forward(side)
        #write the code for if block over here
            turtle.left(175)
            turtle.pencolor("")#Make the pencolor as "red"
        else:
            turtle.left(225)
            turtle.pencolor("")#Make the pencolor as "green"

    #End the color fill

#For Student 2

#write the code for elif block over here

    for x in range(20):
        turtle.fillcolor("")#Fill the color as "cyan"
        #Start the color filling
        turtle.forward(side)
        #write the code for if block over here
            turtle.left(175)
            turtle.pencolor("")#Make the pencolor as "yellow"
        else:
            turtle.left(225)
            turtle.pencolor("")#Make the pencolor as "blue"

    #End the color fill

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
