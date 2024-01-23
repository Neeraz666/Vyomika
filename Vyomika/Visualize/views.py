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






"""   FOR FILES   """
@login_required
def visualizeFile(request):

    # plot_functions = {
    #     "scatter": sns.scatterplot,
    #     "line": sns.lineplot,
    #     "bar": sns.barplot,
    #     "histogram": sns.histplot,
    # }

    if request.method == "POST":
        file = request.FILES.get('fileupload')
        plottype = request.POST.get('plottype')
        xlabelfile = request.POST.get('xlabelfile')
        ylabelfile = request.POST.get('ylabelfile')

        currentuser = request.user

        filevisualize = FileVisualize(file=file, user = currentuser, plottype =plottype ,xlabelfile=xlabelfile, ylabelfile=ylabelfile)
        filevisualize.save()

        # fileurl = 'files/data1.xlsx'

        # df = pd.read_excel(fileurl)


        # if file:
        #     try:
        #         # Read the file using pandas read_excel or read_csv, depending on the file type
        #         if file.name.endswith('.csv'):
        #             df = pd.read_csv(fileurl)
        #         elif file.name.endswith('.xlsx'):
        #         else:
        #             # Handle other file types if needed
        #             return HttpResponse("Unsupported file format")
        #     except Exception as e:
        #         return HttpResponse(f"Error reading file: {str(e)}")
        # else:
        #     return HttpResponse("No file provided")

        # if plottype in plot_functions:
        #     plot_functions[plottype](x=xlabelfile, y=ylabelfile, data=df)
        #     plt.xlabel = xlabelfile
        #     plt.ylabel = ylabelfile

        #     image_buffer = BytesIO()
        #     plt.savefig(image_buffer, format='png')
        #     image_buffer.seek(0)

        # filename = f'graph{filevisualize.num}.png'
        # filevisualize.graph.save(filename, image_buffer)

        return redirect("fileGraph", num=filevisualize.pk)

        
    return render(request, 'Visualize/data.html')

def createfilegraph(filevisualize):
    
    plot_functions = {
        "scatter": sns.scatterplot,
        "line": sns.lineplot,
        "bar": sns.barplot,
        "histogram": sns.histplot,
    }

    fileurl = filevisualize.file.url
    plottype = filevisualize.plottype
    xlabelfile = filevisualize.xlabelfile
    ylabelfile = filevisualize.ylabelfile

    print(fileurl)

    df = pd.read_excel(fileurl)

    if plottype in plot_functions:
        plot_functions[plottype](x=xlabelfile, y=ylabelfile, data=df)
        plt.xlabel = xlabelfile
        plt.ylabel = ylabelfile

        image_buffer = BytesIO()
        plt.savefig(image_buffer, format='png')
        image_buffer.seek(0)

    filename = f'graph{filevisualize.num}.png'
    filevisualize.graph.save(filename, image_buffer)


@login_required
def fileGraph(request, num):
    filedata = FileVisualize.objects.filter(num=num).first()
    createfilegraph(filedata)
    return render(request, 'Visualize/fileviz.html', filedata)


