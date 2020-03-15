# 英語から日本語翻訳するクラス
from googletrans import Translator

class text_trans:
    def __init__(self,en_text):
        self.translator = Translator()
        self.en_text = en_text

    def Trans(self):
        ja_text = self.translator.translate(self.en_text, src="en", dest="ja").text
        return ja_text
