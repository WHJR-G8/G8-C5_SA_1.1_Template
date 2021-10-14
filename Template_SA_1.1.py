import turtle

turtle.showturtle()
turtle.shape('turtle')

side = int(input("Enter the side value"))

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

else:
    
        for x in range(20):
            turtle.fillcolor("red")
            turtle.begin_fill()
            turtle.forward(side)
            if x % 2 == 0:
                turtle.left(175)
                turtle.pencolor('blue')
            else:
                turtle.left(225)
                turtle.pencolor('yellow')

        turtle.end_fill()    

turtle.ht()
