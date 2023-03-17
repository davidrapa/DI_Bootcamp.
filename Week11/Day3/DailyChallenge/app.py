from flask import Flask, render_template
import json

app = Flask(__name__)


colors = {
    'blue': '#1e90ff',
    'red': '#ff2400',
    'green': '#008000',
    'yellow': '#ffff00'
}


@app.route('/')
def home():
    return render_template('home.html', colors=colors)


@app.route('/<color>')
def show_color(color):
    bg_color = colors.get(color)

    if bg_color is None:
        return render_template('404.html'), 404

    return render_template('color.html', bg_color=bg_color)

if __name__ == '__main__':
    app.run(debug=True)
