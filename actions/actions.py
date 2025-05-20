from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionResumoConta(Action):
    def name(self) -> Text:
        return "utter_resumo_conta"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        nome = tracker.get_slot("nome")
        emprestimo = tracker.get_slot("emprestimo")
        portabilidade = tracker.get_slot("portabilidade")
        deposito = tracker.get_slot("deposito")

        dispatcher.utter_message(text=f"Conta criada com sucesso para {nome}.")
        dispatcher.utter_message(text=f"Portabilidade: {'sim' if portabilidade else 'não'}")
        dispatcher.utter_message(text=f"Empréstimo: {'sim' if emprestimo else 'não'}")
        dispatcher.utter_message(text=f"Valor depositado: R$ {deposito}")
        
        return []
