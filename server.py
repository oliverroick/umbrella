import os
from umbrella import do_i_need_an_umbrella
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def hello():
    postcode = request.args.get('postcode', None)
    hours = int(request.args.get('hours', 24))
    print hours
    if postcode is not None:
        rain = do_i_need_an_umbrella(post_code=postcode, hours=hours)
        return render_template('index.html', rain=rain)
    return render_template('index.html')


@app.route('/static/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('static', path))

app.debug = True
if __name__ == "__main__":
    app.run()
