from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import render

from groupo.models import Citation

class CitationsList(ListView):
    context_object_name = 'citation_list'
    def get(self, request):
        if self.request.user.is_authenticated():
            cur_user = self.request.user
            citations = Citation.objects.filter(owner=cur_user)
            return render(request,'groupo/citations_list.html', {'citation_list':citations})
        else:
            return redirect('/login/')

class CitationCreate(CreateView):
    model = Citation
    fields = ['title', 'link', 'notes']
    success_url = '/citations/'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CitationCreate, self).form_valid(form)

class CitationUpdate(UpdateView):
    model = Citation
    fields = ['title', 'link', 'notes']
    success_url = '/citations/'

class CitationDelete(DeleteView):
    model = Citation
    success_url = '/citations/'


