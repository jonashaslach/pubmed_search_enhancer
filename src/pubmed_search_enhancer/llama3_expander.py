import subprocess

MODEL_NAME = "llama3_test"
def get_new_terms(group_name, current_terms):
    prompt = f'''
    I am looking to expand the list of terms associated with the medical category "{group_name}".
    Please provide 5-10 additional terms that specifically fall under the category of "{group_name}".
    The new terms should reflect specific procedures, tools, or techniques relevant to "{group_name}".
    The new terms should not overlap with terms that fit better in other medical imaging or monitoring categories. The complete list of groups is: "Radiographic Imaging", "Microscopy", "Endoscopy", "Computed Tomography", "Nuclear Imaging", "Ultrasound Imaging", "Electrophysiological Monitoring", "Cardiovascular Monitoring", "Ocular Electrophysiology", "Respiratory Monitoring", "Other Physiological Monitoring", "Heart Sound Diagnostic", "Microphone", "DNA Sequencing", "RNA Sequencing", "Epigenomic and Chromatin Analysis", "Genomic Regulation and Interaction", "Single-Cell Sequencing", "Immune Repertoire Sequencing", "Long-Read Sequencing", "Spatial Transcriptomics", "Meta-Omics Sequencing", "Other Specialized Genomics", "Electronic Health Records", "Clinical Trials", "Genomics", "Mass Spectrometry", "Intensive Care Unit", "Robotics", and "Natural Language Processing". The terms should reflect specific procedures, tools, or techniques relevant to "{group_name}".
    The new terms should be unique and not simply extend existing words in the group.
    The new terms should be completely lower case.
    The new terms should case use hyphens instead of spaces if a new term consists of two words like "radiographic-imaging" instead of "radiographic imaging".
    The new terms should be written between two stars (**) and have an explanation on the next line.
    Here is the current list for reference (in no particular order):
    {" ".join(current_terms)}
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
