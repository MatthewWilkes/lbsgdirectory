from pyramid.view import view_config, view_defaults

from lbsgdirectory.models import LetterBox


class LetterboxViews(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    @view_config(context=LetterBox, renderer="lbsgdirectory:templates/mytemplate.pt")
    def view_letterbox(self):
        return {'project': 'individual', 'coords': self.context.latlon()}
    
