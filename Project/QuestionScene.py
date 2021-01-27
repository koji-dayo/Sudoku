from PIL import Image
import tkinter as tk
import numpy as np
import random
import DFS


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
        self.solve4 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.solve9 = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[
            0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        self.solve_map4 = None
        self.question = None
    '''
    問題を生成する。その際、4x4,9x9のどちらかを判定する。
    数独の問題を生成する。まず答えを算出し答えを算出した後ランダムに数字を残す(0に変えるものと数字を残すもの)
    答えはリストになっており、0を代入していく.
    (設定ファイルに事前に複数個、何列穴埋めするか設定しておく。)
    4x4か9x9で条件分岐
    ある行だけ複数個なの事前に設定する。
    '''

    def question_build(self,ques_list):
        #ques_list:問題の空リスト
        #listが何次元か読み取る。
        num_list = len(ques_list)
        k = list(range(1,num_list))

        if num_list == 4:
            k_list = random.sample(k,2)#複数の乱数が含まれる
            num = random.sample(k,2)
            ques_list[0][1] = int(random.uniform(0,num_list+1))
            ques_list[0][2] = int(random.uniform(0,num_list+1))
            ques_list[1][1] = int(random.uniform(0,num_list+1))
            ques_list[2][1] = int(random.uniform(0,num_list+1))
            ques_list[3][3] = int(random.uniform(0,num_list+1))
            #print(ques_list)
            for i in range(num_list):
                for j in range(num_list):
                    if ques_list[i][j] != 0:
                        ques_list[i][j] += 4
            print(ques_list)

            self.question = ques_list
            print(self.question)
            #print(ques_list)
            #ques_list[num_random][num_random] = int(random.uniform(0,len(num_list)+1))
            #深さ優先探索により答えを入手、答えが帰ってこない場合はやり直す。
            sudoku_dfs = DFS.Sudoku_DFS()
            sudoku_dfs.question = ques_list
            sudoku_dfs.solve(sudoku_dfs.question,0,0)
            sudoku_question = sudoku_dfs.question#答え
            if  sudoku_question[0][0] == 0 :
                #print('やり直し')
                self.question_build(self.solve4)
            else:     
                #print('hi')
                #print(sudoku_dfs.question)
                a = sudoku_dfs.question
                #print(a)
                self.solve4 = a#答え
                self.ques = ques_list#問題
        elif num_list == 9:
            k_list = random.sample(k,3)
            num = random.sample(k,3)
            for i in range(num_list):
                ques_list[i][k_list[i]] = num 
                ques_list[i][k_list[i]] = num
                ques_list[i][k_list[i]] = num
        
    #問題の正解を判定する
    def judgment(self,solve_data):
        pass

'''
if __name__ == '__main__':
    ques = Question()
    ques.question_build([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    '''