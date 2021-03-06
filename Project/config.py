import yaml
import tkinter as tk

config = {
    'Sudoku_type_btn': [
        '4x4',
        '6x6',
    ],
    'Sudoku4': [
        450,
        'Question/question4.txt',
        'Question/solve4.txt',
    ],
    'Sudoku9':[
        700,
        'Question/question9.txt',
        'Question/solve9.txt',
   ],
    'Sudoku_name':[
        'Sudoku4',
        'Sudoku6',
    ],
    'question_path':[
        'Question/question'
    ]
    
}
with open('config.yaml', 'w') as file:
    yaml.dump(config, file)

