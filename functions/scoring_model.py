import pandas as pd
import pickle



# function that reads the dataset
def read_data(path="Data/data500new.csv"):
    return pd.read_csv(path).reset_index(drop=True)


# function that loads the pickled model
def load_model(path="Model/model.pkl"):
    with open(path, "rb") as model_file:
        return pickle.load(model_file)


# function that gets model's parameters
def get_model_params(path="model/model.pkl"):
    model = load_model()
    return get_model_params()


def get_coefficients(path="Model/model.pkl"):
    model_file = pickle.load(open(path, 'rb'))
    coefficients = model_file.named_steps["logistic"].coef_
    return coefficients


