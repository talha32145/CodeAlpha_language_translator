import streamlit as st
import requests

API_KEY = "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"
API_URL = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

LANGUAGE_SELECTION = {
    "Arabic": "ar_AR",
    "Czech": "cs_CZ",
    "German": "de_DE",
    "English": "en_XX",
    "Spanish": "es_XX",
    "Estonian": "et_EE",
    "Finnish": "fi_FI",
    "French": "fr_XX",
    "Gujarati": "gu_IN",
    "Hindi": "hi_IN",
    "Italian": "it_IT",
    "Japanese": "ja_XX",
    "Kazakh": "kk_KZ",
    "Korean": "ko_KR",
    "Lithuanian": "lt_LT",
    "Latvian": "lv_LV",
    "Burmese": "my_MM",
    "Nepali": "ne_NP",
    "Dutch": "nl_XX",
    "Romanian": "ro_RO",
    "Russian": "ru_RU",
    "Sinhala": "si_LK",
    "Turkish": "tr_TR",
    "Vietnamese": "vi_VN",
    "Chinese": "zh_CN",
    "Afrikaans": "af_ZA",
    "Azerbaijani": "az_AZ",
    "Bengali": "bn_IN",
    "Farsi": "fa_IR",
    "Hebrew": "he_IL",
    "Croatian": "hr_HR",
    "Indonesian": "id_ID",
    "Georgian": "ka_GE",
    "Khmer": "km_KH",
    "Macedonian": "mk_MK",
    "Malayalam": "ml_IN",
    "Mongolian": "mn_MN",
    "Marathi": "mr_IN",
    "Polish": "pl_PL",
    "Pashto": "ps_AF",
    "Portuguese": "pt_XX",
    "Swedish": "sv_SE",
    "Swahili": "sw_KE",
    "Tamil": "ta_IN",
    "Telugu": "te_IN",
    "Thai": "th_TH",
    "Tagalog": "tl_XX",
    "Ukrainian": "uk_UA",
    "Urdu": "ur_PK",
    "Xhosa": "xh_ZA",
    "Galician": "gl_ES",
    "Slovene": "sl_SI"
}

def language_translator(user_input, source_lang, target_lang):
    payload = {
        "inputs": user_input,
        "parameters": {"src_lang": source_lang, "tgt_lang": target_lang}
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    try:
        return response.json()[0]["translation_text"]
    except Exception as e:
        st.error("⚠️ Translation failed. Please check input or model availability.")
        st.write(response.json())
        return None


st.set_page_config(page_title="🌐 Multilingual Translator", page_icon="🌍", layout="centered")

st.title("🌐 Multi Language Translator.")
st.markdown("Translate text between 50+ languages🚀")

col1, col2 = st.columns(2)

with col1:
    source_lang_name = st.selectbox("Select Source Language:", list(LANGUAGE_SELECTION.keys()), index=list(LANGUAGE_SELECTION.keys()).index("English"))
with col2:
    target_lang_name = st.selectbox("Select Target Language:", list(LANGUAGE_SELECTION.keys()), index=list(LANGUAGE_SELECTION.keys()).index("Urdu"))

text_to_translate = st.text_area("✍️ Enter Text to Translate:", placeholder="Type your text here...")

if st.button("🔁 Translate"):
    if text_to_translate.strip():
        with st.spinner("Translating... ⏳"):
            translated_text = language_translator(
                text_to_translate,
                LANGUAGE_SELECTION[source_lang_name],
                LANGUAGE_SELECTION[target_lang_name]
            )
        if translated_text:
            st.success("✅ Translation Complete!")
            st.text_area("🌍 Translated Text:", translated_text, height=150)
    else:
        st.warning("⚠️ Please enter some text before translating.")

st.markdown("---")
st.caption("Created by Muhammad Talha ✨")

