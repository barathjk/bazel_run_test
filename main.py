# main.py..
import pandas as pd

def main():
    data = {
        'Name': ['Barath', 'Susanth', 'Naren'],
        'Age': [24, 7, 11]
    }
    df = pd.DataFrame(data)
    print(df)
    df.to_excel("Quality_output.xlsx")

if __name__ == "__main__":
    main()
