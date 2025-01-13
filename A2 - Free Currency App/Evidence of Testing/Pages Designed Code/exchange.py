import customtkinter as ctk
from PIL import Image

root = ctk.CTk(fg_color=("#fafafa", "darkblue"))
root.geometry("1000x700")
root.resizable(False, False)
root.title("FreecurrencyAPP")
ctk.set_appearance_mode("light")

my_image = ctk.CTkImage(light_image=Image.open('img/freecurrencyapi.png'), size=(260, 30))
root.image = my_image  # Keep a reference

image_label = ctk.CTkLabel(root, image=my_image, text="")
image_label.grid(row=1, column=1, sticky="nw", padx=(50, 0), pady=(60, 0))

# Tagline label
tagline = ctk.CTkLabel(root, text="Exchange Rates", text_color="black", font=("Arial", 40, "bold"))
tagline.place(relx=0.5, rely=0.35, anchor="center")

# Frame for dropdown and text field
input_frame = ctk.CTkFrame(root, fg_color="transparent")
input_frame.place(relx=0.5, rely=0.55, anchor="center")



textfield_style = {
    "width": 500,
    "height": 50,
    "fg_color": "white",
    "border_color": "white",
    "font": ("Arial", 15)
}

currencies = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"]
# From currency
exchange_dropdown = ctk.CTkOptionMenu(input_frame, values=currencies, **dropdown_style)
exchange_dropdown.grid(row=0, column=0, padx=(0, 10), pady=(0, 30))

rate_text_field = ctk.CTkEntry(input_frame, **textfield_style, state="readonly")
rate_text_field.grid(row=0, column=1, pady=(0, 30))



# Tagline small label
tagline = ctk.CTkLabel(input_frame, text="1 USD = 0.9675 EUR", text_color="black", font=("Arial", 20), wraplength=700, justify="center")
tagline.grid(row=2, column=0, columnspan=2, pady=(20, 0))



def get_started():
    print("Button Pressed")


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
    font=("Arial", 15),
    command=get_started
)

def update_button_position(event=None):
    back_button.place(x=50, y=root.winfo_height() - 70, anchor="sw")

root.bind("<Configure>", update_button_position)
update_button_position()  # Initial positioning



canvas = ctk.CTkCanvas(root, width=300, height=150, bg="white", highlightthickness=0)  # Create a canvas for drawing

# Draw a square on the canvas
rectangle_width = 300  # width of rectangle
rectangle_heigth = 150  # height of rectangle
canvas.create_rectangle(0, 0, rectangle_width, rectangle_heigth, fill="#22D3EE")  # Draw a blue square
# Place the canvas in the bottom-left corner
canvas.place(relx=1, rely=0, anchor='ne')  # Use place to position it at the bottom right


root.mainloop()