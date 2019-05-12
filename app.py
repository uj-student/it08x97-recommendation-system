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

            print("\n\n\nNumber of data sets is: {}".format(count))
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


# calculate TF-IDF - restaurant
def calculate_tf_restaurants():
    r_data = api.read_data_from_json_file("restaurant.json")
    cuisines = []
    # get restaurant cuisines
    for cuisine in r_data["restaurants"]:
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

    k = collections.Counter(cuisines)
    print(collections.Counter(cuisines))

    cuisine_tf = math.log10(len(k))
    print("cuisine tf: {}\n".format(cuisine_tf))

    user_ratings = []
    for user_r in r_data["restaurants"]:
        temp = user_r["restaurant"]["user_rating"]["aggregate_rating"]
        user_ratings.append(temp)
    print(user_ratings)

    k = collections.Counter(user_ratings)
    print(len(k))

    user_ratings_tf = math.log10(len(k))
    print("user rating tf: {}\n".format(user_ratings_tf))

    rating_text = []
    for user_r in r_data["restaurants"]:
        temp = user_r["restaurant"]["user_rating"]["rating_text"]
        rating_text.append(temp)
    print(rating_text)

    k = collections.Counter(rating_text)
    print(k)

    rating_text_tf = math.log10(len(k))
    print("rating text tf: {}\n".format(rating_text_tf))

    price_range = []
    for user_r in r_data["restaurants"]:
        temp = user_r["restaurant"]["price_range"]
        price_range.append(temp)
    print(price_range)

    k = collections.Counter(price_range)
    print(k)

    price_range_tf = math.log10(len(k))
    print("price range tf: {}\n".format(price_range_tf))


# calculate_tf_restaurants()


# calculate TF-IDF - users
def calculate_tf_users():
    file_present = os.path.isfile(TRAINING_DATA)
    if file_present:
        with open(TRAINING_DATA, "r") as csv_data:
            u_data = csv.DictReader(csv_data)
            comfort_food_reasons = []
            for row in u_data:
                comfort_food_reasons.append(row["comfort_food_reasons"])

            # handle comma separated reasons like {'stress, boredom'}
            for i in range(len(comfort_food_reasons)):
                comfort_food_reasons[i] = comfort_food_reasons[i].replace(",", "")

            # create new array that adds each reason into its own cell
            a = []
            for i in range(len(comfort_food_reasons)):
                c = comfort_food_reasons[i].split()
                for j in range(len(c)):
                    a.append(c[j].lower())

            comfort_food_reasons = a

            k = collections.Counter(comfort_food_reasons)

            comfort_food_reasons_tf = math.log10(len(k))
            print("comfort food reasons tf: {}\n".format(comfort_food_reasons_tf))

        with open(TRAINING_DATA, "r") as csv_data:
            u_data = csv.DictReader(csv_data)
            comfort_food_reasons_coded = []
            for row in u_data:
                comfort_food_reasons_coded.append(row["comfort_food_reasons_coded"])

            k = collections.Counter(comfort_food_reasons_coded)
            comfort_food_reasons_coded_ft = math.log10(len(k))
            print("comfort food reasons coded tf: {}\n".format(comfort_food_reasons_coded_ft))

        with open(TRAINING_DATA, "r") as csv_data:
            u_data = csv.DictReader(csv_data)
            cuisine = []
            for row in u_data:
                cuisine.append(row["cuisine"])

            k = collections.Counter(cuisine)
            cuisine_tf = math.log10(len(k))
            print("cuisine tf: {}".format(cuisine_tf))

        with open(TRAINING_DATA, "r") as csv_data:
            u_data = csv.DictReader(csv_data)
            fav_cuisine_coded = []
            for row in u_data:
                fav_cuisine_coded.append(row["fav_cuisine_coded"])

            k = collections.Counter(fav_cuisine_coded)
            fav_cuisine_coded_tf = math.log10(len(k))
            print("fav cuisine coded tf {}".format(fav_cuisine_coded_tf))

        with open(TRAINING_DATA, "r") as csv_data:
            u_data = csv.DictReader(csv_data)
            food_childhood_entries = []
            food_childhood = []
            for row in u_data:
                food_childhood_entries.append(row["food_childhood"])

            food_childhood = food_childhood_entries
            # handle comma separated reasons like {'Quesadilla, chocolate, steak'}
            for i in range(len(food_childhood)):
                food_childhood[i] = food_childhood[i].replace(",", "")

            # create new array that adds each reason into its own cell
            a = []
            for i in range(len(food_childhood)):
                c = food_childhood[i].split()
                for j in range(len(c)):
                    a.append(c[j].lower())

            food_childhood = a

            k = collections.Counter(food_childhood)
            food_childhood_tf = math.log10(len(k))
            print("food childhood tf {}:".format(food_childhood_tf))

        with open(TRAINING_DATA, "r") as csv_data:
            u_data = csv.DictReader(csv_data)
            self_perception_weight = []
            for row in u_data:
                self_perception_weight.append(row["self_perception_weight"])

            k = collections.Counter(self_perception_weight)
            self_perception_weight_tf = math.log10(len(k))
            print("self perception weight tf: {}".format(self_perception_weight_tf))

        with open(TRAINING_DATA, "r") as csv_data:
            u_data = csv.DictReader(csv_data)
            price = []
            print("\nprice")
            for row in u_data:
                # convert amount from $ to Zar
                cost = float(row["pay_meal_out"]) * 14.35
                # round up amount
                cost = math.ceil(cost)
                price.append(cost)

            k = collections.Counter(price)
            price_tf = math.log10(len(k))
            print("price tf: {}".format(price_tf))

            k = 1
            user = []
            for i in u_data:
                print("{} -> {}".format(k, i))
                user.append(i)
                k += 1

            print(user)


