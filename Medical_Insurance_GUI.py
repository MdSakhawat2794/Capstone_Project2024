import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

class InsuranceApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Medical Insurance Price Prediction')

        # Load the data from the CSV file
        self.data = pd.read_csv('Medical_insurance.csv')

        # Setup GUI layout
        self.setup_gui()

    def setup_gui(self):
        # Button to show 'Final Price' only
        final_price_button = ttk.Button(self.master, text="1. Predicted Price", command=self.show_final_price)
        final_price_button.pack(fill=tk.X, padx=5, pady=5)

        # Button to show entire dataset
        dataset_button = ttk.Button(self.master, text="2. Insurance Dataset", command=self.show_dataset)
        dataset_button.pack(fill=tk.X, padx=5, pady=5)

        # Button to exit the application
        exit_button = ttk.Button(self.master, text="3. Exit", command=self.master.quit)
        exit_button.pack(fill=tk.X, padx=5, pady=5)

        # Treeview for displaying data
        self.tree = ttk.Treeview(self.master)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def show_final_price(self):
        # Clear the treeview
        self.tree.delete(*self.tree.get_children())

        # Configuring columns for 'Final Price'
        self.tree['columns'] = ['Predicted Price']
        self.tree['show'] = 'headings'
        self.tree.heading('Predicted Price', text='Predicted Price')

        # Inserting 'Final Price' data
        for index, row in self.data.iterrows():
            self.tree.insert("", "end", values=[row['charges']])

    def show_dataset(self):
        # Clear the treeview
        self.tree.delete(*self.tree.get_children())

        # Configuring columns for the entire dataset
        self.tree['columns'] = list(self.data.columns)
        self.tree['show'] = 'headings'
        for col in self.data.columns:
            self.tree.heading(col, text=col)

        # Inserting dataset into the treeview
        for index, row in self.data.iterrows():
            self.tree.insert("", "end", values=list(row))


if __name__ == '__main__':
    root = tk.Tk()
    app = InsuranceApp(root)
    root.mainloop()


