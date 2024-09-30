import customtkinter as ctk

app = ctk.CTk()  # Используйте CTk
app.title("Hello World")
label = ctk.CTkLabel(app, text="Hello, World!")
label.pack(padx=20, pady=20)
app.mainloop()