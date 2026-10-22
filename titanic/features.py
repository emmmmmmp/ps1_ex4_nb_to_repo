def add_family_size(df):
    return df.assign(**{"Family Size": df["SibSp"] + df["Parch"] + 1})

def add_age_interval(df, boundaries=(16, 32, 48, 64)):
    interval = pd.cut(df["Age"], [-np.inf, *boundaries, np.inf], labels=False)
    return df.assign(**{"Age Interval": interval.fillna(0).astype(float)})