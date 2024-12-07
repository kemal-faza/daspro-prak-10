"""
Nama File: list_24060124120013.py
Deskripsi: Berisi type dan operasi list 
Pembuat: Muhamad Kemal Faza
NIM: 24060124120013
Tanggal: 29/10/2024

DEFINISI DAN SPESIFIKASI TYPE
Konstruktor menambahkan elemen di awal, notasi prefix
    type List: [] atau [e o List]
Konstruktor menambahkan elemen di akhir, notasi postfix
    type List: [] atau [List o e]
"""


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: elemen, List -> List
# Konso(e, L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama
# Realisasi
def Konso(e, L):
    return [e] + L


# Konsi: List, elemen -> List
# Konsi(L, e) menghasilkan sebuah list dari L dan e dengan e sebagai elemen terakhir
# Realisasi
def Konsi(e, L):
    return L + [e]


# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmnt: List tidak kosong -> elemen
# FirstElmnt(L) menghasilkan elemen pertama dari List L
# Realisasi
def FirstElmnt(L):
    return L[0]


# LastElmnt: List tidak kosong -> elemen
# LastElmnt(L) menghasilkan elemen terakhir dari List L
# Realisasi
def LastElmnt(L):
    return L[-1]


# Tail: List tidak kosong -> List
# Tail(L) menghasilkan list tanpa elemen pertama dari list L, mungkin kosong
# Realisasi
def Tail(L):
    return L[1:]


# Head: List tidak kosong -> List
# Head(L) menghasilkan list tanpa elemen terakhir dari list L, mungkin kosong
# Realisasi
def Head(L):
    return L[:-1]


# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty: List -> boolean
# IsEmpty(L) bernilai benar jika list kosong
# Realisasi
def IsEmpty(L):
    return L == [] or L == ""


# IsOneElmnt: List -> boolean
# IsOneElmnt(L) bernilai benar jika list L hanya mempunya satu elemen
def IsOneElmnt(L):
    if IsEmpty(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []


# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
# NBElmnt: List -> integer
# NBElemnt(L) menghasilkan banyaknya eleman di dalam list, nol jika kosong
# Realisasi
def NBElmnt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NBElmnt(Tail(L))


# ElmntKeN: integer >= 0, List -> elemen
# ElmntKeN(N, L) mengirimkan lemen list yang ke N, N <= NBElmnt(L) dan N >= 0
# Realisasi
def ElmntKeN(N, L):
    if N == 1:
        return FirstElmnt(L)
    else:
        return ElmntKeN(N - 1, Tail(L))


# IsMemebr: elemen, List -> boolean
# IsMember(X, L) bernilai benar jika X adalah elemen list L
# Realisasi
def IsMember(X, L):
    if IsEmpty(L):
        return False
    else:
        if FirstElmnt(L) == X:
            return True
        else:
            return IsMember(X, Tail(L))


# Copy: List -> List
# Copy(L) menghasilkan list yang identik dengan list asal
# Realisasi
def Copy(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmnt(L), Copy(Tail(L)))


# Inverse: List -> List
# Inverse(L) menghasilkan list L yang dibalik, yaitu yang urutan elemennya adalah kebalikan dari list asal
# Realisasi
def Inverse(L):
    if IsEmpty(L):
        return []
    else:
        return Konsi(Inverse(Tail(L)), FirstElmnt(L))


# Konkat: 1 List -> List
# Konkat(L1, L2) menghasilkan konkatinasi antara 2 buah list, dengan list L2 "sesudah" list L1
# Realisasi
def Konkat(L1, L2):
    if IsEmpty(L1):
        return L2
    else:
        return Konso(FirstElmnt(L1), Konkat(Tail(L1), L2))


# SumElmnt: List of integer -> integer
# SumElmnt(L) menghasilkan penjumlahan dari setiap elemen di list L
# Realisasi
def SumElmnt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmnt(L) + SumElmnt(Tail(L))


# AvgElmnt: List of integer -> integer
# AvgElmnt(L) menghasilkan nilai rata-rata dari setiap elemen di list L
# Realisasi
def AvgElmnt(L):
    if IsEmpty(L):
        return 0
    else:
        return (FirstElmnt(L) + SumElmnt(Tail(L))) / NBElmnt(L)


# max2: 2 integer -> integer
# max2(a, b) menghasilkan nilai terbesar antara a dan b
# Realisasi
def max2(a, b):
    if a > b:
        return a
    else:
        return b


# MaxElmnt: List of integer -> integer
# MaxElmnt(L) mengembalikan elemen maksimum dari list L
# Realisasi
def MaxElmnt(L):
    if IsOneElmnt(L):
        return FirstElmnt(L)
    else:
        return max2(FirstElmnt(L), MaxElmnt(Tail(L)))


# CekDplkt: integer, List of integer -> integer
# CekDplkt(X, L) mengembalikan banyaknya kemunculan nilai X di dalam list L
# Realisasi
def CekDplkt(X, L):
    if IsEmpty(L):
        return 0
    else:
        if FirstElmnt(L) == X:
            return 1 + CekDplkt(X, Tail(L))
        else:
            return CekDplkt(X, Tail(L))


# MaxNB: List of integer -> <integer, integer>
# MaxNB(L) menghasilkan <max, countMax> dengan max adalah elemen maksimum di dalam list L dan countMax adalah banyaknya kemunculan nilai max di dalam list L
# Realisasi
def MaxNB(L):
    return [MaxElmnt(L), CekDplkt(MaxElmnt(L), L)]


# AddList: 2 List of integer -> List of integer
# AddList(L1, L2) menghasilkan list baru yang setiap elemennya adalah hasil penjumlahan setiap elemen di L1 dan L2 pada posisi yang sama
# Realisasi
def AddList(L1, L2):
    if IsEmpty(L1) and IsEmpty(L2):
        return []
    elif not IsEmpty(L1) and IsEmpty(L2):
        return []
    elif IsEmpty(L1) and not IsEmpty(L2):
        return []
    else:
        return Konso(FirstElmnt(L1) + FirstElmnt(L2), AddList(Tail(L1), Tail(L2)))


# IsPalindrom: List of character -> boolean
# IsPalindrom(L) bernilai benar jika list L merupakan palindrom
# Realisasi
def IsPalindrom(L):
    if IsEmpty(L):
        return True
    elif FirstElmnt(L) != LastElmnt(L):
        return False
    else:
        return IsPalindrom(Head(Tail(L)))
