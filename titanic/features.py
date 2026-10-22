def add_family_size(df):
    return df.assign(**{"Family Size": df["SibSp"] + df["Parch"] + 1})