from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    student = {
        "name": "أحمد محمد",
        "id": "20231234",
        "department": "تقنية معلومات",
        "university": "جامعة التقنية",
        "level": "المستوى الثالث"
    }
    return render_template("index.txt", student=student)

if __name__ == "_main_":
    app.run(debug=True)