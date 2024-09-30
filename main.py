import tkmacosx as tkx
import tkinter as tk 
import platform

class Main():
    def __init__(self, root):  
        self.main_figures = ["♖", "♘", "♗", "♔", 
                             "♕", "♗", "♘", "♖"]
        self.color = ["#FAEBD7", "#6B8E23"]
        self.board = [["" for _ in range(8)] for _ in range(8)]
        self.cells_board = [["" for _ in range(8)] for _ in range(8)]
        self.pressed_btn = None
        self.pressed_btn_text = ""
        self.pressed_btn_pos = []
        self.isPressed = False

        self.init_main(root)

    def move(self, cell_name):
        current_btn = self.cells_board[cell_name[0]][cell_name[1]]
        
        if not self.isPressed and current_btn.cget("text") != "":
            if self.pressed_btn:
                self.pressed_btn.config(bg=self.color[(self.pressed_btn_pos[0] + self.pressed_btn_pos[1]) % 2])
             
            self.pressed_btn = current_btn
            self.pressed_btn.config(bg="orange")
            self.pressed_btn_text = current_btn.cget("text")
            self.pressed_btn_pos = [cell_name[0], cell_name[1]]
            self.isPressed = True

        elif self.isPressed and current_btn.cget("text") == "":
            current_btn.config(bg=self.color[(cell_name[0] + cell_name[1]) % 2])
            self.pressed_btn.config(text="", bg=self.color[(self.pressed_btn_pos[0] + self.pressed_btn_pos[1]) % 2]) 
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
                if platform.system() == "Darwin":
                    self.btn_cell = tkx.Button(self.frame)
                else:
                    self.btn_cell = tk.Button(self.frame)
                    
                self.btn_cell.config(self.frame, text=text,
                                     width=button_size, height=button_size, bd=0, 
                                     bg=self.color[(i + j) % 2], 
                                     fg="black",#self.color[(i + j + 1) % 2],
                                     activebackground=self.color[(i + j) % 2], 
                                     activeforeground="black",#self.color[(i + j + 1) % 2],
                                     font=("Helvetica", "100", "bold"), padx=5, pady=5, 
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

