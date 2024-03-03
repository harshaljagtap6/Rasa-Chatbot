# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "common_function"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        called_intent = tracker.latest_message['intent']['name']
        if called_intent == "custom":
            dispatcher.utter_message(text="Custom called")
        elif called_intent == "custom2":
            dispatcher.utter_message(text="Custom 2 called")

        return []
    

# class CustomAction2(Action):

#     def name(self) -> Text:
#         return "custom_action_2"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="This is custom action 2.")

#         return []
