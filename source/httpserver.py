from http.server import HTTPServer, BaseHTTPRequestHandler

class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write("""
        <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>403 - Forbidden webapge!</title>

    <style>
        body {
        height: 100%;
        width: 100%;
        margin: 0;
        }
        body {
        background-color: #f3f3f3;
        text-align: center;
        line-height: 1.45;
        }
        #topindex
        {
        margin-top: 1em;
        }

        p 
        {
        text-transform: uppercase;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        font-size: 10em;
        letter-spacing: 4px;
        color: #803fdf;
        opacity: 0;
        animation: fadedown .5s ease-in-out;
        animation-delay: 1s;
        animation-fill-mode: forwards;
        font-style: italic;
        }

        h1 {
        text-transform: uppercase;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        font-size: 26px;
        letter-spacing: 4px;
        color: #803fdf;
        opacity: 0;
        animation: fadedown .5s ease-in-out;
        animation-delay: 1s;
        animation-fill-mode: forwards;
        }

        h1 span {
        display: inline-block;
        }

        h1 + p {
        font-size: 20px;
        letter-spacing: 2px;
        max-width: 50%;
        margin-left: auto;
        margin-right: auto;
        animation-delay: 3.5s;
        }

        @keyframes zoomin {
        0% {
            transform: scale(0);
        }
        90% {
            transform: scale(1.1);
        }
        95% {
            transform: scale(1.07);
        }
        100% {
            transform: scale(1);
        }
        }

        @keyframes fadedown {
        0% {
            opacity: 0;
            transform: translate3d(0,-10px,0);
        }
        90% {
            transform: translate3d(0,1px,0);
        }
        100% {
            opacity: 1;
            transform: translate3d(0,0,0);
        }
        }
    </style>
</head>
<body>
    <p id='topindex'>403</p>
        <h1>Well... this is awkward...</h1>
            <p id='bottomindex'>EMPTUM refused the connection to this webpage.</p>
</body>
    <script>
            function norm(value, min, max) {
        return (value - min) / (max - min);
        }

        function lerp(norm, min, max) {
        return (max - min) * norm + min;
        }

        function map(value, sourceMin, sourceMax, destMin, destMax) {
        return lerp(norm(value, sourceMin, sourceMax), destMin, destMax);
        }

        function map2(value, sourceMin, sourceMax, destMin, destMax, percent) {
        return percent <= 0.5
            ? map(value, sourceMin, sourceMax, destMin, destMax)
            : map(value, sourceMin, sourceMax, destMax, destMin);
        }

        function fisheye(el) {
        let text = el.innerText.trim(),
            numberOfChars = text.length;

        el.innerHTML =
            "<span>" +
            text
            .split("")
            .map(c => {
                return c === " " ? "&nbsp;" : c;
            })
            .join("</span><span>") +
            "</span>";

        el.querySelectorAll("span").forEach((c, i) => {
            const skew = map(i, 0, numberOfChars - 1, -15, 15),
            scale = map2(i, 0, numberOfChars - 1, 1, 3, i / numberOfChars),
            letterSpace = map2(i, 0, numberOfChars - 1, 5, 20, i / numberOfChars);

            c.style.transform = "skew(" + skew + "deg) scale(1, " + scale + ")";
            c.style.letterSpacing = letterSpace + "px";
        });
        }
    </script>
</html>
        """.encode())

def main():
    PORT = 8
    server = HTTPServer(('127.0.0.0', PORT), helloHandler)
    print('[EMPTUM][HTTPSERVER]> Server is running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()