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




