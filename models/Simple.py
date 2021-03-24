from tensorflow import keras
import numpy as np


class Simple():
    def __init__(self, data):
        self.data = data
        self.NN = keras.Sequential(
            [
                keras.layers.InputLayer(2),
                keras.layers.Dense(8, activation=keras.activations.sigmoid),
                keras.layers.Dense(8, activation=keras.activations.sigmoid),
                keras.layers.Dense(1, activation=keras.activations.linear)
            ]
        )
        self.NN.compile(optimizer="adam", loss="mse")
        self.train_set = self.data.iloc[:int(len(self.data)*0.6), :]
        self.test_set = self.data.iloc[int(len(self.data)*0.6+1):, :]

    def learn(self, epochs: int):
        results = []
        for epoch_num in range(epochs):
            self.NN.fit(self.train_set[["diff_1", "diff_2"]].values,
                        self.train_set["tomorrow"].values, batch_size=32, epochs=1)
            results.append(self.test())
        return results

    def test(self):
        predictions = self.NN.predict(
            self.test_set[["diff_1", "diff_2"]].values)
        predictions = [x[0] for x in predictions]
        return [self.__test_quantity(predictions), self.__test_ae(predictions)]

    def __test_quantity(self, predictions):
        results = []
        for id, element in enumerate(predictions):
            if element > 0:
                if self.test_set["tomorrow"].values.tolist()[id] > 0:
                    results.append(1)
                else:
                    results.append(0)
            else:
                if self.test_set["tomorrow"].values.tolist()[id] < 0:
                    results.append(1)
                else:
                    results.append(0)
        print(np.sum(results)/len(predictions))
        return np.sum(results)/len(predictions)

    def __test_ae(self, predictions):
        error = 0
        errors = [abs(predictions[i]-self.test_set["tomorrow"].values.tolist()[i])
                  for i, _ in enumerate(predictions)]
        error = np.mean(errors)
        return error
