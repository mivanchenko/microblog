from app import app

@app.route('/hello')
@app.route('/routes')
def index():
    return "Hello, World!"
