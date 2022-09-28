import tensorflow as tf
import numpy as np


model = tf.keras.models.load_model("saved_model/suggestion")

def make_prediction(first:np.ndarray, second:np.ndarray):

    # print(first)
    # print(second)

    pair1 = np.concatenate((first, second))
    pair2 = np.concatenate((second, first))

    pair1 = pair1 / 100
    pair2 = pair2 / 100

    print(pair1, pair2)

    prediction = model.predict(np.array([pair1, pair2]))

    print(prediction)

    # pair = np.concatenate((first, second))

    # pair = pair / 100

    # prediction = model.predict(np.array([pair]))

    return prediction[0, 0]

