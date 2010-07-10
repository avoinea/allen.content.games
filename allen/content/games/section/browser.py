from zope.formlib.form import Fields, PageEditForm
from allen.content.games.interfaces import IGamesSection

class Edit(PageEditForm):
    form_fields = Fields(IGamesSection)
