import customtkinter as ctk
from PIL import Image
import freecurrencyapi


# Initialize the application
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Page Application")
        self.geometry("1000x700")
        self.resizable(False, False)

        # Create a container for all pages
        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=0, sticky="nsew")  # Changed from pack to grid

        # Add these lines here
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # This loop creates instances of different page classes defined further down. 
        self.frames = {}
        for F in (StartPage, MenuPage, QuickConvertPage, ExchangeRatesPage, CurrencyDictionaryPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the start page initially
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        # Show a frame for the given page name.
        frame = self.frames[page_name]
        frame.tkraise()  # Raise the frame to the top of the stacking order

# api functions ----------------------------------------------------------------------------
    
    # Retrieves Currency Data from the API (The value = currency code and the key = exhcange rate)
    def show_currencies(self):
        apikey = freecurrencyapi.Client('fca_live_UGsuYzak3zROde7EAjLjpqja3BGIYiOuBvoCqpO6')
        result = apikey.latest()
        return result['data']
    # Retrieves Currency Data from the API (Currency Information = Currency Code)
    def get_dict_keys(self):
        apikey = freecurrencyapi.Client('fca_live_UGsuYzak3zROde7EAjLjpqja3BGIYiOuBvoCqpO6')
        result = apikey.currencies()  # Fetch currency data
        return result['data']

# Currency Calculations Class ----------------------------------------------------------------------------
class CurrencyPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=("#fafafa", "#fafafa"))
        self.controller = controller
    
    # Retrieves Currency Data from the API (The value = currency code and the key = exhcange rate)
    def get_exchange_rate(self, from_currency, to_currency):
        apikey = freecurrencyapi.Client('fca_live_UGsuYzak3zROde7EAjLjpqja3BGIYiOuBvoCqpO6')
        result = apikey.latest(base_currency=from_currency, currencies=[to_currency])
        return result['data'][to_currency]
    
    # Retrieves Currency Data from the API (Currency Information = Name, Symbol, Native Symbol, Plural Name)
    def show_dict_info(self, currency_code):
        apikey = freecurrencyapi.Client('fca_live_UGsuYzak3zROde7EAjLjpqja3BGIYiOuBvoCqpO6')
        result = apikey.currencies()  # Fetch currency data
        data = result['data'][currency_code]  # Use currency_code variable instead of string literal
        return data['code'], data['name'], data['symbol'], data['symbol_native'], data['name_plural']


# ------------------------------------------------------------------------------------------
# Define the Start Page
class StartPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=("#fafafa", "#fafafa"))
        self.controller = controller

        #Logo on Upper Right
        my_image = ctk.CTkImage(light_image=Image.open('A2 - Free Currency App/03 - Executeable Project Code/freecurrencyapi.png'), size=(260, 30))
        self.image = my_image  # Keep a reference

        image_label = ctk.CTkLabel(self, image=my_image, text="")
        image_label.grid(row=1, column=1, sticky="nw", padx=(50, 0), pady=(60, 0))

        # Tagline label
        tagline = ctk.CTkLabel(self, text="Know what your money's", text_color="black", font=("Arial", 80, "bold"), wraplength=600, justify="left")
        tagline.grid(row=2, column=1, padx=(50, 0), pady=(100, 0), sticky="w")  # Align to the west (left)

        # Tagline blue label
        tagline_blue = ctk.CTkLabel(self, text="worth", text_color="#22D3EE", font=("Arial", 80, "bold"), justify="left")
        tagline_blue.grid(row=3, column=1, padx=(50, 0), sticky="w")  # Align to the west (left)

        #Tagline small label
        tagline = ctk.CTkLabel(self, text="easy money, easy conversion", text_color="black", font=("Arial", 20), wraplength=700, justify="left")
        tagline.grid(row=4, column=1, padx=(50, 0), pady=(0, 0), sticky="w")  # Align to the west (left)

        #Start Button - Navigates to Menu
        start_button = ctk.CTkButton(
            master=self,
            text="Get Started",
            text_color="black",
            border_width=2,    
            fg_color="transparent",
            hover_color="#FAFAFA",
            border_color="black",
            width=170,
            height=50,
            font=("Arial", 15),
            
            command=lambda: controller.show_frame("MenuPage")
        )

        # Anchors it to the lower left position for consitency across all pages
        def update_button_position(event=None):
            start_button.place(x=50, y=self.winfo_height() - 70, anchor="sw")

        self.bind("<Configure>", update_button_position)
        update_button_position()  # Initial positioning


        #Canvas Square Design
        canvas = ctk.CTkCanvas(self, width=300, height=450, bg="white", highlightthickness=0)  # Create a canvas for drawing

        # Draw a square on the canvas
        rectangle_width = 300  # width of rectangle
        rectangle_heigth = 450  # height of rectangle
        canvas.create_rectangle(0, 0, rectangle_width, rectangle_heigth, fill="#22D3EE")  # Draw a blue square
        # Place the canvas in the bottom-left corner
        canvas.place(relx=1, rely=1, anchor='se')  # Use place to position it at the bottom right


