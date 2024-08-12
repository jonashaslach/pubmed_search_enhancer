import subprocess
from .config import MODEL_NAME

def get_new_terms(group_name, current_terms, all_groups):
    """
    Generate new terms for a specific group using a language model.

    Parameters:
        group_name (str): The name of the group for which to generate new terms.
        current_terms (list): List of current terms associated with the group.
        all_groups (list): List of all group names.

    Returns:
        list: List of tuples containing new terms and their explanations.
    """
    all_groups_str = ", ".join(f'"{group}"' for group in all_groups)
    prompt = f'''
    I am looking to expand the list of terms associated with the medical category "{group_name}".
    The new terms should reflect specific procedures, tools, or techniques relevant to "{group_name}".
    The new terms should not overlap with terms that fit better in other medical imaging or monitoring categories.
    The complete list of groups is: {all_groups_str}.
    The new terms should be unique and not simply extend existing words in the group.
    The new terms should be completely lower case.
    The new terms should use hyphens instead of spaces if a new term consists of two words like "radiographic-imaging" instead of "radiographic imaging".
    The new terms should be written between two stars (**) and have an explanation on the next line.
    Here is the current list for reference (in no particular order): {" ".join(current_terms)}.
    Please provide 5-10 additional terms that specifically fall under the category of "{group_name}".
    Make sure that the new terms do not include the words  {" ".join(current_terms)}.
    '''

    result = subprocess.run(
        ["ollama", "run", MODEL_NAME],
        input=prompt,
        text=True,
        capture_output=True
    )

    response = result.stdout.strip()

    terms_with_explanations = []
    try:
        parts = response.split('**')[1:]
        for i in range(0, len(parts), 2):
            term = parts[i].strip()
            explanation = parts[i+1].strip()
            terms_with_explanations.append((term, explanation))
    except Exception as e:
        print(f"Error parsing response: {e}")

    return terms_with_explanations
