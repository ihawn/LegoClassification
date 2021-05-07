from ParseData import *
from Model import *

data = Parse()

encoded_part = data[0]
encoded_type = data[1]
encoded_dim = data[2]
x_train = data[3]

part_data = Prep_Data(encoded_part, x_train)
