import os
import pathlib
from PIL import Image
from numpy import asarray
import numpy as np
import random
import pickle


#Returns the key for encoding and decoding the part, type, and dim as machine readable format
def Encode_As_Digit():
    path = pathlib.Path(r'C:\Users\Isaac\Documents\Datasets\Lego')
    bricks = list(path.glob('dataset\*'))

    part = []
    type = []
    dim = []

    #get image data from filename
    for i in range(len(bricks)):
        filename = os.path.basename(bricks[i])
        img_data = str.split(filename, ' ')
        part.append(img_data[0])

        #sometimes has two or three words describing type
        temp = ''
        for k in range(1, len(img_data) - 2):
            temp += img_data[k] + ' '
        type.append(temp)


        dim.append(img_data[len(img_data) - 2])

    key_part = list(set(part))
    key_type = list(set(type))
    key_dim = list(set(dim))

    pickle.dump(key_part, open("key_part.p", "wb"))
    pickle.dump(key_type, open("key_type.p", "wb"))
    pickle.dump(key_dim, open("key_dim.p", "wb"))

    return part, type, dim, key_part, key_type, key_dim, bricks


def Parse():

    data = Encode_As_Digit()
    part = data[0]
    type = data[1]
    dim = data[2]
    key_part = data[3]
    key_type = data[4]
    key_dim = data[5]
    bricks = data[6]

    encoded_part = []
    encoded_type = []
    encoded_dim = []

    print("Encoding brick data...")
    for i in range(len(part)):
        for k in range(len(key_part)):
            if(part[i] == key_part[k]):
                encoded_part.append(k)
                break
        for k in range(len(key_type)):
            if(type[i] == key_type[k]):
                encoded_type.append(k)
                break
        for k in range(len(key_dim)):
            if(dim[i] == key_dim[k]):
                encoded_dim.append(k)
                break

    brick_matrices = []
    brick_matrices = []
    l = 2000#len(bricks)
    parsed_matrices = 0
    g = []
    for i in range(l):

        brick = Image.open((bricks[i]))
        g.append(asarray(brick))

    if(os.path.exists("brick_matrices.p")):
        brick_matrices = pickle.load(open("brick_matrices.p", "rb"))
    else:
        for i in range(l):
            if (parsed_matrices % 1000 == 0):
                print(parsed_matrices, "/", l)
            parsed_matrices += 1

            brick = Image.open((bricks[i]))
            brick_matrices.append(asarray(brick))

        pickle.dump(brick_matrices, open("brick_matrices.p", "wb"))

    return encoded_part, encoded_type, encoded_dim, brick_matrices


def Prep_Data(input, brick_matrices, split, seed):
    temp = list(zip(brick_matrices, input))
    random.Random(seed).shuffle(temp)
    brick_matrices, input = zip(*temp)

    #define test and train
    pivot = int(split*len(brick_matrices))
    (x_train, y_train), (x_test, y_test) = (brick_matrices[0:pivot], input[0:pivot]), (brick_matrices[(pivot+1):len(brick_matrices)], input[(pivot+1):len(brick_matrices)])

    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_test = np.array(x_test)
    y_test = np.array(y_test)

    #scale matrix data
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255.0
    x_test /= 255.0

    #one hot encode
    y_train = np.utils.to_catagorical(y_train)
    y_test = np.utils.to_catagorical(y_test)
    class_num = y_test.shape[1]

    return x_train, x_test, y_train, y_test, class_num

def Prep_Image_Data():
    
