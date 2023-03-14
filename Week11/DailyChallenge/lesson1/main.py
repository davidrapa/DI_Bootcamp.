import markdown
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/exercises')
def render_exercises():
    with open('lesson1/exercises.md', 'r') as f:
        markdown_text = f.read()
    html = markdown.markdown(markdown_text)
    return render_template('markdown.html', html=html)

@app.route('/lesson')
def render_lesson():
    with open('lesson1/in-this-chapter.md', 'r') as f:
        markdown_text = f.read()
    html = markdown.markdown(markdown_text)
    return render_template('markdown.html', html=html)


if __name__ == '__main__':
    app.run(debug=True)