import json
import random
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Load questions from the JSON file
def load_questions():
    with open('questions.json', 'r', encoding='utf-8') as f:
        return json.load(f)

ALL_QUESTIONS = load_questions()

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Topic selection page
@app.route('/topics')
def topics():
    available_topics = list(ALL_QUESTIONS.keys())
    return render_template('topics.html', topics=available_topics)

# Quiz page
@app.route('/quiz/<topic>')
def quiz(topic):
    if topic not in ALL_QUESTIONS:
        return redirect(url_for('topics'))

    topic_questions = ALL_QUESTIONS[topic]
    random.shuffle(topic_questions)
    selected_questions = topic_questions[:15]

    session['current_quiz_questions'] = selected_questions
    session['current_quiz_topic'] = topic

    return render_template('quiz.html', questions=selected_questions, topic=topic)

# Submission and result page
@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    selected_questions = session.get('current_quiz_questions')
    topic = session.get('current_quiz_topic')

    if not selected_questions or not topic:
        return redirect(url_for('topics'))

    score = 0
    total_questions = len(selected_questions)
    results_detail = []

    for i, q_data in enumerate(selected_questions):
        user_answer = request.form.get(f'question_{i}', '').strip().lower()
        correct_answer = q_data['answer'].strip().lower()

        is_correct = user_answer == correct_answer
        if is_correct:
            score += 1

        results_detail.append({
            'question': q_data['question'],
            'user_answer': request.form.get(f'question_{i}', 'No answer'),
            'correct_answer': q_data['answer'],
            'is_correct': is_correct
        })

    return render_template('result.html',
                           topic=topic,
                           score=score,
                           total_questions=total_questions,
                           results_detail=results_detail)


