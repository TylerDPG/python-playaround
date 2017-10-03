import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("pink")
    brad.speed(12)
    
    for square in range(360/15):
        for turn in range(4):
            brad.forward(100)
            brad.right(90)
            turn += 1
        brad.right(15)
        square += 1
    brad.right(90)
    brad.forward(200)
 
    andy = turtle.Turtle()
    andy.circle(100)
    andy.shape("circle")
    andy.color("blue")
    andy.speed(3)

    lan = turtle.Turtle()
    lan.shape("arrow")
    lan.color("yellow")
    lan.speed(3)

    for triangle_turn in range(3):
        lan.forward(120)
        lan.left(120)
        turn += 1
    
    window.exitonclick()

draw_shapes()
