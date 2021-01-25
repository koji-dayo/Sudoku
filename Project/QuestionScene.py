from PIL import Image
import tkinter as tk

class Question:
    def __init__(self):
        #self.map_data =
        self.map_data4 = [
        tk.PhotoImage(file="image/black.png"),
        tk.PhotoImage(file="image/one.png"),
        tk.PhotoImage(file="image/two.png"),
        tk.PhotoImage(file="image/three.png"),
        tk.PhotoImage(file="image/four.png"),
        tk.PhotoImage(file="image/onered.png"),
        tk.PhotoImage(file="image/twored.png"),
        tk.PhotoImage(file="image/threered.png"),
        tk.PhotoImage(file="image/fourred.png")
        ]

        self.map_data9 = [
        tk.PhotoImage(file="image/black.png"),
        tk.PhotoImage(file="image/one.png"),
        tk.PhotoImage(file="image/two.png"),
        tk.PhotoImage(file="image/three.png"),
        tk.PhotoImage(file="image/four.png"),
        tk.PhotoImage(file="image/five.png"),
        tk.PhotoImage(file="image/six.png"),
        tk.PhotoImage(file="image/seven.png"),
        tk.PhotoImage(file="image/eight.png"),
        tk.PhotoImage(file="image/nine.png"),
        tk.PhotoImage(file="image/onered.png"),
        tk.PhotoImage(file="image/twored.png"),
        tk.PhotoImage(file="image/threered.png"),
        tk.PhotoImage(file="image/fourred.png"),
        tk.PhotoImage(file="image/fivered.png"),
        tk.PhotoImage(file="image/sixred.png"),
        tk.PhotoImage(file="image/sevenred.png"),
        tk.PhotoImage(file="image/eightred.png"),
        tk.PhotoImage(file="image/ninered.png")       
        ]

        #self.solve4 = [[[0,0,0,7],[0,7,0,8],[0,0,0,0],[5,0,0,0]],[[5,0,0,0],[0,0,7,0],[6,0,0,0],[0,0,6,0]],[[0,0,0,0],[0,0,0,5],[7,0,0,0],[0,8,6,0]]]
        self.solve4 = [[0,0,0,7],[0,7,0,8],[0,0,0,0],[5,0,0,0]]
        self.solve9 = []


    #問題の正解を判定する
    def judgment(self,solve_data):
        pass

