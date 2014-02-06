from pyramid.events import BeforeRender
from pyramid.renderers import get_renderer
from pyramid.view import view_config

import lbsgdirectory
from lbsgdirectory.models import Root


def get_template(name):
    renderer = get_renderer(
        name,
        package=lbsgdirectory)
    return renderer.implementation()

def renderer_globals_factory(event):
    event.update({
        'get_template': get_template, 
    })

@view_config(context=Root, renderer='lbsgdirectory:templates/home.pt')
def my_view(request):
    return {'project': 'lbsgdirectory'}

def includeme(config):
    config.add_subscriber(renderer_globals_factory, BeforeRender)
    