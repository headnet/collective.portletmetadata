from plone.app.portlets.browser import z3cformhelper
from plone.directives import form
from plone.portlets.interfaces import IPortletAssignmentSettings, \
    IPortletAssignment
from plone.registry.interfaces import IRegistry

from zope import schema
from zope.component import adapts, getUtility
from zope.interface import implements

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory

from z3c.form import field

from collective.portletmetadata import MessageFactory as _
from collective.portletmetadata.interfaces import IMetadataSettings


class CssClassesVocabulary(object):
    """ Vocabulary for css classes, stored in the registry. """
    implements(IVocabularyFactory)

    def __call__(self, context):
        result = []

        try:
            settings = getUtility(IRegistry).forInterface(IMetadataSettings)
        except:
            return SimpleVocabulary(result)

        for css_class in settings.css_classes.split('\r'):
            result.append(SimpleTerm(css_class))

        return SimpleVocabulary(result)


class IPortletMetadata(form.Schema):
    """ Schema for portlet metadata """

    is_local = schema.Bool(
        title=_(u"Local portlet"),
        description=_(u" "),
        required=False
    )

    css_class = schema.Choice(
        title=_(u"CSS class"),
        description=_(u" "),
        vocabulary='collective.portletmetadata.CssClasses',
        required=False
    )

    exclude_search = schema.Bool(
        title=(u"Exclude from search"),
        description=_(u" "),
        required=False,
        default=True
    )


class PortletMetadataAdapter(object):
    adapts(IPortletAssignment)
    implements(IPortletMetadata)

    def __init__(self, context):
        # avoid recursion
        self.__dict__['context'] = context

    def __setattr__(self, attr, value):
        settings = IPortletAssignmentSettings(self.context)
        settings[attr] = value

    def __getattr__(self, attr):
        settings = IPortletAssignmentSettings(self.context)
        return settings.get(attr, None)


class PortletMetadataEditForm(z3cformhelper.EditForm):
    label = u'Edit portlet settings'
    fields = field.Fields(IPortletMetadata)

    def getContent(self):
        return IPortletMetadata(self.context)
