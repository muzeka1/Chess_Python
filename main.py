import tkinter as tk 

class Main():
    def __init__(self, root):
        self.isPressed = False
        self.main_figures = ["rook", "knight", "bishop", "king", 
                             "queen", "bishop", "knight", "rook"]
        self.board = [[""]*8]*8
        self.init_main(root)
        
    def move(self, cell_name, cell_figure):
        if not self.isPressed and cell_figure != "":
            print('нажали на фигуру ', cell_name, cell_figure)
            self.isPressed = True
        else:
            print('делается ход какой-то на клетку ', cell_name)
            self.isPressed = False
        

    def init_main(self, root):
        # Создаем фрейм для шахматной доски
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        color = ["black", "white"]
        for i in range(0, 8):
            for j in range(0, 8):
                if i == 0 or i == 7:
                    text = self.main_figures[j]
                elif i == 1 or i == 6:
                    text = "pawn"
                else: 
                    text = ""
                self.board[i][j] = text
                
                btn_cell = tk.Button(self.frame, text=text, 
                                     width=6, height=3, bd=0, 
                                     bg=color[(i + j) % 2], 
                                     fg=color[(i + j) % 2 - 1],
                                     activebackground=color[(i + j) % 2], 
                                     activeforeground=color[(i + j) % 2 - 1],
                                     command=lambda cell_name=[i, j], cell_figure = text: self.move(cell_name, cell_figure))
                btn_cell.grid(row=i, column=j, padx=0, pady=0)
            print(self.board[i])

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.title("Chess")
    root.geometry("500x500")
    root.resizable(False, False)
    root.mainloop()


# import tkinter as tk 

# class Main():
#     def __init__(self, root):
#         self.isPressed = False
#         self.main_figures = ["rook", "knight", "bishop", "king", 
#                              "queen", "bishop", "knight", "rook"]
#         self.init_main()
        
#     def move(self, cell_name, cell_figure):
#         if self.isPressed == False and cell_figure != "":
#             print('нажали на фигуру ', cell_name)
#             self.isPressed = True
#         else:
#             print('делается ход какойто на клетку ', cell_name)
#             self.isPressed = False

#     def init_main(self):
#         color = ["black", "white"]
#         for i in range(0, 8):
#             for j in range(0, 8):
#                 if i == 0 or i == 7:
#                     text = self.main_figures[j]
#                 else: 
#                     text = ""
#                 self.frame = tk.Frame(root)
#                 self.frame.pack(expand=True, fill=tk.BOTH)
#                 self.frame.grid(row = i, column = j, padx = 0, pady = 0)
                
#                 btn_cell = tk.Button(self.frame, text = text, 
#                                             width = 6, height = 3, bd = 0, 
#                                             bg = color[(i + j) % 2], fg = color[(i + j) % 2 - 1],
#                                             activebackground = color[(i + j) % 2], 
#                                             activeforeground = color[(i + j) % 2 - 1],
#                                             command = lambda cell_name = [i, j]: self.move(cell_name, "Queen"))
#                 btn_cell.pack()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Main(root)
#     root.title("Chess")
#     root.geometry("500x500")
#     root.resizable(False, False)
#     root.mainloop()