import turtle

turtle.showturtle()
turtle.shape('turtle')

side = int(input("Enter the side value"))

#write the code for if block over here

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
