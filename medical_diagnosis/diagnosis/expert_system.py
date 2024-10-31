from .rules import rules

class KnowledgeBase:
    def __init__(self, rules):
        self.rules = rules

    def get_conditions(self, symptoms):
        matching_conditions = []
        for condition, condition_symptoms in self.rules.items():
            if all(symptom in symptoms for symptom in condition_symptoms):
                matching_conditions.append(condition)
        return matching_conditions

class ExpertSystem:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def diagnose(self, symptoms):
        conditions = self.knowledge_base.get_conditions(symptoms)
        if conditions:
            return f"Possible conditions: {', '.join(conditions)}"
        else:
            return "No matching conditions found."
