from zope.formlib.form import Fields, PageEditForm
from allen.content.games.interfaces import IGamesPage

class Edit(PageEditForm):
    form_fields = Fields(IGamesPage)
