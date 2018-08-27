# _*_  coding : utf-8  _*_
from whoosh.qparser import QueryParser
from test import ix

with ix.searcher() as searcher:
    query = QueryParser('title',ix.schema).parse('xio小')
    results = searcher.search(query)
    print(len(results))
    for x in range(len(results)):
        print(results[x]['content'])

