This flask application is meant to answer the question "what metabolic pathways are in my sample and how many genes are represented in these pathways?", which is a very specific question that may be worded differently depending on the person asking it.

Dependecies:

- Python
- Flask

This is a simple application that takes your input gene, matches it against the KEGG database, and returns all pathways that your genes are related to. It relies on the KEGG REST API and visualizes networks using the BioJS KEGG Viewer. 