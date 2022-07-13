#!/usr/bin/python3

from bs4 import BeautifulSoup
from datetime import datetime
from google.protobuf import text_format
from state_pb2 import Newsletter
from state_pb2 import Provider
from state_pb2 import State
from typing import List
import argparse
import glob
import os

"""
  Returns directory of files.
"""
def parse_parameters() -> str:
    parser = argparse.ArgumentParser("newsletter_tool")
    parser.add_argument("html_dir", help="Directory with html files", type=str)
    args = parser.parse_args()
    assert(not os.path.isfile(args.html_dir))
    return args.html_dir

def glob_files(html_dir: str) -> List[str]:
    files = sorted(glob.glob(html_dir + '/*' + 'html'))
    return files

def process_brew_html(html_string: str):
    soup = BeautifulSoup(html_string, 'html.parser')

def create_state(html_files: List[str]):
    state = State()
    state.newsletters.extend([create_newsletter(html_file) for html_file in html_files])
    state.newsletters[0].widget_articles.extend(create_articles())
    return state

def create_newsletter(html_file):
    newsletter = Newsletter()
    newsletter.provider = Provider.BREW
    newsletter.newsletter_url = "https://raw.githubusercontent.com/vellvisher/PurpleServer/main/" + html_file
    newsletter.upload_time = int(datetime.now().timestamp())
    return newsletter

def create_articles():
    article = Newsletter.Article()
    article.title = "Elon Musk officially tries to abandon Twitter deal"
    article.body = "We’re going to Delaware."
    article.image_url = "https://images.morningbrew.com/gif/2022-04-14/image-1c127e5a8f34be3132cbcb488b1128520128a9e6-480x269-gif/giphy(1).webp"
    return [article]

def write_state(state: State):
    state_text_proto = text_format.MessageToString(state)
    out_file = open("state.textpb", "w+")
    out_file.write(state_text_proto)
    out_file.close()

if __name__ == '__main__':
    html_dir = parse_parameters()
    html_files = glob_files(html_dir)
    state = create_state(html_files)
    write_state(state)
