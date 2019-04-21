from Experiments.markov import Image as IMG, Model
import imageio

import glob
data = []
files = glob.glob("troo/*.jpg")

for a in range(0,10):
    for i in range(0, 19):
        image = imageio.imread(files[i])
        data.append(IMG(image))
        print(str(i) + " read")




model = Model(data,0)
model.compile()
model.generate(20)

a = 5
# print("ahoj")
