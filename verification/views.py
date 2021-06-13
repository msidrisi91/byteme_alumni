from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.models import Profile

@login_required
def userlist(request):
    queryset = Profile.objects.filter(status='Processing')
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'verification/unverifieduserlist.html', {'profiles': users})


@login_required
def verify(request, pk):
    obj = get_object_or_404(Profile, pk=pk)
    obj.status = 'Verified'
    obj.save(update_fields=['status'])
    return redirect('verificationlist')


@login_required
def reject(request, pk):
    obj = get_object_or_404(Profile, pk=pk)
    obj.status = 'Rejected'
    obj.save(update_fields=['status'])
    return redirect('verificationlist')


@login_required
def detailview(request, pk):
    obj = get_object_or_404(Profile, pk=pk)
    return render(request, 'verification/detail_user.html', {'object': obj})

