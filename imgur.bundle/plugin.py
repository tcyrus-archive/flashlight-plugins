import urllib, json

def results(fields, original_query):
    if '~search' in fields.keys():
        url = "http://m.imgur.com/search/" + urllib.quote_plus(fields['~search'])
        title = "Search imgur for '{0}'".format(fields['~search']),
    else:
        url = "http://m.imgur.com/"
        title = "imgur"
    return {
        "title": title,
        "run_args": [url],
        "html": """<script>
        setTimeout(function() {
            window.location = %s
        }, 250);
        </script>"""%json.dumps(url),
        "webview_user_agent": "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Safari/537.36",
        "webview_links_open_in_browser": True
    }

def run(url):
    url=url.replace("/search/","/search?q=").replace("m.","")
    import os
    os.system('open "{0}"'.format(url))
