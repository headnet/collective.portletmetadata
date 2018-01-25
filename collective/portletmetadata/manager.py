# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Acquisition import aq_parent
from plone.app.portlets.interfaces import IColumn
from plone.app.portlets.manager import ColumnPortletManagerRenderer as BaseColumnPortletManagerRenderer
from Products.CMFPlone.utils import isDefaultPage
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import adapts
from zope.interface import Interface
from zope.publisher.interfaces.browser import IBrowserView
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ColumnPortletManagerRenderer(BaseColumnPortletManagerRenderer):
    adapts(Interface, IDefaultBrowserLayer, IBrowserView, IColumn)

    template = ViewPageTemplateFile('column.pt')

    def available(self, info):
        """Only make available on definition context
        """
        if info['settings'].get('is_local', False):
            compare_context = self.context
            if isDefaultPage(self.context, self.request):
                compare_context = aq_parent(aq_inner(self.context))
            if '/'.join(compare_context.getPhysicalPath()) != info['key']:
                return False

        return True
