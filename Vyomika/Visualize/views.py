from django.shortcuts import render
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
            data_list.append(int(data))

        sns.set(style='darkgrid')
        plt.bar(name_list, data_list)
        plt.xlabel('Names', 'Marks')
        plt.title('Marks of students')

        image_buffer = BytesIO()
        plt.savefig(image_buffer, format='png')
        image_buffer.seek(0)

        visualize = Visualize.objects.create(fname=fname,datas=datas, names=names)
        visualize.graph.save('graph.png', image_buffer)
    return render(request, 'Visualize/data.html')

def displayGraph(request, snum):
    data = Visualize.objects.filter(snum=snum)
    context = {'data':data}
    return render(request, 'Visualize/display.html', context)
