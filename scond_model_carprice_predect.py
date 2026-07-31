import pandas as pd
from sklearn import linear_model, model_selection

from sklearn.metrics import mean_absolute_error


df = pd.read_csv("C:\\Users\\pc\\Downloads\\pakistan_used_cars.csv")



df.dropna(inplace=True)

 

data = pd.get_dummies(df, columns=["make", "model", "fuel_type", "transmission", "body_type", "city"], drop_first=True)


feature = data.drop("price_pkr", axis=1)

Target = data["price_pkr"]                


X_train, X_test, Y_train, Y_test = model_selection.train_test_split(feature, Target, test_size=0.4)


# Model banao aur train karo
lr = linear_model.LinearRegression()
lr.fit(X_train, Y_train)



predictions = lr.predict(X_test)



error = mean_absolute_error(Y_test, predictions)
print("MAE ", error)



