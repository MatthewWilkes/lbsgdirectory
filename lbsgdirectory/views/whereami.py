from decimal import Decimal

import pyproj
from pyramid.view import view_config, view_defaults

from lbsgdirectory.models import Root
from lbsgdirectory.BNG import from_osgb36

WGS84=pyproj.Proj("+init=EPSG:4326")
OSGB36=pyproj.Proj("+init=EPSG:27700")


class WhereAmIView(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(context=Root, renderer="lbsgdirectory:templates/where.pt", name="where")
    def whereami(self):
        return {}
    
    @view_config(context=Root, renderer="json", name="where_json")
    def where_result(self):
        try:
            lat = self.request.GET['lat']
            lon = self.request.GET['lon']
            ref = from_osgb36(pyproj.transform(WGS84, OSGB36, lon, lat))
            return {'reference':ref}
        except StandardError:
            return {'reference':"--------"}
    
