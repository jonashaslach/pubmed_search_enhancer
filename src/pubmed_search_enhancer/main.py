import os
from .pubmed_search import perform_searches
from .results_processing import process_results, save_detailed_results
from .plot_heatmap import plot_heatmap
from .seed_terms_combiner import combine_seed_terms


def main(search_combinations=None):
    """
    Main execution function to read from an Excel file, perform searches, and save results.
    """
    if search_combinations is None:
        _, search_combinations = combine_seed_terms()

    results = perform_searches(search_combinations)

    results_dir = os.path.join(os.getcwd(), 'results')
    os.makedirs(results_dir, exist_ok=True)

    results_path = os.path.join(results_dir, 'search_results.xlsx')
    plot_results_path = os.path.join(results_dir, 'plot_results.xlsx')

    # Save detailed results
    save_detailed_results(results, results_path)

    # Process and save summarized results
    process_results(results, plot_results_path)

    # Plot heatmap
    plot_heatmap()


if __name__ == "__main__":
    main()
