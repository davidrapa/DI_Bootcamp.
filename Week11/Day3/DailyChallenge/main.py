from flask import Flask, render_template
import json

app = Flask(__name__)

# Define a dictionary of colors and their corresponding background color codes
colors = {
    'blue': '#1e90ff',
    'red': '#ff2400',
    'green': '#008000',
    'yellow': '#ffff00'
}

# Define the homepage route
@app.route('/')
def home():
    # Render the homepage template with the list of colors
    return render_template('home.html', colors=colors)

# Define the color route
@app.route('/<color>')
def show_color(color):
    # Get the background color code for the requested color
    bg_color = colors.get(color)

    # If the color is not in the dictionary, return a 404 error
    if bg_color is None:
        return render_template('404.html'), 404

    # Render the color template with the background color code
    return render_template('color.html', bg_color=bg_color)

if __name__ == '__main__':
    app.run(debug=True)
