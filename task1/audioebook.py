# ======     14-10-2026 ======

from pypdf import PdfReader
from gtts import gTTS
tts=gTTS('hii this is Padmasri',lang='en')
tts.save('hello.mp3')