from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import EditProfileForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from Data.models import Truyen, Theloai, Checktheloai, Theodoi
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q, Count

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('Home Page')

    def get_object(self):
        return self.request.user

def search_view(request):
    query = request.GET.get('q', '')
    genre_filter = request.GET.getlist('genre')
    chap_filter = request.GET.get('chap')
    source_filter = request.GET.get('source')
    status_filter = request.GET.get('status')
    sort_by_views = request.GET.get('views')

    results = Truyen.objects.annotate(total_chaps=Count('chaptruyen'))

    if query:
        results = results.filter(tentruyen__icontains=query)

    if genre_filter:
        results = results.filter(checktheloai__IDtheloai__tentheloai__in=genre_filter)

    if chap_filter:
        if chap_filter == '0-2':
            results = results.filter(total_chaps__gte=0, total_chaps__lte=2)
        elif chap_filter == '3-5':
            results = results.filter(total_chaps__gte=3, total_chaps__lte=5)
        elif chap_filter == '5+':
            results = results.filter(total_chaps__gt=5)

    if source_filter:
        results = results.filter(nguon__icontains=source_filter)

    if status_filter:
        results = results.filter(trangthai=status_filter)

    if sort_by_views:
        results = results.order_by('-luotxem')

    genres = Theloai.objects.all()
    sources = ['yytruyen', 'doctruyenchu.vn', 'truyenfull.io' ]

    return render(request, 'members/search.html', {
        'results': results,
        'query': query,
        'genres': genres,
        'genre_filter': genre_filter,
        'chap_filter': chap_filter,
        'source_filter': source_filter,
        'status_filter': status_filter,
                'sort_by_views': sort_by_views,
        'sources': sources
    })

@login_required
def toggle_follow(request, truyen_id):
    try:
        truyen = Truyen.objects.get(IDtruyen=truyen_id)
        theodoi, created = Theodoi.objects.get_or_create(user=request.user, IDtruyen=truyen)
        is_following = not created

        if created:
            # Nếu bản ghi được tạo, có nghĩa là người dùng đã theo dõi
            return JsonResponse({'status': 'followed', 'message': 'Theo dõi thành công!'})
        else:
            # Nếu bản ghi đã tồn tại, xóa nó để hủy theo dõi
            theodoi.delete()
            return JsonResponse({'status': 'unfollowed', 'message': 'Hủy theo dõi thành công!'})
    except Truyen.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Truyện không tồn tại!'}, status=404)

@login_required
def tu_truyen_view(request):
    # Lấy danh sách các truyện mà người dùng đang theo dõi
    followed_truyens = Theodoi.objects.filter(user=request.user).select_related('IDtruyen')

    # Tạo một danh sách để lưu trữ thông tin về trạng thái theo dõi
    truyen_info = []
    for follow in followed_truyens:
        is_following = True  # Người dùng đang theo dõi truyện này
        truyen_info.append({
            'truyen': follow.IDtruyen,
            'is_following': is_following,
        })

    return render(request, 'members/tu_truyen.html', {
        'truyen_info': truyen_info,
    })

@login_required
def unfollow_truyen(request, truyen_id):
    try:
        truyen = Truyen.objects.get(IDtruyen=truyen_id)
        theodoi = Theodoi.objects.get(user=request.user, IDtruyen=truyen)
        theodoi.delete()
        return JsonResponse({'status': 'unfollowed', 'message': 'Hủy theo dõi thành công!'})
    except Truyen.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Truyện không tồn tại!'}, status=404)
    except Theodoi.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Bạn chưa theo dõi truyện này!'}, status=404)
