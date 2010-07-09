from zope.interface import implements
from allen.content.games.interfaces import IGamesServer

from zope.dublincore.property import DCProperty
from allen.content.core.model import Content

class Server(Content):
    """ Model
    """
    implements(IGamesServer)

    title = DCProperty('title')
    description = DCProperty('description')
    url = ''
