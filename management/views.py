from django.shortcuts import render
from django.views import View


class ManagementView(View):
    def get(self, request):
        return render(request,'management/dashboard.html')







#Components
def nav_component(requset):
    return render(requset,'management/components/nav_component.html')


def sidenav_component(requset):
    return render(requset,'management/components/sidenav_component.html')