import os
from dotenv import load_dotenv
from google import genai
from pytubefix import YouTube
import re

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
        r'(?:embed\/)([0-9A-Za-z_-]{11})',
        r'(?:watch\?v=)([0-9A-Za-z_-]{11})'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def summarize_video(video_url, user_language):
    try:
        yt = YouTube(video_url)
        
        # Get all available captions
        available_captions = yt.captions
        
        if not available_captions:
            return "Error: No captions available for this video."
        
        caption = None
        
        # Priority order: manual captions in preferred languages
        for lang_code in ['pt', 'en', 'es', 'pt-BR', 'en-US', 'en-GB']:
            if lang_code in available_captions:
                caption = available_captions[lang_code]
                break
        
        # If no manual captions, try auto-generated
        if not caption:
            for lang_code in ['a.pt', 'a.en', 'a.es', 'a.pt-BR', 'a.en-US']:
                if lang_code in available_captions:
                    caption = available_captions[lang_code]
                    break
        
        # If still no caption, get the first available one
        if not caption:
            caption_keys = list(available_captions.keys())
            if caption_keys:
                caption = available_captions[caption_keys[0]]
        
        if not caption:
            return "Error: Could not retrieve captions from this video."
        
        # Get the transcript text (remove SRT formatting)
        transcript_srt = caption.generate_srt_captions()
        
        # Remove timestamps and formatting from SRT
        lines = transcript_srt.split('\n')
        transcript_text = []
        for line in lines:
            # Skip line numbers and timestamps
            if not line.strip().isdigit() and '-->' not in line and line.strip():
                transcript_text.append(line.strip())
        
        transcript_text = ' '.join(transcript_text)
        
        if not transcript_text:
            return "Error: Transcript is empty."
        
        # Generate summary with Gemini
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Summarize this YouTube video transcript in {user_language}. Be the most concise you can, if you're going to display video times in the summary, please use only MM:SS format.\n\nTranscript:\n{transcript_text}"
        )
        
        return response.text
    
    except Exception as e:
        return f"Error: {str(e)}"