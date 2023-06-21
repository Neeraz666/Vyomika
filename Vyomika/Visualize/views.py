from django.shortcuts import render, HttpResponse, redirect
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import matplotlib.pyplot as plt
from .models import Visualize

# Create your views here.

def createGraph(request):
    if request.method == 'POST':
        fname = request.POST.get('name')
        datas = request.POST.get('data')
        names = request.POST.get('names')

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

        filename = f'graph{Visualize.objects.count() + 1}.png'
        visualize = Visualize(fname=fname, datas=datas, names=names)
        visualize.save()
        visualize.graph.save(filename, image_buffer)

        return redirect('displayGraph', snum=visualize.snum)

    return render(request, 'Visualize/data.html')

def displayGraph(request, snum):
    data = Visualize.objects.filter(snum=snum).first()
    context = {'data': data}
    return render(request, 'Visualize/visualize.html', context)
