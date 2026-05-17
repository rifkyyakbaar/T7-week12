import pandas as pd

class DataLoader:
    def __init__(self, file_path="supermarket_sales.csv"):
        try:
            self.df = pd.read_csv(file_path)
        except FileNotFoundError:
            print(f"Error: File {file_path} tidak ditemukan. Pastikan sudah download dari Kaggle!")
            self.df = pd.DataFrame()

    def get_data(self, branch_filter="All"):
        if self.df.empty:
            return self.df
            
        if branch_filter == "All":
            return self.df
        return self.df[self.df['Branch'] == branch_filter]