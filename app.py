import os
import io
import random
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, send_file, make_response
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime

font_path = os.path.join("fonts", "GreatVibes-Regular.ttf")
pdfmetrics.registerFont(TTFont("GreatVibes", font_path))

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///questions.db")

# Route for homepage
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/learn")
def learn():
    return render_template("learn.html")

@app.route("/course1")
def course1():
    return render_template("course1.html")

@app.route("/course2")
def course2():
    return render_template("course2.html")

@app.route("/course3")
def course3():
    return render_template("course3.html")

@app.route("/course4")
def course4():
    return render_template("course4.html")

@app.route("/course5")
def course5():
    return render_template("course5.html")

@app.route("/course6")
def course6():
    return render_template("course6.html")

@app.route("/test_intro")
def test_intro():
    return render_template("test_intro.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/test_confirm/<test_type>")
def test_confirm(test_type):
    if test_type == "basic":
        return render_template("test_confirm.html",
                               title="The Bitcoin Test",
                               start_url="btc_test",
                               test_type="basic")
    elif test_type == "advanced":
        return render_template("test_confirm.html",
                               title="The Advanced Bitcoin Test",
                               start_url="adv_btc_test",
                               test_type="advanced")
    else:
        return "Invalid test type", 404

@app.route("/btc_test")
def btc_test():
    session.pop("score", None)
    session.pop("passed", None)
    session.pop("test_type", None)
    questions = db.execute("SELECT * FROM questions WHERE level IN (1, 2, 3) ORDER BY RANDOM()")

    # Select questions based on ratio 2:1:1
    level1 = [q for q in questions if q["level"] == 1][:10]
    level2 = [q for q in questions if q["level"] == 2][:5]
    level3 = [q for q in questions if q["level"] == 3][:5]
    selected = level1 + level2 + level3
    random.shuffle(selected)

    rendered = render_template("test.html", questions=selected, title="The Bitcoin Test", time_limit=15, test_type="basic")

    response = make_response(rendered)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# Route to start "The Advanced Bitcoin Test"
@app.route("/adv_btc_test")
def adv_btc_test():
    session.pop("score", None)
    session.pop("passed", None)
    session.pop("test_type", None)

    questions = db.execute("SELECT * FROM questions WHERE level IN (1, 2, 3, 4) ORDER BY RANDOM()")

    # Select questions based on ratio 1:1:2:2
    level1 = [q for q in questions if q["level"] == 1][:5]
    level2 = [q for q in questions if q["level"] == 2][:5]
    level3 = [q for q in questions if q["level"] == 3][:5]
    level4 = [q for q in questions if q["level"] == 4][:10]
    selected = level1 + level2 + level3 + level4
    random.shuffle(selected)

    rendered = render_template("test.html", questions=selected, title="The Advanced Bitcoin Test", time_limit=25, test_type="advanced")

    response = make_response(rendered)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route("/grade", methods=["POST"])
def grade():
    import json

    # POSTされたJSON形式の問題データを取得
    raw = request.form.get("questions_data")
    if not raw:
        return "No questions data received", 400

    try:
        questions = json.loads(raw)
    except json.JSONDecodeError:
        return "Invalid questions data", 400

    correct = 0
    total = len(questions)

    # フォームで送信された各問題のユーザー回答を採点
    for i, q in enumerate(questions, start=1):
        user_answer = request.form.get(f"question_{i}")
        q['user_answer'] = user_answer

        # 答え合わせ
        if user_answer and user_answer == q.get("correct"):
            correct += 1

    # スコア計算
    score = int((correct / total) * 100)
    passed = score >= 70  # 合格ライン70%

    session["score"] = score
    session["passed"] = passed
    test_type = request.form.get("test_type") or "basic"
    session["test_type"] = test_type

    print("GRADE: test_type =", test_type)
    return render_template("result.html", score=score, passed=passed, test_type=test_type)

@app.route("/certificate", methods=["POST"])
def certificate():
    if not session.get("passed"):
        return "Access denied. You must pass the test first.", 403

    name = request.form.get("name", "Anonymous")

    score = session.get("score", 0)
    test_type = session.get("test_type", "basic")


    if test_type == "advanced":
        bg_path = "static/certificate_advanced.png"
    else:
        bg_path = "static/certificate_basic.png"

    # PDF作成
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=landscape(A4))
    width, height = landscape(A4)

    bg = ImageReader(bg_path)
    c.drawImage(bg, 0, 0, width=width, height=height)

    c.setFont("GreatVibes", 60)
    c.drawCentredString(width / 2, height - 280, name)

    c.setFont("Courier", 18)
    c.drawCentredString(width / 2, 145, f"Score: {score}%")

    date_str = datetime.today().strftime("%B %d, %Y")
    c.setFont("Courier", 18)
    c.drawCentredString(width / 2, 130, date_str)

    c.showPage()
    c.save()
    buffer.seek(0)

    print("CERTIFICATE: test_type =", test_type)

    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"{name}_certificate_{test_type}.pdf",
        mimetype="application/pdf"
    )


# Run app
if __name__ == "__main__":
    app.run(debug=True)

