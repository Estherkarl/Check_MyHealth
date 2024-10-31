from django.shortcuts import render
from .forms import SymptomsForm
from .expert_system import ExpertSystem, KnowledgeBase
from .rules import rules

# Initialize the expert system with rules
knowledge_base = KnowledgeBase(rules)
expert_system = ExpertSystem(knowledge_base)

def home(request):
    return render(request, 'home.html')

def symptoms_info(request):
    return render(request, 'symptoms_info.html', {'rules': rules})

def diagnose_view(request):
    if request.method == 'POST':
        form = SymptomsForm(request.POST)
        if form.is_valid():
            symptoms_input = form.cleaned_data['symptom']
            symptoms = [symptom.strip() for symptom in symptoms_input.split(',')]
            result = expert_system.diagnose(symptoms)
            return render(request, 'diagnosis/result.html', {'result': result})
    else:
        form = SymptomsForm()
    
    return render(request, 'diagnosis/form.html', {'form': form})
