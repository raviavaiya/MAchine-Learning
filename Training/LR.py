import joblib as jb
import pandas as pd
class  Housing_price_Model:
    def __init__(self):
        self.model = jb.load('./Model/MLR_Housing.pkl')

    def predict(self):
        data = {
            'area': [3500, 2200, 3000],  # Example area values
            'bedrooms': [4, 3, 3],       # Number of bedrooms
            'bathrooms': [2, 1, 1],      # Number of bathrooms
            'stories': [2, 1, 1],        # Number of stories
            'parking': [1, 0, 1],        # Number of parking spaces
            'mainroad_yes': [1, 1, 1],   # Whether the house is on the main road
            'guestroom_yes': [1, 0, 1],  # Whether there is a guestroom
            'basement_yes': [0, 0, 1],   # Whether there is a basement
            'hotwaterheating_yes': [0, 1, 0],  # Whether there is hot water heating
            'airconditioning_yes': [1, 0, 1],  # Whether there is air conditioning
            'prefarea_yes': [0, 0, 1],   # Whether it’s in a preferred area
            'furnishingstatus_semi-furnished': [1, 0, 1],  # Semi-furnished status
            'furnishingstatus_unfurnished': [0, 1, 0]      # Unfurnished status
        }
        
        X = pd.DataFrame(data)
        
        # # Getting the target price (if it's for training)
        # price = float(input("Enter the house price (for training): "))
        # y = pd.Series([price])
        y= self.model.predict(X)
        return X,y

if  __name__=="__main__": 
    # Example usage of the function
    Housing_price_Model_predictor = Housing_price_Model()
    X_input, y_input = Housing_price_Model_predictor.predict()
    print("\nInput DataFrame:\n", X_input)
    print("\nTarget Series:\n", y_input)
