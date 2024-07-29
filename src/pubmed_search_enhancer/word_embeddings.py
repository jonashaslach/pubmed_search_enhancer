from gensim.models import KeyedVectors
from .config import WORD_EMBEDDINGS_MODEL_PATH, MIN_SCORE

def load_word_embeddings(model_path=WORD_EMBEDDINGS_MODEL_PATH):
    model = KeyedVectors.load_word2vec_format(model_path, binary=True)
    return model

def find_similar_words(word, model, topn=1000, min_score=MIN_SCORE):
    try:
        similar_words = model.most_similar(word, topn=topn)
        filtered_words = [
            (w, s) for w, s in similar_words
            if (',' not in w and '/' not in w and '+' not in w and '*' not in w and '.' not in w and '\'' not in w and '=' not in w
                and not (word in w and w != word and (w.startswith(word + '-') or w.endswith('-' + word)))
                and s >= min_score
            )
        ]
        return filtered_words
    except KeyError:
        return []

def extend_terms_with_embeddings(groups, model):
    extended_groups = {}
    for group, terms in groups.items():
        extended_terms = set(terms)
        for term in terms:
            similar_words = find_similar_words(term, model)
            print(f"Similar words for '{term}': {[w for w, s in similar_words]}")  # Debug print
            for word, score in similar_words:
                extended_terms.add(word)
        extended_groups[group] = list(extended_terms)
    return extended_groups
