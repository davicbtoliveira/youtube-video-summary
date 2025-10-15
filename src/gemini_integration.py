import os
from dotenv import load_dotenv
from google import genai
from pytubefix import YouTube

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def summarize_video(video_url, user_language):
    try:
        yt = YouTube(video_url)

        caption = None

        for lang_code in ['pt', 'en', 'es']:
            caption = yt.captions.get_by_language_code(lang_code)
            if caption:
                break

        if not caption:
            for lang_code in ['pt', 'en', 'es']:
                caption = yt.captions.get_by_language_code(f'a.{lang_code}')
                if caption:
                    break

        if not caption and len(yt.captions) > 0:
            caption = list(yt.captions.values())[0]
        
        if not caption:
            return "Error: No captions available for this video (manual or auto-generated)."
        
        transcript_text = caption.generate_srt_captions()
        
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Summarize this YouTube video transcript in {user_language}. Be the most concise you can, if you're going to display video times in the summary, please use only MM:SS format.\n\nTranscript:\n{transcript_text}"
        )
        
        return response.text
    
    except Exception as e:
        return f"Error: {str(e)}. The video may not have captions available."