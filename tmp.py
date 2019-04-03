from tkinter import (
    Tk, Label, Entry, Button, Listbox
)

class MainWindow():

    def __init__(self, root):
        super().__init__()

        self.root = root

        #this is the user menu, loads everytime on launch
        Button(self.root, text = "View Restaurants", 
                height=4, width=16, 
                padx=1, pady=1, 
                command=viewingRestaurantWindow)\
            .pack()

        Button(self.root, text = "Add Restaurant(s)\nnot yet working", 
                height=4, width=16, 
                padx=1, pady=1)\
            .pack()

        Button(self.root, text = "View Meal Types", 
                height=4, width=16, 
                padx=1, pady=1, 
                command=viewingMealTypeWindow)\
            .pack()

        Button(self.root, text = "Get Recommendation", 
                height=4, width=16, 
                padx=1, pady=1,
                command=GetRecommendation)\
        .pack()

        Button(self.root, text='Quit',
                width=16,
                fg='red', 
                command=self.root.destroy)\
        .pack()
        
#re-useable method to pressback and destroy window
def pressBackButton(window):
    return Button(window, text="Back", command=window.destroy)
#------------------------------------------------------------------
class ViewRestaurantsWindow():
    
    def __init__(self):
        window = Tk()
        window.title("View Restaurants")
        listbox = Listbox(window, width=30, height=15)
        listbox.insert(1, "Restaurant")
        listbox.insert(2, "Restaurant")
        listbox.insert(3, "Restaurant")
        listbox.insert(4, "Restaurant")
        listbox.insert(5, "Restaurant")
        listbox.pack()

        Button(window, text="Back", command=window.destroy).pack()

#------------------------------------------------------------------
class ViewMealTypesWindow():

    def __init__(self):
        window = Tk()
        window.title("Meal Types")
        listbox = Listbox(window, width=30, height=15)
        listbox.insert(1, "Meal Type")
        listbox.insert(2, "Meal Type")
        listbox.insert(3, "Meal Type")
        listbox.insert(4, "Meal Type")
        listbox.insert(5, "Meal Type")
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
                .pack()
        Button(window, text="I want a user id", 
                        height=2, width=16,
                        command=createUserId)\
                .pack()
        Button(window, text="Back", command=window.destroy)\
                .pack()

def viewingRestaurantWindow():
    ViewRestaurantsWindow()

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

        Label(window, text="Full Name: ",width=10,font=(10)).pack()

        Entry(window).pack()

        Label(window, text="User Id: ",width=10,font=(10)).pack()

        Entry(window).pack()

        Button(window, text="Sign Up").pack()
        Button(window, text="Back", command=window.destroy).pack()


#------------------------------------------------------------------
#look up user
class LogIn():
    def __init__(self): 
        window = Tk()
        window.geometry("300x150")
        window.title("Search")

        Label(window, text="User Id: ",width=10,font=(10)).pack()

        Entry(window).pack()

        Label(window, text="User Id: ",width=10,font=(10)).pack()

        Entry(window).pack()

        Button(window, text="Search").pack()
        Button(window, text="Back", command=window.destroy).pack() 

def createUserId():
    SignUp()

def getUserId():
    LogIn()

#------------------------------------------------------------------
def launchApp():
    window = Tk()
    window.geometry("500x500")
    window.title("Restaurant Recommendation System")
    Label(window, text = "Welcome to RRS"
                , width=20, font=("bold", 20))\
    .pack()
    MainWindow(window)
    window.mainloop()


launchApp()