import csv
import itertools

from pyramid.view import view_config, view_defaults

from lbsgdirectory.models import Boxes, Root
from lbsgdirectory.models import LetterBox


class LetterboxListingView(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    @view_config(context=Boxes, renderer="lbsgdirectory:templates/boxes.pt")
    def view_letterbox(self):
        boxes = self.context.values()
        town = lambda box: box.town
        boxes = sorted(boxes, key=town)
        locations = itertools.groupby(boxes, town)
        locations = [(town, list(boxes)) for (town, boxes) in locations]
        return {'locations':locations}
    
    @view_config(context=Root, renderer="lbsgdirectory:templates/boxes.pt", name="import")
    def import_letterboxes(self):
        f = open(self.request.GET.get("path"))
        for row in csv.DictReader(f):
            box = LetterBox(int(row['number']), row['type'], row['town'], row['postcode'], row['location'], row['gridref'])
            print box
            self.context['boxes'].add_box(box)
        return {'boxes':[]}
        
