import tkinter as tk 

class Main():
    def __init__(self, root):
        self.init_main()

    def move(self, cell_name, cell_figure):
        print(cell_name)

    def init_main(self):
        color = ["black", "white"]
        for i in range(0, 8):
            for j in range(0, 8):
                self.frame = tk.Frame(root)
                self.frame.grid(row = i, column = j, padx = 0, pady = 0)
                
                btn_cell = tk.Button(self.frame, text = color[(i + j) % 2], 
                                            width = 3, height = 3, bd = 0, 
                                            bg = color[(i + j) % 2], fg = color[(i + j) % 2 - 1],
                                            activebackground = color[(i + j) % 2], 
                                            activeforeground = color[(i + j) % 2 - 1],
                                            command = lambda cell_name = [i, j]: self.move(cell_name, "Queen"))
                btn_cell.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.title("Chess")
    root.geometry("900x600")
    root.resizable(False, False)
    root.mainloop()