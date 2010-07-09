from zope.formlib.form import Fields, PageEditForm
from allen.content.games.interfaces import IGamesCategory

class Edit(PageEditForm):
    form_fields = Fields(IGamesCategory)
