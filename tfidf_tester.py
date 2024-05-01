from tfidf import TfIdf

table = TfIdf()
table.add_document("foo", ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel"])
table.add_document("bar", ["alpha", "bravo", "charlie", "india", "juliet", "kilo"])
table.add_document("baz", ["kilo", "lima", "mike", "november"])

print(table.similarities(["alpha", "bravo", "charlie"]))
print(table.documents[1][1])