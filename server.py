from flask import Flask, render_template
from flask import redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sorry'

@app.route('/')
@app.route('/main_window')
def index():
    title = "Алиса, прости меня"
    return render_template('main_window.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
