# jogo-da-forca

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:34:23 2015

@author: Hugo Felix
"""

import turtle
from random import choice
window = turtle.Screen()
window.bgcolor('black')
window.title('Jogo da forca')
turtle.color('white')
answer="sim"
lista=[]
while True and answer=="sim":
    turtle.clear() 
    turtle.penup()
    turtle.setpos(-100,260)
    turtle.pendown()
    turtle.write('Bem vindo ao jogo da forca!', font=('Comic Sans MS',15,'normal'))
    turtle.pensize(3)
    turtle.speed(5)
    turtle.penup()
    turtle.setpos(-300,-200)
    turtle.pendown()
    turtle.setpos(-200,-200)
    turtle.setpos(-250,-200)
    turtle.setpos(-250,250)
    turtle.setpos(100,250)
    turtle.setpos(100,230)
    turtle.penup()
    turtle.setpos(-150,-200)
    turtle.pendown()
    f=open('entrada.txt',encoding='utf-8')
    p=f.readlines()
    e=choice(p)
    if e=='':
        e=choice(p)
    p.remove(e)
    e=e.strip().lower()
    erros=0
    acertos=0
    for i in e:
        if i!=' ':
            turtle.forward(20)
        else:
            turtle.penup()
            turtle.forward(20)
            turtle.pendown()
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()
    while erros<6 :
        letra=window.textinput('','Escolha uma letra:').lower().strip()
        turtle.pensize(3)
        if letra in e:
            lista.append(letra)
            acertos+=1
            turtle.penup()
            turtle.setpos(-150,-190)
            turtle.pendown()
            n=e.count(letra)
            i=-1
            j=0
            while j<n:
                i=e.index(letra,i+1)
                turtle.penup()
                turtle.setpos((-150+(i*25)),-195)
                turtle.pendown()
                turtle.write(letra,font=('Comic Sans MS',20,'normal'))
                j+=1
            if letra=='a' and e[i]==('ã' or 'á' or 'à'):
                turtle.penup()
                turtle.setpos((-150+(i*25)),-195)
                turtle.pendown()
                turtle.write(e[i],font=('Comic Sans MS',20,'normal'))
            if letra=='e' and e[i]==('é' or 'ê'):
                turtle.penup()
                turtle.setpos((-150+(i*25)),-195)
                turtle.pendown()
                turtle.write(e[i],font=('Comic Sans MS',20,'normal'))
            if letra=='i' and e[i]==('í'):
                turtle.penup()
                turtle.setpos((-150+(i*25)),-195)
                turtle.pendown()
                turtle.write(e[i],font=('Comic Sans MS',20,'normal'))
            if letra=='o' and e[i]==('ô' or 'õ' or 'ó'):
                turtle.penup()
                turtle.setpos((-150+(i*25)),-195)
                turtle.pendown()
                turtle.write(e[i],font=('Comic Sans MS',20,'normal'))
            if letra=='u' and e[i]==('ú'):
                turtle.penup()
                turtle.setpos((-150+(i*25)),-195)
                turtle.pendown()
                turtle.write(e[i],font=('Comic Sans MS',20,'normal'))
        else:
            erros+=1
        if len(lista)==len(e):

            turtle2=turtle.Turtle()
            turtle2.penup()
            turtle2.setpos(0,150)
            turtle2.color("white")
            turtle2.write("Ganhou!", font =("Arial", 20,"normal"))
        if erros==1:
            turtle.penup()
            turtle.setpos(100,160)
            turtle.pendown()
            turtle.circle(35)
        if erros==2:
            turtle.penup()
            turtle.setpos(100,160)
            turtle.pendown()
            turtle.setpos(100,90)
        if erros==3:
            turtle.penup()
            turtle.setpos(100,90)
            turtle.pendown()
            turtle.setpos(70,60)
        if erros==4:
            turtle.penup()
            turtle.setpos(100,90)
            turtle.pendown()
            turtle.setpos(130,60)
        if erros==5:
            turtle.penup()
            turtle.setpos(100,130)
            turtle.pendown()
            turtle.setpos(70,160)
        if erros==6:
            turtle.penup()
            turtle.setpos(100,130)
            turtle.pendown()
            turtle.setpos(130,160)
            turtle.penup()
            turtle.setpos(150,160)
            turtle.pendown()
            turtle.write('PERDEU!',font=('Comic Sans MS',20,'normal'))
            answer=window.textinput(' ','Deseja jogar mais uma vez?').lower().strip()
            if answer=='nao':
                turtle.penup()
                turtle.setpos(0,0)
                turtle.pendown()
                turtle.write('Obrigado por jogar.',font=('Comic Sans MS',20,'normal'))
            if answer=='não':
                turtle.penup()
                turtle.setpos(0,0)
                turtle.pendown()
                turtle.write('Obrigado por jogar.',font=('Comic Sans MS',20,'normal'))
window.exitonclick()

