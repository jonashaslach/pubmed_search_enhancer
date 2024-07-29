import pandas as pd
from .config import MODALITIES_GROUP_COLUMN, MODALITIES_COLUMN, TASKS_COLUMN, ML_TASKS_GROUP_COLUMN
from .load_data import load_excel_data


def map_groups(search_results):
    """
    Map detailed search queries to their respective group names.

    Parameters:
        search_results (list of dict): List of search results with query and hits.

    Returns:
        list of dict: List of mapped results with group names and hits.
    """
    df_modalities, df_ml_tasks = load_excel_data()

    modality_groups = df_modalities.set_index(MODALITIES_COLUMN)[MODALITIES_GROUP_COLUMN].to_dict()
    task_groups = df_ml_tasks.set_index(TASKS_COLUMN)[ML_TASKS_GROUP_COLUMN].to_dict()

    mapped_results = []
    for result in search_results:
        query = result['query']
        hits = result['hits']
        modality_query, task_query = query.split(' AND ')[0].strip('()'), query.split(' AND ')[1].strip('()')

        modality_items = [mod.strip(' "') for mod in modality_query.split(' OR ')]

        modality_group = "Unknown"
        for modality, group in modality_groups.items():
            if all(mod in modality_items for mod in modality.split()):
                modality_group = group
                break

        task_group = "Unknown"
        for task, group in task_groups.items():
            if all(t in task_query for t in task.split()):
                task_group = group
                break

        mapped_results.append({'Group Modality': modality_group, 'Group Task': task_group, 'Hits': hits})

    return mapped_results

def save_detailed_results(results, results_path):
    """
    Save the detailed search results.

    Parameters:
        results (list of dict): List of search results with detailed queries and hits.
        results_path (str): Path to save the detailed results.
    """
    detailed_results = []
    for result in results:
        query = result['query']
        hits = result['hits']
        modality_query, task_query = query.split(' AND ')[0], query.split(' AND ')[1]
        detailed_results.append({'Modality': modality_query, 'Task': task_query, 'Hits': hits})

    df_detailed_results = pd.DataFrame(detailed_results)
    df_detailed_results.to_excel(results_path, index=False)

def process_results(results, plot_results_path):
    """
    Process and save the summarized search results.

    Parameters:
        results (list of dict): List of search results with detailed queries and hits.
        plot_results_path (str): Path to save the summarized results.
    """
    mapped_results = map_groups(results)

    df_summary = pd.DataFrame(mapped_results)
    df_summary = df_summary.groupby(['Group Modality', 'Group Task']).sum().reset_index()
    df_summary = df_summary.sort_values(by=['Group Modality', 'Group Task'])
    df_summary.to_excel(plot_results_path, index=False)
