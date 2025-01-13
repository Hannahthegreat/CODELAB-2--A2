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


# Common styles
dropdown_style = {
    "width": 200,
    "height": 50,
    "fg_color": "#22D3EE",
    "button_color": "#22D3EE",
    "button_hover_color": "#1CB5D1",
    "font": ("Arial", 15)
}


currencies = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"]
# From currency
exchange_dropdown = ctk.CTkOptionMenu(root, values=currencies, **dropdown_style)
exchange_dropdown.grid(row=2, column=1, padx=(50, 0), pady=(100, 0), sticky="w")



# Currency Information
dict_frame = ctk.CTkFrame(root, fg_color="white")
dict_frame.grid(row=3, column=2, sticky="w", padx=10, pady=10)

# Tagline label
master_name = ctk.CTkLabel(dict_frame, text="EURO", text_color="black", font=("Arial", 40, "bold"))
master_name.grid(row=0, column=0, padx=50, pady=30, sticky="w")

info_style = {
    "text_color":"black", 
    "font":("Arial", 30), 
    "wraplength":500,  # Adjust this value as needed
    "justify":"left"
}

name = ctk.CTkLabel(dict_frame, text="Name: European ", **info_style)
name.grid(row=1, column=0, padx=50, pady=10, sticky="w")
symbol = ctk.CTkLabel(dict_frame, text="Symbol: European ", **info_style)
symbol.grid(row=2, column=0, padx=50, pady=10, sticky="w")
native_symbol = ctk.CTkLabel(dict_frame, text="Native Symbol: European ", **info_style)
native_symbol.grid(row=3, column=0, padx=50, pady=10, sticky="w")
name_plural = ctk.CTkLabel(dict_frame, text="Name Plural: European ", **info_style)
name_plural.grid(row=4, column=0, padx=50, pady=(10, 30), sticky="w")

# After adding all labels, update the frame
dict_frame.update_idletasks()

# Get the required width and height
req_width = dict_frame.winfo_reqwidth()
req_height = dict_frame.winfo_reqheight()

# Set the width to be wider (e.g., 1.2 times the required width)
dict_frame.configure(width=max(600, int(req_width * 1.2)), height=req_height)

# Prevent the frame from adjusting its size
dict_frame.grid_propagate(False)



def get_started():
    print("Button Pressed")


start_button = ctk.CTkButton(
    master=root,
    text="Get Started",
    text_color="black",
    border_width=2,    
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



canvas = ctk.CTkCanvas(root, width=300, height=150, bg="white", highlightthickness=0)  # Create a canvas for drawing

# Draw a square on the canvas
rectangle_width = 300  # width of rectangle
rectangle_heigth = 150  # height of rectangle
canvas.create_rectangle(0, 0, rectangle_width, rectangle_heigth, fill="#22D3EE")  # Draw a blue square
# Place the canvas in the bottom-left corner
canvas.place(relx=1, rely=0, anchor='ne')  # Use place to position it at the bottom right




root.mainloop()