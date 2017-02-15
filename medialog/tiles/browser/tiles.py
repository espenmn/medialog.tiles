# -*- coding: utf-8 -*-

from plone import api
from plone.app.tiles.browser.add import DefaultAddForm
from plone.app.tiles.browser.add import DefaultAddView
from plone.app.tiles.browser.edit import DefaultEditForm
from plone.app.tiles.browser.edit import DefaultEditView
from plone.memoize.view import memoize
from plone.supermodel import model
from plone.directives import form
from plone.tiles import Tile
from plone.tiles.data import TransientTileDataManager
from plone.tiles.interfaces import ITileDataManager
from zope import schema
from zope.i18nmessageid import MessageFactory
#from zope.interface import provider


#????
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserView
from zope.schema import getFields
from plone.tiles.interfaces import ITileType


from collective.z3cform.datagridfield import DataGridFieldFactory 
from collective.z3cform.datagridfield import DictRow


from plone.app.textfield import RichText
from plone.app.textfield.value import RichTextValue


_ = MessageFactory('medialog.tiles')

 
 
    
class IMultiTile(model.Schema):
    
    css_class =schema.TextLine(
        title = _("css class", default=u"CSS class"),
        required = False,
        description = _("help_css_class",
                      default="CSS Class"),
    )
    
    body = RichText(title=u"Rich text",
        
    )
    
    
class MultiTile(Tile):
    """A tile that displays image and richtext"""

    def __init__(self, context, request):
        super(MultiTile, self).__init__(context, request)
        
    @property
    def data(self):
        data = super(MultiTile, self).data
        return data
        
     