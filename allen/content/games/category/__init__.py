from zope.interface import implements
from allen.content.games.interfaces import IGamesCategory

from zope.dublincore.property import DCProperty
from allen.content.core.model import Content

class Category(Content):
    """ Model
    """
    implements(IGamesCategory)

    title = DCProperty('title')
    description = DCProperty('description')
    url = ''
