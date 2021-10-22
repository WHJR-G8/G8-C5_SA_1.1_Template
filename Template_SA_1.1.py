import turtle

turtle.showturtle()
turtle.shape('turtle')

side = int(input("Enter the side value"))

#For Student 1


    for x in range(20):
        turtle.fillcolor("")
        turtle.begin_fill()
        turtle.forward(side)
        
       
            turtle.left(175)
            turtle.pencolor("")
            
        
            turtle.left(225)
            turtle.pencolor("")
            
    turtle.end_fill()

#For Student 2


    for x in range(20):
        turtle.fillcolor("")
        turtle.begin_fill()
        turtle.forward(side)
        
       
            turtle.left(175)
            turtle.pencolor("")
            
        
            turtle.left(225)
            turtle.pencolor("")

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
