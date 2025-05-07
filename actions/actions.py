from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRegistrarCompra(Action):
    def name(self):
        return "action_registrar_compra"

    def run(self, dispatcher, tracker, domain):
        produto = tracker.get_slot("produto")
        dispatcher.utter_message(text=f"Compra do {produto} registrada!")
        return []
