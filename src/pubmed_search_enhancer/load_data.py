import pandas as pd
from .config import EXCEL_PATH, MODALITIES_SHEET_NAME, ML_TASKS_SHEET_NAME, MODALITIES_GROUP_COLUMN, ML_TASKS_GROUP_COLUMN

def load_excel_data():
    """
        Load data from the Excel file.

        Returns:
            tuple: DataFrames for selected columns.
    """
    xls = pd.ExcelFile(EXCEL_PATH)
    df_modalities = pd.read_excel(xls, MODALITIES_SHEET_NAME)
    df_ml_tasks = pd.read_excel(xls, ML_TASKS_SHEET_NAME)

    df_modalities[MODALITIES_GROUP_COLUMN] = df_modalities[MODALITIES_GROUP_COLUMN].ffill()
    df_ml_tasks[ML_TASKS_GROUP_COLUMN] = df_ml_tasks[ML_TASKS_GROUP_COLUMN].ffill()

    return df_modalities, df_ml_tasks

def get_unique_groups(df_modalities):
    """
    Get the list of unique groups from the modalities DataFrame.

    Parameters:
        df_modalities (DataFrame): DataFrame containing modalities data.

    Returns:
        list: List of unique group names.
    """
    return df_modalities[MODALITIES_GROUP_COLUMN].unique().tolist()
