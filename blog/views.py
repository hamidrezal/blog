from django.shortcuts import render
from django.views import View


# Components
    #1- Footer Components


class HomeScreenView(View):
    def get(self, request):
        return render(request, 'blog/index.html')

def header_component(request):
    return render(request, 'blog/components/header_component.html')

# Footer Components
def footer_component(request):
    return render(request,'blog/components/footer_component.html')