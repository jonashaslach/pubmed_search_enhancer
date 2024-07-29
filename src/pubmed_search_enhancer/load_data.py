import pandas as pd
from .config import EXCEL_PATH, MODALITIES_SHEET_NAME, ML_TASKS_SHEET_NAME, MODALITIES_GROUP_COLUMN, ML_TASKS_GROUP_COLUMN

def load_excel_data():
    xls = pd.ExcelFile(EXCEL_PATH)
    df_modalities = pd.read_excel(xls, MODALITIES_SHEET_NAME)
    df_ml_tasks = pd.read_excel(xls, ML_TASKS_SHEET_NAME)

    df_modalities[MODALITIES_GROUP_COLUMN] = df_modalities[MODALITIES_GROUP_COLUMN].ffill()
    df_ml_tasks[ML_TASKS_GROUP_COLUMN] = df_ml_tasks[ML_TASKS_GROUP_COLUMN].ffill()

    return df_modalities, df_ml_tasks
