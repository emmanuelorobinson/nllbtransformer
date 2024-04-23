from flask import Flask, request, jsonify
from transformers import pipeline
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)

# Use a pipeline as a high-level helper
pipe = pipeline("translation", model="facebook/nllb-200-distilled-600M")

# Load model directly
# tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
# model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")


@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    source_text = data.get('source')
    target_lang = data.get('target', 'arb_Arab')
    source_lang = data.get('source_lang', 'eng_Latn')

    if not source_text:
        return jsonify({'error': 'Source text is required'}), 400

    try:
        # Use the pipeline for translation
        translation = pipe(source_text, tgt_lang=target_lang, src_lang=source_lang)[0]['translation_text']
        return jsonify({'translation': translation})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)