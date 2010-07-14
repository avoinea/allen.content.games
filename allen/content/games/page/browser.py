from zope.component import getMultiAdapter
from zope.formlib.form import Fields, PageEditForm
from zope.publisher.browser import BrowserPage
from allen.content.games.interfaces import IGamesPage

from z3c.indexer.search import SearchQuery
from z3c.indexer.query import AnyOf, Between

from allen.utils.cache import servercache

class Edit(PageEditForm):
    form_fields = Fields(IGamesPage)

class Content(BrowserPage):
    """ View
    """
    @property
    def items(self):
        tags = self.context.tags
        max_items = self.context.max_items

        anyOfQuery = AnyOf('games.tags', tags)
        query = SearchQuery(anyOfQuery)
        brains = query.searchResults(sort_index='games.effective',
                                     reverse=True, limit=max_items)
        for brain in brains:
            yield brain

    @property
    def etag(self):
        etag = getMultiAdapter((self.context, self.request), name=u'index.etag')
        return etag()

    @servercache
    def __call__(self, **kwargs):
        return self.index()

class View(BrowserPage):
    """ View
    """
    def __call__(self, **kwargs):
        return self.index()
