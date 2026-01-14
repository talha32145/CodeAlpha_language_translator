🌐 Multilingual Translator App

A Streamlit-based multilingual translation application powered by Facebook’s mBART Large-50 model via Hugging Face Inference API.
This app enables real-time translation between 50+ languages through a simple and intuitive interface.

🚀 Features
🌍 Multi-Language Support

Translate between 50+ global languages

Supports major languages like:

English, Urdu, Arabic, Hindi, French, Spanish, Chinese, German

Regional languages: Pashto, Bengali, Tamil, Telugu, Marathi, Nepali

European, Asian, African languages

🤖 AI-Powered Translation

Uses facebook/mbart-large-50-many-to-many-mmt

High-quality neural machine translation

Handles long and complex sentences

🎨 User-Friendly Interface

Clean Streamlit UI

Source & target language selection

Loading spinner during translation

Copy-ready translated output

⚡ Real-Time Processing

Fast response using Hugging Face API

Error handling for unavailable models or invalid input

🛠️ Tech Stack
Category	Tools
Language	Python
Frontend	Streamlit
Model	mBART-Large-50
API	Hugging Face Inference API
Networking	Requests
Deployment	Streamlit


⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/Multilingual-Translator.git
cd Multilingual-Translator

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Get Hugging Face API Key

Go to 👉 https://huggingface.co/settings/tokens

Create a Read Access Token

Replace in code:

API_KEY = "YOUR_API_KEY"


⚠️ Security Tip: Use environment variables instead of hardcoding API keys.

4️⃣ Run the App
streamlit run app.py

📦 Required Python Packages
streamlit
requests

🧠 How It Works

User selects source and target languages

Enters text to translate

Text is sent to Hugging Face Inference API

mBART model processes translation

Translated output is displayed instantly

🌐 Supported Languages (Examples)

English 🇬🇧

Urdu 🇵🇰

Arabic 🇸🇦

French 🇫🇷

German 🇩🇪

Spanish 🇪🇸

Chinese 🇨🇳

Japanese 🇯🇵

Hindi 🇮🇳

Pashto 🇦🇫

Turkish 🇹🇷

Bengali 🇧🇩
(and many more)

⚠️ Limitations

Requires active internet connection

Subject to Hugging Face API rate limits

Translation quality depends on model availability




⭐ Support & Contribution

If you like this project:

⭐ Star the repository

🍴 Fork & enhance

💬 Share feedback
