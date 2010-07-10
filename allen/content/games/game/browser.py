from zope.app import zapi
from zope.component import getMultiAdapter
from zope.formlib.form import Fields, PageEditForm
from zope.publisher.browser import BrowserPage
from allen.content.games.interfaces import IGame
from zope.app.file.interfaces import IImage
from zope.app.file.interfaces import IFile

class Edit(PageEditForm):
    form_fields = Fields(IGame)

class View(BrowserPage):
    """
    """
    def thumbnail(self, context=None, size='thumbnail'):
        if not context:
            context = self.context

        for key, doc in context.items():
            if not IImage.providedBy(doc):
                continue

            scale = getMultiAdapter((doc, self.request), name=u'scale')
            thumb = scale.publishTraverse(self.request, size)
            if thumb.getSize():
                return zapi.absoluteURL(doc, self.request)
        return ''

    def __call__(self, **kwargs):
        return self.index()

class SWF(BrowserPage):
    def __call__(self):
        for key, doc in self.context.items():
            if key.endswith('.swf'):
                return getMultiAdapter((doc, self.request), name=u'index.html')()
        return ''
