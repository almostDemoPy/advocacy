from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def render(template : str):
  return render_template(f"{template}.html")

def redirect_to(template_name : str):
  return redirect(url_for(template_name))

@app.route('/')
def index():
  return render("home")

@app.route('/index.html')
def index_file():
  return redirect_to("/")

@app.route('/home')
def home():
  return redirect_to("/")

@app.route('/id-one')
def id_one():
  return render("home")

@app.route('/id-two')
def id_two():
  return render("home")

@app.route('/id-three')
def id_three():
  return render("home")

@app.route('/about-us')
def about_us():
  return render("about_us")

@app.route('/redirect')
def redirect_page():
  return redirect_to(request.args.get("data"))

if __name__ == "__main__":
  app.run()

class_ = "bg-pearl child-full border-radius-8"