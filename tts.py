from gtts import gTTS
import os
import streamlit as st 
import time


# Header 

gTTS(":orange[Hello, I'm binny, Your text to speech converter]",lang='en')
os.system("afplay intro.mp3")

st.set_page_config(page_title="NLP - project on Text to Speech conversion", page_icon="mic", layout="wide", initial_sidebar_state="expanded")

st.header(" :orange[Hello 👋, I'm Binny, an NLP model to convert text to speech 🤖 ]")

# Text to convert to speech
text = st.text_area(label='Text content',height=400, placeholder="Binny :\n\nI'm an NLP model who can help you convert your english text to five different langaue tones,You can write anything here, and I'll convert it to speech.Choose your preferred language from the dropdown list to hear the text spoken in that language, and also don't forget to convert the speech file to an audio file to download and use it for own purpose. . .")

# background picture 
# CSS code snippet for background image properties
pg_bg =  """
<style>
[data-testid="stAppViewContainer"]{
background-image: url('https://cdn.pixabay.com/photo/2022/06/08/05/47/stars-7249785_1280.jpg');
background-size: cover;
}
</style> """

# st.markdown(pg_bg,unsafe_allow_html=True)

lang_list = ['English (Australia)', 'English (United Kingdom)', 'English (United States)', 'English (Canada)', 
             'English (India)', 'English (Ireland)', 'English (South Africa)', 'French (Canada)', 
             'French (France)', 'Mandarin (China Mainland)', 'Mandarin (Taiwan)', 'Portuguese (Brazil)', 
             'Portuguese (Portugal)', 'Spanish (Mexico)', 'Spanish (Spain)', 'Spanish (United States)']
st.expander("select language")
language = st.selectbox(label = 'Select the language ',options=lang_list)
val = lang_list.index(language)

code = ['en', 'en', 'en', 'en', 'en', 'en', 'en', 'fr', 'fr', 'zh-CN', 'zh-TW', 'pt', 'pt', 'es', 'es', 'es']

lang_code = code[val]

# Create a gTTS object

if len(text) > 3:
    if st.button(label= "Convert the text to speech"):
        tts = gTTS(text, lang=lang_code)
        tts.save("output.mp3")
        print("enteredt 2 ")
        os.system("afplay output.mp3")
if len(text) > 3:
    if st.button(label='Create an audio file'):
        time.sleep(3)
        with st.status("Converted Successfully !!! ✅"):
            for i in range(0,1000):
                pass
        with open("output.mp3", "rb") as file:
            st.download_button(
            label="Download audio file",
            data=file,
            file_name='audio_file.mp3',
            mime='audio/mp3')



st.expander("This model is from an opensource library ")
# Save the audio file
# tts.save("output.mp3")

# Play the audio file (Linux/Mac)
# os.system("afplay output.mp3")  # On Mac
# os.system("aplay output.mp3")  # On Linux