import freecurrencyapi

def get_exchange_rate():
    apikey = freecurrencyapi.Client('fca_live_UGsuYzak3zROde7EAjLjpqja3BGIYiOuBvoCqpO6')
    result = apikey.latest()
    return result['data']['EUR']

def convert_usd_to_eur():
    amount_usd = float(input("Enter the amount in USD: "))
    exchange_rate = get_exchange_rate()
    
    amount_eur = amount_usd * exchange_rate
    
    print(f"\n{amount_usd:.2f} USD is equal to {amount_eur:.2f} EUR")
    print(f"Exchange rate: 1 USD = {exchange_rate:.4f} EUR")


def get_currencies():
    apikey = freecurrencyapi.Client('fca_live_UGsuYzak3zROde7EAjLjpqja3BGIYiOuBvoCqpO6')
    result = apikey.latest()
    return result['data'].keys()


def show_currencies():
    show = input("Type yes to show currencies: ")
    currencies = get_currencies()
    
    if show=="yes":
        print(currencies)


def get_dict_keys():
    apikey = freecurrencyapi.Client('fca_live_UGsuYzak3zROde7EAjLjpqja3BGIYiOuBvoCqpO6')
    result = apikey.currencies()  # Fetch currency data
    return result['data'].keys()

def print_dict_keys():
    info = get_dict_keys()
    print(info)

def get_info():
    apikey = freecurrencyapi.Client('fca_live_UGsuYzak3zROde7EAjLjpqja3BGIYiOuBvoCqpO6')
    result = apikey.currencies(currencies=['CNY'])  # Fetch currency data
    data = result['data']['CNY']  # Access the EUR data
    return data['name'], data['symbol'], data['symbol_native'],data['name_plural']  # Return symbol and name


def show_info():
    symbol, name, symbol_native, name_plural = get_info()
    print(f"{name}")
    print(f"{symbol}")
    print(f"{symbol_native}")
    print(f"{name_plural}")
    
# convert_usd_to_eur()
# show_currencies()
print_dict_keys()
show_info()