import turtle
import math

def vykresli(x, y, n):
    # Nastavení turtle plátna
    turtle.screensize(300, 300)
    turtle.setup(width=500, height=500)
    turtle.speed(2)
    
    # Nastavení barev
    initials_color = "blue"
    polygon_color = "red"
    
    # Přesun na levý horní roh oblasti 100x100 pixelů
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Nastavení barvy pro iniciály a vykreslení
    turtle.pencolor(initials_color)
    
    # Kreslení iniciály "J"
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x + 20, y)
    turtle.goto(x + 20, y - 25)

    turtle.goto(x - 5, y - 25)
    turtle.goto(x - 5, y - 15)
    
    # Kreslení iniciály "K"
    turtle.penup()
    turtle.goto(x + 40, y)
    turtle.pendown()
    turtle.goto(x + 40, y - 30)
    turtle.penup()
    turtle.goto(x + 40, y - 15)
    turtle.pendown()
    turtle.goto(x + 55, y)
    turtle.penup()
    turtle.goto(x + 40, y - 15)
    turtle.pendown()
    turtle.goto(x + 55, y - 30)

    # Přesun pod iniciály pro vykreslení n-úhelníku
    turtle.penup()
    turtle.goto(x + 70, y + 15)
    turtle.pendown()
    
    # Nastavení barvy pro polygon
    turtle.pencolor(polygon_color)

    # Výpočet délky strany a úhlu pro pravidelný n-úhelníku
    if n < 3:
        print("Počet stran musí být větší než 2.")
        return
    
    side_length = 30
    angle = 360 / n

    # Vykreslení pravidelného n-úhelníku
    for _ in range(n):
        turtle.forward(side_length)
        turtle.right(angle)
    
    turtle.hideturtle()
    turtle.done()

# Příklad volání funkce
vykresli(-50, 50, 5)
