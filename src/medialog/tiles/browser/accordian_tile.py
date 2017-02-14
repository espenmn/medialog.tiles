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


_ = MessageFactory('medialog.iconpicker')


class IAccordianTile(model.Schema):
   sometext = schema.Text(
   title=u"Select an object",   # XXX replace this with a message factory
   required=True,
   )
   
class AccordianTile(Tile):
    """ An expanding tile """

    def __init__(self, context, request):
        super(AccordionTile, self).__init__(context, request)
    
    @property
    def data(self):
        data = super(AccordionTile, self).data
        return data
