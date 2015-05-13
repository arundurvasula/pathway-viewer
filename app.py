import json
import flask
import requests


app = flask.Flask(__name__)

def get_pathway(gene):
	r = requests.get('http://rest.kegg.jp/find/genes/'+gene)
	first_line = r.content.split("\n")[0]
	first_gene = first_line.split("\t")[0]
	gene = requests.get('http://rest.kegg.jp/get/'+first_gene).content.split("\n")
	pathway = filter(lambda x:'PATHWAY' in x, gene)[0].split("\t")[0].split(" ")[5]
	pathway_name = filter(lambda x:'PATHWAY' in x, gene)[0].split("\t")[0].split(" ")[7:]
	pathway_name = " ".join(pathway_name)
	return pathway, first_gene, pathway_name

@app.route("/")
def index():
    """
    When you request the root path, you'll get the index.html template.
    """
    return flask.render_template("index.html")

@app.route("/data", methods=['POST'])
def data():
	"""
	use the input gene names to make a request to KEGG
	finds the pathway and the genes
	"""
	multiple_genes = False
	data = ""
	if "\n" not in flask.request.form['gene-names']:
		data = flask.request.form['gene-names']
		pathway, gene, pathway_name = get_pathway(data)
	else:
		multiple_genes = True
		data = flask.request.form['gene-names'].split("\n")
		pathway = []
		gene = []
		pathway_name = []
		for entry in data:
			p, g, pn = get_pathway(entry)
			pathway.append(p)
			gene.append(g)
			pathway_name.append(pn)

	return flask.render_template("data.html", multiple_genes=multiple_genes, pathway=pathway, genes=gene, genes_req=data, pathway_name=pathway_name)

if __name__ == "__main__":
    import os

    port = 8000

    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}".format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)