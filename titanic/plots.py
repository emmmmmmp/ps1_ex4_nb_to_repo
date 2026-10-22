import matplotlib.pyplot as plt
import seaborn as sns

def plot_counts(df, column, hue, palette, figsize):
    """Plot passenger counts grouped by the requested hue."""
    fig, ax = plt.subplots(figsize=figsize)
    sns.countplot(data=df, x=column, hue=hue, palette=palette, ax=ax)
    ax.set_title(f"Number of passengers / {column}")
    ax.grid(color="black", linestyle="-.", linewidth=0.5, axis="y")
    ax.set_axisbelow(True)
    fig.tight_layout()
    plt.show()


def plot_distributions(df, column, hue, palette, figsize, bins):
    """Plot a feature distribution grouped by the requested hue."""
    fig, ax = plt.subplots(figsize=figsize)
    sns.histplot(data=df, x=column, hue=hue, palette=palette, bins=bins, ax=ax)
    ax.set_title(f"Passenger distribution / {column}")
    fig.tight_layout()
    plt.show()