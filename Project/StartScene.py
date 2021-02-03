from functools import partial
from PIL import Image, ImageTk
import tkinter as tk
import numpy as np
import configparser
import yaml
import MainScene
#Start Menu
#最初の起動画面
title_logo = "image/gametitle.png"
sudoku_name = None
class Start(tk.Frame):
    def __init__(self,master):
        self.master = master
        super().__init__(self.master)
        with open('config.yaml','r') as file:
            self.config = yaml.load(file,Loader=yaml.SafeLoader)
        self.pack()
        self.master.title("Game")
        self.createWidgets()

    def createWidgets(self):
        global im,sudoku_name
        read_image = Image.open("Image/gametitle.png")
        self.canvas = tk.Canvas(self,width=read_image.width,height=read_image.height)#キャンパスサイズ
        self.canvas.grid(row=0,column=0)
        im = ImageTk.PhotoImage(image=read_image)
        self.canvas.create_image(0, 0, anchor='nw', image=im)
        for i in range(0,len(self.config['Sudoku_type_btn'])):
            self.btn = tk.Button(self.master,text=self.config['Sudoku_type_btn'][i],foreground='#ff0000',font=("", 20),width = 20,height=3,bg="black",command=partial(self.newWindow,self.config['Sudoku_name'][i]))
            self.btn.place(x=120,y=250+(i*100))
            #print(self.btn)
            
    def newWindow(self,name):
        game = MainScene.Game(self.master,self.config[name])
        game.mainloop()
        
def main():
    root = tk.Tk()
    root.resizable(width=False,height=False)
    start = Start(master=root)
    start.mainloop()

if __name__ == '__main__':
    main()

