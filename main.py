import tkinter as tk 
import platform

class Movement():
    def __init__(self):
        self.figure = ""
        self.chah = []
    
    def find_possible_move(self, coords, figure, color):
        self.possible_moves = []
        self.figure = figure
        x = coords[0]
        y = coords[1]
        print("корды текущей фигуры: ", x, y)
        if self.figure == "♙":
            if color == "white":
                if x == 1 and self.board[x+2][y] == "":
                    self.possible_moves.append([x+2, y])
                if x+1 <= 7 and self.board[x+1][y] == "":
                    self.possible_moves.append([x+1, y])
                if x+1 <= 7 and y-1 >= 0 and self.board[x+1][y-1] != "" and self.cells_board[x+1][y-1].cget("fg") != color:
                    self.possible_moves.append([x+1,y-1])
                if x+1 <= 7 and y+1 <= 7 and self.board[x+1][y+1] != "" and self.cells_board[x+1][y+1].cget("fg") != color:
                    self.possible_moves.append([x+1,y+1])
            if color == "black":
                if x == 6 and self.board[x-2][y] == "":
                    self.possible_moves.append([x-2, y])
                if x-1 >= 0 and self.board[x-1][y] == "":
                    self.possible_moves.append([x-1, y])
                if x-1 >= 0 and y-1 >= 0 and self.board[x-1][y-1] != "" and self.cells_board[x-1][y-1].cget("fg") != color:
                    self.possible_moves.append([x-1,y-1])
                if x-1 >= 0 and y+1 <= 7 and self.board[x-1][y+1] != "" and self.cells_board[x-1][y+1].cget("fg") != color:
                    self.possible_moves.append([x-1,y+1])
                    
        if self.figure == "♔" :
            self.possible_moves.append([x-1, y-1])
            self.possible_moves.append([x+1, y+1])
            self.possible_moves.append([x, y+1])
            self.possible_moves.append([x, y-1])
            self.possible_moves.append([x+1, y])
            self.possible_moves.append([x-1, y])
            self.possible_moves.append([x+1, y-1])
            self.possible_moves.append([x-1, y+1])
                    
        if self.figure == "♕":
            for i in range(1, 8):
                if y-i <= 0 or self.board[x][y-i] != "":
                        self.possible_moves.append([x, y-i])
                        break
                self.possible_moves.append([x, y-i])
                
            for i in range(1, 8):
                if y+i >= 7 or self.board[x][y+i] != "":
                        self.possible_moves.append([x, y+i])
                        break
                self.possible_moves.append([x, y+i])
            
            for i in range(1, 8):
                if x-i <= 0 or self.board[x-i][y] != "":
                        self.possible_moves.append([x-i, y])
                        break
                self.possible_moves.append([x-i, y])
            
            for i in range(1, 8):
                if x+i >= 7 or self.board[x+i][y] != "":
                        self.possible_moves.append([x+i, y])
                        break
                self.possible_moves.append([x+i, y])
                
            for i in range(1, 8):
                if x-i == 0 or y+i >= 7 or x == 0 or self.board[x-i][y+i] != "":
                        self.possible_moves.append([x-i, y+i])
                        break
                self.possible_moves.append([x-i, y+i])
                
            for i in range(1, 8):
                if x-i <= 0 or y-i <= 0 or self.board[x-i][y-i] != "":
                        self.possible_moves.append([x-i, y-i])
                        break
                self.possible_moves.append([x-i, y-i])
            
            for i in range(1, 8):
                if x+i >= 7 or y+i >= 7 or self.board[x+i][y+i] != "":
                        self.possible_moves.append([x+i, y+i])
                        break
                self.possible_moves.append([x+i, y+i])
                
            for i in range(1, 8):
                if x+i >= 7 or y-i<=0 or self.board[x+i][y-i] != "":
                        self.possible_moves.append([x+i, y-i])
                        break
                self.possible_moves.append([x+i, y-i])

        
        if self.figure == "♖":
            for i in range(1, 8):
                if y-i <= 0 or self.board[x][y-i] != "":
                        self.possible_moves.append([x, y-i])
                        break
                self.possible_moves.append([x, y-i])
                
            for i in range(1, 8):
                if y+i >= 7 or self.board[x][y+i] != "":
                        self.possible_moves.append([x, y+i])
                        break
                self.possible_moves.append([x, y+i])
            
            for i in range(1, 8):
                if x-i <= 0 or self.board[x-i][y] != "":
                        self.possible_moves.append([x-i, y])
                        break
                self.possible_moves.append([x-i, y])
            
            for i in range(1, 8):
                if x+i >= 7 or self.board[x+i][y] != "":
                        self.possible_moves.append([x+i, y])
                        break
                self.possible_moves.append([x+i, y])
        
        if self.figure == "♗":
            for i in range(1, 8):
                if x-i <= 0 or y+i>=7 or self.board[x-i][y+i] != "":
                        self.possible_moves.append([x-i, y+i])
                        break
                self.possible_moves.append([x-i, y+i])
                
            for i in range(1, 8):
                if x-i <= 0 or y-i<=0 or self.board[x-i][y-i] != "":
                        self.possible_moves.append([x-i, y-i])
                        break
                self.possible_moves.append([x-i, y-i])
            
            for i in range(1, 8):
                if x+i >= 7 or y+i>=7 or self.board[x+i][y+i] != "":
                        self.possible_moves.append([x+i, y+i])
                        break
                self.possible_moves.append([x+i, y+i])
                
            for i in range(1, 8):
                if x+i >= 7 or y-i<=0 or self.board[x+i][y-i] != "":
                        self.possible_moves.append([x+i, y-i])
                        break
                self.possible_moves.append([x+i, y-i])
        
        if figure == "♘":
            self.possible_moves.append([x+2, y+1])
            self.possible_moves.append([x+2, y-1])
            self.possible_moves.append([x+1, y+2])
            self.possible_moves.append([x+1, y-2])
            self.possible_moves.append([x-2, y-1])
            self.possible_moves.append([x-2, y+1])
            self.possible_moves.append([x-1, y-2])
            self.possible_moves.append([x-1, y+2])
        #for i in range(0, len(possible_moves)):


                    
