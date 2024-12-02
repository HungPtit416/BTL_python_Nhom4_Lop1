from django.shortcuts import render
from Data.models import Truyen, Chaptruyen

def ChapView(request, idTruyen, id):
    myTruyen = Truyen.objects.get(IDtruyen=idTruyen)
    myChap = Chaptruyen.objects.get(id=id)

    # Lấy thông tin về chương trước và chương tiếp theo
    prevChap = Chaptruyen.objects.filter(IDtruyen=idTruyen, chap__lt=myChap.chap).order_by('-chap').first()
    nextChap = Chaptruyen.objects.filter(IDtruyen=idTruyen, chap__gt=myChap.chap).order_by('chap').first()

    # Tạo URL cho các chương trước và tiếp theo
    prevChapUrl = f"/chap/{idTruyen}/{prevChap.id}" if prevChap else None
    nextChapUrl = f"/chap/{idTruyen}/{nextChap.id}" if nextChap else None

    # Truyền các thông tin vào template
    content = {
        "myTruyen": myTruyen,
        "myChap": myChap,
        "prevChapUrl": prevChapUrl,
        "nextChapUrl": nextChapUrl
    }

    return render(request, "ChapView/index.html", content)