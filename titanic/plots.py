import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

TARGET = "Survived"

def plot_counts(df, column, hue, palette, figsize, ax=None):
    """Plot passenger counts grouped by the requested hue."""
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    sns.countplot(
        data=df, x=column, hue=hue,
        palette=palette, ax=ax,
    )
    ax.set_title(f"Number of passengers / {column}")
    ax.grid(color="black", linestyle="-.", linewidth=0.5, axis="y")
    ax.set_axisbelow(True)
    fig.tight_layout()
    return fig


def plot_distributions(df, column, hue, palette, figsize, bins, ax=None):
    """Plot a feature distribution grouped by the requested hue."""
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    sns.histplot(
        data=df, x=column, hue=hue,
        palette=palette, bins=bins, ax=ax,
    )
    ax.set_title(f"Passenger distribution / {column}")
    fig.tight_layout()
    return fig


def label_survival_rates(ax, data, column):
    """Add within-group percentage to the original count plots."""
    counts = pd.crosstab(data[column], data[TARGET]).reindex(columns=[0, 1], fill_value=0)
    order = [label.get_text() for label in ax.get_xticklabels()]
    counts = counts.loc[order]
    totals = counts.sum(axis=1)
    for outcome, bars in zip([0, 1], ax.containers):
        labels = [f"{value:.1%}" for value in counts[outcome] / totals]
        ax.bar_label(bars, labels=labels, padding=3, fontsize=9)
    ax.set_xticks(ax.get_xticks(), [f"{name}\n(n={totals.loc[name]})" for name in order])
    ax.set_ylim(0, ax.get_ylim()[1] * 1.16)
    ax.set_ylabel("Passenger count")
    ax.grid(axis="y", color="#DCE4EB", linestyle="-", linewidth=0.6)


def rate_and_n(data):
    return f"{data[TARGET].mean():.1%} (n={len(data)})"
    

def export_figure(fig, filename, FIGURES_DIR):
    os.makedirs(FIGURES_DIR, exist_ok=True)
    fig.savefig(
        os.path.join(FIGURES_DIR, filename),
        dpi=180,
        bbox_inches="tight",
    )
    plt.show()
    plt.close(fig)