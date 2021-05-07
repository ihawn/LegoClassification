from ParseData import *
from Model import *
import time

#parameters
split = 0.8
epochs = 10
seed = 10

data = Parse()

encoded_part = data[0]
encoded_type = data[1]
encoded_dim = data[2]
x_train = data[3]

part_data = Prep_Data(encoded_part, x_train, split, seed)
type_data = Prep_Data(encoded_type, x_train, split, seed)
dim_data = Prep_Data(encoded_dim, x_train, split, seed)

x_train = part_data[0]
x_test = part_data[1]

y_train_part = part_data[2]
y_test_part = part_data[3]
class_num_part = part_data[4]

y_train_type = type_data[2]
y_test_type = type_data[3]
class_num_type = type_data[4]

y_train_dim = dim_data[2]
y_test_dim = dim_data[3]
class_num_dim = dim_data[4]


print("Training for dim")
Train_And_Test('DimensionModel.h5', 'softmax', x_train, y_train_dim, x_test, y_test_dim, class_num_dim, seed, epochs)
