from django.shortcuts import render
import matplotlib.pyplot as plt

# Create your views here.
def displaygraph(request):
    data = [23, 25, 47, 30, 21]
    names = ['Ram', 'Shayam', 'Niraj', 'Hari', 'Ramesh']

    plt.bar(names, data)
    plt.xlabel('Names')
    plt.ylabel('Marks')
    plt.title('Marks of Students')


    plot_path = 'static/bar.jpeg'
    plt.savefig(plot_path)

    return render(request, 'Home/index.html', {'plot_path':plot_path})
    