from pybtex.database.input import bibtex
from articles.models import Collection,Article

def Bibtex_parser(file,collection_name):
	# Generate bibtex parser and import the uploaded file
	parser   = bibtex.Parser()
	bib_data = parser.parse_file(file)

	items    = bib_data.entries.keys()
	
	# Check to is if this is already a collection
	try:
		# If already exists, make current
		col = Collection.objects.get(name=collection_name)
	except:
		# If is doesn't exist, start a new one
		col = Collection(name=collection_name)
		col.save()

	for item in items:
		a =  bib_data.entries[item].fields['author'].replace('{','').replace('}','')
		try:
			j = bib_data.entries[item].fields['journal'].replace('{','').replace('}','')
		except:
			j = "N/A"
			
		try:
			v =  int(bib_data.entries[item].fields['volume'])
		except:
			v = 0
		
		try:
			p  =  bib_data.entries[item].fields['pages']
		except:
			p  = "N/A"
		
		try:
			y =  int(bib_data.entries[item].fields['year'])
		except:
			y = 0
		
		t = bib_data.entries[item].fields['title'].replace('{','').replace('}','').capitalize()
		
		# put all the information together
		# Check to see if this article has been put in this collection before
		try:
			# This article exists in this collection already, so do nothing
			Article.objects.get(title=t,collection=col)
		except:
			# A new article for this collection, put it in
			ref = Article(author_list=a,journal=j,volume=v,pages=p,year=y,title=t,collection=col)
			ref.save()
			del ref