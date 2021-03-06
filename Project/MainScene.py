import tkinter as tk
import configparser
import csv
import random
import pandas as pd
import QuestionScene
import numpy as np

class Game(tk.Frame):
    def __init__(self,master,size):
        super().__init__(master)
        self.pack()
        self.master = master
        self.pack()
        self.width = size[0]
        self.height = size[0]
        self.chip = 0
        self.master.geometry(str(self.width)+"x"+str(self.height))
        #ランダムに問題を抽出する
        #map_data = pd.read_csv(size[1])
        random_num = int(random.uniform(0,2))
        #self.map_question = map_data['question'][random_num]
        que_scene = QuestionScene.Question()
        #self.map_data =  que_scene.question_build([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        que_scene.question_build([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        self.map_img = que_scene.ques#問題
        print(self.map_img)
        self.map_data = self.map_img
        for i in range(len(self.map_img[0])):
            for j in range(len(self.map_img[0])):
                if self.map_img[i][j] != 0:
                    self.map_data[i][j] = self.map_img[i][j] + 4       
        print(self.map_data)
        # self.map_data = que_scene.question#表示用の問題
        #print(self.map_data)
        a = que_scene.dfs_build(self.map_img)
        #self.question = que_scene.solve4#答え
        print(self.map_data)
        print('答えは'+str(a))
        self.img = que_scene.map_data4#画像リスト
        #print(self.img)
        #print(self.map_data)
        self.num = len(self.map_data[random_num])
        #print(self.num)
        #print(type(self.map_data[random_num]))
        self.createWidgets()

    def createWidgets(self):
        self.cvs_bg = tk.Canvas(bg = "white",width = self.width,height=self.height)
        self.cvs_bg.place(x=10, y=10)
        #self.cvs_bg = tk.Canvas(width=360, height=360, bg="black")
        #self.cvs_bg.place(x=10, y=10)
        self.cvs_bg.bind("<Button-1>", self.set_map)
        self.cvs_bg.bind("<B1-Motion>", self.set_map)

        self.cvs_chip = tk.Canvas(width=60, height=340, bg="black")
        self.cvs_chip.place(x=330, y=10)
        self.cvs_chip = tk.Canvas(width=60, height=340, bg="black")
        self.cvs_chip.place(x=330, y=10)
        self.cvs_chip.bind("<Button-1>", self.select_chip)
        self.btn = tk.Button(text="回答する", font=("Times New Roman", 20), fg="blue", command=self.put_data)
        self.btn.place(x=120, y=350)
        #Image List
        #ques = QuestionScene.Question()
        #print(ques.map_data4)
        #self.img = ques.map_data4
        #self.map_data.shape
        #print(self.img)

        self.draw_map()
        self.draw_chip()

    def draw_map(self):
        self.cvs_bg.delete("BG")
        for y in range(self.num):
            for x in range(self.num):
                self.cvs_bg.create_image(60*x+30, 60*y+30, image=self.img[self.map_data[y][x]], tag="BG")
    def set_map(self,e):
        x = int(e.x/60)
        y = int(e.y/60)
        if 0 <= x and x <= (self.num-1) and 0 <= y and y <= (self.num-1):
            if self.map_data[y][x] <=self.num:#もし初期値の数字(与えられる問題の数字)じゃない場合、数字を書き込めるようにする。
                self.map_data[y][x] = self.chip
                self.draw_map() 
    #数字出力(右側)
    def select_chip(self,e):
        #global chip
        y = int(e.y/60)
        if 0 <= y and y < (self.num+1):
            self.chip = y
            self.draw_chip()

    #数字出力(右側)
    def draw_chip(self):
        self.cvs_chip.delete("CHIP")
        for i in range(self.num+1):
            self.cvs_chip.create_image(30, 30+i*60, image=self.img[i], tag="CHIP")
        self.cvs_chip.create_rectangle(4, 4+60*self.chip, 57, 57+60*self.chip, outline="red", width=3, tag="CHIP")

    #データ出力
    def put_data(self):
        print(self.question)
        print(self.map_img)
        if self.question == self.map_img:
            self.draw_txt("ゲームクリア",170,270,30,"pink")
        else:
            self.draw_txt("不正解！！",170,270,30,"blue")

           
    def draw_txt(self,txt, x, y, siz, col): # 文字をウィンドウに表示する
        fnt = ("Times New Roman", siz, "bold")
        self.cvs_bg.create_text(x+2, y+2, text=txt, fill="black", font=fnt, tag="SCREEN")
        self.cvs_bg.create_text(x, y, text=txt, fill=col, font=fnt, tag="SCREEN")

