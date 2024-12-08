from django.shortcuts import render
from django.views import View
from jarvischef.forms import ReciepeForm
from .groq import get_chat_response  # Import your Groq function

# Create your views here.

class home(View):
    def get(self,request):
        form = ReciepeForm()
        return render(request,"masterchef/index.html",{"form":form})
    
    def post(self,request):
        form = ReciepeForm(request.POST)
        if form.is_valid():
            reciepe_form= form.cleaned_data['reciepe_message']
            # print(reciepe_form)
            response = get_chat_response(reciepe_form)

        return render(request,"masterchef/index.html",{"form":form,"response":response})
    

