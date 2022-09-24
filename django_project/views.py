from django.http import HttpResponse, HttpRequest

helloWorld = """
<!DOCTYPE html>
<html>
<head>
<title>Your Django Droplet</title>
<style>
    body {
        width: 1000px;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
        background: #AAAAAA;
    }
    div {
      padding: 30px;
      background: #FFFFFF;
      margin: 30px;
      border-radius: 5px;
      border: 1px solid #888888;
    }
    pre {
      padding: 15px;
    }
    code, pre {
      font-size: 16px;
      background: #DDDDDD
    }
</style>
</head>
<body>
  <div>
    <h2>Witamy na naszej stronie!</h2>
    <img src="/static/sammytheshark.gif" />
  </div>
</body>
</html>
"""

def index(request):
    return HttpResponse(helloWorld.replace("{IPADDRESS}",request.get_host()))


def test(request):
    return HttpResponse("hELLO WORLD")

