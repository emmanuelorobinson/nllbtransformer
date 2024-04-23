# Facebook Translation Model Experimentation

This repository contains code for experimenting with Facebook's translation model using the Hugging Face Transformers library and Flask web framework.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone this repository or create a new project directory.
2. Install the required Python packages:

```bash
pip install transformers flask
pip install 'transformers[torch]'
pip install 'transformers[tf-cpu]'
pip install 'transformers[flax]'
```

## Usage

```bash
python app.py
```

This will start a Flask server on `http://localhost:5000/`. You can access the translation model by sending a POST request to `http://localhost:5000/translate` with the following JSON payload:

```json
{
    "text": "Hello, how are you?",
    "source_lang": "arb_Arab",
    "target": "eng_Latn"
}
```

- source_lang: The text to be translated.
- target: (optional): The target language code (e.g., arb_Arab for Arabic). Default is arb_Arab.
- source_lang (optional): The source language code (e.g., eng_Latn for English). Default is eng_Latn.

The server will return a JSON response with the translated text:

```json
{
    "translation": "مرحبًا، كيف حالك؟"
}
```

## Code Explanation

The provided code sets up a Flask application with a single route /translate that accepts POST requests.

1. The transformers library is imported, and the pipeline function is used to load the pre-trained Facebook translation model (facebook/nllb-200-distilled-600M).
2. The /translate route accepts JSON data containing the source text, target language, and source language.
3. If the source text is not provided, an error message is returned.
4. The pipe function from the Hugging Face Transformers library is called with the provided source text, target language, and source language to perform the translation.
5. The translated text is returned as a JSON response.
6. If an exception occurs during the translation process, an error message is returned.

## Note
The provided code assumes that you have installed the necessary dependencies, including the Hugging Face Transformers library and Flask. If you encounter any issues related to missing dependencies, please make sure to install them using pip before running the application.