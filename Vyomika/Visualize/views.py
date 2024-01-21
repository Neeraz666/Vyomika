from django.shortcuts import render, HttpResponse, redirect
from io import BytesIO
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import matplotlib.pyplot as plt
from .models import Visualize, FileVisualize
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
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

        currentuser = request.user

        visualize = Visualize(fname=fname, user = currentuser ,datas=datas, names=names)
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


@login_required
def visualizeFile(request):

    plot_functions = {
        "scatter": sns.scatterplot,
        "line": sns.lineplot,
        "bar": sns.barplot,
        "histogram": sns.histplot,
    }

    if request.method == "POST":
        file = request.FILES.get('fileUp')
        plottype = request.POST.get('plottype')
        xlabel = request.POST.get('xlabel')
        ylabel = request.POST.get('ylabel')

        df = pd.DataFrame(file)

        if plottype in plot_functions:
            plot_functions[plottype](x=xlabel, y=ylabel, data=df)
            plt.xlabel = xlabel
            plt.ylabel = ylabel

            image_buffer = BytesIO()
            plt.savefig(image_buffer, format='png')
            image_buffer.seek(0)

        currentuser = request.user

        filevisualize = FileVisualize(file=file, user = currentuser)
        filevisualize.save()

        filename = f'graph{filevisualize.num}.png'
        filevisualize.graph.save(filename, image_buffer)

@login_required
def filegraph(request, num):
    filedata = FileVisualize.objects.filter(num=num).first()
    url = filedata.graph.url

    return render(request, '', url)