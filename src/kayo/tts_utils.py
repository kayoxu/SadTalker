import os
import uuid

from gtts import gTTS
from datetime import datetime


def tts_gfile(data: str, lang='zh-cn', save_path='/ddata/ai/sd/tts/'):
    tts = gTTS(text=data, lang=lang)
    fileName = datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + uuid.uuid4() + '_tg.mp3'
    sp = os.path.join(save_path, fileName)
    tts.save(sp)
    return sp
