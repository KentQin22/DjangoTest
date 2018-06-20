from django.http import HttpResponse
#编写视图处理函数，一个函数相当是一个视图

def run_views(request):
    #request中主要封装的请求的信息
    return HttpResponse("<h1>航航来耍，有美女哟！</h1>")
