from pyramid.view import view_config, view_defaults

from lbsgdirectory.models import LetterBox


class LetterboxViews(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    @view_config(context=LetterBox, renderer="lbsgdirectory:templates/individual.pt")
    def view_letterbox(self):
        try:
            coords = self.context.latlon()
        except TypeError:
            coords = None
        return {'project': 'individual', 'coords': coords}
    
