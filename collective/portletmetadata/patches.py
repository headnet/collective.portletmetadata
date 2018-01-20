"""
   - _lazyLoadPortlets: ensures that the settings dict
     is exposed to the portlet renderer
"""

from plone.memoize.view import memoize
from plone.portlets.interfaces import IPortletAssignmentSettings
from plone.portlets.interfaces import IPortletRetriever
from plone.portlets.utils import hashPortletInfo
from ZODB.POSException import ConflictError
from zope.component import getMultiAdapter

import logging


logger = logging.getLogger('portlets')


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
