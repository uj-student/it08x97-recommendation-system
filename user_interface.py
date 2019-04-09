from tkinter import (
    Tk, 
    Label, 
    Entry, 
    Button, 
    Listbox
)
import api


class MainWindow:

    def __init__(self, root):
        super().__init__()

        self.root = root

        # this is the user menu, loads every time on launch
        Button(self.root, text="View Restaurants Types",
               height=4, width=16,
               padx=1, pady=1,
               command=viewing_restaurant_types_window)\
            .place(x=150, y=90)

        Button(self.root, text="View Restaurant",
               height=4, width=16,
               padx=1, pady=1,
               command=viewing_restaurant_window)\
            .place(x=150, y=180)

        Button(self.root, text="View Meal Types",
               height=4, width=16,
               padx=1, pady=1,
               command=viewing_meal_type_window)\
            .place(x=150, y=270)

        Button(self.root, text="View Cuisines",
               height=4, width=16,
               padx=1, pady=1,
               command=viewing_cuisines_window) \
            .place(x=150, y=360)

        Button(self.root, text="Get Recommendation",
                height=4, width=16,
                padx=1, pady=1,
                command=get_recommendation_menu)\
            .place(x=150, y=450)

        Button(self.root, text='Quit',
                width=16,
                fg='red', 
                command=self.root.destroy)\
            .place(x=150, y=530)


# reusable method to press-back and destroy window
def press_back_button(window):
    return Button(window, text="Back", command=window.destroy)
# ------------------------------------------------------------------


class ViewRestaurantTypeWindow:
    
    def __init__(self):
        data = api.get_establishments()
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


class ViewMealTypesWindow:

    def __init__(self):
        window = Tk()
        window.title("Meal Types")
        listbox = Listbox(window, width=30, height=15)
        # listbox.insert(1, "Meal Type")
        # listbox.insert(2, "Meal Type")
        # listbox.insert(3, "Meal Type")
        # listbox.insert(4, "Meal Type")        
        listbox.pack()

        Button(window, text="Back", command=window.destroy).pack()
# ------------------------------------------------------------------


class ViewCuisinesWindow:

    def __init__(self):
        data = api.get_cuisines()
        window = Tk()
        window.title("View Cuisines")
        listbox = Listbox(window, width=30, height=15)
        for cuisi in data["cuisines"]:
            listbox.insert(1, cuisi['cuisine']['cuisine_name'])
        listbox.pack()

        Button(window, text="Back", command=window.destroy).pack()
# ------------------------------------------------------------------


class GetRecommendation:
    def __init__(self):
        window = Tk()
        window.geometry('400x200')
        window.title("Get Recommendations")

        Button(window, text="I have a user id",
               height=2, width=16,
               command=get_user_id)\
            .place(x=40, y=70)
        Button(window, text="I want a user id",
               height=2, width=16,
               command=create_user_id)\
            .place(x=210, y=70)
        Button(window, text="Back", command=window.destroy)\
            .place(x=175, y=150)
# ------------------------------------------------------------------


def viewing_restaurant_types_window():
    ViewRestaurantTypeWindow()


def viewing_restaurant_window():
    ViewRestaurantWindow()


def viewing_meal_type_window():
    ViewMealTypesWindow()


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
                , width=20, font=("bold", 20))\
        .place(x=90, y=53)
    MainWindow(window)
    window.mainloop()


_launch()
