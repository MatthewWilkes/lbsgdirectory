from persistent.mapping import PersistentMapping
from BTrees.IOBTree import IOBTree

import pyproj

from lbsgdirectory.BNG import to_osgb36

WGS84=pyproj.Proj("+init=EPSG:4326")
OSGB36=pyproj.Proj("+init=EPSG:27700")

class Root(PersistentMapping):
    __parent__ = __name__ = None

    def __init__(self, *args, **kwargs):
        super(Root, self).__init__(*args, **kwargs)
        self['boxes'] = Boxes()

class Boxes(IOBTree):
    __name__ = 'boxes'
    
    def __getitem__(self, key):
        return super(Boxes, self).__getitem__(int(key))
    
    def add_box(self, box):
        self[box.id] = box

class LetterBox(object):
    
    def __init__(self, reference, lbtype, town, code, location, gridref):
        self.id = reference
        self.type = lbtype
        self.town = town
        self.code = code
        self.location = location
        self.gridref = gridref
    
    def latlon(self):
        coords = to_osgb36(self.gridref)
        return pyproj.transform(OSGB36, WGS84, *coords)[::-1]
    
    def __name__(self):
        return "%d" % self.id

def appmaker(zodb_root):
    if not 'app_root' in zodb_root:
        app_root = Root()
        zodb_root['app_root'] = app_root
        import transaction
        transaction.commit()
    return zodb_root['app_root']

def includeme(config):
    pass