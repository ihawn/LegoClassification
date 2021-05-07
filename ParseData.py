import os
import pathlib
from PIL import Image
from numpy import asarray

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

    print("Converting images to matrices")

    brick_matrices = []

    for i in range(len(bricks)):
        brick = Image.open((bricks[i]))
        brick_matrices.append(a)

    for i in range(10000):
        print(encoded_part[i])

Parse()