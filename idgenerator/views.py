from django.shortcuts import redirect, render
from django.views.generic import ListView
from .forms import DocForm
from request_da.request_data import get_data_from_form
from .models import Doc
from django.contrib import messages


class DocListView(ListView):
    model = Doc
    template_name = "ii.html"

    def get(self, request):
        form = DocForm()
        return render(request, 'ii.html', context={'form': form})

    def post(self, request):
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            done_image = get_data_from_form(form.cleaned_data)

            messages.success(request, 'Документ сгенерирован')
        return redirect(done_image)
