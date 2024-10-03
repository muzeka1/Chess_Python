import tkinter as tk 
import platform
from PIL import Image, ImageTk

board = [["" for _ in range(8)] for _ in range(8)]
cells_board = [["" for _ in range(8)] for _ in range(8)]

class Movement():
    def __init__(self, coords, figure, color, possible_moves, flag):
        self.coords = coords
        self.figure = figure
        self.color = color 
        self.possible_moves = possible_moves
        self.flag = flag
        
    

    def all_cycle_directions(self, directions, x, y):
        for dx, dy in directions:
            for i in range(1, 8):
                nx, ny = x + i * dx, y + i * dy
                if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[nx]):
                    break
                if board[nx][ny] != "":
                    if cells_board[nx][ny].cget("fg") != self.color:
                        self.possible_moves.append([nx, ny])
                    break
                self.possible_moves.append([nx, ny])

    def find_possible_move(self):
        x,y = self.coords[0], self.coords[1]

        if self.figure == "♟":
            if self.color == "white":
                if x == 1 and board[x+2][y] == "":
                    self.possible_moves.append([x+2, y])
                if x+1 <= 7 and board[x+1][y] == "":
                    self.possible_moves.append([x+1, y])
                if x+1 <= 7 and y-1 >= 0 and ((board[x+1][y-1] != "" and cells_board[x+1][y-1].cget("fg") != self.color) or self.flag == True):
                    self.possible_moves.append([x+1,y-1])
                if x+1 <= 7 and y+1 <= 7 and ((board[x+1][y+1] != "" and cells_board[x+1][y+1].cget("fg") != self.color) or self.flag == True):
                    self.possible_moves.append([x+1,y+1])
            if self.color == "black":
                if x == 6 and board[x-2][y] == "":
                    self.possible_moves.append([x-2, y])
                if x-1 >= 0 and board[x-1][y] == "":
                    self.possible_moves.append([x-1, y])
                if x-1 >= 0 and y-1 >= 0 and ((board[x-1][y-1] != "" and cells_board[x-1][y-1].cget("fg") != self.color) or self.flag == True):
                    self.possible_moves.append([x-1,y-1])
                if x-1 >= 0 and y+1 <= 7 and ((board[x-1][y+1] != "" and cells_board[x-1][y+1].cget("fg") != self.color) or self.flag == True):
                    self.possible_moves.append([x-1,y+1])
                    
        if self.figure == "♚":
            directions = [(-1, -1), (1, 1), (0, 1), (0, -1), 
                          (1, 0), (-1, 0), (1, -1), (-1, 1)]
            for direct in directions:
                self.possible_moves.append([x + direct[0], y + direct[1]])
                    
        if self.figure == "♛":
            directions = [
                (0, -1), (0, 1), (-1, 0), (1, 0),
                (-1, -1), (-1, 1), (1, -1), (1, 1)
            ]
            self.all_cycle_directions(directions, x, y)

        if self.figure == "♜":
            directions = [
                (0, -1), (0, 1), (-1, 0), (1, 0),
            ]
            self.all_cycle_directions(directions, x, y)
        
        if self.figure == "♝":
            directions = [
                (-1, -1), (-1, 1), (1, -1), (1, 1)
            ]
            self.all_cycle_directions(directions, x, y)

        if self.figure == "♞":
            directions = [
                (2, 1), (2, -1), (1, 2), (1, -2), 
                (-2, -1), (-2, 1), (-1, -2), (-1, 2)
            ]
            for direct in directions:
                self.possible_moves.append([x + direct[0], y + direct[1]])

                    
