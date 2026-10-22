#data loading functions

from pathlib import Path

import pandas as pd


def load_titanic_data(
    data_dir: str | Path
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load the Titanic training and test datasets.

    Args:
        data_dir: Directory containing train.csv and test.csv.

    Returns:
        A tuple containing the training and test DataFrames.
    """
    data_dir = Path(data_dir)

    train_df = pd.read_csv(data_dir / "train.csv")
    test_df = pd.read_csv(data_dir / "test.csv")

    return train_df, test_df

def summarise_missing_data(df: pd.DataFrame) -> pd.DataFrame:
    """Summarise missing values and data types by column.

    Args:
        df: DataFrame to inspect.

    Returns:
        A DataFrame containing missing-value counts,
        percentages and column data types.
    """
    total = df.isna().sum()
    percent = total / len(df) * 100 if len(df) else total.astype(float)

    summary = pd.DataFrame({
        "Total": total,
        "Percent": percent,
        "Types": df.dtypes.astype(str)
    })

    return summary




def summarise_frequent_values(df: pd.DataFrame) -> pd.DataFrame:
    """Find the most frequently occurring value in each column.

    Missing values are excluded from frequency counts.

    Args:
        df: DataFrame to analyse.

    Returns:
        A DataFrame containing non-missing counts,
        modal values, frequencies and percentages.
    """
    rows = []

    for column in df.columns:
        counts = df[column].value_counts(dropna=True)
        total = df[column].count()

        if counts.empty:
            most_frequent = None
            frequency = 0
        else:
            most_frequent = counts.index[0]
            frequency = int(counts.iloc[0])

        rows.append({
            "Column": column,
            "Total": total,
            "Most frequent item": most_frequent,
            "Frequency": frequency,
            "Percent from total":
                round(frequency / total * 100, 3)
                if total else 0.0
        })

    return pd.DataFrame(rows).set_index("Column")


def summarise_unique_values(df: pd.DataFrame) -> pd.DataFrame:
    """Count non-missing and unique values in each column.

    Args:
        df: DataFrame to inspect.

    Returns:
        A DataFrame containing non-missing observation
        counts and unique-value counts by column.
    """
    return pd.DataFrame({
        "Total": df.count(),
        "Uniques": df.nunique()
    })



def combine_datasets(
    train_df: pd.DataFrame,
    test_df: pd.DataFrame
) -> pd.DataFrame:
    """Combine Titanic train and test data for analysis.

    Adds a 'set' column identifying the source dataset.
    Missing columns are retained and filled with NaN.

    Args:
        train_df: Titanic training dataset.
        test_df: Titanic test dataset.

    Returns:
        A combined DataFrame identifying train/test rows.
    """
    train = train_df.copy()
    test = test_df.copy()

    train["set"] = "train"
    test["set"] = "test"

    return pd.concat(
        [train, test],
        axis=0,
        ignore_index=True
    )

def summarise_survival(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate mean survival by title and sex."""
    return df[["Titles", "Sex", "Survived"]].groupby(
        ["Titles", "Sex"], as_index=False
    ).mean()


