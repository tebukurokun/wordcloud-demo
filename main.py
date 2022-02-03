import numpy as np
import os
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from janome.tokenizer import Tokenizer
import re

FONT_PATH = "/Users/tebukuro/Library/Fonts/ipaexg.ttf"  # FIXME
FILE_NAME = 'sample'


def main():
    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    text = open(path.join(d, f'{FILE_NAME}.txt')).read()

    word_str = get_word_str(text)

    wc = WordCloud(font_path=FONT_PATH, max_font_size=40).generate(word_str)

    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()

    wc.to_file(FILE_NAME + ".png")


def get_word_str(text):
    t = Tokenizer()
    token = t.tokenize(text)
    word_list = []

    for line in token:
        tmp = re.split('\t|,', str(line))
        if tmp[1] in ["名詞"]:
            if tmp[2] in ["一般", "固有名詞"]:
                word_list.append(tmp[0])

    return " ".join(word_list)


if __name__ == '__main__':
    main()
