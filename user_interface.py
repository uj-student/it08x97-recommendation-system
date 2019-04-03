from tkinter import (
    Tk, 
    Label, 
    Entry, 
    Button, 
    Listbox
)
import api
import json

class MainWindow():

    def __init__(self, root):
        super().__init__()

        self.root = root

        #this is the user menu, loads everytime on launch
        Button(self.root, text = "View Restaurants Types", 
                height=4, width=16, 
                padx=1, pady=1, 
                command=viewingRestaurantTypesWindow)\
            .place(x = 150, y = 90)

        Button(self.root, text = "View Restaurant", 
                height=4, width=16, 
                padx=1, pady=1,
                command=viewingRestaurantWindow)\
            .place(x = 150, y = 180)

        Button(self.root, text = "View Meal Types", 
                height=4, width=16, 
                padx=1, pady=1, 
                command=viewingMealTypeWindow)\
            .place(x = 150, y = 270)

        Button(self.root, text = "Get Recommendation", 
                height=4, width=16, 
                padx=1, pady=1,
                command=GetRecommendation)\
        .place(x = 150, y = 360)

        Button(self.root, text='Quit',
                width=16,
                fg='red', 
                command=self.root.destroy)\
        .place(x = 150,y = 440)
        
#re-useable method to pressback and destroy window
def pressBackButton(window):
    return Button(window, text="Back", command=window.destroy)
#------------------------------------------------------------------
class ViewRestaurantTypeWindow():
    
    def __init__(self):
        data = json.loads(api.get_establishments())
        window = Tk()
        window.title("Restaurants Types")
        listbox = Listbox(window, width=30, height=15)
        for establishment in data['establishments']:
            listbox.insert(1, establishment['establishment']['name'])
        listbox.pack()

        Button(window, text="Back", command=window.destroy).pack()

#------------------------------------------------------------------

class ViewRestaurantWindow():
    
    def __init__(self):
        data = json.loads(api. get_rest())
        window = Tk()
        window.title("View Restaurants")
        listbox = Listbox(window, width=30, height=15)
        for rest in data['restaurants']:
            listbox.insert(1, rest['restaurant']['name'])
        listbox.pack()

        Button(window, text="Back", command=window.destroy).pack()

#------------------------------------------------------------------

class ViewMealTypesWindow():

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

#------------------------------------------------------------------
class GetRecommendation():
    def __init__(self):
        window = Tk()
        window.geometry('400x200')
        window.title("Get Recommendations")

        Button(window, text="I have a user id", 
                        height=2, width=16,
                        command=getUserId)\
                .place(x = 40, y = 70)
        Button(window, text="I want a user id", 
                        height=2, width=16,
                        command=createUserId)\
                .place(x = 210, y = 70)
        Button(window, text="Back", command=window.destroy)\
                .place(x = 175, y = 150)

def viewingRestaurantTypesWindow():
    ViewRestaurantTypeWindow()

def viewingRestaurantWindow():
    ViewRestaurantWindow()

def viewingMealTypeWindow():
    ViewMealTypesWindow()

def getRecommendationMenu():
    GetRecommendation()

#------------------------------------------------------------------
#to get user id
class SignUp():

    def __init__(self):
        window = Tk()
        window.geometry("300x150")
        window.title("Sign Up")

        Label(window, text="Full Name: ",width=10,font=(10)).place(x=20, y=40)

        Entry(window).place(x=100, y=40)

        Label(window, text="User Id: ",width=10,font=(10)).place(x=20, y=40)

        Entry(window).place(x=100, y=40)

        Button(window, text="Sign Up").place(x=120, y=70)
        Button(window, text="Back", command=window.destroy).place(x=180, y=70)


#------------------------------------------------------------------
#look up user
class LogIn():
    def __init__(self): 
        window = Tk()
        window.geometry("300x150")
        window.title("Search")

        Label(window, text="User Id: ",width=10,font=(10)).place(x=20, y=40)

        Entry(window).place(x=100, y=40)

        Label(window, text="User Id: ",width=10,font=(10)).place(x=20, y=40)

        Entry(window).place(x=100, y=40)

        Button(window, text="Search").place(x=120, y=70)
        Button(window, text="Back", command=window.destroy).place(x=180, y=70) 

def createUserId():
    SignUp()

def getUserId():
    LogIn()

#------------------------------------------------------------------
def launchApp():
    window = Tk()
    window.geometry("500x800")
    window.title("Restaurant Recommendation System")
    Label(window, text = "Welcome to RRS"
                , width=20, font=("bold", 20))\
    .place(x = 90, y = 53)
    MainWindow(window)
    window.mainloop()


launchApp()