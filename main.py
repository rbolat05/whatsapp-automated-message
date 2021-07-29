from scraper import sender
from preprocessor import Preprocessor
from file_reader import reader
from bot_settings import phones_filetype

if __name__ == '__main__':

    with open('message.txt', encoding='utf8') as f:
        msg = f.read()
    msg = msg.split('\n')

    phones_list = reader(phones_filetype)
    phones_list_prep = list(map(Preprocesser.tr, phones_list))

    sender(msg, phones_list_prep)

