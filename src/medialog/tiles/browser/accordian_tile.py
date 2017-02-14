from plone.app.vocabularies.catalog import CatalogSource
from plone.supermodel import model
from zope import schema

from plone.app.tiles.browser.add import DefaultAddForm
from plone.app.tiles.browser.add import DefaultAddView
from plone.app.tiles.browser.edit import DefaultEditForm
from plone.app.tiles.browser.edit import DefaultEditView

from plone.tiles import Tile
from plone.tiles.data import TransientTileDataManager
from plone.tiles.interfaces import ITileDataManager

class IAccordianTile(model.Schema):
   content_uid = schema.Choice(
   title=u"Select an object",   # XXX replace this with a message factory
   required=True,
   source=CatalogSource(portal_type=['Folder',]),
   )
   
class AccordianTile(Tile):
    """ An expanding tile """

    def __init__(self, context, request):
        super(AccordionTile, self).__init__(context, request)
    
    @property
    def data(self):
        data = super(AccordionTile, self).data
        return data
