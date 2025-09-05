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
H_FONT = ("Lucida Handwriting", 30, "bold")
M_FONT = ("Lucida Handwriting", 18, "bold")
S_FONT = ("Lucida Handwriting", 14, "bold")
api_url = "https://zenquotes.io/api/random"

# --------------------------- Function --------------------------- #
def random_quote():
    try:
        new_quote_btn.config(text= "loading", state="disabled")
        window.update()
        response = requests.get(api_url)
        quote_api_response = response.json()
        new_quote = quote_api_response[0]["q"]
        new_author = quote_api_response[0]["a"]
        quote_label.config(text=new_quote)
        author_label.config(text=f"- {new_author}")
        new_quote_btn.config(text = "New Random Quote",state="normal")

    except  requests.exceptions.RequestException as e:
        quote_label.config(text = "Failed to fetch quote. Please try again.")
        author_label.config(text= e.__str__(), wraplength=350)
        window.update()
        print(e.args)
        return e

# --------------------------- UI --------------------------- #


window = tk.Tk()
window.title("Random Quotes")
window.minsize(400, 400)
window.config(padx=20, pady=20, bg = COLOR_BG )


label1 = tk.Label(text="Random Quotes", font= H_FONT)
label1.config(bg = COLOR_BG, fg= COLOR_TEXT, highlightthickness = 0, padx = 20, pady = 30, justify = "center")
label1.grid(column=0, row=0,columnspan=2)



quote_label = tk.Label(text="Quote goes here", font= M_FONT)
quote_label.config(bg=COLOR_BG, fg=COLOR_TEXT, wraplength=350, justify="center", padx=10, pady=10)
quote_label.grid(column=0, row=1, columnspan=2)


author_label = tk.Label(text="- Author", font= S_FONT)
author_label.config(bg = "PaleTurquoise", highlightthickness = 0, padx = 10, pady = 10)
author_label.grid(column=1, row=2)


new_quote_btn = tk.Button(text="Get New Quote", font= S_FONT)
new_quote_btn.config(
    bg=COLOR_PRIMARY,
    fg=COLOR_BUTTON_TEXT,
    activebackground=COLOR_HIGHLIGHT,
    activeforeground=COLOR_BUTTON_TEXT,
    relief="groove",
    bd=2,
    padx=10,
    pady=10,
)
#     relief="raised"
# new_quote_btn.config(bg = "PaleTurquoise", highlightthickness = 0, padx = 10, pady = 10)
new_quote_btn.grid(column=0, row=3, columnspan=2, pady = (30,5))


credit_label = tk.Label(
    window,
    text="Quotes provided by zenquotes.io",
    font=("Arial", 10),
    bg=COLOR_BG,
    fg=COLOR_TEXT
)
credit_label.grid(column=0, row=4, columnspan=2)

random_quote()

new_quote_btn.configure(command=random_quote)

window.mainloop()