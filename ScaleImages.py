from PIL import Image
import pathlib

path = pathlib.Path(r'C:\Users\Isaac\Documents\Datasets\Lego')
bricks = list(path.glob('dataset\*'))

basewidth = 128

#Scales images down to basewidth
for i in range(len(bricks)):
    if(i%1000 == 0):
        print(i, '/', len(bricks))

    img = Image.open(bricks[i])
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(bricks[i])