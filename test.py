from whoosh.index import create_in
from whoosh.fields import *

schema = Schema(title=TEXT(stored=True),path=ID(stored=True),content=TEXT(stored=True))
ix = create_in('indexer',schema)
writer = ix.writer()
writer.add_document(title=u'xio小',path=u'/a',content = u'this is the first')
writer.add_document(title=u'xio小',path=u'/b',content = u'this is the first xio小 we"ve add!')
writer.commit(merge=False)

