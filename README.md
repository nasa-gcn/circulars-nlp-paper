# Large Language Model Driven Analysis of General Coordinates Network (GCN) Circulars

This work applies the large language models (LLMs) to the problem of reliably identifying astrophysical events and extracting structured information from the unstructured text of GCN Circulars. With over 40,500 Circulars accumulated over three decades, manual extraction of key observational parameters such as redshift, messenger type, and observed wavebands would become less feasible.<br>
We demonstrates that LLMs, combined with neural topic modeling, contrastive fine-tuning, and retrieval-augmented generation, can classify observations by messenger and waveband, and automatically extract information such as GRB redshifts with high accuracy.

Beyond proof of concept, this work contributes to:<br> 
(A) Classification of observation types and their tabular data <br>
(B) Redshift tables from GCNs <br> 
(C) Open-source release of all codes

| Directory                     | Description                                                                                                                      |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **`data/`**                   | Archived GCN Circulars in JSON format (up to May 2025) and a custom stop-word list for text preprocessing.                       |
| **`topic-modeling/`**         | Jupyter notebooks for unsupervised topic classification, gravitational-wave–focused analysis, and observational type clustering. |
| **`information-extraction/`** | Code for the redshift extraction pipeline and evaluation scripts against the *Swift* Observatory’s manual redshift catalog.      |
| **`figures/`**                | All figures and plots included in the paper.                                                                                     |
| **`tables/`**                 | Tabular data products - redshift tables and classified observational and gravitational-wave Circulars.                             |
