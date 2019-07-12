import random
import pandas as pd

class RandomModel():

    def __init__(self):
        pass

    def fit(self,X_train,Y_train):
        pass

    def predict(self,X_test):
        outcome = [random.randint(0,1) for i in range(len(X_test))]
        return pd.DataFrame(outcome)