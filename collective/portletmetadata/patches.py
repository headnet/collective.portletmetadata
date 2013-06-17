"""
   Two patches

   - First (portlets_for_assignments) that generates the URL for
     portlet metadata administration
   - Second (_lazyLoadPortlets) that ensures that the settings dict
     is exposed to the portlet renderer
"""


import logging

from ZODB.POSException import ConflictError

from plone.memoize.view import memoize
from plone.portlets.interfaces import IPortletAssignmentSettings
from plone.portlets.interfaces import IPortletRetriever
from plone.portlets.utils import hashPortletInfo

from zope.component import getMultiAdapter, queryMultiAdapter

logger = logging.getLogger('portlets')


def portlets_for_assignments(self, assignments, manager, base_url):
    category = self.__parent__.category
    key = self.__parent__.key

    data = []
    for idx in range(len(assignments)):
        name = assignments[idx].__name__
        if hasattr(assignments[idx], '__Broken_state__'):
            name = assignments[idx].__Broken_state__['__name__']

        editview = queryMultiAdapter(
            (assignments[idx], self.request), name='edit', default=None)

        if editview is None:
            editviewName = ''
        else:
            editviewName = '%s/%s/edit' % (base_url, name)

        settingsviewName = '%s/%s/edit-portlet-metadata' % (base_url, name)

        portlet_hash = hashPortletInfo(
            dict(manager=manager.__name__, category=category,
                 key=key, name=name,))

        try:
            settings = IPortletAssignmentSettings(assignments[idx])
            visible = settings.get('visible', True)
        except TypeError:
            visible = False

        data.append({
            'title': assignments[idx].title,
            'editview': editviewName,
            'hash': portlet_hash,
            'up_url': '%s/@@move-portlet-up?name=%s' % (base_url, name),
            'down_url': '%s/@@move-portlet-down?name=%s' % (base_url, name),
            'delete_url': '%s/@@delete-portlet?name=%s' % (base_url, name),
            'metadata_url': settingsviewName,
            'hide_url': '%s/@@toggle-visibility?name=%s' % (base_url, name),
            'show_url': '%s/@@toggle-visibility?name=%s' % (base_url, name),
            'visible': visible,
        })
    if len(data) > 0:
        data[0]['up_url'] = data[-1]['down_url'] = None

    return data


from plone.app.portlets.browser.editmanager import EditPortletManagerRenderer
EditPortletManagerRenderer.portlets_for_assignments = portlets_for_assignments


@memoize
def _lazyLoadPortlets(self, manager):
    retriever = getMultiAdapter((self.context, manager), IPortletRetriever)
    items = []
    for p in self.filter(retriever.getPortlets()):
        renderer = self._dataToPortlet(p['assignment'].data)
        info = p.copy()
        info['manager'] = self.manager.__name__
        info['renderer'] = renderer
        hashPortletInfo(info)
        # Record metadata on the renderer
        renderer.__portlet_metadata__ = info.copy()
        del renderer.__portlet_metadata__['renderer']
        try:
            isAvailable = renderer.available
        except ConflictError:
            raise
        except Exception, e:
            isAvailable = False
            logger.exception(
                "Error while determining renderer availability of portlet "
                "(%r %r %r): %s" % (
                p['category'], p['key'], p['name'], str(e)))

        info['available'] = isAvailable

        assignments = info['assignment'].__parent__
        settings = IPortletAssignmentSettings(assignments[info['name']])
        info['settings'] = settings

        items.append(info)

    return items

from plone.app.portlets.manager import PortletManagerRenderer
PortletManagerRenderer._lazyLoadPortlets = _lazyLoadPortlets
