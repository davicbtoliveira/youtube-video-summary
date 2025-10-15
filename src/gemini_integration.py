import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi

import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def summarize_video(video_url):
    video_id = video_url.split("v=")[1].split("&")[0]
    
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    
    text = " ".join([item['text'] for item in transcript])
    
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = f"Summarize this YouTube video transcript: {text}. Be the most concise you can, if you're going to display video times in the summary, please use only MM:SS"
    
    response = model.generate_content(prompt)
    
    return response.text