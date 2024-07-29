#seed_terms_combiner.py
from .config import MODALITIES_GROUP_COLUMN, MODALITIES_COLUMN, TASKS_COLUMN, ML_TASKS_GROUP_COLUMN, MESH_TERMS
from .load_data import load_excel_data


def combine_seed_terms():
    df_modalities, df_ml_tasks = load_excel_data()

    grouped_modalities = df_modalities.groupby(MODALITIES_GROUP_COLUMN)[MODALITIES_COLUMN].apply(lambda mods: ' OR '.join(mods))
    grouped_tasks = df_ml_tasks.groupby(ML_TASKS_GROUP_COLUMN)[TASKS_COLUMN].apply(lambda tasks: ' OR '.join(tasks))

    initial_terms = {mod_group: mod_terms.split(" OR ") for mod_group, mod_terms in grouped_modalities.items()}

    combinations = [f"({mod_terms}) AND ({task_terms}) AND {MESH_TERMS}" for mod_terms in grouped_modalities for task_terms in grouped_tasks]

    return initial_terms, combinations
