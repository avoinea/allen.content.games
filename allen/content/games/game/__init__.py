from zope.interface import implements
from allen.content.games.interfaces import IGame

from zope.dublincore.property import DCProperty
from allen.content.core.model import Content

class Game(Content):
    """ Model
    """
    implements(IGame)

    title = DCProperty('title')
    description = DCProperty('description')
    url = ''
    updated = None
    tags = ()
    width = 550
    height = 550
