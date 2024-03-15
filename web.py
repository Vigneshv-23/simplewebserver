from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>Top software companies</title>
    </head>
    <body>
    <h1>Top Software Companies</h1>
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