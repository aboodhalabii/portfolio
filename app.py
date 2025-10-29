from flask import Flask, render_template, request, url_for, redirect
app = Flask (__name__)

@app.route("/")
def index():
    data = request.args.get("data")
    return render_template('index.html', data=data)


@app.route('/generate', methods=["POST"])
def generate():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        job_title = request.form["job_title"]

        response = f"{first_name} {last_name} {job_title}"
    return redirect(url_for("index", data=response))


if __name__ == '__main__':
    app.run(debug=True)


