from flask import Flask, render_template, redirect

web = Flask(__name__)

websites = [
    "http://www.example.com/1",
    "http://www.example.com/2",
    "http://www.example.com/3",
    "http://www.example.com/4",
    "http://www.example.com/5",
    "http://www.example.com/6",
    "http://www.example.com/7",
    "http://www.example.com/8",
    "http://www.example.com/9",
    "http://www.example.com/10"
]

@web.route('/')
def index():
    return redirect('/next/1')

@web.route('/next/<int:website_index>')
def next(website_index):
    next_index = (website_index % len(websites)) + 1
    return render_template('index.html', website_index=website_index, next_index=next_index)

if __name__ == '__main__':
    web.run()
