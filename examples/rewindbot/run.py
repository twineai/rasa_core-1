#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.realpath(os.path.join(script_dir, "..", "..")))

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter

def run_bot(serve_forever=True):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(script_dir)

    agent = Agent.load("models/dialogue",
                       interpreter=RegexInterpreter())

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")
    run_bot()
