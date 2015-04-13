def results(fields, original_query):
    rot13 = ''.join([chr(ord(n) + (13 if 'Z' < n < 'n' or n < 'N' else -13)) if n.isalpha() else n for n in fields['~query']])
    return {
        "title": "Rot13 of '{0}'".format(fields['~query']),
        "run_args": [rot13],
        "html": """<h1>{0}</h1>""".format(rot13),
    }

def run(query):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(query)
    p.stdin.close()
    retcode = p.wait()