# ------------------------------------------------------------------------------------------
# Define the Menu Page
class MenuPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color=("#fafafa", "#fafafa"))
        self.controller = controller

        #Logo on Upper Right
        my_image = ctk.CTkImage(light_image=Image.open('A2 - Free Currency App/03 - Executeable Project Code/freecurrencyapi.png'), size=(260, 30))
        self.image = my_image  # Keep a reference

        image_label = ctk.CTkLabel(self, image=my_image, text="")
        image_label.grid(row=1, column=1, sticky="nw", padx=(50, 0), pady=(60, 0))

        # Header Label
        header = ctk.CTkLabel(self, text="what do you want to know?", text_color="black", font=("Arial", 40, "bold"))
        header.place(relx=0.5, rely=0.35, anchor="center")

        #Menu Buttons
        menu_frame = ctk.CTkFrame(self, fg_color="transparent")
        menu_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Global Style - Menu Button Styles
        button_width = 200
        button_height = 50
        button_font = ("Arial", 15)
        button_style = {
            "fg_color": "#22D3EE",
            "text_color": "white",
            "hover_color": "#21BCD3",
            "width": button_width,
            "height": button_height,
            "font": button_font
        }


        #Button Creation
        button1 = ctk.CTkButton(menu_frame, text="Quick Convert", **button_style, command=lambda: controller.show_frame("QuickConvertPage"))
        button2 = ctk.CTkButton(menu_frame, text="Exchange Rates", **button_style, command=lambda: controller.show_frame("ExchangeRatesPage"))
        button3 = ctk.CTkButton(menu_frame, text="Currency Dictionary", **button_style, command=lambda: controller.show_frame("CurrencyDictionaryPage"))
        #Button Placement
        button1.grid(row=0, column=0, padx=10, pady=10)
        button2.grid(row=0, column=1, padx=10, pady=10)
        button3.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


        #Go Back Button
        back_button = ctk.CTkButton(
            master=self,
            text="Go Back",
            text_color="black",
            border_width=2,    
            fg_color="transparent",
            hover_color="#FAFAFA",
            border_color="black",
            width=170,
            height=50,
            font=("Arial", 15),
            
            command=lambda: controller.show_frame("StartPage")
        )

        # Anchors it to the lower left position for consitency across all pages
        def update_button_position(event=None):
            back_button.place(x=50, y=self.winfo_height() - 70, anchor="sw")

        self.bind("<Configure>", update_button_position)
        update_button_position()  # Initial positioning


        #Canvas Square Design
        canvas = ctk.CTkCanvas(self, width=300, height=150, bg="white", highlightthickness=0)  # Create a canvas for drawing

        # Draw a square on the canvas
        rectangle_width = 300  # width of rectangle
        rectangle_heigth = 150  # height of rectangle
        canvas.create_rectangle(0, 0, rectangle_width, rectangle_heigth, fill="#22D3EE")  # Draw a blue square
        # Place the canvas in the bottom-left corner
        canvas.place(relx=1, rely=0, anchor='ne')  # Use place to position it at the bottom right

