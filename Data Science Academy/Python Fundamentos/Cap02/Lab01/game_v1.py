# Game Ping-Pong
#Import das bibliotecas
from tkinter import *
import random
import time

#Pergunta o level
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))
#Conforme o level escolhido, configura o tamanho da barra
length = 500/level


#Instância a biblioteca gráfica
root = Tk()
#Mostra um titulo na tela
root.title("Ping Pong")
#Permite ou não aumento da tela
root.resizable(0,0)
#motra a tela centralizada
root.wm_attributes("-topmost", -1)

#Tamanho da tela
canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
#Encapsula tudo
canvas.pack()
#Aplica configurações no obejto root
root.update()

# Variável
count = 0
lost = False

#Criação da classe bola
class Bola:
    #Define o constrututor da classe e suas variáveis
    def __init__(self, canvas, Barra, color):
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        starts_x = [-3, -2, -1, 1, 2, 3]
        #valor aleatório para bola se mover
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3
    
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    #Cria metódo para definir as coordenadas da barra
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)

        #compara a posição da bolinha com a barra, para saber se a barra conseguiu segurar a bola
        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1
                score()

        #se a bolinha atravessar, gameover
        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True

#Cria classe para controle da barra
class Barra:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    #controla o desenho da barra
    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)
    #Metodo controla movimento para esquerda
    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3
    #Metodo controla movimento para direita
    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3

#Inicia o jogo
def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1)
    Barra.draw()
    Bola.draw()

#Controla pontuação
def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

#Exibe menssagem Game over
def game_over():
    canvas.itemconfig(game, text="Game over!")

#Define cor da barra e da bolinha
Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")

#Define fonte, tamanho e cor da letra
score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game)

#mantem o jogo continuo
root.mainloop()
