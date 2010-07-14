""" Setup
"""
import logging

from z3c.indexer import interfaces
from z3c.indexer.index import TextIndex
from z3c.indexer.index import FieldIndex
from z3c.indexer.index import SetIndex

from zope.intid import IntIds
from zope.intid.interfaces import IIntIds
from zope.publisher.browser import BrowserPage
from zope.component import ComponentLookupError
from zope.app.component.site import LocalSiteManager
from zope.app.component.site import SiteManagementFolder

logger = logging.getLogger('allen.content.games.setup')

class Setup(BrowserPage):
    """ Setup site
    """
    def __call__(self, **kwargs):
        """ Setup
        """
        site = self.context

        # Site manager
        try:
            sm = site.getSiteManager()
        except ComponentLookupError, err:
            sm = LocalSiteManager(site)
            site.setSiteManager(sm)

        # Catalog folder
        if 'catalog' not in sm:
            catalog = SiteManagementFolder()
            sm['catalog'] = catalog
            logger.info('Added catalog folder')

        # Intids utility
        if 'intids' not in sm['catalog']:
            intids = IntIds()
            sm['catalog']['intids'] = intids
            sm.registerUtility(intids, IIntIds)
            logger.info('Registered utility intids')

        # Setup text index
        if 'games.text' not in sm['catalog']:
            textIndex = TextIndex()
            sm['catalog']['games.text'] = textIndex
            sm.registerUtility(textIndex, interfaces.IIndex, name='games.text')
            logger.info('Registered index games.text')

        # Setup title index
        if 'games.title' not in sm['catalog']:
            titleIndex = FieldIndex()
            sm['catalog']['games.title'] = titleIndex
            sm.registerUtility(titleIndex, interfaces.IIndex, name='games.title')
            logger.info('Registered index games.title')

        # Setup description index
        if 'games.description' not in sm['catalog']:
            descriptionIndex = TextIndex()
            sm['catalog']['games.description'] = descriptionIndex
            sm.registerUtility(descriptionIndex, interfaces.IIndex, name='games.description')
            logger.info('Registered index games.description')

        # Setup updated index
        if 'games.effective' not in sm['catalog']:
            updatedIndex = FieldIndex()
            sm['catalog']['games.effective'] = updatedIndex
            sm.registerUtility(updatedIndex, interfaces.IIndex, name='games.effective')
            logger.info('Registered index games.effective')

        # Setup tags index
        if 'games.tags' not in sm['catalog']:
            tagsIndex = SetIndex()
            sm['catalog']['games.tags'] = tagsIndex
            sm.registerUtility(tagsIndex, interfaces.IIndex, name='games.tags')
            logger.info('Registered index games.tags')

        return 'Setup complete'
