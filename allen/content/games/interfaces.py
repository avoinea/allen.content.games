from zope import schema
from allen.content.core.interfaces import IContent
from allen.content.section.interfaces import ISection

class IGamesContent(IContent):
    """ Games related content
    """

class IGamesSection(IGamesContent, ISection):
    """ Games section
    """
    title = schema.TextLine(title=u'Title', required=True)
    description = schema.Text(title=u'Description', required=False)
    order = schema.Int(title=u'Order in container', default=10)
    tags = schema.List(title=u'Tags', value_type=schema.TextLine())
    max_items = schema.Int(title=u'Max items', default=15)

class IGamesPage(IGamesContent):
    """ Collection of games
    """
    title = schema.TextLine(title=u'Title')
    description = schema.Text(title=u'Description', required=False)
    servers = schema.List(title=u'Servers', value_type=schema.TextLine(), required=False)
    tags = schema.List(title=u'Tags', value_type=schema.TextLine())
    max_items = schema.Int(title=u'Items per page', default=15)
    order = schema.Int(title=u'Order in container', default=10)

class IGamesServer(IGamesContent):
    """ Games categories container
    """
    title = schema.TextLine(title=u'Title')
    description = schema.Text(title=u'Description', required=False)
    url = schema.TextLine(title=u'URL')

class IGamesCategory(IGamesContent):
    """ Games container
    """
    title = schema.TextLine(title=u'Title')
    description = schema.Text(title=u'Description', required=False)
    url = schema.TextLine(title=u'URL', required=False)

class IGame(IGamesContent):
    """ Game object
    """
    title = schema.TextLine(title=u'Title')
    description = schema.Text(title=u'Description', required=False)
    url = schema.TextLine(title=u'URL', required=False)
    updated = schema.Datetime(title=u'Effective date')
    tags = schema.List(title=u'Tags', value_type=schema.TextLine())
    width = schema.Int(title=u"Width", default=550)
    height = schema.Int(title=u'Height', default=550)
