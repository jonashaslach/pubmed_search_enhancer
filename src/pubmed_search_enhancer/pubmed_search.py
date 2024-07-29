from Bio import Entrez
from tqdm import tqdm
from .config import EMAIL


def get_search_hits(query):
    """
    Execute a PubMed search for the specified query and return the count of hits.

    Parameters:
        query (str): The search query for which PubMed hits are counted.

    Returns:
        int: The number of hits found for the query on PubMed.
    """
    Entrez.email = EMAIL
    handle = Entrez.esearch(db='pubmed', term=query, retmax=0)
    results = Entrez.read(handle)
    return int(results['Count'])


def perform_searches(search_queries):
    """
    Perform PubMed searches for a list of search queries.

    Parameters:
        search_queries (list of str): List of search queries.

    Returns:
        list of dict: List of search results with query and hits.
    """
    results = []
    for query in tqdm(search_queries, desc="Processing search queries"):
        hits = get_search_hits(query)
        results.append({'query': query, 'hits': hits})
    return results
