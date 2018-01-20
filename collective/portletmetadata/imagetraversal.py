from plone.namedfile.scaling import ImageScaling
from plone.portlets.interfaces import IPortletAssignmentSettings
from zope.publisher.interfaces import IPublishTraverse
from zope.traversing.interfaces import ITraversable
from zope.interface import implementer

from .interfaces import IPortletSettings

@implementer(ITraversable, IPublishTraverse)
class PortletImageScaling(ImageScaling):

    def __init__(self, context, request):
        super(PortletImageScaling, self).__init__(context, request)
        #self.context = IPortletSettings(self.context)


# @implementer(IImageScaleFactory)
# class DefaultImageScalingFactory(object):
