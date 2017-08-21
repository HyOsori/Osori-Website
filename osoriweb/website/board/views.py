from django.shortcuts import render,redirect

# Create your views here.
def board(request):
    return redirect('noti_board')

def noti_board(request):
    return render(request, 'board/noti_board.html', {})

def info_board(request):
    return render(request, 'board/info_board.html', {})

def free_board(request):
    return render(request, 'board/free_board.html', {})