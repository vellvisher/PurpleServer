#!/usr/bin/python3

import argparse
from state_pb2 import State
from state_pb2 import Newsletter
from state_pb2 import Provider
from datetime import datetime
from google.protobuf import text_format

parser = argparse.ArgumentParser("newsletter_tool")
parser.add_argument("html", help="HTML file with newsletter content", type=str)
args = parser.parse_args()
assert(args.html.endswith(".html"))

state = State()

newsletter = state.newsletters.add()
newsletter.provider = Provider.BREW
newsletter.newsletter_url = "https://raw.githubusercontent.com/vellvisher/PurpleServer/main/" + args.html
newsletter.upload_time = int(datetime.now().timestamp())
state_text_proto = text_format.MessageToString(state)

out_file = open("state.textpb", "w+")
out_file.write(state_text_proto)
out_file.close()
