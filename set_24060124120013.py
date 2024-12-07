from list_24060124120013 import *


# DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK HIMPUNAN
# Rember: elemen, list -> list
# Rember(x,L) menghapus sebuah elemen x yang pertama kali dari list L
#   Jika x ada di list L, maka elemen L berkurang 1.
#   Jika x tidak ada di list L maka L tetap. List kosong tetap menjadi list kosong.
def Rember(x, L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmnt(L) == x:
            return Tail(L)
        else:
            return Konso(FirstElmnt(L), Rember(x, Tail(L)))


# Rember2: elemen, list -> list
# Rember2(x,L) menghapus sebuah elemen x yang terakhir kali ditemui dari list L
#   Jika x ada di list L, maka elemen L berkurang 1.
#   Jika x tidak ada di list L maka L tetap. List kosong tetap menjadi list kosong.
def Rember2(x, L):
    if IsEmpty(L):
        return []
    else:
        if LastElmnt(L) == x:
            return Head(L)
        else:
            return Konsi(LastElmnt(L), Rember2(x, Head(L)))


# MultiRember: elemen, list -> list
# MultiRember(x,L) menghapus semua kemunculan elemen x dari list L.
#   List baru yang dihasilkan tidak lagi memiliki elemen x.
#   List kosong tetap menjadi list kosong.
def MultiRember(x, L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmnt(L) == x:
            return MultiRember(x, Tail(L))
        else:
            return Konso(FirstElmnt(L), MultiRember(x, Tail(L)))


# DEFINISI DAN SPESIKASI KONSTRUKTOR SET DARI LIST
# MakeSet: list -> set
# MakeSet(L) membuat set dari list L dengan menghapus semua kemunculan lebih dari satu kali yang menggunakan fungsi IsMember(x, L)
#   list kosong tetap menjadi himpunan kosong
def MakeSet(L):
    if IsEmpty(L):
        return []
    else:
        if IsMember(FirstElmnt(L), Tail(L)):
            return MakeSet(Tail(L))
        else:
            return Konso(FirstElmnt(L), MakeSet(Tail(L)))


# MakeSet2: list -> set
# MakeSet2(L) membuat set dari list L dengan menghapus semua kemunculan lebih dari satu kali yang menggunakan fungsi MultiRember(x, L)
#   list kosong tetap menjadi himpunan kosong
def MakeSet2(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmnt(L), MakeSet2(MultiRember(FirstElmnt(L), Tail(L))))


# DEFINISI DAN SPESIKASI KONSTRUKTOR SET
# KonsoSet: elemen,set -> set
# konsoSet(e,H) menambahkan sebuah elemen e sebagai elemen pertama set H
#   dengan syarat e belum ada di dalam himpunan H
def KonsoSet(e, H):
    if not IsMember(e, H):
        return Konso(e, H)
    else:
        return H


# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSet: list -> boolean
# IsSet(L) mengembalikan true jika L adalah sebuah set
def IsSet(L):
    if IsEmpty(L):
        return True
    else:
        if IsMember(FirstElmnt(L), Tail(L)):
            return False
        else:
            return IsSet(Tail(L))


# IsSubset: 2 set -> boolean
# IsSubset(H1,H2) mengembalikan true jika H1 merupakan subset dari H2
def IsSubset(H1, H2):
    if IsEmpty(H1):
        return True
    else:
        if IsMember(FirstElmnt(H1), H2):
            return IsSubset(Tail(H1), H2)
        else:
            return False


# IsEqualSet: 2 set -> boolean
# IsEqualSet(H1,H2} benar jika H1 adalah set yang sama dengan H2 yang menggunakan fungsi IsSubset(H1, H2)
def IsEqualSet(H1, H2):
    return IsSubset(H1, H2) and IsSubset(H2, H1)


# IsEqualSet2: 2 set -> boolean
# IsEqualSet2(H1,H2} benar jika H1 adalah set yang sama dengan H2
def IsEqualSet2(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return True
    elif not IsEmpty(H1) and IsEmpty(H2):
        return False
    elif IsEmpty(H1) and not IsEmpty(H2):
        return False
    else:
        if FirstElmnt(H1) == FirstElmnt(H2):
            return IsEqualSet2(Tail(H1), Tail(H2))
        else:
            return False


# IsIntersect: 2 set -> boolean
# IsIntersect(H1,H2) benar jika H1 beririsan dengan H2
def IsIntersect(H1, H2):
    if IsEmpty(H1):
        return False
    else:
        if IsMember(FirstElmnt(H1), H2):
            return True
        else:
            return IsIntersect(Tail(H1), H2)


# DEFINISI DAN SPESIFIKASI OPERASI TERHADAP HIMPUNAN
# MakeIntersect: 2 set -> set
# MakeIntersect(H1,H2) menghasilkan set baru yang merupakan hasil irisan antara H1 dan H2, rekursif terhadap H1
def MakeIntersect(H1, H2):
    if IsEmpty(H1):
        return []
    else:
        if IsMember(FirstElmnt(H1), H2):
            return Konso(FirstElmnt(H1), MakeIntersect(Tail(H1), H2))
        else:
            return MakeIntersect(Tail(H1), H2)


# MakeIntersect2: 2 set -> set
# MakeIntersect2(H1,H2) menghasilkan set baru yang merupakan hasil irisan antara H1 dan H2, rekursif terhadap H2
def MakeIntersect2(H1, H2):
    if IsEmpty(H2):
        return []
    else:
        if IsMember(FirstElmnt(H2), H1):
            return Konso(FirstElmnt(H2), MakeIntersect2(Tail(H2), H1))
        else:
            return MakeIntersect2(Tail(H2), H1)


# MakeUnion: 2 set -> set
# MakeUnion(H1,H2) menghasilkan set baru yang merupakan hasil gabungan antara H1 dan H2, rekursif terhadap H1
def MakeUnion(H1, H2):
    if IsEmpty(H1):
        return H2
    else:
        if IsMember(FirstElmnt(H1), H2):
            return MakeUnion(Tail(H1), H2)
        else:
            return Konso(FirstElmnt(H1), MakeUnion(Tail(H1), H2))


# MakeUnion2: 2 set -> set
# MakeUnion2(H1,H2) menghasilkan set baru yang merupakan hasil gabungan antara H1 dan H2, rekursif terhadap H2
def MakeUnion2(H1, H2):
    if IsEmpty(H2):
        return H1
    else:
        if IsMember(FirstElmnt(H2), H1):
            return MakeUnion2(Tail(H2), H1)
        else:
            return Konso(FirstElmnt(H2), MakeUnion2(Tail(H2), H1))


# NBIntersect: 2 set -> integer
# NBIntersect(H1,H2) menghasilkan jumlah elemen yang beririsan pada H1 dan H2
#   tanpa memanfaatkan fungsi MakeIntersect(H1,H2).
def NBIntersect(H1, H2):
    if IsEmpty(H1):
        return 0
    else:
        if IsMember(FirstElmnt(H1), H2):
            return 1 + NBIntersect(Tail(H1), H2)
        else:
            return NBIntersect(Tail(H1), H2)


# NBUnion: 2 set -> integer
# NBUnion(H1,H2) menghasilkan jumlah elemen hasil gabungan antara H1 dan H2
#   tanpa memanfaatkan fungsi MakeUnion(H1,H2).


def NBUnion(H1, H2):
    if IsEmpty(H1):
        return NBElmnt(H2)
    else:
        if IsMember(FirstElmnt(H1), H2):
            return NBUnion(Tail(H1), H2)
        else:
            return 1 + NBUnion(Tail(H1), H2)
