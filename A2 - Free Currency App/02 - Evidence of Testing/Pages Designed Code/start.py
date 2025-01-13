import customtkinter as ctk
from PIL import Image

root = ctk.CTk(fg_color=("#fafafa", "darkblue"))
root.geometry("1000x700")
root.resizable(False, False)
root.title("FreecurrencyAPP")
ctk.set_appearance_mode("light")


#Logo on Upper Right
my_image = ctk.CTkImage(light_image=Image.open('img/freecurrencyapi.png'), size=(260, 30))
root.image = my_image  # Keep a reference

image_label = ctk.CTkLabel(root, image=my_image, text="")
image_label.grid(row=1, column=1, sticky="nw", padx=(50, 0), pady=(60, 0))

# Tagline label
tagline = ctk.CTkLabel(root, text="Know what your money's", text_color="black", font=("Arial", 80, "bold"), wraplength=600, justify="left")
tagline.grid(row=2, column=1, padx=(50, 0), pady=(100, 0), sticky="w")  # Align to the west (left)

# Tagline blue label
tagline_blue = ctk.CTkLabel(root, text="worth", text_color="#22D3EE", font=("Arial", 80, "bold"), justify="left")
tagline_blue.grid(row=3, column=1, padx=(50, 0), sticky="w")  # Align to the west (left)

#Tagline small label
tagline = ctk.CTkLabel(root, text="easy money, easy conversion", text_color="black", font=("Arial", 20), wraplength=700, justify="left")
tagline.grid(row=4, column=1, padx=(50, 0), pady=(0, 0), sticky="w")  # Align to the west (left)

#Start Button - Navigates to Menu
start_button = ctk.CTkButton(
    master=root,
    text="Get Started",
    text_color="black",
    border_width=2,    
    corner_radius=50,
    fg_color="transparent",
    hover_color="#FAFAFA",
    border_color="black",
    width=170,
    height=50,
    font=("Arial", 15)
)

def update_button_position(event=None):
    start_button.place(x=50, y=root.winfo_height() - 70, anchor="sw")

root.bind("<Configure>", update_button_position)
update_button_position()  # Initial positioning


#Canvas Square Design

canvas = ctk.CTkCanvas(root, width=300, height=450, bg="white", highlightthickness=0)  # Create a canvas for drawing

# Draw a square on the canvas
rectangle_width = 300  # width of rectangle
rectangle_heigth = 450  # height of rectangle
canvas.create_rectangle(0, 0, rectangle_width, rectangle_heigth, fill="#22D3EE")  # Draw a blue square
# Place the canvas in the bottom-left corner
canvas.place(relx=1, rely=1, anchor='se')  # Use place to position it at the bottom right


root.mainloop()