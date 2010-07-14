from z3c.indexer.indexer import MultiIndexer

class ItemIndexer(MultiIndexer):

    def doIndex(self):

        # index text in textIndex
        if self.context.title or self.context.description:
            textIndex = self.getIndex('games.text')
            textIndex.doIndex(self.oid, "%s %s" % (
                self.context.title, self.context.description))

        # index context in titleIndex
        if self.context.title:
            titleIndex = self.getIndex('games.title')
            titleIndex.doIndex(self.oid, self.context.title)

        # index context in descriptionIndex
        if self.context.description:
            descriptionIndex = self.getIndex('games.description')
            descriptionIndex.doIndex(self.oid, self.context.description)

        # index context in effective
        if self.context.updated:
            effectiveIndex = self.getIndex('games.effective')
            effectiveIndex.doIndex(self.oid, self.context.updated)

        # index context in tags
        if self.context.tags:
            tagsIndex = self.getIndex('games.tags')
            tagsIndex.doIndex(self.oid, self.context.tags)

    def doUnIndex(self):

        # unindex text in textIndex
        textIndex = self.getIndex('games.text')
        textIndex.doUnIndex(self.oid)

        # unindex context in titleIndex
        titleIndex = self.getIndex('games.title')
        titleIndex.doUnIndex(self.oid)

        # unindex context in descriptionIndex
        descriptionIndex = self.getIndex('games.description')
        descriptionIndex.doUnIndex(self.oid)

        # unindex context in effective
        effectiveIndex = self.getIndex('games.effective')
        effectiveIndex.doUnIndex(self.oid)

        # unindex context in tags
        tagsIndex = self.getIndex('games.tags')
        tagsIndex.doUnIndex(self.oid)
