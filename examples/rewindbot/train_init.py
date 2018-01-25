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
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy


if __name__ == '__main__':
    os.chdir(script_dir)

    utils.configure_colored_logging(loglevel="INFO")

    training_data_file = 'stories.md'
    model_path = 'models/dialogue'

    agent = Agent("domain.yml",
                  policies=[KerasPolicy()])

    agent.train(
            training_data_file,
            augmentation_factor=50,
            max_history=2,
            epochs=500,
            batch_size=10,
            validation_split=0
    )

    agent.persist(model_path)
