from django.http import HttpResponse


def index(request):
    current_user = request.user
    if current_user.is_authenicated():
        citation_list = Citation.objects.filter(owner=current_user)
        template = loader.get_template('polls/index.html')
        context = {
            'citation_list': citation_list,
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect("/login/")
