import pandas as pd
import matplotlib.pyplot as plt

def get_signal1_signal2(df: pd.DataFrame , label: str , color: str = None) -> None: # type: ignore
    """
    This function plots Signal1 vs Signal2 for a given label in the dataset.
    :param df: DataFrame containing the dataset
    :param label: The label for which the plot is to be generated
    :param color: Color for the scatter plot points
    :return: None
    """
    plt.figure(figsize=(10, 6))
    df_label = df[df['Label'] == label]
    if color:
        plt.scatter(df_label['Signal1'], df_label['Signal2'], alpha=0.6 , color = color)
    else:
        plt.scatter(df_label['Signal1'], df_label['Signal2'], alpha=0.6)

    # Add titles and labels for clarity
    plt.title(f'Signal1 vs. Signal2 for Label {label}')
    plt.xlabel('Signal1')
    plt.ylabel('Signal2')
    plt.grid(True)
    plt.show()