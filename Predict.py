import matplotlib.pyplot as plt
from tensorflow import keras
import pickle
from ParseData import *


key_dim = pickle.load(open("key_dim.p", 'rb'))
key_part = pickle.load(open("key_part.p", 'rb'))
key_type = pickle.load(open("key_type.p", 'rb'))

split = 0.8
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

model_dim = keras.models.load_model("DimensionModel.h5")

prediction_dim = model_dim.predict(x_test)

for i in range(30):
    plt.grid(False)
    plt.imshow(x_test[i], cmap=plt.cm.binary)
    plt.title("Prediction: " + key_dim[np.argmax(prediction_dim[i])])

    plt.xlabel("Actual: " + key_dim[(np.argmax(y_test_dim[i]))])
    plt.show()