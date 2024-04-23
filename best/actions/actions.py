from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionModuleInfo(Action):
    def name(self) -> Text:
        return "action_module_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        module = tracker.get_slot("module")

        if module:
            # Provide information about the specified module
            # You can fetch this from a database or API
            response = f"The {module} module covers topics such as [...]. It is assessed through [...] and has learning outcomes including [...]."
        else:
            response = "I'm sorry, I didn't catch which module you were asking about. Could you please provide the module name?"

        dispatcher.utter_message(text=response)

        return []

class ActionGeneralQuestion(Action):
    def name(self) -> Text:
        return "action_general_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Implement logic to handle general questions
        # You can use a knowledge base or FAQ lookup here
        response = "I'm afraid I don't have a specific answer to that question. Please check the University's website or contact the admissions team for more information."

        dispatcher.utter_message(text=response)

        return []





