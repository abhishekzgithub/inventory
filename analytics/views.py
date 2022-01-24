from django.shortcuts import render

def display_piechart(request, context={}):
    labels = ["January","February","March","April","May"]
    data = [65, 59, 80, 81, 56]

    # queryset = Order.objects.order_by('-created_timestamp')[:5]
    # for city in queryset:
    #     labels.append(city.name)
    #     data.append(city.population)

    # return render(request, 'pie_chart.html', {
    #     'labels': labels,
    #     'data': data,
    # })
    context["labels"]=labels
    context["data"]=data
    return render(request, "analytics/piechart.html", context)

def display_line_chart(request, context={}):
    labels = ["January","February","March","April","May"]
    data = [65, 59, 80, 81, 56, 55, 40]

    # queryset = Order.objects.order_by('-created_timestamp')[:5]
    # for city in queryset:
    #     labels.append(city.name)
    #     data.append(city.population)

    # return render(request, 'pie_chart.html', {
    #     'labels': labels,
    #     'data': data,
    # })
    context["labels"]=labels
    context["data"]=data
    return render(request, "analytics/linechart.html", context)


def display_bar_chart(request, context={}):
    labels = ["January","February","March","April","May"]
    data = [65, 59, 80, 81, 56, 55, 40]

    # queryset = Order.objects.order_by('-created_timestamp')[:5]
    # for city in queryset:
    #     labels.append(city.name)
    #     data.append(city.population)

    # return render(request, 'pie_chart.html', {
    #     'labels': labels,
    #     'data': data,
    # })
    context["labels"]=labels
    context["data"]=data
    return render(request, "analytics/barchart.html", context)