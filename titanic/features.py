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

def parse_names(row):
    try:
        text = row["Name"]
        split_text = text.split(",")
        family_name = split_text[0]
        next_text = split_text[1]
        split_text = next_text.split(".")
        title = (split_text[0] + ".").lstrip().rstrip()
        next_text = split_text[1]
        if "(" in next_text:
            split_text = next_text.split("(")
            given_name = split_text[0]
            maiden_name = split_text[1].rstrip(")")
            return pd.Series([family_name, title, given_name, maiden_name])
        else:
            given_name = next_text
            return pd.Series([family_name, title, given_name, None])
    except Exception as ex:
        print(f"Exception: {ex}")

def parse_names_execution(df):
    df = df.copy()
    df[NAME_COLUMNS] = df.apply(parse_names, axis=1)
    return df