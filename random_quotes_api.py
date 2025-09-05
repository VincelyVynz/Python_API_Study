# --------------------------- Random Quotes --------------------------- #
import tkinter as tk
import requests


# --------------------------- Color Palette --------------------------- #
COLOR_BG = "#AFEEEE"        # PaleTurquoise
COLOR_PRIMARY = "#87CEFA"   # LightSkyBlue (button background)
COLOR_HIGHLIGHT = "#20B2AA" # LightSeaGreen (hover / active background)
COLOR_TEXT = "#2F4F4F"      # DarkSlateGray (text color)
COLOR_ACCENT = "#E0FFFF"    # LightCyan (quote box background)
COLOR_BUTTON_TEXT = "#ffffff"

# --------------------------- Fonts --------------------------- #
H_FONT = ("Lucida Handwriting", 24, "bold")
M_FONT = ("Lucida Handwriting", 20, "bold")
S_FONT = ("Lucida Handwriting", 14, "bold")
api_url = "https://zenquotes.io/api/random"
PLACEHOLDER = "Hello !"

# TODO 1: Create a Tkinter window with a title and set a reasonable size
window = tk.Tk()
window.title("Random Quotes")
window.minsize(400, 400)
window.config(padx=20, pady=20, bg = "PaleTurquoise")
label1 = tk.Label(text="Random Quotes", font= H_FONT)
label1.config(bg = "PaleTurquoise", highlightthickness = 0, padx = 20, pady = 30)
label1.grid(column=0, row=0)

# TODO 2: Add a large Label widget to display the quote text

quote_label = tk.Label(text=PLACEHOLDER, font= M_FONT)
quote_label.config(bg = "PaleTurquoise", highlightthickness = 0, padx = 10, pady = 10)
quote_label.grid(column=1, row=0)
quote_label.grid(column=0, row=1)
# TODO 3: Add a smaller Label widget below to display the author name

author_label = tk.Label(text=PLACEHOLDER, font= S_FONT)
author_label.config(bg = "PaleTurquoise", highlightthickness = 0, padx = 10, pady = 10)
author_label.grid(column=0, row=2)

# TODO 4: Add a Button widget labeled "New Quote"
new_quote_btn = tk.Button(text="New Quote", font= S_FONT)
new_quote_btn.config(bg = "PaleTurquoise", highlightthickness = 0, padx = 10, pady = 10)
new_quote_btn.grid(column=0, row=3)
# TODO 5: Write a function that makes a GET request to https://zenquotes.io/api/random

def random_quote():
    try:
        response = requests.get(api_url)
        quote_api_response = response.json()
        new_quote = quote_api_response[0]["q"]
        new_author = quote_api_response[0]["a"]
        quote_label.config(text=new_quote)
        author_label.config(text=new_author)

    except  requests.exceptions.RequestException as e:
        print(e)
        return e

# TODO 6: Parse the JSON response to extract the quote ("q") and author ("a")

# TODO 7: Update the quote and author Labels with the fetched data when the button is clicked
new_quote_btn.configure(command=random_quote)
# TODO 8: Disable the button and change its text to "Loading..." while fetching data
# TODO 9: Re-enable the button and reset its text after the data is fetched or if an error occurs
# TODO 10: Handle errors gracefully (network issues, JSON parsing errors) and display a friendly message in the UI
# TODO 11 (Optional): Style the labels and window for better readability (fonts, colors, padding)
# TODO 12 (Optional): Test the app by clicking the button multiple times and with no internet connection to check error handling




window.mainloop()