import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_heatmap():
    """
    Loads search result data from an Excel file and creates a heatmap to visualize the number of PubMed search hits.

    This function reads result data from an Excel file, transforms it into a pivot table, and creates a heatmap. The
    color scale of the heatmap is dynamically adjusted based on the 90th percentile of the hit numbers to provide
    better visual differentiation of the values.

    Returns:
        None: The function displays the heatmap directly and does not return any values.
    """

    relative_path = 'results/plot_results.xlsx'
    full_path = os.path.join(os.getcwd(), relative_path)
    df = pd.read_excel(full_path)

    pivot_df = df.pivot(index='Group Modality', columns='Group Task', values='Hits')

    vmin = 0
    vmax = pivot_df.quantile(0.9).max()

    plt.figure(figsize=(17, 9.5))
    sns.heatmap(pivot_df, annot=True, fmt="d", cmap="YlOrRd", vmin=vmin, vmax=vmax)
    plt.title('Heatmap of PubMed Search Hits')

    plt.subplots_adjust(left=0.2, right=1.15, top=0.95, bottom=0.2)

    plt.show()


if __name__ == "__main__":
    plot_heatmap()
