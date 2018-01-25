from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet, UserUtteranceReverted

class ActionDoDestructiveThingOne(Action):
    def name(self):
        return 'action_do_destructive_thing_one'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Doing destructive thing one")
        return []


class ActionDoDestructiveThingTwo(Action):
    def name(self):
        return 'action_do_destructive_thing_two'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Doing destructive thing two")
        return []


class ActionDoInconsequentialThing(Action):
    def name(self):
        return 'action_do_inconsequential_thing'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Doing an inconsequential thing that shouldn't be remembered")
        return [UserUtteranceReverted()]
