import tkinter as tk
from tkinter import ttk, messagebox
import requests

import freecurrencyapi

client = freecurrencyapi.Client('fca_live_UGsuYzak3zROde7EAjLjpqja3BGIYiOuBvoCqpO6')
# print(client.status())


# GET INPUT FROM USD TO EURO
amount = float(input("Input amount (USD): "))

result = client.currencies(currencies=['EUR', 'CAD', 'USD'])

for i in result:
    for j in i.items():
        print(j)

