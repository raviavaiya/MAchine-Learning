import pandas as pd
import joblib as jb

class CarPriceModel:
    def __init__(self):
        #  LOAd The Car Model
        self.Model=jb.load('./Model/MLR_Car.pkl')

    def Predict(self):
        data={
            'Year': [2014, 2013, 2017],               # Manufacturing year
            'Present_Price': [5.59, 9.54, 9.85],      # Current price of the car (in lakhs)
            'Kms_Driven': [27000, 43000, 6900],       # Kilometers driven by the car
            'Fuel_Type_Petrol': [1, 0, 1],            # Petrol (1) or Diesel (0)
            'Seller_Type_Individual': [0, 0, 1],      # Dealer (0) or Individual (1)
            'Transmission_Manual': [1, 1, 1],         # Manual (1) or Automatic (0)
            'Owner': [0, 0, 0]
        }
        
        X=pd.DataFrame(data)

        y_pred=self.Model.Predict(X)

        return X,y_pred

if __name__ == "__main__":
    car=CarPriceModel()
    X_input,y_input=car.Predict()
    print("\nInput DataFrame:\n", X_input)
    print("\nPredicted Selling Prices:\n", y_input)