def calculate_tf_childhood_food():
    file_present = os.path.isfile(TRAINING_DATA)
    if file_present:
        with open(TRAINING_DATA, "r") as csv_data:
            u_data = csv.DictReader(csv_data)
            food_childhood_entries = []
            food_childhood = []

            for row in u_data:
                food_childhood_entries.append(row["food_childhood"])

            food_childhood = food_childhood_entries
            # handle comma separated reasons like {'Quesadilla, chocolate, steak'}
            for i in range(len(food_childhood)):
                food_childhood[i] = food_childhood[i].replace(",", "")

            # create new array that adds each reason into its own cell
            tmp = []
            for i in range(len(food_childhood)):
                c = food_childhood[i].split()
                for j in range(len(c)):
                    tmp.append(c[j].lower())

            food_childhood = tmp

            k = collections.Counter(food_childhood)
            food_childhood_tf = math.log10(len(k))
            print("food childhood tf {}:".format(food_childhood_tf))

            users_food = []
            print("child hood array: ", food_childhood_entries)
            for i in range(len(food_childhood_entries)):
                childhood_food = food_childhood_entries[i]
                childhood_food = childhood_food.replace(",", "").lower().split()
                users_food.append(childhood_food)

        return [users_food, food_childhood_tf]

# calculate_tf_users()
# print("App class: ", type(calculate_tf_users()))


