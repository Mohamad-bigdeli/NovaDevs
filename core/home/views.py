from django.shortcuts import render
from django.views import generic
from .models import Member, Service

# Create your views here.

class Index(generic.ListView):
    
    model = Member
    template_name = "index/index.html"
    context_object_name = "members"

    def get_context_data(self, **kwargs):
        kwargs["services"] = Service.objects.all()
        return super().get_context_data(**kwargs)

class MemberDetail(generic.DeleteView):
    model = Member
    context_object_name = "member"
    template_name = "detail/member_detail.html"