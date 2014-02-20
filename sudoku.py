#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
This software generates a empty matrice and purpose to
solve, by specifying constant values, the Sudoku,
if possible.
'''

from Tkinter import *

###[ DISPLAY ]###

class aCase:
    def __init__(self, root, r, c):
        self.dValue = StringVar()
        self.ent = Entry(root, textvariable=self.dValue, width=2)
        self.ent.grid(row=r, column=c)

    def getValue(self):
        if self.ent.get()=='' or int(self.ent.get())<1 or int(self.ent.get())>9:
            return 0

        return int(self.ent.get())

    def putValue(self, v):
        self.dValue.set(v)

class Application(Tk):
    def __init__(self):
        self.root = Tk()
        self.root.title('Solver Sudoku')

        self.solve = Button(self.root, text="Go !", command=self.SolveMe)
        self.quitt = Button(self.root, text="Exit", command=self.OutMe)
        self.newpl = Button(self.root, text='New', command=self.newp)

        self.solve.grid(row=10, column=0, columnspan=5)
        self.quitt.grid(row=10, column=2, columnspan=6)
        self.newpl.grid(row=10, column=6, columnspan=5)

        self.case = []
        for i in range(9):
            for j in range(9):
                self.case += [aCase(self.root, i+1, j)]

    def OutMe(self):
        del(self.case)
        self.root.destroy()
        self.root.quit()
    
    def newp(self):
    	for i in range( len(self.case) ):
    		self.case[i].putValue('')

    def SolveMe(self):
        self.matrice = [0] * 9
        for i in range(0, 9):
            self.matrice[i] = [0] * 9

        self.n = 0
        for i in range( len(self.matrice) ):
            for j in range( len(self.matrice) ):
                self.matrice[i][j] = self.case[self.n].getValue()
                self.n+=1

        self.resolved = Solver(self.matrice)

        self.n = 0
        for i in range( len(self.resolved) ):
            for j in range( len(self.resolved) ):
                self.case[self.n].putValue(self.resolved[i][j])
                self.n+=1

###[ RESOLUTION ]###

def valid(v, i, j, g):
    for a in range( len(g) ):
        if g[a][j]==v or g[i][a]==v:
            return False

    if i < 3:
        f = 0
        if j < 3:
            h = 0
        elif j < 6:
            h = 3
        else:
            h = 6
    elif i < 6:
        f = 3
        if j < 3:
            h = 0
        elif j < 6:
            h = 3
        else:
            h = 6
    else:
        f = 6
        if j < 3:
            h = 0
        elif j < 6:
            h = 3
        else:
            h = 6

    for d in range(f, f+3):
        for e in range(h, h+3):
            if g[d][e]==v:
                return False

    return True

def Solver(g):
    for i in range( len(g) ):
        for j in range( len(g) ):
            if g[i][j]==0:
                n = 0
                for k in range(1, 10):
                    if valid(k, i, j, g)==True:
                        n = 1
                        g[i][j] = k
                        if Solver(g)==0:
                            g[i][j]=0
                            n = 0
                if n==0:
                    return 0
    return g

app = Application()
app.root.mainloop()
