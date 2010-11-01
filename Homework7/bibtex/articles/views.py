from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from articles.models import Collection,Article
from bibtex.Bibtex_parsing import * 

def collections(request, template_name="articles/list.html"):
	current_collections = Collection.objects.all()
	
	return render_to_response(template_name, {'current_collections': current_collections,})
	
def upload_file(request,template_name="articles/list.html"):
	if request.method == 'POST':
		# Write uploaded data to file
		with open('refs.bib', 'wb+') as destination:
			for chunk in request.FILES['data_file'].chunks():
				destination.write(chunk)

		Bibtex_parser('refs.bib',request.POST['name'])
		return render_to_response(template_name, {'current_file': request.POST['name']},context_instance=RequestContext(request))
	else:
		return render_to_response(template_name, {'current_file': None},context_instance=RequestContext(request))
		
def db_query(request,template_name="articles/list.html"):
	if request.method == 'POST':
		query =  request.POST["query"]
		
		# Parse the query into the relevant format for the Python API
		query = query.replace(' ','').replace('<','__lte=').replace('>','__gte=').replace('and',',').replace('contains','__contains=')
		
		try:
			# Give it a go if it's a valid eval
			query_matches = eval("Article.objects.filter(" + query + ")")
			return render_to_response(template_name, {'query_matches': query_matches,},context_instance=RequestContext(request))
		except:
			return render_to_response(template_name,context_instance=RequestContext(request))
	else:
		return render_to_response(template_name,context_instance=RequestContext(request))