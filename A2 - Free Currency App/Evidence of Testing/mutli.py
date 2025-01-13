import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x700")
        self.resizable(False, False)
        self.title("FreecurrencyAPP")
        ctk.set_appearance_mode("light")
        
        self.frames = {}
        for F in (Start, Menu, Quick_convert):
            frame = F(self, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(Start)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
class Start(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=("#fafafa", "#fafafa"))
        label = ctk.CTkLabel(self, text="Start")
        label.pack(pady=10, padx=10)
        
        button = ctk.CTkButton(self, text="Go to Menu",
                               command=lambda:controller.show_frame(Menu))
        button.pack()

class Menu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=("#fafafa", "#fafafa"))
        label = ctk.CTkLabel(self, text="Menu")
        label.pack(pady=10, padx=10)
        
        button = ctk.CTkButton(self, text="Go to Quick Convert",
                               command=lambda:controller.show_frame(Quick_convert))
        button.pack()

class Quick_convert(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=("#fafafa", "#fafafa"))
        label = ctk.CTkLabel(self, text="Quick Convert")
        label.pack(pady=10, padx=10)
        
        button = ctk.CTkButton(self, text="Go to Start",
                               command=lambda:controller.show_frame(Start))
        button.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
    


# Tested out multiple page application using tkinter