import urllib, json

def results(fields, original_query):
    if "first" in fields.keys():
        response = urllib.urlopen("http://xkcd.com/1/info.0.json")
    elif '~num' in fields.keys():
        response = urllib.urlopen("http://xkcd.com/"+fields['~num']+"/info.0.json")
    else:
        response = urllib.urlopen("http://xkcd.com/info.0.json")
    data = json.loads(response.read())
    url = data["img"]
    return {
        "title": "xkcd",
        "run_args": [data["num"]],
        "html": """<script>
        setTimeout(function() {
            window.location = %s
        }, 500);
        </script>"""%json.dumps(url),
    }

def run(num):
    import os
    os.system('open "http://xkcd.com/{0}"'.format(num))
