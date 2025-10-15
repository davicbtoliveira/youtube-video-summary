import streamlit as st
from pytubefix import YouTube
from pytubefix.cli import on_progress
import time

from gemini_integration import summarize_video

def main():
    st.title("Youtube Videos Summary App")
    st.write("Welcome to the Youtube Videos Summary application!")

    video_url = st.text_input("Enter YouTube video URL:")
    yt = YouTube(video_url, on_progress_callback=on_progress) if video_url else None
    video_title = yt.title if yt else "No video loaded"

    user_language = ["English", "PT-BR", "Spanish"]
    if 'language' not in st.session_state:
        st.session_state.language = "English"

    selected_language = st.selectbox("Select Language", user_language, index=user_language.index(st.session_state.language))
    st.session_state.language = selected_language

    st.markdown("""
    <style>
    .stButton>button {
        background-color: #FF0000 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    sumarizeButton = st.button("Summarize Video")

    if sumarizeButton:
        if not video_url or video_url.strip() == "":
            st.error("Please enter a valid YouTube video URL.")
        else:
            try:
                st.info(f"🔄 Processing video: **{video_title}**")
            except Exception as e:
                st.error(f"Error fetching video title: {str(e)}")
                st.info(f"🔄 Processing video: **{video_title}**")


            summary_placeholder = st.empty()

            summary_placeholder.markdown("""
            <div style="text-align: center; margin-top: 20px;">
                <span> Video summary will be displayed here in a few seconds</span>
                <span class="dot">.</span>
                <span class="dot">.</span>
                <span class="dot">.</span>
            </div>
            <style>
            .dot {
                animation: jump 1.5s infinite;
                display: inline-block;
            }
            .dot:nth-child(1) { animation-delay: 0s; }
            .dot:nth-child(2) { animation-delay: 0.5s; }
            .dot:nth-child(3) { animation-delay: 1s; }
            @keyframes jump {
                0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
                40% { transform: translateY(-5px); }
                60% { transform: translateY(-2px); }
            }
            </style>
            """, unsafe_allow_html=True)

            summary_text = summarize_video(video_url, selected_language)

            summary_placeholder.markdown(f"""
            <div style="text-align: center; margin-top: 20px; padding: 10px; border: 1px solid #ddd; border-radius: 5px;">
                <h3>Video Summary</h3>
                <p>{summary_text}</p>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()