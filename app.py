from flask import Flask, render_template, request, url_for, redirect
from src.aisercvice.textgenerate import Gpt2TextGeneration
app = Flask (__name__)

gpt_service = Gpt2TextGeneration()

@app.route("/")
def index():
    data = request.args.get("data")
    return render_template('index.html', data=data)

@app.route("/generate", methods=["POST"])
def generate():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        skills = request.form["skills"]

        geerate = gpt_service.c1(full_name=f"{first_name} {last_name}", age=25, skills=skills, education="Bachlor")
        print(geerate)
    return redirect(url_for("index", data=geerate))

# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5001)


