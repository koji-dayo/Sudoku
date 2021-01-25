from PIL import Image
import tkinter as tk
import numpy as np
import random


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
        self.solve4 = [[],[],[],[]]
        self.solve9 = [[],[],[],[],[],[],[],[]]
    '''
    問題を生成する。その際、4x4,9x9のどちらかを判定する。
    数独の問題を生成する。まず答えを算出し答えを算出した後ランダムに数字を残す(0に変えるものと数字を残すもの)
    答えはリストになっており、0を代入していく.
    '''

    def question_build(self,ques_list):
        #ques_list:問題の空リスト
        #listが何次元か読み取る。
        num_list = len(ques_list)
        num_random = int(random.uniform(0,len(num_list)+1))
        for i in range(len(ques_list)):
            for j in range(len(ques_list)):
                
                

        
    #問題の正解を判定する
    def judgment(self,solve_data):
        pass

