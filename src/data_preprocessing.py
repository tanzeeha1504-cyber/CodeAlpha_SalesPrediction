import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # 🔥 Remove unwanted column
    if "Unnamed: 0" in df.columns:
        df = df.drop("Unnamed: 0", axis=1)

    return df

def preprocess_data(df):
    # Features
    X = df[["TV", "Radio", "Newspaper"]]

    # Target
    y = df["Sales"]

    return X, y