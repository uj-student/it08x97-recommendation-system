from tkinter import (
    Tk,
    Label,
    Entry,
    Button,
    Listbox,
    Text
)

import api
import app


class MainWindow:

    def __init__(self, root):
        super().__init__()

        self.root = root

        # this is the user menu, loads every time on launch
        Button(self.root, text="View Restaurants",
               height=4, width=18,
               padx=1, pady=1,
               command=viewing_restaurant_window) \
            .place(x=150, y=90)

        Button(self.root, text="View Cuisines",
               height=4, width=18,
               padx=1, pady=1,
               command=viewing_cuisines_window) \
            .place(x=150, y=180)

        Button(self.root, text="View Restaurants Types",
               height=4, width=18,
               padx=1, pady=1,
               command=viewing_restaurant_types_window) \
            .place(x=150, y=270)

        Button(self.root, text="Recommendation Menu",
               height=4, width=18,
               padx=1, pady=1,
               command=get_recommendation_menu) \
            .place(x=150, y=360)

        Button(self.root, text='Quit',
               width=16,
               fg='red',
               command=self.root.destroy) \
            .place(x=150, y=450)


# reusable method to press-back and destroy window
def press_back_button(window):
    return Button(window, text="Back", command=window.destroy)


# ------------------------------------------------------------------


class ViewRestaurantTypeWindow:

    def __init__(self):
        data = api.get_establishments()
        print(type(data), "Heloooooooooooo")
        window = Tk()
        window.title("Restaurants Types")
        listbox = Listbox(window, width=30, height=15)
        for establishment in data['establishments']:
            listbox.insert(1, establishment['establishment']['name'])
        listbox.pack()

        Button(window, text="Back", command=window.destroy).pack()


# ------------------------------------------------------------------


class ViewRestaurantWindow:

    def __init__(self):
        data = api.get_restaurants()
        window = Tk()
        window.title("View Restaurants")
        listbox = Listbox(window, width=30, height=15)
        for rest in data["restaurants"]:
            listbox.insert(1, rest["restaurant"]["name"])
        listbox.pack()

        Button(window, text="Back", command=window.destroy).pack()


# ------------------------------------------------------------------


class ViewCuisinesWindow:

    def __init__(self):
        data = api.get_cuisines()
        window = Tk()
        window.title("View Cuisines")
        listbox = Listbox(window, width=30, height=15)
        for cuisine in data["cuisines"]:
            listbox.insert(1, cuisine['cuisine']['cuisine_name'])
        listbox.pack()

        Button(window, text="Back", command=window.destroy).pack()


# ------------------------------------------------------------------


class GetRecommendation:

    def __init__(self):
        window = Tk()
        window.geometry('400x200')
        window.title("Get Recommendations")

        Button(window, text="Train Model",
               height=2, width=16,
               command=self.train_model) \
            .pack()

        Button(window, text="Test Model",
               height=2, width=16,
               command=create_user_id) \
            .pack()

        Button(window, text="Get Recommendation",
               height=2, width=16,
               command=create_user_id) \
            .pack()

        Button(window, text="Back", command=window.destroy) \
            .place(x=175, y=150)

    def train_model(self):
        self.window = Tk()
        # self.window.geometry('400x200')
        self.window.title("Training Model")

        text = Text(self.window, width=40, height=25)
        text.pack()
        text.insert("end", "\tRecommended Restaurants: \n")
        for i in app.calculate_df_cuisine():
            text.insert("end", "{}\n".format(i))
        text.tag_config('word_class', font='arial 12 bold italic', lmargin1=30,
                        spacing1=10, spacing3=15)
        text.pack()

        Button(self.window, text="Back", command=self.window.destroy).pack()

    @staticmethod
    def format_output():
        output = app.calculate_df_cuisine()
        for i in output:
            return i


# ------------------------------------------------------------------


def viewing_restaurant_types_window():
    ViewRestaurantTypeWindow()


def viewing_restaurant_window():
    ViewRestaurantWindow()


def viewing_cuisines_window():
    ViewCuisinesWindow()


def get_recommendation_menu():
    GetRecommendation()


# ------------------------------------------------------------------


# to get user id
class SignUp:

    def __init__(self):
        window = Tk()
        window.geometry("300x150")
        window.title("Sign Up")

        Label(window, text="Full Name: ", width=10, font=10).place(x=20, y=40)

        Entry(window).place(x=100, y=40)

        Label(window, text="User Id: ", width=10, font=10).place(x=20, y=40)

        Entry(window).place(x=100, y=40)

        Button(window, text="Sign Up").place(x=120, y=70)
        Button(window, text="Back", command=window.destroy).place(x=180, y=70)


# ------------------------------------------------------------------


# look up user
class LogIn:
    def __init__(self):
        window = Tk()
        window.geometry("300x150")
        window.title("Search")

        Label(window, text="User Id: ", width=10, font=10).place(x=20, y=40)

        Entry(window).place(x=100, y=40)

        Label(window, text="User Id: ", width=10, font=10).place(x=20, y=40)

        Entry(window).place(x=100, y=40)

        Button(window, text="Search").place(x=120, y=70)
        Button(window, text="Back", command=window.destroy).place(x=180, y=70)


def create_user_id():
    SignUp()


def get_user_id():
    LogIn()


# ------------------------------------------------------------------


def _launch():
    window = Tk()
    window.geometry("500x800")
    window.title("Restaurant Recommendation System")
    Label(window, text="Welcome to RRS"
          , width=20, font=("bold", 20)) \
        .place(x=90, y=53)
    MainWindow(window)
    window.mainloop()


_launch()
