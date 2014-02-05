from pyramid.view import view_config

from lbsgdirectory.models import Root

@view_config(context=Root, renderer='lbsgdirectory:templates/mytemplate.pt')
def my_view(request):
    return {'project': 'lbsgdirectory'}

def includeme(config):
    pass