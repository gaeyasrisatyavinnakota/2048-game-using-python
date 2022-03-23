## 2048 game using python
# Code In Place 2021 Final Project 
#Gaeya Sri Satya Vinnakota 
"""
In this project, I have basically recreated the "2048 game". which is a quite popular game having a grid with numbered tiles and is played by moving left, right, up or down. There will be change in the number on the tiles if any tile was moved or merged with a tile with same number on it which was done using the controls. If there is no legal move then the game ends. 
I have recreated the game with 4*4 grid and tiles being numbered as 0(represents the empty tile), 2, 4, 8, 16 and so on (multiples of 2) with the controls as A(left),W(up),S(down),D(right).
Hope the one plays it enjoys the game as much as I enjoyed learning the python programming in Code In Place 2021 and creating this game..
Link to the Code: https://drive.google.com/file/d/1-Aq3rFl0eJTTpQjXg0e7hmzwYbWqQVze/view?usp=sharing
"""

#------------importing specific functions from modules--------------#
from math import log
from random import randint

#---------defining the display framework and score for the game-------#
matrix = [[0 for i in range(4)] for j in range(4)]  #creating a matix for the framework of the 2048 game
score = 0                                           #defining the score of the player of the game



"""
This function does the process of merging 
i.e..,. the main game algorithm..
""" 
def merge(count):
    global matrix,score
    for i in range(count):
        matrix = list(zip(*matrix[::-1]))
    result = []
    for numbers in matrix:
        prev = None
        store = []
        for next_ in numbers:
            if not next_:
                continue 
            if prev is None:
                prev = next_
            elif prev == next_:
                score += prev
                store.append(prev + next_)
                prev = None
            else:
                store.append(prev)
                prev = next_
        if prev is not None:
            store.append(prev)
        store.extend([0] *(4 - len(store)))
        result.append(store)
    for i in range(-count % 4):
        result = list(zip(*result[::-1]))
        matrix = list(zip(*matrix[::-1]))
    matrix = [list(i) for i in matrix]
    result = [list(i) for i in result]
    if result != matrix:
        matrix = result
        insert_number()
    else:
        zeros = 0
        for i in matrix:
            zeros += i.count(0)
        if zeros == 0:
            print("Game Over\t Score =",score)
            exit(0)



"""
This function takes the input and performs the next required action
i.e.,. does rearrangement if the input is among the feasible ones
and tells player the feasible keys if the input is not among the feasible ones
"""
def rearrange(ip):
    count = {'w': 3, 'a': 0, 's': 1,'d': 2}
    if ip in count:
        merge(count[ip])
    else:
        print("W|S|A|D only")



"""
This function prints the matrix
"""
def print_matrix():
    print("+" + "-" * 35 + "+")
    for i in matrix:
        c = "|"
        for j in i:
            print("|{:4d}".format(j), end="    ")
        if i == matrix[-1]:
            c = "+"
        print("|\n" + c + "-"*35 + c)
    print("score =",score)



"""
This function generates the initial matrix of the game
from which the player starts the game
"""
def insert_number():
    global matrix
    zeros = []
    for i in matrix:
        for j in i:
            if j == 0:
                zeros.append((matrix.index(i), i.index(j)))
    if len(zeros) == 0:
        print("Game Over\t score=",score)
        exit(0)
    position = zeros[randint(0, len(zeros)-1)]
    high = max(max(matrix, key=lambda x: max(x)))
    if high !=0:
        high = log(high, 2)
    else:
        high=1
    matrix[position[0]][position[1]] = 2**randint(1, high)



def main():
    print("Controls:\tW - Up | S - Down | A - Left | D - Right")         #printing the details of the control that has to be used by the player.
    insert_number()                                                         # generating the initial matrix
    while True:
        print_matrix()                                                   # printing the matrix
        ch = input("next move-->").lower()                               #taking the input 
        rearrange(ch)                                                    #genrating the result 

if __name__ == '__main__':
    main()