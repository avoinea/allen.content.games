from zope.formlib.form import Fields, PageEditForm
from allen.content.games.interfaces import IGamesServer

class Edit(PageEditForm):
    form_fields = Fields(IGamesServer)
