import pandas as pd
import csv
from datetime import datetime


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date","amount","category","description"]
    
    @classmethod
    def initialize_csv(cls):
        """
        Ensures that the CSV file exists.
        If the file doesn't exist, it creates one with the required column names.
        """
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
    
    @classmethod
    def add_entry(cls, date, amount, category, description):
        """
        Adds a new entry (row) to the CSV file.
        """
        new_entry = {
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        }
        
        with open(cls.CSV_FILE, "a",newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        
        print("Entry added succesfully")

CSV.initialize_csv()
CSV.add_entry('2025-05-06',100,'Groceries','I bought carrots')