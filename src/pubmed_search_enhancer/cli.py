import sys
import copy
from .main import main
from .gui import start_gui
from .seed_terms_combiner import combine_seed_terms
from .word_embeddings import load_word_embeddings, extend_terms_with_embeddings

def update_search_combinations(search_combinations, selected_terms, init_terms):

    def quote_terms(terms):
        return [f'"{term}"' for term in terms]

    initial_term_patterns = {group: " OR ".join(terms) for group, terms in init_terms.items()}
    for group, terms in selected_terms.items():
        if terms:
            init_terms[group].extend(terms)

    updated_combinations = []
    for combination in search_combinations:
        updated_combination = combination
        for group, terms in init_terms.items():
            if terms:
                quoted_terms = quote_terms(terms)
                term_pattern = " OR ".join(quoted_terms)
                initial_pattern = initial_term_patterns[group]
                updated_combination = updated_combination.replace(f"({initial_pattern})", f"({term_pattern})")
        updated_combinations.append(updated_combination)
    return updated_combinations

if __name__ == "__main__":
    initial_terms, search_combinations = combine_seed_terms()
    gui_terms = copy.deepcopy(initial_terms)
    selected_terms = start_gui(gui_terms)

    model = load_word_embeddings()
    final_terms = extend_terms_with_embeddings(gui_terms, model)
    updated_combinations = update_search_combinations(search_combinations, final_terms, initial_terms)

    sys.exit(main(updated_combinations))  # pragma: no cover
