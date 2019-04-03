import csv
import random

MY_CSV = "food_coded_temp.csv"

def open_user_file():
	# open csv file and write each row into array (students)
	with open(MY_CSV) as csv_data:
		data = csv.DictReader(csv_data)
		count = 0
		students =[]
		for row in data:
			students.append(row)
			count += 1 #keep track of entries into array
	print("\n\n\nNumber of datasets is: {}".format(count))

	return students

def split_data(data):
	#data will be split into 80% train and 20% test
	x_ = 0.8 * len(data)
	x_ = int(x_)
	print ("\n\nNumber of training set: {}".format(x_) )

	x_train = []
	#training data is selected at random form array
	for row in range(x_):
		#pick random number
		index = random.randint(0, len(data) - 1)
		#pick data at randomly selected place 
		get_data = data[index]
		#add data selected randomly to new training set array
		x_train.append(get_data)
		#delete selected data from original array
		del data[index]

	print("Training set has {} students.\n".format(len(x_train)))

	print("\nTest set is {} students.".format(len(data)))

split_data(open_user_file())

