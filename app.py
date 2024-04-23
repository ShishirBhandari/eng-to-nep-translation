from flask import Flask, render_template, request

from transformers import pipeline
print('Loading model started')
translator = pipeline("translation", model="rujengelal/LMPT_project", src_lang="eng_Latn", tgt_lang="npi_Deva")
print('Loading model complete')
app = Flask(__name__)

def translate(text):
    return translator(text)[0]['translation_text']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def process_text():
    if request.method == 'POST':
        input_text = request.form['input_text']
        return render_template('result.html', input_text=translate(input_text))

if __name__ == '__main__':
    app.run(debug=True)
