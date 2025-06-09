import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
from nltk.tag import pos_tag
import re

class EssayScorer:
    def __init__(self):
        # Download required NLTK data
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
        try:
            nltk.data.find('taggers/averaged_perceptron_tagger')
        except LookupError:
            nltk.download('averaged_perceptron_tagger')
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet')

    def analyze(self, essay_text):
        # Basic text preprocessing
        sentences = sent_tokenize(essay_text)
        words = word_tokenize(essay_text.lower())
        
        # Calculate various metrics
        metrics = {
            'word_count': len(words),
            'sentence_count': len(sentences),
            'avg_sentence_length': len(words) / len(sentences) if sentences else 0,
            'vocabulary_diversity': len(set(words)) / len(words) if words else 0,
            'grammar_score': self._check_grammar(essay_text),
            'structure_score': self._analyze_structure(sentences),
            'vocabulary_score': self._analyze_vocabulary(words)
        }
        
        # Calculate overall score (weighted average)
        weights = {
            'grammar_score': 0.3,
            'structure_score': 0.3,
            'vocabulary_score': 0.4
        }
        
        overall_score = sum(metrics[key] * weights[key] for key in weights.keys())
        
        # Generate feedback
        feedback = self._generate_feedback(metrics)
        
        # Convert scores to percentages
        metrics['grammar_score'] = round(metrics['grammar_score'] * 100, 2)
        metrics['structure_score'] = round(metrics['structure_score'] * 100, 2)
        metrics['vocabulary_score'] = round(metrics['vocabulary_score'] * 100, 2)
        
        return round(overall_score * 100, 2), feedback, metrics

    def _check_grammar(self, text):
        # Basic grammar check (placeholder - can be enhanced with more sophisticated checks)
        sentences = sent_tokenize(text)
        score = 0.7  # Base score
        
        # Check for basic sentence structure
        for sentence in sentences:
            words = word_tokenize(sentence)
            if len(words) > 3:  # Basic sentence length check
                score += 0.1
            if any(word[0].isupper() for word in words):  # Capitalization check
                score += 0.1
                
        return min(score, 1.0)

    def _analyze_structure(self, sentences):
        # Analyze essay structure
        if not sentences:
            return 0.0
            
        # Check for paragraph structure
        paragraphs = len(re.split(r'\n\s*\n', '\n'.join(sentences)))
        structure_score = min(paragraphs / 5, 1.0)  # Normalize to 1.0
        
        return structure_score

    def _analyze_vocabulary(self, words):
        # Analyze vocabulary complexity
        if not words:
            return 0.0
            
        # Count unique words and their complexity
        unique_words = set(words)
        complex_words = sum(1 for word in unique_words if len(word) > 6)
        
        vocabulary_score = (complex_words / len(unique_words)) * 0.7 + 0.3
        return min(vocabulary_score, 1.0)

    def _generate_feedback(self, metrics):
        feedback = []
        
        # Grammar feedback
        if metrics['grammar_score'] < 0.7:
            feedback.append("Consider reviewing grammar and punctuation.")
            
        # Structure feedback
        if metrics['structure_score'] < 0.6:
            feedback.append("Try to organize your essay into clear paragraphs.")
            
        # Vocabulary feedback
        if metrics['vocabulary_score'] < 0.6:
            feedback.append("Consider using more varied and sophisticated vocabulary.")
            
        # Length feedback
        if metrics['word_count'] < 200:
            feedback.append("Your essay is quite short. Consider expanding your ideas.")
        elif metrics['word_count'] > 1000:
            feedback.append("Your essay is quite long. Consider being more concise.")
            
        # Sentence length feedback
        if metrics['avg_sentence_length'] > 25:
            feedback.append("Some sentences are quite long. Consider breaking them into shorter ones.")
            
        return feedback 