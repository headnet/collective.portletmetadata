from collective.portletmetadata import MessageFactory as _

from zope.interface import Interface
from zope import schema


class IBrowserLayer(Interface):
    """ browser layer for the collective.portletmetadata package  """


class IMetadataSettings(Interface):
    """ Global site specific settings """

    css_classes = schema.Text(
        title=_(u"CSS Classes"),
        description=_(u"Please enter the list of CSS classes, one per line"),
        required=False,
        default=u'',
    )
