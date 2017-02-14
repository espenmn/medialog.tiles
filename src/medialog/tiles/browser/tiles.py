# -*- coding: utf-8 -*-

from plone.supermodel import model
from plone.tiles import Tile
from zope import schema
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.tiles')

class MyTile(Tile):
    def __call__(self):
        return u'<html><body><p>Hello world</p></body></html>'



class IMyTile(model.Schema):
    iconfield = schema.TextLine(
        title = _("icon", default=u"Icon"),
        required = False,
        description = _("help_icon",
                      default="Choose Icon"),
        )
    

from plone import api
from plone.app.textfield import RichText
from plone.app.tiles.browser.add import DefaultAddForm
from plone.app.tiles.browser.add import DefaultAddView
from plone.app.tiles.browser.edit import DefaultEditForm
from plone.app.tiles.browser.edit import DefaultEditView
from plone.memoize.view import memoize
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from plone.tiles import Tile
from plone.tiles.data import TransientTileDataManager
from plone.tiles.interfaces import IPersistentTile
from plone.tiles.interfaces import ITile
from plone.tiles.interfaces import ITileDataManager
from plone.tiles.interfaces import ITileType
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from zope.component import queryMultiAdapter

from zope.interface import implementer
from zope.interface import provider
from zope.publisher.browser import BrowserView
from zope.schema import getFields
from zope.traversing.browser.absoluteurl import absoluteURL



 
#from medialog.iconpicker.widgets.widget import IconPickerFieldWidget
#from medialog.iconpicker.widgets.widget import ColorPickerFieldWidget
#from medialog.iconpicker.interfaces import IIconPickerSettings


class ILRTile(model.Schema):
    iconfield = schema.TextLine(
        title = _("icon", default=u"Icon"),
        required = False,
        description = _("help_icon",
                      default="Choose Icon"),
    )
    
    left = schema.Bool(
        title = _("floatleft", default=u"Float Left"),
        required = False,
        description = _("left_icon",
                      default="Float left or right?"),
    )
    
    body = RichText(title = _(u"body_text", default=u"Body text"),
        required = False,
        description = _("body_icon",
                      default="Body text"),
    )
    
    image = NamedBlobImage(
        title=_(u"Please upload an image"),
        required=False,
    )

class LRTile(Tile):
    """A tile that displays icon and some text"""

    def __init__(self, context, request):
        super(LRTile, self).__init__(context, request)
                
    @property
    def data(self):
        data = super(LRTile, self).data
        return data

        
    @property
    def css_class(self):
        if self.left:
        	return "left-floating"
        else:
        	return "right-floating"
