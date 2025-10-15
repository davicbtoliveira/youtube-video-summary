import streamlit as st

def main():
    st.title("Youtube Videos Summary App")
    st.write("Welcome to the Youtube Videos Summary application!")
    
    st.markdown("""
    <style>
    .stButton>button {
        background-color: #FF0000 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.button("Send to Summarizer")

if __name__ == "__main__":
    main()