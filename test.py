from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("Running test.py...")

# Use a pipeline as a high-level helper
pipe = pipeline("translation", model="facebook/nllb-200-distilled-600M")


# source_text = data.get('source')
# target_lang = data.get('target', 'arb_Arab')
# source_lang = data.get('source_lang', 'eng_Latn')
source_text = ("<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body>\n<p>This chapter describes some of the communication "
               "tools and methods used by Department project team members. Stakeholders must choose appropriate tools "
               "and methods to accomplish the communication task at hand.</p>\n</body>\n</html>")

target_lang = 'arb_Arab'
source_lang = 'eng_Latn'

if not source_text:
    # return jsonify({'error': 'Source text is required'}), 400
    print('Source text is required')
try:
    # Use the pipeline for translation
    translation = pipe(source_text, tgt_lang=target_lang, src_lang=source_lang)[0]['translation_text']
    # return jsonify({'translation': translation})
    print({'translation': translation})
except Exception as e:
    # return jsonify({'error': str(e)}), 500
    print({'error': str(e)})