def calculate_df_cuisine():
    r_data = api.read_data_from_json_file("restaurant.json")
    r_id = []
    r_name = []
    cuisines = []
    restaurant_cuisines = []
    count = []
    restaurant_object = {}
    # get restaurant id
    for ids in r_data["restaurants"]:
        tmp_id = ids["restaurant"]["id"].lower()
        tmp_name = ids["restaurant"]["name"]
        tmp_cuisine = ids["restaurant"]["cuisines"].lower()
        # c_count = tmp_cuisine.count(",")
        # for c in range(c_count + 1):
        r_id.append(tmp_id)
        r_name.append(tmp_name)
        # count.append(c_count + 1)
        cuisines.append(tmp_cuisine)

    print("CUISINES: ", len(r_id))

    restaurant_cuisines = cuisines

    for i in range(len(cuisines)):
        cuisines[i] = cuisines[i].replace(",", "")

    a = []
    for i in range(len(cuisines)):
        c = cuisines[i].split()
        for j in range(len(c)):
            a.append(c[j])

    cuisines = a

    print(len(r_id), "\n", r_id)
    print(len(cuisines), "\n", cuisines)
    print(count)

    for i in range(len(r_id)):
        restaurant_object.update([(r_id[i], restaurant_cuisines[i])])

    a = []
    print("\n\n{:<15} {:<10}\n".format('Restaurant-Id', 'Cuisines'))
    for k, v in restaurant_object.items():
        print("{:<15} {:<10} ".format(k, v))

    for i in restaurant_object.items():
        v = str(i).replace(",", "")
        print(v)

    cuisines = []
    # get restaurant cuisines
    for cuisine in r_data["restaurants"]:
        temp = cuisine["restaurant"]["cuisines"]
        cuisines.append(temp)

    # cuisines formatted as [Contemporary, Burger, Pizza]
    # remove comma (,)
    for i in range(len(cuisines)):
        cuisines[i] = cuisines[i].replace(",", "").lower()

    # create new array that adds each cuisine into its own cell
    a = []
    for i in range(len(cuisines)):
        c = cuisines[i].split()
        for j in range(len(c)):
            a.append(c[j])

    cuisines = a

    print(cuisines)
    k = collections.Counter(cuisines)
    print(k)

    a = math.log10(len(cuisines))
    print("cuisine tf: {}".format(a))

    # cuisines["IDF"] = a - math.log10(len(k))
    print(a - math.log10(len(k)))

    # df of cuisines
    df = []
    for i in k:
        # cuisines["IDF"] = a - math.log10(len(k))
        df.append(a - math.log10(k[i]))

    print("cuisine df: \n{}".format(df))

    # tf
    tf = []
    for value in k:
        tf.append(k[value])

    print("tf length: {}\ntf:\n{}".format(len(tf), tf))

    print("length of tf is: {} \nlength of df id: {}".format(len(tf), len(df)))

    # tf-dfi
    tf_dfi = []
    if len(tf) == len(df):
        for value in range(len(df)):
            tmp = (tf[value] * df[value])
            tf_dfi.append(tmp)

    print("TF_DFI: \n{}".format(tf_dfi))

    tf_dfi_sq = []
    for value in range(len(df)):
        tmp = tf_dfi[value] ** 2
        tf_dfi_sq.append(tmp)

    print("TF_DFI_sq: \n{}".format(tf_dfi_sq))

    vector_length = []
    for value in range(len(df)):
        tmp = math.sqrt(tf_dfi_sq[value])
        vector_length.append(tmp)

    print("Vector length: \n{}".format(vector_length))

    cuisine_wt = []
    for value in range(len(tf_dfi)):
        tmp = tf_dfi[value] / vector_length[value]
        cuisine_wt.append(tmp)

    print("cuisine_wt: \n{}".format(cuisine_wt))
    # return float(cuisine_wt)
    # cuisine_wt same as tf_dfi, thus can use either going forward.

    user_ratings = []
    for user_r in r_data["restaurants"]:
        temp = user_r["restaurant"]["user_rating"]["aggregate_rating"]
        user_ratings.append(temp)
    print(user_ratings)

    p = collections.Counter(cuisines).most_common()

    someobj = {}
    someobj.update(p)

    print(someobj)
    obj = {}
    i = 0
    print("\n\n{:<15} {:<10} {:<10}".format("Cuisines", "Count", "Tf-Idf"))
    for k, v in someobj.items():
        print("{:<15} {:<10} {:<10}".format(k, v, tf_dfi[i]))
        obj.update([(k, tf_dfi[i])])
        i += 1

    tmp = []
    for o in restaurant_cuisines:
        tmp.append(o.split())
    print("tmp cuisines", tmp, " \n", len(tmp))

    restaurant_score = []
    for o in tmp:
        for i in o:
            print(i)
            value = 1
            if i in obj.keys():
                print(obj.get(i))
                value = obj.get(i) * value
        restaurant_score.append(value)

    print("\n\n{:<15} {:<50} {:<10}".format("Restaurant Id", "Cuisines", "Restaurant Score"))
    for i in range(len(r_id)):
        print("{:<15} {:<50} {:<10}".format(r_id[i], restaurant_cuisines[i], restaurant_score[i]))

    user_score = calculate_tf_childhood_food()[1]
    users_childhood_food = calculate_tf_childhood_food()[0]
    cuisine_score = obj
    print("User Score: ", user_score, "\n", type(users_childhood_food))
    print(cuisine_score.keys())

    tmp_results = []
    for i in range(len(users_childhood_food)):
        for j in users_childhood_food[i]:
            if j in cuisine_score.keys():
                c = cuisine_score.get(j)
                print("childhood food found: ", j, " ", c)
                # print("Score: ", c * user_score)
                tmp_results.append(j)
    print("Found matches for users: ", tmp_results)

    i = 0
    j = len(restaurant_score)
    while i < j:
        mid = int((i + j) / 2)
        if restaurant_score[mid] == user_score:
            print(restaurant_score[mid])
        # If target is less than array
        # element, then search in left
        if user_score < restaurant_score[mid]:
            # If target is greater than previous
            # to mid, return closest of two
            if user_score > 0 and user_score > restaurant_score[mid - 1]:
                print("\n\n\nhyh", get_closest(restaurant_score[mid - 1], restaurant_score[mid], user_score))
            # Repeat for left half
            j = user_score
            # If target is greater than mid
        else:
            if mid < len(restaurant_score) - 1 and user_score < restaurant_score[mid + 1]:
                print("tjv", get_closest(restaurant_score[mid], restaurant_score[mid + 1], user_score))
            # update i
            i = mid + 1

    # Only single element left after search

    print("\n\n\n\n\naaaaaaa ", restaurant_score[mid])
    a = restaurant_score[mid]
    b = []
    for i in range(len(restaurant_score)):
        if a == restaurant_score[i]:
            print(r_name[i])
            b.append(r_name[i])
    return b


    # Method to compare which one is the more close.

# We find the closest by taking the difference
# between the target and both values. It assumes
# that val2 is greater than val1 and target lies
# between these two.
def get_closest(val1, val2, target):
    if abs(target - val1) >= abs(val2 - target):
        return val2
    else:
        return val1


# need to add object to handle array data
calculate_df_cuisine()