class Main():
    def __init__(self, root):  
        self.main_figures = ["♜", "♞", "♝", "♚", 
                             "♛", "♝", "♞", "♜"]
        self.color = ["#c8c8c8", "#6B8E23"]#FAEBD7
        self.turn = 0
        self.figure_color = ["white", "black"]
        self.turn_color = "white"
        self.possible_moves_figure = []
        self.cells_on_attack = []
        self.pressed_btn = None
        self.pressed_btn_text = ""
        self.pressed_btn_pos = []
        self.pressed_btn_bg = ""
        self.pressed_btn_fg = ""
        self.isPressed = False
        self.black_king = [7, 3]
        self.white_king = [0, 3]
        self.shah = False

        self.init_main(root)
        
    def find_all_moves(self, turn_color):
        for i in range(1, 8):
            for j in range(1, 8):
                if board[i][j] != "" and board[i][j] != "♚" and turn_color == cells_board[i][j].cget("fg"):
                    object_class_movement = Movement([i, j], board[i][j], turn_color, self.possible_moves_figure, True)
                    object_class_movement.find_possible_move()
                    
    def move(self, cell_cords):
        current_btn = cells_board[cell_cords[0]][cell_cords[1]]
    
        if not self.isPressed and current_btn.cget("text") != "" and current_btn.cget("fg") == self.turn_color:
            print("ВЫБРАЛИ ФИГУРУ")
            if self.pressed_btn:
                self.pressed_btn.config(bg=self.color[(self.pressed_btn_pos[0] + self.pressed_btn_pos[1]) % 2])
            self.pressed_btn = current_btn
            self.pressed_btn_bg = current_btn.cget("bg")
            self.pressed_btn.config(bg="orange")
            self.pressed_btn_text = current_btn.cget("text")
            self.pressed_btn_pos = [cell_cords[0], cell_cords[1]]
            self.pressed_btn_fg = current_btn.cget("fg")
            object_class_movement = Movement(cell_cords, self.pressed_btn_text, self.turn_color, self.possible_moves_figure, False)
            object_class_movement.find_possible_move()
            print(self.possible_moves_figure)
            self.isPressed = True
            return

        if current_btn.cget("fg") == self.pressed_btn_fg and current_btn.cget("fg") == self.turn_color and current_btn.cget("text") != "":
            print("ПОМЕНЯЛИ ФИГУРУ")
            self.pressed_btn.config(bg = self.pressed_btn_bg)
            self.pressed_btn = current_btn
            self.pressed_btn_bg = current_btn.cget("bg")
            self.pressed_btn.config(bg="orange")
            self.pressed_btn_text = current_btn.cget("text")
            self.pressed_btn_pos = [cell_cords[0], cell_cords[1]]
            self.possible_moves_figure = []
            
            object_class_movement = Movement(cell_cords, self.pressed_btn_text, self.turn_color, self.possible_moves_figure, False)
            object_class_movement.find_possible_move()
            print(self.possible_moves_figure)
            self.isPressed = True
            return

        if self.isPressed and (current_btn.cget("text") == "" or current_btn.cget("fg") != self.turn_color):
            if cell_cords in self.possible_moves_figure and (cell_cords in self.cells_on_attack or self.cells_on_attack == []):
                print("ПОСТАВИЛИ ФИГУРУ", self.turn_color)
                
                self.pressed_btn.config(text="", bg=self.pressed_btn_bg) 
                board[self.pressed_btn_pos[0]][self.pressed_btn_pos[1]] = ""
                board[cell_cords[0]][cell_cords[1]] = self.pressed_btn_text
                current_btn.config(text=self.pressed_btn_text, fg = self.turn_color)

                if current_btn.cget("text") == "♚":
                    if self.turn_color == "black":
                        self.black_king = cell_cords
                        
                    if self.turn_color == "white":
                        self.white_king = cell_cords

                self.isPressed = False
                self.possible_moves_figure = []
                
                object_class_movement = Movement(cell_cords, self.pressed_btn_text, self.turn_color, self.possible_moves_figure, True)
                object_class_movement.find_possible_move()
                print(self.pressed_btn_text)
                
                self.shah = False
                self.cells_on_attack = []
                
                if self.turn_color == "white":
                    if self.black_king in self.possible_moves_figure:
                        x = self.black_king[0] - cell_cords[0]
                        y = self.black_king[1] - cell_cords[1]
                        if x > 0 and y > 0:
                            for i in range(0, x):
                                self.cells_on_attack.append([cell_cords[0]+i, cell_cords[1]+i])
                        if x > 0 and y < 0:
                            for i in range(0, x):
                                self.cells_on_attack.append([cell_cords[0]+i, cell_cords[1]-i])
                        if x < 0 and y > 0:
                            for i in range(0, abs(x)):
                                self.cells_on_attack.append([cell_cords[0]-i, cell_cords[1]+i])
                        if x < 0 and y < 0:
                            for i in range(0, abs(x)):
                                self.cells_on_attack.append([cell_cords[0]-i, cell_cords[1]-i])
                        if x == 0:
                            if y > 0:
                                for i in range(0, y):
                                    self.cells_on_attack.append([cell_cords[0], cell_cords[1]+i])
                            else:
                                for i in range(0, abs(y)):
                                    self.cells_on_attack.append([cell_cords[0], cell_cords[1]-i])
                        if y == 0:
                            if x > 0:
                                for i in range(0, x):
                                    self.cells_on_attack.append([cell_cords[0]+i, cell_cords[1]])
                            else:
                                for i in range(0, abs(x)):
                                    self.cells_on_attack.append([cell_cords[0]-i, cell_cords[1]])
                        
                        self.shah = True
                        print('БЕЛЫЕ ПОСТАВИЛИ ШАХ', self.cells_on_attack)
                else:
                    if self.white_king in self.possible_moves_figure:
                        x = self.white_king[0] - cell_cords[0]
                        y = self.white_king[1] - cell_cords[1]
                        if x > 0 and y > 0:
                            for i in range(0, x):
                                self.cells_on_attack.append([cell_cords[0]+i, cell_cords[1]+i])
                        if x > 0 and y < 0:
                            for i in range(0, x):
                                self.cells_on_attack.append([cell_cords[0]+i, cell_cords[1]-i])
                        if x < 0 and y > 0:
                            for i in range(0, abs(x)):
                                self.cells_on_attack.append([cell_cords[0]-i, cell_cords[1]+i])
                        if x < 0 and y < 0:
                            for i in range(0, abs(x)):
                                self.cells_on_attack.append([cell_cords[0]-i, cell_cords[1]-i])
                        if x == 0:
                            if y > 0:
                                for i in range(0, y):
                                    self.cells_on_attack.append([cell_cords[0], cell_cords[1]+i])
                            else:
                                for i in range(0, abs(y)):
                                    self.cells_on_attack.append([cell_cords[0], cell_cords[1]-i])
                        if y == 0:
                            if x > 0:
                                for i in range(0, x):
                                    self.cells_on_attack.append([cell_cords[0]+i, cell_cords[1]])
                            else:
                                for i in range(0, abs(x)):
                                    self.cells_on_attack.append([cell_cords[0]-i, cell_cords[1]])
                        self.shah = True
                        print('ЧЕРНЫЕ ПОСТАВИЛИ ШАХ', self.cells_on_attack)
                    
                if self.shah:
                    self.possible_moves_figure = []
                    self.find_all_moves(self.figure_color[(self.turn + 1) % 2])
                    print(self.possible_moves_figure)
                    for i in self.cells_on_attack:
                        if i in self.possible_moves_figure:
                            print('есть кем закрыть')
                            self.shah = False
                            break
                
                if self.shah:
                    print('мээээ')
                
                self.possible_moves_figure = []
                self.turn += 1
                self.turn_color = self.figure_color[self.turn % 2]
                
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
                    text = "♟"
                else: 
                    text = ""
                if platform.system() == "Darwin":
                    from tkmacosx import Button
                    self.btn_cell = Button(self.frame, text=text,
                                     width=button_size, height=button_size, bd=0,
                                     bg=self.color[(i + j) % 2], 
                                     activebackground=self.color[(i + j) % 2], 
                                     font=("Helvetica", "100", "bold"), padx=5, pady=5, 
                                     command=lambda cell_cords=[i, j]: self.move(cell_cords))
                else:
                    self.btn_cell = tk.Button(self.frame, text=text,
                                     width=button_size, height=button_size, bd=0, 
                                     bg=self.color[(i + j) % 2],
                                     activebackground=self.color[(i + j) % 2], 
                                     font=("Helvetica", "70"), padx=5, pady=5, 
                                     command=lambda cell_cords=[i, j]: self.move(cell_cords))
                    
                if i in [0,1]:
                    self.btn_cell.config(fg = "white")
                if i in [6,7]:
                    self.btn_cell.config(fg = "black")
                self.btn_cell.grid(row=i, column=j, sticky='nsew') 
                cells_board[i][j] = self.btn_cell
                board[i][j] = text

        for i in range(0, 8):
            self.frame.grid_rowconfigure(i, weight=1)
            self.frame.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":  
    root = tk.Tk()
    app = Main(root)
    root.title("Chess")
    root.geometry("700x700")
    root.resizable(False, False)
    ico = Image.open('icon.png')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)
    root.mainloop()

    