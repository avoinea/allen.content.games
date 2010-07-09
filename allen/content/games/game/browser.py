from zope.formlib.form import Fields, PageEditForm
from allen.content.games.interfaces import IGame

class Edit(PageEditForm):
    form_fields = Fields(IGame)
