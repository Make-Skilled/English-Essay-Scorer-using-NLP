from flask import Blueprint, render_template, request, jsonify
from app.models.essay_scorer import EssayScorer

main = Blueprint('main', __name__)
essay_scorer = EssayScorer()

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@main.route('/analyze', methods=['POST'])
def analyze_essay():
    data = request.get_json()
    essay_text = data.get('essay', '')
    
    if not essay_text:
        return jsonify({'error': 'No essay provided'}), 400
    
    # Analyze the essay
    score, feedback, metrics = essay_scorer.analyze(essay_text)
    
    return jsonify({
        'score': score,
        'grammar_score': metrics['grammar_score'],
        'vocabulary_score': metrics['vocabulary_score'],
        'structure_score': metrics['structure_score'],
        'feedback': feedback
    }) 