# main.py
import pandas as pd

def main():
    data = {
        'Name': ['Barath', 'Susanth', 'Naren'],
        'Age': [24, 7, 9]
    }
    df = pd.DataFrame(data)
    print(df)

if __name__ == "__main__":
    main()
