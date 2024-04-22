
import streamlit as st

from transformers import pipeline
print('Loading model started')
translator = pipeline("translation", model="rujengelal/LMPT_project", src_lang="eng_Latn", tgt_lang="npi_Deva")
print('Loading model complete')

def translate(text):
    return translator(text)[0]['translation_text']


def read_text_file(uploaded_file):
    if uploaded_file is not None:
        text = uploaded_file.getvalue().decode("utf-8")
        return text
    return ""

def main():
    st.title("Text Reader App")
    st.write("Enter text to be translated")

    # Text input
    input_text = st.text_area("Enter text:")
    # Button to display entered text
    if st.button("Translate Text"):
        if input_text.strip():
            st.write("Entered text is translated to:")
            st.write(translate(input_text))
        else:
            st.warning("Please enter some text.")


main()
