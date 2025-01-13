import customtkinter as ctk
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x700")
        self.resizable(False, False)
        self.title("FreecurrencyAPP")
        ctk.set_appearance_mode("light")

        # Create a container for pages
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        # Initialize pages
        self.start_page = StartPage(self.container, self)
        self.menu_page = MenuPage(self.container, self)

        # Show the start page initially
        self.start_page.pack(fill="both", expand=True)

    def show_start_page(self):
        self.menu_page.pack_forget()  # Hide menu page
        self.start_page.pack(fill="both", expand=True)  # Show start page

    def show_menu_page(self):
        self.start_page.pack_forget()  # Hide start page
        self.menu_page.pack(fill="both", expand=True)  # Show menu page


class StartPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=("#fafafa", "#fafafa"))

        # Logo on Upper Right
        my_image = ctk.CTkImage(light_image=Image.open('img/freecurrencyapi.png'), size=(260, 30))
        self.image_label = ctk.CTkLabel(self, image=my_image, text="")
        self.image_label.grid(row=1, column=1, sticky="nw", padx=(50, 0), pady=(60, 0))

        # Tagline label
        tagline = ctk.CTkLabel(self, text="Know what your money's", text_color="black", font=("Arial", 80, "bold"), wraplength=600, justify="left")
        tagline.grid(row=2, column=1, padx=(50, 0), pady=(100, 0), sticky="w")

        # Tagline blue label
        tagline_blue = ctk.CTkLabel(self, text="worth", text_color="#22D3EE", font=("Arial", 80, "bold"), justify="left")
        tagline_blue.grid(row=3, column=1, padx=(50, 0), sticky="w")

        # Tagline small label
        tagline_small = ctk.CTkLabel(self, text="easy money, easy conversion", text_color="black", font=("Arial", 20), wraplength=700, justify="left")
        tagline_small.grid(row=4, column=1, padx=(50, 0), pady=(0, 0), sticky="w")

        # Start Button - Navigates to Menu
        start_button = ctk.CTkButton(
            master=self,
            text="Get Started",
            text_color="black",
            border_width=2,
            corner_radius=50,
            fg_color="transparent",
            hover_color="#f6f6f6",
            border_color="black",
            width=170,
            height=50,
            font=("Arial", 15),
            command=controller.show_menu_page  # Navigate to menu page
        )
        
        def update_button_position(event=None):
            start_button.place(x=50, y=self.winfo_height() - 70, anchor="sw")

        self.bind("<Configure>", update_button_position)
        update_button_position()  # Initial positioning

        # Canvas Square Design
        canvas = ctk.CTkCanvas(self, width=300, height=450, bg="white", highlightthickness=0)
        
        # Draw a square on the canvas
        rectangle_width = 300  
        rectangle_height = 450  
        canvas.create_rectangle(0, 0, rectangle_width, rectangle_height, fill="#22D3EE")  
        
        # Place the canvas in the bottom-left corner
        canvas.place(relx=1, rely=1, anchor='se')


class MenuPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=("#fafafa", "darkblue"))

        # Logo on Upper Right
        my_image = ctk.CTkImage(light_image=Image.open('img/freecurrencyapi.png'), size=(260, 30))
        self.image_label = ctk.CTkLabel(self, image=my_image, text="")
        self.image_label.grid(row=1, column=1, sticky="nw", padx=(50, 0), pady=(60, 0))

        # Header Label
        header = ctk.CTkLabel(self, text="What do you want to know?", text_color="black", font=("Arial", 40, "bold"))
        header.place(relx=0.5, rely=0.35, anchor="center")

        # Menu Buttons
        menu_frame = ctk.CTkFrame(self, fg_color="transparent")
        menu_frame.place(relx=0.5, rely=0.55, anchor="center")

        button_width = 200
        button_height = 50
        button_font = ("Arial", 15)
        
        button_style = {
            "fg_color": "#22D3EE",
            "text_color": "white",
            "corner_radius": 50,
            "hover_color": "#21BCD3",
            "width": button_width,
            "height": button_height,
            "font": button_font
        }

        button1 = ctk.CTkButton(menu_frame, text="Quick Convert", **button_style)
        button2 = ctk.CTkButton(menu_frame, text="Exchange Rates", **button_style)
        button3 = ctk.CTkButton(menu_frame, text="Currency Dictionary", **button_style)

        # Button Placement
        button1.grid(row=0,column=0,padx=10,pady=10)
        button2.grid(row=0,column=1,padx=10,pady=10)
        button3.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

        # Go Back Button - Navigates back to Start Page
        back_button = ctk.CTkButton(
            master=self,
            text="Go Back",
            text_color="black",
            border_width=2,
            corner_radius=50,
            fg_color="transparent",
            hover_color="#f6f6f6",
            border_color="black",
            width=170,
            height=50,
            font=("Arial", 15),
            command=controller.show_start_page  # Navigate back to start page
        )

        def update_button_position(event=None):
            back_button.place(x=50,y=self.winfo_height()-70 ,anchor='sw')

        self.bind("<Configure>", update_button_position)
        update_button_position() 

        # Canvas Square Design for Menu Page
        canvas = ctk.CTkCanvas(self,width=300,height=150,bg='#22D3EE',highlightthickness='0')
        
        rectangle_width = 300  
        rectangle_height = 150  
        canvas.create_rectangle(0 ,0 ,rectangle_width ,rectangle_height ,fill='#22D3EE')  
        
        canvas.place(relx='1',rely='0',anchor='ne') 


if __name__ == "__main__":
    app = App()
    app.mainloop()
