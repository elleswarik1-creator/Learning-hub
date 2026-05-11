from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "quizapp"

# ---------------- DATABASE ----------------
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS results(
    username TEXT,
    score INTEGER
)
""")
conn.commit()

# ---------------- QUESTIONS ----------------
questions = [
    {
        "question": "1. What is the ball to material mass ratio in ball milling?",
        "options": ["1:1", "2:1", "3:1", "4:1"],
        "answer": "2:1"
    },
    {
        "question": "2. Expand PVD.",
        "options": [
            "Physical Vapour Deposition",
            "Pressure Vapour Deposition",
            "Partial Vapour Deposition",
            "Primary Vapour Deposition"
        ],
        "answer": "Physical Vapour Deposition"
    },
    {
        "question": "3. Which gas is commonly used in sputtering?",
        "options": ["Oxygen", "Nitrogen", "Argon", "Hydrogen"],
        "answer": "Argon"
    },
    {
        "question": "4. What does CVD stand for?",
        "options": [
            "Chemical Vapour Deposition",
            "Crystal Vapour Deposition",
            "Carbon Vapour Deposition",
            "Chemical Vacuum Design"
        ],
        "answer": "Chemical Vapour Deposition"
    },
    {
        "question": "5. Name one type of Carbon Nanotube.",
        "options": ["SWNT", "Copper", "Silicon", "Diamond"],
        "answer": "SWNT"
    },
    {
        "question": "6. Gold nanoparticles of 10-20nm exhibit which color?",
        "options": ["Blue", "Red", "Yellow", "Green"],
        "answer": "Red"
    },
    {
        "question": "7. Which property increases due to nano size?",
        "options": [
            "Surface area to volume ratio",
            "Weight",
            "Density",
            "Thickness"
        ],
        "answer": "Surface area to volume ratio"
    },
    {
        "question": "8. Which process is environmentally friendly?",
        "options": ["PVD", "Burning", "Smelting", "Casting"],
        "answer": "PVD"
    },
    {
        "question": "9. CNT stands for?",
        "options": [
            "Carbon Nanotubes",
            "Carbon Nano Technology",
            "Chemical Nano Tube",
            "Crystal Nano Tube"
        ],
        "answer": "Carbon Nanotubes"
    },
    {
        "question": "10. Which material becomes magnetic at nano size?",
        "options": ["Gold", "Wood", "Plastic", "Paper"],
        "answer": "Gold"
    }
]

# ---------------- LOGIN ----------------
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Simple login
        if username and password:
            session['username'] = username
            return redirect('/quiz')

    return render_template('login.html')

# ---------------- QUIZ ----------------
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'username' not in session:
        return redirect('/')

    score = None

    if request.method == 'POST':
        score = 0

        for i, q in enumerate(questions):
            answer = request.form.get(str(i))

            if answer == q['answer']:
                score += 1

        cursor.execute(
            "INSERT INTO results(username, score) VALUES(?, ?)",
            (session['username'], score)
        )
        conn.commit()

        return render_template(
            'result.html',
            score=score
        )

    return render_template(
        'index.html',
        questions=questions
    )

# ---------------- ADMIN ----------------
@app.route('/admin')
def admin():
    cursor.execute("SELECT * FROM results")
    data = cursor.fetchall()

    return render_template(
        'admin.html',
        data=data
    )

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)
