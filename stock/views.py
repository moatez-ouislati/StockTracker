from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, StockUpViewForm
from .models import StockItem, Category
from stock_tracker.settings import LOW_QUANTITY
from django.contrib import messages

class Index(TemplateView):
    template_name = 'stock/index.html'
    
class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        
        items = StockItem.objects.filter(user=self.request.user.id).order_by('id')
        low_stock = StockItem.objects.filter(
            user=self.request.user.id,
            quantity__lte = LOW_QUANTITY
        )
        
        if low_stock .count() > 0:
            if low_stock.count() > 1:
                messages.error(request, f'{low_stock.count()} Stock running low for this item!')
                
            else:
                messages.error(request, f'{low_stock.count()} Stock running low for this item!')
                
        low_stock_id = StockItem.objects.filter(
            user = self.request.user.id,
            quantity__lte = LOW_QUANTITY
        ).values_list('id', flat=True)
                
        return render(request, 'stock/dashboard.html', {'items':items, 'low_stock_id':low_stock_id})

class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'stock/signup.html', {'form': form})
        
    def post(self, request):
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            
            login(request, user)
            return redirect('index')
        
        return render(request, 'stock/signup.html', {'form':form})

class AddItem(LoginRequiredMixin, CreateView):
    model         = StockItem
    form_class    = StockUpViewForm
    template_name = 'stock/item_form.html'
    success_url   = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class EditItem(LoginRequiredMixin, UpdateView):
    
    model         = StockItem
    form_class    = StockUpViewForm
    template_name = 'stock/item_form.html'
    success_url   = reverse_lazy('dashboard')
    
class DeleteItem(LoginRequiredMixin, DeleteView):
    model               = StockItem
    template_name       = 'stock/delete_item.html'
    success_url         = reverse_lazy('dashboard')
    context_object_name = 'item'
    
    
