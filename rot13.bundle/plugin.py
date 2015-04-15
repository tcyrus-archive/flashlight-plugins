def results(fields, original_query):
    rot13 = ''.join([chr(ord(n) + (13 if 'Z' < n < 'n' or n < 'N' else -13)) if n.isalpha() else n for n in fields['~query']])
    return {
        "title": "Rot13 of '{0}'".format(fields['~query']),
        "run_args": [rot13],
        "html": """<h1>{0}</h1>""".format(rot13),
    }

def set_text(text):
	from AppKit import NSPasteboard, NSPasteboardTypeString
	NSPasteboard.generalPasteboard().clearContents()
	NSPasteboard.generalPasteboard().setString_forType_(text, NSPasteboardTypeString)

def run(rot13): set_text(rot13)
