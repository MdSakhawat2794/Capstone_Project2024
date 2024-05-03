import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBRegressor
import numpy as np

class InsuranceApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Medical Insurance Price Prediction')
        self.data = pd.read_csv('Medical_insurance.csv')
        self.model = self.train_model()
        self.setup_gui()

    def setup_gui(self):
        predicted_price_button = ttk.Button(self.master, text="1. Predicted Price", command=self.show_predicted_price)
        predicted_price_button.pack(fill=tk.X, padx=5, pady=5)
        dataset_button = ttk.Button(self.master, text="2. Insurance Dataset", command=self.show_dataset)
        dataset_button.pack(fill=tk.X, padx=5, pady=5)
        exit_button = ttk.Button(self.master, text="3. Exit", command=self.master.quit)
        exit_button.pack(fill=tk.X, padx=5, pady=5)
        self.tree = ttk.Treeview(self.master)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def train_model(self):
        categorical_features = ['sex', 'smoker', 'region']
        one_hot_encoder = OneHotEncoder()
        one_hot_encoded = one_hot_encoder.fit_transform(self.data[categorical_features])
        X = self.data.drop(['charges'] + categorical_features, axis=1)
        X = np.hstack([X.values, one_hot_encoded.toarray()])
        y = self.data['charges'].values
        model = XGBRegressor(objective='reg:squarederror')
        model.fit(X, y)
        return model

    def show_predicted_price(self):
        self.tree.delete(*self.tree.get_children())  # Clear the treeview
        self.tree['columns'] = ['Predicted Price']
        self.tree['show'] = 'headings'
        self.tree.heading('Predicted Price', text='Predicted Price')

        X = self.data.drop('charges', axis=1)
        predicted_prices = self.model.predict(X)
        for price in predicted_prices:
            self.tree.insert("", "end", values=[price])

    def show_dataset(self):
        self.tree.delete(*self.tree.get_children())  # Clear the treeview
        self.tree['columns'] = list(self.data.columns)
        self.tree['show'] = 'headings'
        for col in self.data.columns:
            self.tree.heading(col, text=col)
        for index, row in self.data.iterrows():
            self.tree.insert("", "end", values=list(row))

if __name__ == '__main__':
    root = tk.Tk()
    app = InsuranceApp(root)
    root.mainloop()
