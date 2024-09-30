import tkinter as tk 

class Main():
    def __init__(self, root):  # исправлено на __init__
        self.main_figures = ["♖", "♘", "♗", "♔", 
                             "♕", "♗", "♘", "♖"]
        self.color = ["black", "white"]
        self.board = [["" for _ in range(8)] for _ in range(8)]
        self.cells_board = [["" for _ in range(8)] for _ in range(8)]
        self.pressed_btn = None
        self.pressed_btn_text = ""
        self.isPressed = False

        self.init_main(root)

    def move(self, cell_name):
        current_btn = self.cells_board[cell_name[0]][cell_name[1]]
        if not self.isPressed and current_btn.cget("text") != "":
            print("нажали на фигуру ", cell_name)
            if self.pressed_btn:
                self.pressed_btn.config(bg="SystemButtonFace") 
            self.pressed_btn = current_btn
            self.pressed_btn.config(bg="orange")
            self.pressed_btn_text = current_btn.cget("text")
            self.isPressed = True

        elif self.isPressed and current_btn.cget("text") == "":
            print("делается ход какой-то на клетку ", cell_name)
            current_btn.config(bg=self.color[(cell_name[0] + cell_name[1]) % 2])
            self.pressed_btn.config(text="")
            current_btn.config(text=self.pressed_btn_text)
            self.isPressed = False
        

    def init_main(self, root):
        self.frame = tk.LabelFrame(root)
        self.frame.pack(expand=True)

        button_size = 80  

        for i in range(0, 8):
            for j in range(0, 8):
                if i == 0 or i == 7:
                    text = self.main_figures[j]
                elif i == 1 or i == 6:
                    text = "♙"
                else: 
                    text = ""
                
                self.btn_cell = tk.Button(self.frame, text=text,
                                     width=button_size, height=button_size, bd=0, 
                                     bg=self.color[(i + j) % 2], 
                                     fg=self.color[(i + j + 1) % 2],
                                     activebackground=self.color[(i + j) % 2], 
                                     activeforeground=self.color[(i + j + 1) % 2],
                                     font=("Helvetica", "50", "bold"), padx=5, pady=5, 
                                     command=lambda cell_name=[i, j]: self.move(cell_name))
                
                self.btn_cell.grid(row=i, column=j, sticky='nsew') 
                self.cells_board[i][j] = self.btn_cell


        for i in range(8):
            self.frame.grid_rowconfigure(i, weight=1)
            self.frame.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":  
    root = tk.Tk()
    app = Main(root)
    root.title("Chess")
    root.geometry("700x700")
    root.resizable(False, False)
    root.mainloop()