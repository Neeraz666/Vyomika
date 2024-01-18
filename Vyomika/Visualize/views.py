from django.shortcuts import render, HttpResponse, redirect
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import matplotlib.pyplot as plt
from .models import Visualize
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def createGraph(request):
    if request.method == 'POST':
        fname = request.POST.get('name')
        datas = request.POST.get('data')
        names = request.POST.get('names')
        file = request.FILES.get('fileUp')

        marks = datas.split(',')
        data_list = []
        name_list = names.split(',')

        for data in marks:
            data = data.strip()
            data_list.append(int(data))

        sns.set(style='darkgrid')
        plt.bar(name_list, data_list)
        plt.xlabel('Names')
        plt.ylabel('Marks')
        plt.title('Marks of students')

        image_buffer = BytesIO()
        plt.savefig(image_buffer, format='png')
        image_buffer.seek(0)

        visualize = Visualize(fname=fname, datas=datas, names=names, file=file)
        visualize.save()

        filename = f'graph{visualize.snum}.png'
        visualize.graph.save(filename, image_buffer)

        return redirect('displayGraph', snum=visualize.snum)

    return render(request, 'Visualize/data.html')

@login_required
def displayGraph(request, snum):
    data = Visualize.objects.filter(snum=snum).first()
    url = f'/media/graph{snum}.png'
    context = {'data': data, 'url':url}
    return render(request, 'Visualize/visualize.html', context)
