import tkinter as tk 

class Main():
    def __init__(self, root):
        self.main_figures = ["rook", "knight", "bishop", "king", 
                             "queen", "bishop", "knight", "rook"]
        self.color = ["black", "white"]
        self.board = [["" for _ in range(8)] for _ in range(8)]
        self.cells_board = [["" for _ in range(8)] for _ in range(8)]
        self.btn_cell = tk.Button()
        self.pressed_btn = tk.Button()
        self.pressed_btn_text = ""
        self.isPressed = False

        self.init_main(root)

    def move(self, cell_name):
        current_btn = self.cells_board[cell_name[0]][cell_name[1]]
        if self.isPressed == False and current_btn.cget("text") != "":
            print("нажали на фигуру ", cell_name)
            self.pressed_btn.config(bg = "orange")
            self.pressed_btn_text = current_btn.cget("text")
            self.pressed_btn = current_btn
            self.isPressed = True

        elif self.isPressed == True and current_btn.cget("text") == "":
            print("делается ход какой-то на клетку ", cell_name)
            current_btn.config(bg = self.color[(cell_name[0] + cell_name[1])%2])
            self.pressed_btn.config(text = "")
            current_btn.config(text = self.pressed_btn_text)
            self.isPressed = False
        

    def init_main(self, root):
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        
        for i in range(0, 8):
            for j in range(0, 8):
                if i == 0 or i == 7:
                    text = self.main_figures[j]
                elif i == 1 or i == 6:
                    text = "pawn"
                else: 
                    text = ""
                self.board[i][j] = text
                
                self.btn_cell = tk.Button(self.frame, text=text,
                                     width=3, height=3, bd=0, 
                                     bg=self.color[(i + j) % 2], 
                                     fg=self.color[(i + j) % 2 - 1],
                                     activebackground=self.color[(i + j) % 2], 
                                     activeforeground=self.color[(i + j) % 2 - 1],
                                     command=lambda cell_name=[i, j]: self.move(cell_name))
                self.btn_cell.grid(row=i, column=j, padx=0, pady=0)
                self.cells_board[i][j] = self.btn_cell

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.title("Chess")
    root.geometry("500x500")
    root.resizable(False, False)
    root.mainloop()
