from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from groupo.models import Citation

class CitationsList(ListView):
    current_user = self.request.user
    if current_user.is_authenticated():
        queryset = Citation.objects.filter(owner=current_user)
        context_object_name = 'citation_list'
    model = Citation
    
    def dispatch(self, request, *args, **kwargs):
        # check if there is some citations
        if not self.request.user.is_authenticated():
            return redirect('/login/')
        else:
            return super(CitationsList, self).dispatch(request, *args, **kwargs)

class CitationCreate(CreateView):
    model = Citation
    fields = ['title', 'link', 'notes']
    success_url = reverse_lazy('groupo:citation_list')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateArticle, self).form_valid(form)

class CitationUpdate(UpdateView):
    model = Citation
    fields = ['title', 'link', 'notes']
    success_url = reverse_lazy('groupo:citation_list')

class CitationDelete(DeleteView):
    model = Citation
    success_url = reverse_lazy('groupo:citation_list')


