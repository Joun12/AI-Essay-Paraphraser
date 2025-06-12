import streamlit as st

def set_page_config():
    """Set the page configuration"""
    st.set_page_config(
        page_title="AI Essay Paraphraser",
        page_icon="📝",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

def apply_custom_css():
    """Apply custom CSS styling"""
    st.markdown("""
        <style>
        /* Main container styling */
        .main {
            padding: 2rem;
            background-color: #f8f9fa;
        }
        
        /* Title styling */
        h1 {
            color: #2c3e50;
            font-size: 2.5rem !important;
            font-weight: 700 !important;
            margin-bottom: 1rem !important;
            text-align: center;
        }
        
        /* Subheader styling */
        h3 {
            color: #34495e;
            font-size: 1.5rem !important;
            font-weight: 600 !important;
            margin-bottom: 1rem !important;
        }
        
        /* Text area styling */
        .stTextArea textarea {
            font-size: 16px;
            border-radius: 10px;
            border: 2px solid #e0e0e0;
            padding: 15px;
            background-color: white;
            transition: border-color 0.3s ease;
        }
        
        .stTextArea textarea:focus {
            border-color: #3498db;
            box-shadow: 0 0 0 1px #3498db;
        }
        
        /* Button styling */
        .stButton button {
            width: 100%;
            margin: 10px 0;
            padding: 12px;
            font-size: 16px;
            font-weight: 600;
            border-radius: 8px;
            border: none;
            transition: all 0.3s ease;
        }
        
        /* Paraphrase button */
        .stButton button:first-child {
            background-color: #3498db;
            color: white;
        }
        
        .stButton button:first-child:hover {
            background-color: #2980b9;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        /* Clear button */
        .stButton button:last-child {
            background-color: #e74c3c;
            color: white;
        }
        
        .stButton button:last-child:hover {
            background-color: #c0392b;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        /* Result box styling */
        .result-box {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
            border: 2px solid #e0e0e0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        /* Info message styling */
        .stInfo {
            background-color: #e8f4f8;
            border-radius: 10px;
            padding: 15px;
            border: 1px solid #b3e0ff;
        }
        
        /* Warning message styling */
        .stWarning {
            background-color: #fff3cd;
            border-radius: 10px;
            padding: 15px;
            border: 1px solid #ffeeba;
        }
        
        /* Tips section styling */
        .tips-section {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            border: 1px solid #e9ecef;
        }
        
        /* Divider styling */
        hr {
            border: none;
            height: 1px;
            background-color: #e0e0e0;
            margin: 2rem 0;
        }
        
        /* Column styling */
        .stColumn {
            padding: 0 15px;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    """Render the header section"""
    st.title("📝 AI Essay Paraphraser")
    st.markdown(
        "<div style='text-align: center; color: #666; margin-bottom: 2rem;'>"
        "Transform your text into a fresh, rephrased version while maintaining its original meaning."
        "</div>",
        unsafe_allow_html=True
    )

def render_input_section():
    """Render the input section"""
    st.subheader("Input Text")
    if 'input_text' not in st.session_state:
        st.session_state.input_text = ""
    
    return st.text_area(
        "Enter your paragraph here:",
        value=st.session_state.input_text,
        height=200,
        placeholder="Type or paste your text here...",
        key="input_text_area"
    )

def render_output_section():
    """Render the output section"""
    st.subheader("Paraphrased Output")
    if 'output_text' not in st.session_state:
        st.session_state.output_text = ""
    
    if st.session_state.output_text:
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.write(st.session_state.output_text)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("Your paraphrased text will appear here.")

def render_buttons():
    """Render the action buttons"""
    col3, col4 = st.columns(2)
    with col3:
        paraphrase_clicked = st.button("🔄 Paraphrase", use_container_width=True)
    with col4:
        clear_clicked = st.button("🗑️ Clear All", use_container_width=True)
    return paraphrase_clicked, clear_clicked

def render_footer():
    """Render the footer section with tips"""
    st.markdown("---")
    st.markdown(
        "<div class='tips-section'>"
        "<h3 style='color: #2c3e50; margin-bottom: 1rem;'>💡 Tips</h3>"
        "<ul style='color: #666;'>"
        "<li>Keep your input text clear and well-structured for better results</li>"
        "<li>The model works best with paragraphs of moderate length</li>"
        "<li>You can paraphrase multiple times to get different variations</li>"
        "</ul>"
        "</div>",
        unsafe_allow_html=True
    )

def render_layout():
    """Render the main layout"""
    # Create two columns for input and output
    col1, col2 = st.columns(2)
    
    with col1:
        text_input = render_input_section()
        st.session_state.input_text = text_input
    
    with col2:
        render_output_section()
    
    return text_input

def clear_all():
    """Clear both input and output text"""
    st.session_state.input_text = ""
    st.session_state.output_text = "" 