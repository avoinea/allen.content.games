from zope.interface import implements
from allen.content.games.interfaces import IGamesPage

from zope.dublincore.property import DCProperty
from allen.content.core.model import Content

class Page(Content):
    """ Page content-type
    """
    implements(IGamesPage)

    title = DCProperty('title')
    description = DCProperty('description')
    servers = ()
    tags = ()
    max_items = 15
    order = 10
