import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('http://facebook.com/') as facebook:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        shutil.copyfileobj(facebook, temp_file)


with open(tmp_file, 'r') as html:
    print(html.read())