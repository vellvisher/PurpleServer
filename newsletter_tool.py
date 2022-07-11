#!/usr/bin/python3

import argparse
from state_pb2 import State
from state_pb2 import Newsletter
from state_pb2 import Provider
from datetime import datetime
from google.protobuf import text_format
from bs4 import BeautifulSoup

def parse_parameters():
    parser = argparse.ArgumentParser("newsletter_tool")
    parser.add_argument("html", help="HTML file with newsletter content", type=str)
    args = parser.parse_args()
    assert(args.html.endswith(".html"))
    return args.html

def process_brew_html(html_string: str):
    soup = BeautifulSoup(html_string, 'html.parser')

def create_state(html_file: str):
    state = State()
    state.newsletters.extend([create_newsletter(html_file = html_file)])
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
    html_file = parse_parameters()
    state = create_state(html_file)
    write_state(state)
