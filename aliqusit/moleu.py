def my_view(request):
    context = {'title': 'My Title', 'message': 'Hello, world!'}
    return render(request, 'my_template.html', context)
