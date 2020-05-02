from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import smart_str
def index(request):
	context = {
		'message': 'Welcome my BBS',
		'players': ["勇者","戦士","魔法使い"]
		}
	#smart_str(context, encoding='utf-8', strings_only=False, errors='strict') 
	#context.encode("raw_unicode_escape").decode("utf-8")
	return render(request, 'bbs/index.html' , context)