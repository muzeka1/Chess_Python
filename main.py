import tkinter as tk 


class Main():
    def __init__(self, root):
        self.init_main()

    def move(self, cell_name, figure):
        print(cell_name)

    def init_main(self):
        j = 1
        color = ["white", "black"]
        for i in range(0, 64):
            text = str(i + 1)
            
            
            if i % 8 == 0 and j == 0:
                j = 1
            elif i % 8 == 0 and j == 1:
                j = 0

            self.frame = tk.Frame(root);
            self.frame.grid(row = i // 8, column = i % 8, padx=0, pady=0);
            cell_name = str(i // 8) + " " + str(i % 8)
            btn_main_startgame = tk.Button(self.frame, text = color[i%2+j-1], 
                                           width = 3, height = 3, bd = 0, 
                                           bg = color[i%2+j-1], fg = color[i%2+j-2],
                                           activebackground = color[i%2+j-1], 
                                           activeforeground = color[i%2+j-2],
                                           command = lambda cell_name = cell_name: self.move(cell_name, "Queen"))
            btn_main_startgame.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.title("Chess")
    root.geometry("900x600")
    root.resizable(False, False)
    root.mainloop()


# ФИЗУЛИ ЧМО