from django.shortcuts import render
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

# Create your views here.

def about(request):
    return render(request, 'Home/about.html')

def create_barplot(*args):
    plt.bar(args[0], args[1])
    plt.xlabel('Names')
    plt.ylabel('Marks')
    plt.title('Marks of Students')


    plot_path = 'static/bar.jpeg'
    plt.savefig(plot_path)

    return plot_path

def displaygraph(request):
    data = [23, 25, 47, 30, 21]
    names = ['Ram', 'Shayam', 'Niraj', 'Hari', 'Ramesh']
    
    plot_path = create_barplot(names, data)

    return render(request, 'Home/index.html', {'plot_path':plot_path})
    