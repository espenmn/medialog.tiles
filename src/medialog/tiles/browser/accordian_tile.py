# -*- coding: utf-8 -*-

#from plone.app.standardtiles.contentlisting import ContentListingTile, DefaultQuery as baseDefaultQuery, DefaultSortOn as baseDefaultSortOn
#from plone.app.z3cform.widget import QueryStringFieldWidget
#from plone.autoform.directives import widget
from zope.interface import implementer
from zope.component import adapter
#from plone.app.imaging.interfaces import IImageScaling
from plone.supermodel import model
#from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from z3c.form.interfaces import IValue
from z3c.form.util import getSpecification
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from zope.component import queryUtility, getMultiAdapter, queryMultiAdapter
from zope.publisher.browser import BrowserView
from zope.schema import getFields
from zope import schema
from plone.tiles import Tile
from plone.tiles.interfaces import ITileType

#_ = MessageFactory('medialog.tiles')


class IAccordionTile(model.Schema):
    sometext = schema.Text(
    title=u"Select an object",   # XXX replace this with a message factory
    required=True,
   )
   
class AccordionTile(Tile):
    """ An expanding tile """

    def __init__(self, context, request):
        super(AccordionTile, self).__init__(context, request)
    
    @property
    def data(self):
        data = super(AccordionTile, self).data
        return data

#    def getUID(self):
#        return self.request.get('URL').split('/')[-1]

           
