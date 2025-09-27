'''Rajzol egy 150 pontos
egyenlő szárú háromszöget a képernyő közepére
A színe legyen piros
A rajzolás induljon a h betűre
Kilépés legyen q betűre
'''
import turtle

def inditas():
    turtle.hideturtle()
    turtle.clear()
    turtle.pencolor("red")
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(-75, -37.5)
    turtle.pendown()

    for i in range(3):
        turtle.forward(150)
        turtle.left(120)


#applikáció
ablak = turtle.Screen()
ablak.bgcolor("gray")

turtle.onkey(inditas, "h")
turtle.listen()
turtle.onkey(turtle.bye, "q")
turtle.mainloop()
