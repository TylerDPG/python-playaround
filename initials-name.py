import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("gray")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("pink")
    brad.speed(12)

    brad.forward(100)
    brad.left(180)
    brad.forward(50)
    brad.left(90)
    brad.forward(100)

    wye = turtle.Turtle()
    wye.shape("turtle")
    wye.color("pink")
    wye.speed(12)

    wye.turtle.setx(90)
    wye.left(90)
    wye.forward(50)
    wye.left(60)
    wye.forward(54)
    wye.left(180)
    wye.forward(54)
    wye.right(60)
    
    window.exitonclick()

draw_shapes()
