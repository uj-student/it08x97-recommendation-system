import csv
import random
import os
import api
import collections
import math

MY_CSV = "food_coded_temp.csv"
TRAINING_SET = "train.csv"
TEST_SET = "test.csv"
TRAINING_DATA = "training_model.csv"


def open_user_file():
    file_present = os.path.isfile(MY_CSV)
    if file_present:
        # open csv file and write each row into array (students)
        with open(MY_CSV, "r") as csv_data:
            data = csv.DictReader(csv_data)
            count = 0
            students = []
            for row in data:
                students.append(row)
                count += 1  # keep track of entries into array

            print("\n\n\nNumber of datasets is: {}".format(count))
        return students


def split_data(data):
    # data will be split into 80% train and 20% test
    x_ = 0.8 * len(data)
    x_ = int(x_)
    print("\n\nNumber of training set: {}".format(x_))

    x_train = []
    # training data is selected at random form array
    for row in range(x_):
        # pick random number
        index = random.randint(0, len(data) - 1)
        # pick data at randomly selected place
        get_data = data[index]
        # add data selected randomly to new training set array
        x_train.append(get_data)
        # delete selected data from original array
        del data[index]

    print("Training set has {} students.\n".format(len(x_train)))

    print("\nTest set is {} students.".format(len(data)))

    heading = ["GPA", "Gender", "breakfast", "calories_chicken", "calories_day", "calories_scone", "coffee",
               "comfort_food", "comfort_food_reasons", "comfort_food_reasons_coded", "cook",
               "comfort_food_reasons_coded", "cuisine", "diet_current", "diet_current_coded", "drink", "eating_changes",
               "eating_changes_coded", "eating_changes_coded1", "eating_out", "employment", "ethnic_food", "exercise",
               "father_education", "father_profession", "fav_cuisine", "fav_cuisine_coded", "fav_food", "food_childhood",
               "fries", "fruit_day", "grade_level", "greek_food", "healthy_feeling", "healthy_meal", "ideal_diet",
               "ideal_diet_coded", "income", "indian_food", "italian_food", "life_rewarding", "marital_status",
               "meals_dinner_friend", "mother_education", "mother_profession", "nutritional_check", "on_off_campus",
               "parents_cook", "pay_meal_out", "persian_food", "self_perception_weight", "soup", "sports", "thai_food",
               "tortilla_calories", "turkey_calories", "type_sports", "veggies_day", "vitamins", "waffle_calories",
               "weight"]

    with open(TRAINING_SET, "w") as training:
        csv_train = csv.DictWriter(training, fieldnames=heading)
        csv_train.writeheader()

        for row in x_train:
            csv_train.writerow(row)

    with open(TEST_SET, 'w') as test:
        csv_test = csv.DictWriter(test, fieldnames=heading)
        csv_test.writeheader()

        for row in data:
            csv_test.writerow(row)


def select_fields_for_model():
    file_present = os.path.isfile(TRAINING_SET)
    if file_present:
        model_headings = ["Gender", "breakfast", "coffee", "comfort_food_reasons", "comfort_food_reasons_coded", "cook",
                          "cuisine", "diet_current_coded", "drink", "eating_changes", "eating_changes_coded1", "eating_out",
                          "employment", "exercise", "fav_cuisine_coded", "fav_food", "food_childhood", "fries", "fruit_day",
                          "greek_food", "healthy_feeling", "ideal_diet_coded", "indian_food", "italian_food",
                          "life_rewarding", "marital_status", "nutritional_check", "parents_cook", "pay_meal_out",
                          "persian_food", "self_perception_weight", "soup", "sports", "thai_food", "veggies_day", "vitamins"
                          , "weight"]

        with open(TRAINING_SET, "r") as csv_data:
            data = csv.DictReader(csv_data)

            with open(TRAINING_DATA, "w") as model:
                model_csv = csv.DictWriter(model, fieldnames=model_headings)
                model_csv.writeheader()

                for col in data:
                    # remove unwanted data columns before writing to file
                    del col['mother_profession'], col['calories_scone'], col['calories_day'], col['tortilla_calories'], \
                        col['comfort_food'], col['calories_chicken'], col['on_off_campus'], col['diet_current'], \
                        col['healthy_meal'], col['mother_education'], col['ethnic_food'], col['father_profession'], \
                        col['eating_changes_coded'], col['turkey_calories'], col['ideal_diet'], col['waffle_calories'], \
                        col['income'], col['meals_dinner_friend'], col['grade_level'], col['type_sports'], \
                        col['fav_cuisine'], col['father_education'], col['GPA']

                    model_csv.writerow(col)

                print("Variables successfully Added!!!")


# select_fields_for_model()
# split_data(open_user_file())


# calculate TF-IDF
def calculate_tf_idf():
    data = api.read_data_from_file("restaurant.json")
    cuisines = []
    # get restaurant cuisines
    for cuisine in data["restaurants"]:
        temp = cuisine["restaurant"]["cuisines"]
        cuisines.append(temp)

    # cuisines formatted as [Contemporary, Burger, Pizza]
    # remove comma (,)
    for i in range(len(cuisines)):
        cuisines[i] = cuisines[i].replace(",", "")

    # create new array that adds each cuisine into its own cell
    a = []
    for i in range(len(cuisines)):
        c = cuisines[i].split()
        for j in range(len(c)):
            a.append(c[j])

    cuisines = a
    print(cuisines)

    k = collections.Counter(cuisines)
    print(collections.Counter(cuisines))

    cuisine_tf = math.log10(len(k))
    print(cuisine_tf)


calculate_tf_idf()
