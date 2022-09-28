import tensorflow as tf
import numpy as np


model = tf.keras.models.load_model("saved_model/suggestion")

def make_prediction(first:np.ndarray, second:np.ndarray):

    # print(first)
    # print(second)

    pair = np.concatenate((first, second))

    if(second[0] > first[0]):
        pair = np.concatenate((second,first))

    pair = pair / 100

    print(pair)

    prediction = model.predict(np.array([pair]))

    print(prediction)

    return prediction[0, 0]

