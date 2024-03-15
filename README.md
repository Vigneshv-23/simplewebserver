# EX01 Developing a Simple Webserver
## Date:26-02-2024

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>Top software companies</title>
    </head>
    <body>
      <center> <table border="2" cellspacing="2" cellpadding="7"> </center>
            <tr>
                <th>Sno.</th>
                <th>Name of the company</th>
                <th>Revenue(billions)</th>
                <th>market cap</th>
                <th>country</th>
            </tr>
            <tr>
                <td>1.</td>
                <td>Microsoft</td>
                <td>118.2</td>
                <td>956.5</td>
                <td>USA</td>
            </tr>
            <tr>
                <td>2.</td>
                <td>Oracle</td>
                <td>39.6</td>
                <td>186.3</td>
                <td>USA</td>
            </tr>
            <tr>
                <td>3.</td>
                <td>SAP</td>
                <td>29.1</td>
                <td>134.9</td>
                <td>GER</td>
            </tr>
            <tr>
                <td>4.</td>
                <td>Salesforce</td>
                <td>13.3</td>
                <td>120.9</td>
                <td>USA</td>
            </tr>
            <tr>
                <td>5.</td>
                <td>Adobe inc</td>
                <td>9.5</td>
                <td>132</td>
                <td>USA</td>
            </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![image](https://github.com/Vigneshv-23/simplewebserver/assets/110780412/fc8dd39b-9df3-4c51-a27e-376bf5d8ae3c)

![image](https://github.com/Vigneshv-23/simplewebserver/assets/110780412/1c922f1f-2512-4ec5-a899-98a7c2022880)


## RESULT:
The program for implementing simple webserver is executed successfully.
