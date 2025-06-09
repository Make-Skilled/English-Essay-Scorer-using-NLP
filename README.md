# English Essay Scorer using NLP

An intelligent system that evaluates and scores English essays using Natural Language Processing (NLP) techniques. The system analyzes grammar, vocabulary, and structure to provide comprehensive scores and feedback.

## Features

- Essay scoring based on multiple criteria
- Grammar and spelling analysis
- Vocabulary assessment
- Structural analysis
- Detailed feedback and suggestions
- Modern and responsive web interface
- Real-time scoring dashboard

## Tech Stack

- **Backend**: Python, Flask
- **NLP Libraries**: NLTK, Scikit-learn
- **Frontend**: HTML, CSS, Tailwind CSS
- **Database**: SQLite (for storing essays and scores)

## Project Structure

```
english-essay-scorer/
├── app/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   │   ├── index.html
│   │   └── dashboard.html
│   ├── models/
│   │   └── essay_scorer.py
│   └── __init__.py
├── requirements.txt
└── run.py
```

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download NLTK data:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('averaged_perceptron_tagger')
   nltk.download('wordnet')
   ```
5. Run the application:
   ```bash
   python run.py
   ```

## Usage

1. Open your browser and navigate to `http://localhost:5000`
2. On the landing page, you can learn about the system's features
3. Navigate to the dashboard to submit and score essays
4. View detailed analysis and feedback for each essay

## Contributing

Feel free to submit issues and enhancement requests!