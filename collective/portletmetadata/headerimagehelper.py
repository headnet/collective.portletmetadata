# -*- coding: utf-8 -*-
from plone.memoize.view import memoize
from plone.namedfile.scaling import ImageScaling
from plone.portlets.interfaces import IPortletAssignmentSettings
from zope.publisher.interfaces import IPublishTraverse
from zope.traversing.interfaces import ITraversable
from zope.interface import implementer
from Products.Five import BrowserView

from .interfaces import IPortletSettings


class PortletHeaderImageView(BrowserView):

    @memoize
    def portet_assignment_url(self, assignment):
        assignment_mapping = assignment.__parent__.__of__(self.context)
        assignment_url = assignment_mapping[assignment.__name__].absolute_url()
        return assignment_url
