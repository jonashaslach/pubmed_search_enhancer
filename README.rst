========================
PubMed Search Enhancer
========================

Requirements
------------

Works with: Python 3.12.4

To run this project, you need to install `Ollama` and download the `BioWordVec` vector from the following GitHub pages:

- `Ollama`: https://github.com/ollama/ollama
- `BioWordVec`: https://github.com/ncbi-nlp/BioSentVec

Setup
-----

1. **Create a Custom Model with Ollama and Set the top-k Parameter to 1**:

   .. code-block:: bash

      echo "FROM llama3\n\nPARAMETER top_k 1" > custom_model_file && ollama create custom_llama3 -f custom_model_file

2. **Clone the Repository**:

   .. code-block:: bash

      git clone https://github.com/jonashaslach/pubmed_search_enhancer.git

3. **Install Required Packages**:

   .. code-block:: bash

      pip install -r requirements.txt

4. **Edit config.py and set the variables**:

5. **Move the BioWordVec vector file into the resources directory**:

Usage
-----

To run the tool:

.. code-block:: bash

   python -m src.pubmed_search_enhancer.cli run

The heatmap will plot automatically. If you already have the `plot_results.xlsx` file and only want to plot the results, run the following to visualize the results with a heatmap:

.. code-block:: bash

   python -m src.pubmed_search_enhancer.plot_heatmap

Features
--------

* Enhances PubMed searches using advanced NLP models.
* Generates heatmaps for visualizing search results.
* Configurable settings for customized search and visualization.

License
-------

* Free software: MIT license

Credits
-------

* `Ollama`: https://github.com/ollama/ollama
* `BioWordVec`: https://github.com/ncbi-nlp/BioSentVec

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
