from random import randint
from zipfile import ZipFile
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View, ListView
from .forms import DocForm
from request_da.request_data import get_data_from_form
from pathlib import Path
from plow.plow import creator_archive
from django.http import FileResponse


class DocListView(ListView):
    form_class = DocForm
    template_name = "ii.html"

    def get(self, request):
        form = DocForm()
        return render(request, 'ii.html', context={'form': form})

    def post(self, request):
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            done_image = get_data_from_form(form.cleaned_data)
            needs_file = Path(done_image).absolute()
            response = FileResponse(open(done_image, 'rb'))
            return response
            # print(needs_file)
            # archive = creator_archive(needs_file)
            # response = HttpResponse(archive, content_type="application/zip")
            # return response
        # return render(request, 'return_doc.html', context={'img': done_image})
