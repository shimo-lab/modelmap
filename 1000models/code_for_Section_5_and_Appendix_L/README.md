# Code for Section 5 and Appendix L

## Setup

These scripts are designed to run in a Docker environment.
If you do not use Docker, please install the packages listed in [requirements.txt](requirements.txt).

### Build the Docker image

```bash
$ bash scripts/docker/build.sh
```

### Start the Docker container

```bash
$ bash scripts/docker/run.sh
```

## Predicting Model Performance from Model Coordinates (Section 5)

Generate the group five-fold splits based on model type and the random five-fold splits:

```bash
$ python src_pred_perform/split_data.py
```

Train and predict with the log-likelihood matrix $L$ and the double-centered log-likelihood matrix $Q$ using group 5-fold and random 5-fold splits:

```bash
$ python src_pred_perform/train_and_pred.py 
```

Evaluate the predictions and reproduce Tables 2, 7, 8, and 9:

```bash
$ python src_pred_perform/eval_prediction.py
```

Plot a scatter diagram of predictions versus ground truth (Figures 8 and 18):

```bash
$ python src_pred_perform/plot_prediction.py
```

Compute the correlation coefficients between mean log-likelihoods and benchmark scores (Table 3) and draw their scatter diagram:

```bash
$ python src_pred_perform/eval_and_plot_meanlogp.py
```

## Model List (Appendix L)

### Step 1 Download model cards from the Hugging Face Hub

To obtain fresh model cards, run `src_model_list/step1_download_model_card.py`.

🚨 Note: This step is unnecessary when reproducing the model list already included with the paper.

### Step 2: Create BibTeX entries using the arXiv API

The file [../data/model-metadata/model-data-1018.pkl](../data/model-metadata/model-data-1018.pkl) stores tag information for each model. 
For every arXiv ID contained in these tags, BibTeX entries have been generated via the arXiv API. 
To generate them again, run `src_model_list/step2_make_arxiv_bibtex_from_tag.py`.

🚨 Note: This step is not necessary when reproducing the model list already included with the paper.

### Step 3: Extract BibTeX from model cards and merge with the arXiv entries

```bash
$ python src_model_list/step3_extract_mdbib_and_merge_arxivbib.py
```

### Step 4: Normalize BibTeX notation

This script standardizes the BibTeX entries and assigns entry IDs corresponding to each model.
See the paper for details.

```bash
$ python src_model_list/step4_normalize_bibtex_notation.py
```

🚨 Note: The model list in the paper does not sort entries that share the same year, whereas this script orders them alphabetically by author. 
Consequently, the citation order for a given model may differ slightly.

### Step 5: Create the model-list LaTeX file

```bash
$ python src_model_list/step5_make_model_list_tex.py
```