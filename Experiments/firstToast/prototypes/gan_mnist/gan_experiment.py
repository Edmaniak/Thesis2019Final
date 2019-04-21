from keras.datasets import mnist

from Experiments.firstToast.prototypes import GAN
import numpy as np

gan = GAN()

(X_train, _), (_,_) = mnist.load_data()

X_train = (X_train.astype(np.float32) - 127.5) / 127.5
X_train = np.expand_dims(X_train, axis=3)

gan.train(X_train)