# ------------------------------------------------------------------------------------------     
# Define the Quick Convert Page
class QuickConvertPage(CurrencyPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)


        my_image = ctk.CTkImage(light_image=Image.open('A2 - Free Currency App/03 - Executeable Project Code/freecurrencyapi.png'), size=(260, 30))
        self.image = my_image  # Keep a reference

        image_label = ctk.CTkLabel(self, image=my_image, text="")
        image_label.grid(row=1, column=1, sticky="nw", padx=(50, 0), pady=(60, 0))

        # Tagline label
        tagline = ctk.CTkLabel(self, text="Quick Convert", text_color="black", font=("Arial", 40, "bold"))
        tagline.place(relx=0.5, rely=0.35, anchor="center")

        # Frame for dropdown and text field
        input_frame = ctk.CTkFrame(self, fg_color="transparent")
        input_frame.place(relx=0.5, rely=0.55, anchor="center")

        # Common styles
        dropdown_style = {
            "width": 100,
            "height": 50,
            "fg_color": "#22D3EE",
            "button_color": "#22D3EE",
            "button_hover_color": "#1CB5D1",
            "font": ("Arial", 15),
        }

        textfield_style = {
            "width": 500,
            "height": 50,
            "fg_color": "white",
            "border_color": "white",
            "font": ("Arial", 15)
        }


        #This is a variable storing or retreiving the currency code from the dictionary of the show_currencies function  defined in the App base class
        currencies = list(self.controller.show_currencies().keys())
        
        # From currency
        self.from_dropdown = ctk.CTkOptionMenu(input_frame, values=currencies, **dropdown_style, command=self.update_conversion)
        self.from_dropdown.set("USD")
        self.from_dropdown.grid(row=0, column=0, padx=(0, 10), pady=(0, 30))

        self.from_text_field = ctk.CTkEntry(input_frame, text_color="black", **textfield_style)
        self.from_text_field.grid(row=0, column=1, pady=(0, 30))
        self.from_text_field.bind("<KeyRelease>", self.update_conversion)

        # To currency
        self.to_dropdown = ctk.CTkOptionMenu(input_frame, values=currencies, **dropdown_style, command=self.update_conversion)
        self.to_dropdown.set("EUR")
        self.to_dropdown.grid(row=1, column=0, padx=(0, 10))

        self.to_text_field = ctk.CTkEntry(input_frame, text_color="black", **textfield_style)
        self.to_text_field.grid(row=1, column=1)

        # Exchange Rate label
        self.exchange_rate_label = ctk.CTkLabel(input_frame, text="", text_color="black", font=("Arial", 20), wraplength=700, justify="center")
        self.exchange_rate_label.grid(row=2, column=0, columnspan=2, pady=(20, 0))

        # Initial conversion
        self.update_conversion()

    # This Function gets the information from the dropdown and text field and converts the currency be retreiving the right exchange rate.
    def update_conversion(self, *args):
        try: #gets the input from the "form_dropdown" "to_dropdown" and the "from_text_field" (The currency codes and the base_amount) 
            from_currency = self.from_dropdown.get()
            to_currency = self.to_dropdown.get()
            amount = float(self.from_text_field.get() or 0)
            
            # Using the defined get_exchang_rate function from the CurrencyPage class 
            # it calculates the converted amount by retrieveing the right exchange rate
            exchange_rate = self.get_exchange_rate(from_currency, to_currency)  # Use inherited method
            converted_amount = amount * exchange_rate
            
            #Prints the converted amount in the "to_text_field"
            self.to_text_field.delete(0, 'end')
            self.to_text_field.insert(0, f"{converted_amount:.2f}")

            #Prints the exchange rate equivalent to 1 base currency in the "exchange_rate_label"
            self.exchange_rate_label.configure(text=f"1 {from_currency} = {exchange_rate:.4f} {to_currency}")
        except ValueError:
            # Handle invalid input
            self.to_text_field.delete(0, 'end')
            self.exchange_rate_label.configure(text="Invalid input")
        
        #Directs the user back to the Menu Page
        back_button = ctk.CTkButton(
            master=self,
            text="Go Back",
            text_color="black",
            border_width=2,    
            fg_color="transparent",
            hover_color="#FAFAFA",
            border_color="black",
            width=170,
            height=50,
            font=("Arial", 15),
            
            command=lambda: self.controller.show_frame("MenuPage")
        )
        # Anchors it to the lower left position for consitency across all pages
        def update_button_position(event=None):
            back_button.place(x=50, y=self.winfo_height() - 70, anchor="sw")

        self.bind("<Configure>", update_button_position)
        update_button_position()  # Initial positioning



        canvas = ctk.CTkCanvas(self, width=300, height=150, bg="white", highlightthickness=0)  # Create a canvas for drawing

        # Draw a square on the canvas
        rectangle_width = 300  # width of rectangle
        rectangle_heigth = 150  # height of rectangle
        canvas.create_rectangle(0, 0, rectangle_width, rectangle_heigth, fill="#22D3EE")  # Draw a blue square
        # Place the canvas in the bottom-left corner
        canvas.place(relx=1, rely=0, anchor='ne')  # Use place to position it at the bottom right

