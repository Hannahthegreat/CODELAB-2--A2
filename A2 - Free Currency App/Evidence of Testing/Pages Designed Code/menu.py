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

# Header Label
header = ctk.CTkLabel(root, text="what do you want to know?", text_color="black", font=("Arial", 40, "bold"))
header.place(relx=0.5, rely=0.35, anchor="center")

#Menu Buttons
menu_frame = ctk.CTkFrame(root, fg_color="transparent")
menu_frame.place(relx=0.5, rely=0.5, anchor="center")

#Menu Button Styles
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


#Button Creation
button1 = ctk.CTkButton(menu_frame, text="Quick Convert", **button_style)
button2 = ctk.CTkButton(menu_frame, text="Exchange Rates", **button_style)
button3 = ctk.CTkButton(menu_frame, text="Currency Dictionary", **button_style)
#Button Placement
button1.grid(row=0, column=0, padx=10, pady=10)
button2.grid(row=0, column=1, padx=10, pady=10)
button3.grid(row=1, column=0, columnspan=2, padx=10, pady=10)



#Go Back Button

back_button = ctk.CTkButton(
    master=root,
    text="Go Back",
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
    back_button.place(x=50, y=root.winfo_height() - 70, anchor="sw")

root.bind("<Configure>", update_button_position)
update_button_position()  # Initial positioning


#Canvas Square Design

canvas = ctk.CTkCanvas(root, width=300, height=150, bg="white", highlightthickness=0)  # Create a canvas for drawing

# Draw a square on the canvas
rectangle_width = 300  # width of rectangle
rectangle_heigth = 150  # height of rectangle
canvas.create_rectangle(0, 0, rectangle_width, rectangle_heigth, fill="#22D3EE")  # Draw a blue square
# Place the canvas in the bottom-left corner
canvas.place(relx=1, rely=0, anchor='ne')  # Use place to position it at the bottom right


root.mainloop()