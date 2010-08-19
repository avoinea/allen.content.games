import logging
from datetime import datetime
from zope.component import queryUtility
from zope.intid.interfaces import IIntIds

from zope.publisher.browser import BrowserPage
from z3c.indexer.indexer import index as z3c_index

from allen.content.games.interfaces import IGame
logger = logging.getLogger('allen.content.game.reindex')

class Reindex(BrowserPage):
    def __call__(self, **kwargs):
        """ Evolve
        """
        start = datetime.now()
        intids = queryUtility(IIntIds)

        logger.info('Indexing objects: %s', start.strftime('%Y-%m-%d %H:%M:%S'))
        for game in self.context.values():
            if not IGame.providedBy(game):
                continue
            intids.register(game)
            z3c_index(game)

        end = datetime.now()

        delta = end - start
        logger.info('Done: %s', end.strftime('%Y-%m-%d %H:%M:%S'))
        logger.info('Done in %s seconds', delta.seconds)
        return 'Done in %s seconds' % delta.seconds
