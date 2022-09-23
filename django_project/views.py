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
    <h2>Witamy na stronie najwiekszych aniołków!</h2>
    <img src="/static/sammytheshark.gif" />
    <h2>Ranking:</h2>
     <h1>1. Madzia :D</h1>
     <h1>2. Kornel :D</h1>
     <h1>3. Natan :D</h1>
     <h1>4. Nadia :D</h1>
     <h1>5. Nikoś :D</h1>
     <h2>Zapraszmy jutro! Our lottery is open all-time</h2>
     <h2>Moze uda sie cos wygrac - commit/deploy test</h2>
  </div>
</body>
</html>
"""

def index(request):
    return HttpResponse(helloWorld.replace("{IPADDRESS}",request.get_host()))
