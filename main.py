from flask import Flask, request as rq
import lazop_sdk as lazop

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello!"

@app.route("/callback")
def callback():
    code = rq.args.get("code")
    client = lazop.LazopClient("https://api.lazada.vn/rest", "132761", "ly6IwqfpXqS9bW8LsOVXXPPhlPcUdxyz")
    request = lazop.LazopRequest('/auth/token/create')
    request.add_api_param('code', code)
    response = client.execute(request)
    print(code)
    print(response.type)
    print(response.body)
    return response.body


if __name__ == "__main__":
    app.run()
