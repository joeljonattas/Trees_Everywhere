from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import PlantedTree
from .forms import LoginForm, AddPlantedTreeForm
from django.views.generic import CreateView
from rest_framework import viewsets, permissions
from .serializers import PlantedTreeSerializer

def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_trees')
    else:
        login_form = LoginForm()
    return render(request, 'accounts/login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def user_trees(request):
    trees = PlantedTree.objects.filter(user=request.user)
    return render(request, 'trees/user_trees.html', {'trees': trees})

@login_required
def tree_detail(request, id):
    tree = PlantedTree  .objects.get(id=id)
    return render(request, 'trees/tree_detail.html', {'tree': tree})

class PlantedTreeCreateView(CreateView):
    model = PlantedTree
    template_name = 'trees/add_tree.html'
    success_url = reverse_lazy('user_trees')
    form_class = AddPlantedTreeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class PlantedTreeApiView(viewsets.ModelViewSet):
    queryset = PlantedTree.objects.all()
    serializer_class = PlantedTreeSerializer
    permission_classes = [permissions.IsAuthenticated]

