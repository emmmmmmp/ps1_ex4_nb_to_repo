def add_family_size(df):
    return df.assign(**{"Family Size": df["SibSp"] + df["Parch"] + 1})

def add_age_interval(df, boundaries=(16, 32, 48, 64)):
    interval = pd.cut(df["Age"], [-np.inf, *boundaries, np.inf], labels=False)
    return df.assign(**{"Age Interval": interval.fillna(0).astype(float)})

def add_fare_interval(df, boundaries=(7.91, 14.454, 31)):
    interval = pd.cut(df["Fare"], [-np.inf, *boundaries, np.inf], labels=False)
    return df.assign(**{"Fare Interval": interval.fillna(0).astype(float)})

def add_sex_pclass(df):
    combined = df.apply(
        lambda row: row["Sex"][0].upper() + "_C" + str(row["Pclass"]), axis=1
    )
    return df.assign(Sex_Pclass=combined)