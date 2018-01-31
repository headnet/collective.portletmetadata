# -*- coding: utf-8 -*-
from collective.portletmetadata import MessageFactory as _
from plone.namedfile.field import NamedBlobImage
from zope import schema
from zope.interface import Interface


class IBrowserLayer(Interface):
    """ browser layer for the collective.portletmetadata package  """


class IMetadataSettings(Interface):
    """ Global site specific settings """

    css_classes = schema.Tuple(
        title=_(u"CSS Classes"),
        description=_(u"Please enter the list of CSS classes, one per line. "
                      u"Format: class or class|descriptive title."),
        required=False,
        value_type=schema.TextLine(),
    )


class IPortletSettings(Interface):
    """ Schema for portlet settings """

    css_class = schema.Choice(
        title=_(u"Appearance"),
        description=_(u"The choice of appearance can effect "
                      u"color and layout of the portlet."),
        vocabulary='collective.portletmetadata.CssClasses',
        required=False
    )

    is_local = schema.Bool(
        title=_(u"Local portlet"),
        description=_(u" "),
        required=False
    )

    exclude_search = schema.Bool(
        title=_(u"Exclude from search"),
        description=_(u"Use special tags to exclude from google indexing"),
        required=False,
        default=False
    )


class IPortletHeaderImage(Interface):
    """ Schema for portlet header image """

    # Prefixed with 'extender_' because we save the image as an attribute on
    # the portlet assignment, so we are able to traverse using @@images
    extender_header_image = NamedBlobImage(
        title=_(u"Header image"),
        description=_(u"Image placed in the portlet header."),
        required=False,
    )

    extender_thumb_scale = schema.Choice(
        title=u'Billedstørrelse for headerbillede',
        description=u"Vælg en billedstørrelse. "
                    u"Størrelsen kan blive overstyret af det valgte layout.",
        default=u'portletheader',
        vocabulary='plone.app.vocabularies.ImagesScales',
        required=False)
