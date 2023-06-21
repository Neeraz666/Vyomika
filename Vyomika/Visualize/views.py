from django.shortcuts import render
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import matplotlib.pyplot as plt
from .models import Visualize

# Create your views here.
def datainput(request):
    if request.method == 'POST':
        datas = request.POST.get('data')
        names = request.POST.get('names')

        data_list = []
        name_list = []

        for data in datas.split(','):
            data_list.append(int(data))
        
        for name in names.split(','):
            name_list.append(name)

        sns.set(style='darkgrid')
        plt.bar(name_list, data_list)
        plt.xlabel('Names', 'Marks')
        plt.title('Marks of students')

        image_buffer = BytesIO()
        plt.savefig(image_buffer, format='png')
        image_buffer.seek(0)

        visualize = Visualize(datas=datas, names=names)
        visualize.graph.save('graph.png', image_buffer)

    return render(request, 'Visualize/data.html')