# ------------------------------------------------------------------------------------------
# Define the Exchange Rates Page
class ExchangeRatesPage(CurrencyPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)


        my_image = ctk.CTkImage(light_image=Image.open('A2 - Free Currency App/03 - Executeable Project Code/freecurrencyapi.png'), size=(260, 30))
        self.image = my_image  # Keep a reference

        image_label = ctk.CTkLabel(self, image=my_image, text="")
        image_label.grid(row=1, column=1, sticky="nw", padx=(50, 0), pady=(60, 0))

        # Tagline label
        tagline = ctk.CTkLabel(self, text="Exchange Rates", text_color="black", font=("Arial", 40, "bold"))
        tagline.place(relx=0.5, rely=0.35, anchor="center")

        # Frame for dropdown and text field
        input_frame = ctk.CTkFrame(self, fg_color="transparent")
        input_frame.place(relx=0.5, rely=0.55, anchor="center")

        # Common styles
        textfield_style = {
            "width": 500,
            "height": 50,
            "fg_color": "white",
            "border_color": "white",
            "font": ("Arial", 15),
            "text_color": "black"
        }
        
        dropdown_style = {
            "width": 200,
            "height": 50,
            "fg_color": "#22D3EE",
            "button_color": "#22D3EE",
            "button_hover_color": "#1CB5D1",
            "font": ("Arial", 15)
}

        #This is a variable storing or retreiving the currency code from the dictionary of the show_currencies function  defined in the App base class
        currencies = list(self.controller.show_currencies().keys())
        
        # Currency dropdown
        self.exchange_dropdown = ctk.CTkOptionMenu(input_frame, values=currencies, **dropdown_style, command=self.update_exchange_rate)
        self.exchange_dropdown.set("USD")
        self.exchange_dropdown.grid(row=0, column=0, padx=(0, 10), pady=(0, 30))

        self.rate_text_field = ctk.CTkEntry(input_frame, **textfield_style)
        self.rate_text_field.grid(row=0, column=1, pady=(0, 30))

        # Exchange Rate label
        self.exchange_rate_label = ctk.CTkLabel(input_frame, text="", text_color="black", font=("Arial", 20), wraplength=700, justify="center")
        self.exchange_rate_label.grid(row=2, column=0, columnspan=2, pady=(20, 0))

    # This Function gets the information from the dropdown and text field and retrieves the right exchange rate.
    def update_exchange_rate(self, *args):
        try: # gets data input in the exchange_dropdown as selected_currency, then uses the function of get_exchange_rate 
            selected_currency = self.exchange_dropdown.get()
            exchange_rate = self.get_exchange_rate('USD', selected_currency)  # Use inherited method
            
            # prints the exchange rate to the rate_text_field and sets it to read only
            self.rate_text_field.configure(state="normal")
            self.rate_text_field.delete(0, 'end')
            self.rate_text_field.insert(0, f"{exchange_rate:.4f}")
            self.rate_text_field.configure(state="readonly")
            
            #Prints the exchange rate equivalent to 1 USD in the "exchange_rate_label"
            self.exchange_rate_label.configure(text=f"1 USD = {exchange_rate:.4f} {selected_currency}")
        except Exception as e:
            print(f"Error updating exchange rate: {e}")
            self.rate_text_field.configure(state="normal")
            self.rate_text_field.delete(0, 'end')
            self.rate_text_field.insert(0, "Error")
            self.rate_text_field.configure(state="readonly")
       
        back_button = ctk.CTkButton(
            master=self,
            text="Go Back",
            text_color="black",
            border_width=2,    
            fg_color="transparent",
            hover_color="#FAFAFA",
            border_color="black",
            width=170,
            height=50,
            font=("Arial", 15),
            
            command=lambda: self.controller.show_frame("MenuPage")
        )

        def update_button_position(event=None):
            back_button.place(x=50, y=self.winfo_height() - 70, anchor="sw")

        self.bind("<Configure>", update_button_position)
        update_button_position()  # Initial positioning



        canvas = ctk.CTkCanvas(self, width=300, height=150, bg="white", highlightthickness=0)  # Create a canvas for drawing

        # Draw a square on the canvas
        rectangle_width = 300  # width of rectangle
        rectangle_heigth = 150  # height of rectangle
        canvas.create_rectangle(0, 0, rectangle_width, rectangle_heigth, fill="#22D3EE")  # Draw a blue square
        # Place the canvas in the bottom-left corner
        canvas.place(relx=1, rely=0, anchor='ne')  # Use place to position it at the bottom right

