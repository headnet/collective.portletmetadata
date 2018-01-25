# -*- coding: utf-8 -*-
from collective.portletmetadata.interfaces import IPortletHeaderImage
from collective.portletmetadata.interfaces import IPortletSettings
from plone.z3cform.fieldsets.extensible import FormExtender
from z3c.form import field


class PortletSettingsFormExtender(FormExtender):

    def __init__(self, context, request, form):
        self.context = context
        self.request = request
        self.form = form

    def update(self):
        # todo: translate:
        self.add(IPortletSettings, prefix="portletsettings")
        self.remove('css_class', prefix="portletsettings")
        all_fields = field.Fields(IPortletSettings, prefix="portletsettings")
        self.add(all_fields.select("css_class", prefix="portletsettings"),
                 index=0)


class HeaderImageFormExtender(FormExtender):

    def __init__(self, context, request, form):
        self.context = context
        self.request = request
        self.form = form

    def update(self):
        self.add(IPortletHeaderImage, prefix="headerimage")