class Main():
    def __init__(self, root):  
        self.main_figures = ["♖", "♘", "♗", "♔", 
                             "♕", "♗", "♘", "♖"]
        self.color = ["#FFEBCD", "#6B8E23"]#FAEBD7
        self.turn = 0
        self.figure_color = ["white", "black"]
        self.turn_color = "white"
        self.board = [["" for _ in range(8)] for _ in range(8)]
        self.cells_board = [["" for _ in range(8)] for _ in range(8)]
        self.pressed_btn = None
        self.pressed_btn_text = ""
        self.pressed_btn_pos = []
        self.pressed_btn_bg = ""
        self.isPressed = False
        self.black_king = [7, 3]
        self.white_king = [0, 3]

        self.init_main(root)

    def move(self, cell_name):
        current_btn = self.cells_board[cell_name[0]][cell_name[1]]
        
        if not self.isPressed and current_btn.cget("text") != "" and current_btn.cget("fg") == self.turn_color:
            if self.pressed_btn:
                self.pressed_btn.config(bg=self.color[(self.pressed_btn_pos[0] + self.pressed_btn_pos[1]) % 2])
            self.pressed_btn = current_btn
            self.pressed_btn_bg = current_btn.cget("bg")
            self.pressed_btn.config(bg="orange")
            self.pressed_btn_text = current_btn.cget("text")
            self.pressed_btn_pos = [cell_name[0], cell_name[1]]
            Movement.find_possible_move(self, cell_name, self.pressed_btn_text, self.turn_color)
            print(self.possible_moves)
            self.isPressed = True
            return
            
        if current_btn == self.pressed_btn:
            self.isPressed = False
            current_btn.config(bg = self.pressed_btn_bg)
            return

        elif self.isPressed and (current_btn.cget("text") == "" or current_btn.cget("fg") != self.turn_color):
            if cell_name in self.possible_moves:
                self.pressed_btn.config(text="", bg=self.pressed_btn_bg) 
                self.board[self.pressed_btn_pos[0]][self.pressed_btn_pos[1]] = ""
                self.board[cell_name[0]][cell_name[1]] = self.pressed_btn_text
                current_btn.config(text=self.pressed_btn_text, fg = self.turn_color)
                self.turn += 1
                self.turn_color = self.figure_color[self.turn % 2]
                self.isPressed = False
                
            for i in range(0, 8):
                print(self.board[i])
            return
        
        


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
                    from tkmacosx import Button
                    self.btn_cell = Button(self.frame, text=text,
                                     width=button_size, height=button_size, bd=0, 
                                     bg=self.color[(i + j) % 2], 
                                     activebackground=self.color[(i + j) % 2], 
                                     font=("Helvetica", "100", "bold"), padx=5, pady=5, 
                                     command=lambda cell_name=[i, j]: self.move(cell_name))
                else:
                    self.btn_cell = tk.Button(self.frame, text=text,
                                     width=button_size, height=button_size, bd=0, 
                                     bg=self.color[(i + j) % 2],
                                     activebackground=self.color[(i + j) % 2], 
                                     font=("Helvetica", "70"), padx=5, pady=5, 
                                     command=lambda cell_name=[i, j]: self.move(cell_name))
                    
                if i in [0,1]:
                    self.btn_cell.config(fg = "white")
                if i in [6,7]:
                    self.btn_cell.config(fg = "black")
                self.btn_cell.grid(row=i, column=j, sticky='nsew') 
                self.cells_board[i][j] = self.btn_cell
                self.board[i][j] = text

        for i in range(0, 8):
            self.frame.grid_rowconfigure(i, weight=1)
            self.frame.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":  
    root = tk.Tk()
    app = Main(root)
    root.title("Chess")
    root.geometry("700x700")
    root.resizable(False, False)
    root.mainloop()