AIClubProject1NewsFeed
==============================

The first AI club project for 2020 pertains to the DS/ML code for the [D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[. It pertains to the DS/ML code for the [A[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C at NC State project for 2020. It pertains to the DS/ML code used to create an application regarding analyzing news sources for the 2020 election starting out with a recommendation engine and branching into other aspects. 

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

Article Reliability and Bias Scores
------------

The article reliability and bias scores used to classify articles when training the model, as well as the articles themselves, are from an interactive media bias chart found [here](https://ichart.vercel.app/) (or [here](https://www.adfontesmedia.com/interactive-media-bias-chart-2/) if the first link does not work for some reason). These two classifiers, or labels, are measured on the following scales:

##### Reliability
- 0.0 to 8.0 - Contains Inaccurate / Fabricated Information
- 8.0 to 16.0 - Propaganda / Contains Misleading Information
- 16.0 to 24.0 - Selective or Incomplete Story / Unfair Persuasion
- 24.0 to 32.0 - Opinion or High Variation in Reliability
- 32.0 to 40.0 - Analysis or High Variation in Reliability
- 40.0 to 48.0 - Complex Analysis or Mix of Fact Reporting and Analysis
- 48.0 to 56.0 - Fact Reporting
- 56.0 to 64.0 - Original Fact Reporting

##### Bias
- -42.0 to -30.0 - Most Extreme Left
- -30.0 to -18.0 - Hyper-Partisan Left
- -18.0 to -6.0 - Skews Left
- -6.0 to 6.0 - Neutral or Balanced Bias
- 6.0 to 18.0 - Skews Right
- 18.0 to 30.0 - Hyper-Partisan Right
- 30.0 to 42.0 - Most Extreme Right

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
