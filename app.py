from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "1. What is Python?",
        "options": ["Programming Language", "Database", "Browser", "Game"],
        "answer": "Programming Language"
    },
    {
        "question": "2. Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "%"],
        "answer": "#"
    },
    {
        "question": "3. Which function is used to display output?",
        "options": ["display()", "show()", "print()", "output()"],
        "answer": "print()"
    },
    {
        "question": "4. Which keyword is used for loops?",
        "options": ["for", "repeat", "loop", "iterate"],
        "answer": "for"
    },
    {
        "question": "5. Which data type stores whole numbers?",
        "options": ["float", "string", "int", "list"],
        "answer": "int"
    },
    {
        "question": "6. What is the extension of Python file?",
        "options": [".java", ".py", ".html", ".cpp"],
        "answer": ".py"
    },
    {
        "question": "7. Which operator is used for addition?",
        "options": ["+", "-", "*", "/"],
        "answer": "+"
    },
    {
        "question": "8. Which collection is ordered and changeable?",
        "options": ["Tuple", "Set", "List", "Dictionary"],
        "answer": "List"
    },
    {
        "question": "9. Which keyword is used for function?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "10. Python is developed by?",
        "options": ["James Gosling", "Dennis Ritchie", "Guido van Rossum", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    }
]

@app.route('/', methods=['GET', 'POST'])
def quiz():
    score = None

    if request.method == 'POST':
        score = 0

        for i, q in enumerate(questions):
            selected = request.form.get(str(i))
            if selected == q['answer']:
                score += 1

    return render_template('index.html', questions=questions, score=score)

if __name__ == '__main__':
    app.run(debug=True)