# ------------------------------------------------------------------------------------------
# Define the Currency Dictionary Page
class CurrencyDictionaryPage(CurrencyPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        my_image = ctk.CTkImage(light_image=Image.open('A2 - Free Currency App/03 - Executeable Project Code/freecurrencyapi.png'), size=(260, 30))
        self.image = my_image  # Keep a reference

        image_label = ctk.CTkLabel(self, image=my_image, text="")
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


        #This is a variable storing or retreiving the currency code from the dictionary of the get_dict_keys function  defined in the App base class
        currencies = list(self.controller.get_dict_keys().keys())
        
        # From currency
        self.exchange_dropdown = ctk.CTkOptionMenu(self, values=currencies, **dropdown_style, command=self.update_dict)
        self.exchange_dropdown.set("EUR")
        self.exchange_dropdown.grid(row=2, column=1, padx=(50, 0), pady=(100, 0), sticky="w")
        
        # Create frame to place the currency information in
        dict_frame = ctk.CTkFrame(self, fg_color="white")
        dict_frame.grid(row=3, column=2, sticky="w", padx=10, pady=10)

        # Heading for Currency Displayed
        self.master_name = ctk.CTkLabel(dict_frame, text="", text_color="black", font=("Arial", 40, "bold"))
        self.master_name.grid(row=0, column=0, padx=50, pady=30, sticky="w")


        # Common Style
        info_style = {
            "text_color":"black", 
            "font":("Arial", 30), 
            "wraplength":500,  # Adjust this value as needed
            "justify":"left"
        }

        self.name = ctk.CTkLabel(dict_frame, text="", **info_style)
        self.name.grid(row=1, column=0, padx=50, pady=10, sticky="w")
        self.symbol = ctk.CTkLabel(dict_frame, text="", **info_style)
        self.symbol.grid(row=2, column=0, padx=50, pady=10, sticky="w")
        self.native_symbol = ctk.CTkLabel(dict_frame, text="", **info_style)
        self.native_symbol.grid(row=3, column=0, padx=50, pady=10, sticky="w")
        self.name_plural = ctk.CTkLabel(dict_frame, text="", **info_style)
        self.name_plural.grid(row=4, column=0, padx=50, pady=(10, 30), sticky="w")



        # After adding all labels, update the frame
        dict_frame.update_idletasks()

        # Get the required width and height
        req_width = dict_frame.winfo_reqwidth()
        req_height = dict_frame.winfo_reqheight()

        # Set the width to be wider (e.g., 1.2 times the required width)
        dict_frame.configure(width=max(600, int(req_width * 1.2)), height=req_height)

        # Prevent the frame from adjusting its size
        dict_frame.grid_propagate(False)


        back_button = ctk.CTkButton(
            master=self,
            text="Go Back",
            text_color="black",
            border_width=2,    
            fg_color="transparent",
            hover_color="#FAFAFA",
            border_color="black",
            width=170,
            height=50,
            font=("Arial", 15),
            
            command=lambda: controller.show_frame("MenuPage")
        )

        def update_button_position(event=None):
            back_button.place(x=50, y=self.winfo_height() - 70, anchor="sw")

        self.bind("<Configure>", update_button_position)
        update_button_position()  # Initial positioning



        canvas = ctk.CTkCanvas(self, width=300, height=150, bg="white", highlightthickness=0)  # Create a canvas for drawing

        # Draw a square on the canvas
        rectangle_width = 300  # width of rectangle
        rectangle_heigth = 150  # height of rectangle
        canvas.create_rectangle(0, 0, rectangle_width, rectangle_heigth, fill="#22D3EE")  # Draw a blue square
        # Place the canvas in the bottom-left corner
        canvas.place(relx=1, rely=0, anchor='ne')  # Use place to position it at the bottom right


    # This function retrieves the data of each currency code by specific keys (name, symbol, native symbol, and plural name).
    def update_dict(self, *args):
        try:
            currency_code = self.exchange_dropdown.get()  # Get selected currency code from dropdown
            code, name, symbol, symbol_native, name_plural = self.show_dict_info(currency_code)  # Call show_dict_info

            # Update UI labels with the fetched information
            self.master_name.configure(text=f"{code}")
            self.name.configure(text=f"Name: {name}")
            self.symbol.configure(text=f"Symbol: {symbol}")
            self.native_symbol.configure(text=f"Native Symbol: {symbol_native}")
            self.name_plural.configure(text=f"Plural Name: {name_plural}")
        except KeyError:
            # Handle case where currency_code is not found in data
            self.name.configure(text="Invalid input")
            self.symbol.configure(text="Invalid input")
            self.native_symbol.configure(text="Invalid input")
            self.name_plural.configure(text="Invalid input")
        except Exception as e:
            print(f"Error: {e}")
            # Handle other exceptions


# Run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()
