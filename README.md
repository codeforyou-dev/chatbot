# Simple Chatbot

A lightweight conversational AI built with Hugging Face's BlenderBot and deployed using Streamlit. This chatbot, named "Grok," is designed to provide simple, engaging responses while maintaining a consistent AI identity.

## Features
- **Conversational AI**: Powered by `facebook/blenderbot-400M-distill`, a distilled version of BlenderBot for efficient dialogue generation.
- **Custom Identity**: Responds as "Grok, created by xAI," with filters to prevent unwanted persona details (e.g., jobs, pets).
- **Specific Query Handling**: Recognizes and answers queries like:
  - "What's your name?" → "I’m Grok, created by xAI."
  - "What time is it?" → Provides the current time.
  - "Where are you?" → "I’m Grok, an AI, so I exist in the cloud."
  - "What’s the latest updates?" → Offers to search the web or X (search implementation pending).
- **Context Awareness**: Maintains a short conversation history (last 3 messages) to improve response relevance.
- **Interactive UI**: Simple chat interface with real-time updates via Streamlit.

## Prerequisites
- Python 3.8+
- Required libraries:
  - `transformers` (Hugging Face)
  - `torch` (PyTorch for model inference)
  - `streamlit`

## Installation
1. **Clone the Repository** (if hosted on GitHub/GitLab):
   ```bash
   git clone <repository-url>
   cd simple-chatbot

## Limitations
    BlenderBot may occasionally generate off-topic responses due to its training data, though filters minimize this.
    No persistent memory beyond 3 messages—future enhancements could use a database.
    Search functionality is offered but not yet implemented.
## Credits
    Built with Streamlit.
    Powered by Hugging Face Transformers.
    Inspired by xAI’s Grok, developed with assistance from Grok 3.

## Future Enhancements
    Integrate web/X search using an API (e.g., Google Search, X API).
    Add support for more custom queries (e.g., weather, news).
    Improve UI with Streamlit components or custom styling.
    Fine-tune BlenderBot for a more "Grok-like" personality.