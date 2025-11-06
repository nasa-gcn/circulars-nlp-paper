# Large Language Model Driven Analysis of General Coordinates Network (GCN) Circulars

[![DOI](https://zenodo.org/badge/1064265611.svg)](https://doi.org/10.5281/zenodo.17538207)

This work applies the large language models (LLMs) to the problem of reliably identifying astrophysical events and extracting structured information from the unstructured text of GCN Circulars. The Circulars archive contains over 40,500 observational reports spanning nearly 30 years with a record of the rich history of discoveries in time-domain and multi-messenger (TDAMM) astronomy. Given the volume and diversity of this dataset, manual extraction of key observational parameters such as redshift, messenger type, and observed wavebands is a challenging task.<br>

We demonstrate that LLMs, combined with neural topic modeling, contrastive fine-tuning, and retrieval-augmented generation (RAG), can classify Circulars by messenger type and observation waveband, and automatically extract information such as gamma-ray burst (GRB) redshifts with high accuracy.<br>

Beyond proof of concept, this work provides:<br>
(A) Classification of observation types and their tabular data <br>
(B) Redshift tables from GCN Circulars <br>
(C) Open-source release of all analysis codes

## Repository Structure

| Directory                     | Description                                                                                                                               |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **`data/`**                   | Archived GCN Circulars in JSON format (up to May 2025) and a custom stop-word list for text preprocessing.                                |
| **`topic-modeling/`**         | Jupyter notebooks for unsupervised topic classification, gravitational-wave focused, and observational type clustering.                   |
| **`information-extraction/`** | Notebook for the redshift extraction pipeline and evaluation against the Swift Observatory’s manual redshift catalog.                     |
| **`figures/`**                | All plots that are included in the paper.                                                                                                 |
| **`tables/`**                 | (a) Classified observational and gravitational-wave Circulars <br> (b) Redshift tables, including both raw and duplicate-removed versions |
