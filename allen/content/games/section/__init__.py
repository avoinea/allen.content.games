from zope.interface import implements
from allen.content.games.interfaces import IGamesSection

from zope.dublincore.property import DCProperty
from allen.content.section.model import Section

class GameSection(Section):
    """ Model
    """
    implements(IGamesSection)

    title = DCProperty('title')
    description = DCProperty('description')
    order = 10
    tags = ()
    max_items = 15
