# -*- coding: utf-8 -*-

from plone import api
#from plone.app.tiles.browser.add import DefaultAddForm
#from plone.app.tiles.browser.add import DefaultAddView
#from plone.app.tiles.browser.edit import DefaultEditForm
#from plone.app.tiles.browser.edit import DefaultEditView
from plone.memoize.view import memoize
from plone.supermodel import model
from plone.tiles import PersistentTile
from zope import schema
from zope.i18nmessageid import MessageFactory

#from collective.z3cform.datagridfield import DataGridFieldFactory 
#from collective.z3cform.datagridfield import DictRow

from plone.directives import form

from plone.app.textfield import RichText
from plone.app.textfield.value import RichTextValue
from plone.namedfile.field import NamedBlobFile
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces.controlpanel import IImagingSchema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.component import getUtility
from zope.interface import provider


_ = MessageFactory('medialog.tiles')


def get_settings():
    registry = getUtility(IRegistry)
    settings = registry.forInterface(
        IImagingSchema,
        prefix="plone",
        check=False
    )
    return settings
    
@provider(IContextSourceBinder)
def image_scales(context):
    values = []
    settings = get_settings()
    for allowed_size in settings.allowed_sizes:
        name = allowed_size.split()[0]
        if name not in ("thumb", "tile", "icon", "listing"):
            values.append(SimpleTerm(name, name, _(allowed_size)))
    return SimpleVocabulary(values)
 
    
class IMultiTile(model.Schema):
    
    css_class = schema.Choice(
        title = _("css class", default=u"CSS class"),
        required = False,
        description = _("help_css_class",
                      default="CSS Class"),
        values=("left", "right", "left dark", "right dark", "left grey", "right grey", "center", "text-on-image", "text-on-image black", "text-on-image center"),
    )
    
    body = RichText(title=u"Rich text",
        
    )
    
    image = NamedBlobFile(
        title=_(u'Please, upload an image'),
    )
    
    scale = schema.Choice(
        title=_(u'Select maximum display size'),
        source=image_scales
    )
    
    width_class = schema.Choice(
        title = _("width class"),
        required = False,
        description = _("help_width_class"),
        values=("full", "medium", "two", "three", "four"),
    )
    

class IAccordionTile(model.Schema):
    
    zone=schema.TextLine (
         title=_(u'Zone'),
        required=False,
    )
    title=schema.TextLine (
        title=_(u'Title'),
        required=True,
    )
    
    body = RichText(title=u"Rich text",
        
    )
    
    css_class=schema.TextLine (
        title=_(u'CSS class'),
        required=False,
    )
    
    width_class = schema.Choice(
        title = _("width class"),
        required = False,
        description = _("help_width_class"),
        values=("full", "medium", "two", "three", "four"),
    )
    
class IRiktekstTile(model.Schema):
    
    css_class=schema.TextLine (
        title=_(u'CSS class'),
        required=False,
    )
    
    
    body = RichText(title=u"Rich text",
        
    )
    
    
    width_class = schema.Choice(
        title = _("width class"),
        required = False,
        description = _("help_width_class"),
        values=("full", "medium", "two", "three", "four", "five"),
    )


class IColorboxTile(model.Schema):
    
    css_class=schema.TextLine (
        title=_(u'CSS class'),
        required=False,
    )
    
    icon=schema.TextLine (
        title=_(u'Icon'),
        required=False,
    )
    
    image = NamedBlobFile(
        title=_(u'Please, upload an image'),
        required=False,
    
    )
    
    scale = schema.Choice(
        title=_(u'Select maximum display size'),
        source=image_scales
    )
    
    title=schema.TextLine (
        title=_(u'Title'),
        required=True,
    )
    
    body = RichText(title=u"Rich text",
        
    )
    
    moretext=schema.TextLine (
        title=_(u'Readmore text'),
        required=False,
    )
    
    link = schema.URI(title=u"Link",
        required=False,
    )
    
    linkbox = schema.Bool(title=u"Link whole box",
        required=False,
    )
    
    width_class = schema.Choice(
        title = _("width class"),
        required = False,
        description = _("help_width_class"),
        values=("full", "medium", "two", "three", "four"),
    )
    

class IReadmoreTile(model.Schema):
    
    moretext=schema.TextLine (
        title=_(u'Title'),
        required=True,
    )
    

    link = schema.URI(title=u"Link",
        
    )
    
    css_class=schema.TextLine (
        title=_(u'CSS class'),
        required=False,
    )
    
    width_class = schema.Choice(
        title = _("width class"),
        required = False,
        description = _("help_width_class"),
        values=("full", "medium", "two", "three", "four"),
    )
    

class IInfoTile(model.Schema):
    
    title=schema.TextLine (
        title=_(u'Title'),
        required=False,
    )
    
    
    body = RichText(title=u"Rich text",
        
    )
    
    moretext=schema.TextLine (
        title=_(u'Readmore text'),
        required=False,
    )
    
    image = NamedBlobFile(
        title=_(u'Please, upload an image'),
    )
    
    scale = schema.Choice(
        title=_(u'Select maximum display size'),
        source=image_scales
    )
    
    link = schema.URI(title=u"Link",
        
    )
    
    icon=schema.TextLine (
        title=_(u'Icon'),
        required=False,
    )
    
    height=schema.TextLine(
        title=_(u'Height'),
        required=False,
    )
    
    width_class = schema.Choice(
        title = _("width class"),
        required = False,
        description = _("help_width_class"),
        values=("full", "medium", "two", "three", "four"),
    )
    
    css_class=schema.TextLine (
        title=_(u'CSS class'),
        required=False,
    )
    
class MultiTile(PersistentTile):
    """A tile that displays image and richtext"""

#    def __init__(self, context, request):
#        super(MultiTile, self).__init__(context, request)
        
class RiktekstTile(PersistentTile):
    """A tile that displays accordion"""
    

class AccordionTile(PersistentTile):
    """A tile that displays accordion"""
    
class ColorboxTile(PersistentTile):
    """A tile that displays a box"""
    
class InfoTile(PersistentTile):
    """A tile that displays image and richtext"""
    
class ReadmoreTile(PersistentTile):
    """A tile that displays image and richtext"""
    
