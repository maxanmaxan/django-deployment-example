from django.shortcuts import render
from django.views import View

# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        context_dict = {'text' : 'hello world', 'number' : 100}
        return render(request, 'basic_app/index.html', context_dict)

class Other(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'basic_app/other.html')

class Relative(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'basic_app/rel_url_temp.html')
