# 🎥 AI YouTube Video Summarizer

A powerful web application that leverages AI to generate concise summaries of YouTube videos in multiple languages. Built with Streamlit and powered by Google's Gemini AI.

## 📋 Overview

This application extracts transcripts from YouTube videos (both manual and auto-generated captions) and uses Google's Gemini 2.5 Flash model to generate intelligent, concise summaries. Perfect for quickly understanding video content without watching the entire video.

## ✨ Features

- **Multi-language Support**: Generate summaries in English, Portuguese (PT-BR), and Spanish
- **Automatic Caption Detection**: Works with both manual and auto-generated YouTube captions
- **Smart Summarization**: Uses Google Gemini AI for context-aware, concise summaries
- **Time-stamped Summaries**: Optional timestamps in MM:SS format for easy reference
- **User-friendly Interface**: Clean, intuitive Streamlit-based web interface
- **Real-time Processing**: Visual feedback during video processing

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Google Gemini API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/davicbtoliveira/youtube-video-summary.git
cd youtube-video-summary
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

4. Run the application:
```bash
streamlit run src/app.py
```

## 📦 Dependencies

- **streamlit**: Web application framework
- **pytubefix**: YouTube video information and caption extraction
- **google-genai**: Google Gemini AI integration
- **youtube-transcript-api**: Backup transcript extraction
- **python-dotenv**: Environment variable management

## 🎯 How It Works

1. **Input**: User provides a YouTube video URL
2. **Caption Extraction**: The app extracts available captions (manual or auto-generated)
3. **AI Processing**: Transcript is sent to Google Gemini AI for summarization
4. **Output**: Concise summary displayed in the selected language

## 🔧 Technical Architecture

```
AI-sumary/
├── src/
│   ├── app.py                 # Main Streamlit application
│   └── gemini_integration.py  # AI integration and caption extraction
├── .env                       # Environment variables (API keys)
├── requirements.txt           # Project dependencies
└── README.md                 # Project documentation
```

## 🌟 Use Cases

- **Students**: Quickly review educational content
- **Researchers**: Extract key points from conference talks
- **Content Creators**: Analyze competitor videos
- **Professionals**: Stay updated with industry content efficiently
- **Language Learners**: Get summaries in preferred language

## 🔐 Privacy & Security

- API keys are stored securely in `.env` files
- No video content is stored permanently
- Transcripts are processed in real-time and not cached

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## ⚠️ Limitations

- Requires videos to have captions (manual or auto-generated)
- Summary quality depends on transcript accuracy
- API rate limits may apply based on your Gemini API plan

## 🙏 Acknowledgments

- Google Gemini AI for powerful language processing
- Streamlit for the amazing web framework
- PyTubeFix community for YouTube integration

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.