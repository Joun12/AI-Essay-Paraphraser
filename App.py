from transformers import BartForConditionalGeneration, BartTokenizer
import streamlit as st
from frontend import (
    set_page_config,
    apply_custom_css,
    render_header,
    render_layout,
    render_buttons,
    render_footer,
    clear_all
)

# Load BART model and tokenizer
@st.cache_resource
def load_model():
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)
    return model, tokenizer

def paraphrase_text(text, model, tokenizer):
    """Generate paraphrased text using the BART model"""
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    outputs = model.generate(
        inputs["input_ids"],
        max_length=1024,
        num_beams=5,
        early_stopping=True,
        no_repeat_ngram_size=2
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def main():
    # Initialize frontend
    set_page_config()
    apply_custom_css()
    render_header()
    
    # Load model
    model, tokenizer = load_model()
    
    # Render main layout and get user input
    text_input = render_layout()
    
    # Handle button clicks
    paraphrase_clicked, clear_clicked = render_buttons()
    
    if paraphrase_clicked:
        if text_input.strip() == "":
            st.warning("Please enter some text to paraphrase.")
        else:
            with st.spinner("Generating paraphrase..."):
                output_text = paraphrase_text(text_input, model, tokenizer)
                st.session_state.output_text = output_text
                st.rerun()
    
    if clear_clicked:
        clear_all()
        st.rerun()
    
    # Render footer
    render_footer()

if __name__ == "__main__":
    main()
