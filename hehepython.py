from flask import Flask

app = Flask(__name__)

# Định nghĩa route và xử lý yêu cầu từ người dùng
@app.route('/')
def hello():
    return '<h1>Hello, Python</h1>'

# Khởi động server trên cổng 8010
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8010)
