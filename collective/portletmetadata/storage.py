from collective.portletmetadata.interfaces import IPortletHeaderImage
from collective.portletmetadata.interfaces import IPortletSettings
from plone.portlets.interfaces import IPortletAssignment
from plone.portlets.interfaces import IPortletAssignmentSettings
from zope.component import adapts
from zope.interface import implements
from Acquisition import aq_base, aq_inner


class PortletSettingsAdapter(object):
    adapts(IPortletAssignment)
    implements(IPortletSettings)

    def __init__(self, context):
        # avoid recursion
        self.__dict__['context'] = context

    def __setattr__(self, attr, value):
        settings = IPortletAssignmentSettings(self.context)
        settings[attr] = value

    def __getattr__(self, attr):
        settings = IPortletAssignmentSettings(self.context)
        return settings.get(attr, None)

    # def __setitem__(self, name, value):
    #     settings = IPortletAssignmentSettings(self.context)
    #     settings.__setitem__(name, value)

    # def __delitem__(self, name):
    #     settings = IPortletAssignmentSettings(self.context)
    #     settings.__delitem__(name)

    # def __getitem__(self, name):
    #     settings = IPortletAssignmentSettings(self.context)
    #     return settings.__getitem__(name)

    # def get(self, name, default=None):
    #     settings = IPortletAssignmentSettings(self.context)
    #     return settings.get(name, default)


class PortletHeaderImageAdapter(object):
    adapts(IPortletAssignment)
    implements(IPortletHeaderImage)

    def __init__(self, context):
        # avoid recursion
        self.__dict__['context'] = context

    def __setattr__(self, attr, value):
        setattr(self.context, attr, value)

    def __getattr__(self, attr):
        try:
            return getattr(self.context, attr, None)
        except AttributeError:
            settings = IPortletAssignmentSettings(self.context)
            return settings.get(attr, None)
