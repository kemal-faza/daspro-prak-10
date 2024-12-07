from list_24060124120013 import *
from set_24060124120013 import *


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# KonsLo: list, list of list -> list of list
# KonsLo(L, S) membentuk list baru dengan list (L) yang diberikan sebagai elemen pertama list of list (S).
def KonsLo(L, S):
    return [L] + S


# KonsLi: list of list, list -> list of list
# KonsLi(S, L) membentuk list baru dengan list (L) yang diberikan sebagai elemen terakhir list of list
def KonsLi(S, L):
    return S + [L]


# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstList: list of list tidak kosong -> list
# FirstList(S) menghasilkan elemen pertama list (mungkin sebuah list atau atom)
def FirstList(S):
    return S[0]


# LastList: list of list tidak kosong -> list
# LastList(S) menghasilkan elemen terakhir list (mungkin sebuah list atau atom)
def LastList(S):
    return S[-1]


# TailList: list of list tidak kosong -> list of list
# TailList(S) menghasilkan sisa list of list S tanpa elemen pertamanya
def TailList(S):
    return S[1:]


# HeadLIst: list of list tidak kosong -> list of list
# HeadLIst(S) menghasilkan sisa list of list S tanpa elemen terakhirnya
def HeadList(S):
    return S[:-1]


# DEFINISI DAN SPESIFIKASI PREDIKAT KHUSUS LIST
# IsAtom: list of list -> boolean
# IsAtom(S) benar jika S adalah sebuah atom
def IsAtom(L):
    return type(L) != list


# IsList: list of list -> boolean
# IsList(S) benar jika S adalah sebuah list
def IsList(L):
    return type(L) == list


# IsEmpty: list of list -> boolean
# IsEmpty(S) benar jika S adalah list of list kosong
def IsEmpty(S):
    return S == []


# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
# IsEqS: 2 list of list -> boolean
# IsEqS(S1, S2) benar jika S1 memiliki elemen dengan nilai dan urutan yang sama dengan S2
def IsEqS(S1, S2):
    if IsEmpty(S1) and IsEmpty(S2):
        return True
    elif IsEmpty(S1) and not IsEmpty(S2):
        return False
    elif not IsEmpty(S1) and IsEmpty(S2):
        return False
    else:
        if IsAtom(FirstList(S1)) and IsAtom(FirstList(S2)):
            return FirstList(S1) == FirstList(S2) and IsEqS(TailList(S1), TailList(S2))
        elif IsList(FirstList(S1)) and IsList(FirstList(S2)):
            return IsEqS(FirstList(S1), FirstList(S2)) and IsEqS(
                TailList(S1), TailList(S2)
            )
        else:
            return False


# IsMemberS: elemen, list of list-> boolean
# IsMemberS(x,S) mengembalikan true jika elemen x ada di dalam list of list S
#   Contoh aplikasi:
#   IsMemberS(3, []) {menghasilkan false}
#   IsMemberS(3, [2, 4, 3, [1], [4,5]]) {menghasilkan true}
#   IsMemberS(3, [2, 4, 7, [1], [3,5]]) {menghasilkan true}
def IsMemberS(x, S):
    if IsEmpty(S):
        return False
    elif IsAtom(FirstList(S)):
        return x == FirstList(S) or IsMemberS(x, TailList(S))
    else:
        return IsMemberS(x, FirstList(S)) or IsMemberS(x, TailList(S))


# IsMemberLS: list, list of list -> boolean
# IsMemberLS(L, S) mengembalikan true jika list L ada di dalam list of list S
def IsMemberLs(L, S):
    if IsEmpty(S):
        return False
    elif IsAtom(FirstList(S)):
        return IsMemberLs(L, TailList(S))
    else:
        return IsEqS(L, FirstList(S)) or IsMemberLs(L, TailList(S))


# RemberList: elemen, list of list -> list of list
# RemberList(x,S) menghapus semua elemen x yang ada di list of list S
#   Contoh aplikasi:
#   RemberList(3, []) {menghasilkan []}
#   RemberList(3, [4, 3, [2,4], 3]) {menghasilkan [4, [2,4]]}
#   RemberList(3, [2, 4, [3,6,9], 5, 3]) {menghasilkan [2, 4, [6,9], 5]}
def RemberList(x, S):
    if IsEmpty(S):
        return S
    elif IsList(FirstList(S)):
        return KonsLo(RemberList(x, FirstList(S)), RemberList(x, TailList(S)))
    else:
        if x == FirstList(S):
            return RemberList(x, TailList(S))
        else:
            return KonsLo(FirstList(S), RemberList(x, TailList(S)))


# Max: list of list -> integer
# Max(S) mengembalikan elemen maksimum di dalam list of list S
#   Contoh aplikasi:
#   Max([4, 5, 6, [8,9,10], [12,0], 8]) {menghasilkan 12}
#   Max([4, 15, 6, [8,9,10], [12,0], 8]) {menghasilkan 15}
def Max(S):
    if IsOneElmnt(S):
        if IsList(FirstList(S)):
            return max2(Max(FirstList(S)), Max(TailList(S)))
        else:
            return FirstList(S)
    else:
        if IsAtom(FirstList(S)):
            return max2(FirstList(S), Max(TailList(S)))
        else:
            return max2(Max(FirstList(S)), Max(TailList(S)))


# NBElmtAtom: list of list -> integer
# NBElmtAtom(S) mengembalikan banyaknya elemen list of list S yang berupa atom
#   Contoh aplikasi:
#   NBElmtAtom([4, 5, 6, [8,9,10], [12,0], 8]) {menghasilkan 4}
#   NBElmtAtom([4, 15, 6, [8,9], 10, [12], 8]) {menghasilkan 5}
#   NBElmtAtom([[8,9,10]]) {menghasilkan 0}
def NBElmntAtom(S):
    if IsEmpty(S):
        return 0
    elif IsAtom(FirstList(S)):
        return 1 + NBElmntAtom(TailList(S))
    else:
        return NBElmntAtom(TailList(S))


# NBElmntList: list of list -> integer
# NBElmntList(S) mengembalikan banyaknya elemen list of list S yang berupa list
#   Contoh aplikasi:
#   NBElmntList([4, 5, 6, [8,9,10], [12,0], 8]) {menghasilkan 2}
#   NBElmntList([[4, 15], 6, [8,9], 10, [12], 8]) {menghasilkan 3}
#   NBElmntList([[8,9,10]]) {menghasilkan 1}
def NBElmntList(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return 1 + NBElmntList(TailList(S))
    else:
        return NBElmntList(TailList(S))


# SumLoL: list of list -> integer
# SumLoL(S) mengembalikan jumlah semua elemen dalam list of list S
#   Contoh aplikasi:
#   SumLoL([[]]) {menghasilkan 0}
#   SumLoL([4, 5, 6, [2,3,1]]) {menghasilkan 21}
#   SumLoL([[2,3,4]]) {menghasilkan 9}
def SumLol(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return SumLol(FirstList(S)) + SumLol(TailList(S))
    else:
        return FirstList(S) + SumLol(TailList(S))


# MaxNBElmntList: list of list -> integer
# MaxNBElmntList(S) mengembalikan banyaknya elemen list maksimum yang ada pada list of list S
#   Contoh aplikasi:
#   MaxNBElmntList([[4,5,6,7], [8,9,10], [12,0], 8]) {menghasilkan 4}
#   MaxNBElmntList([[4,15], 6, [8,9], 10, [12], 8]) {menghasilkan 2}
#   MaxNBElmntList([8,9,10]) {menghasilkan 0}
def MaxNBElmntList(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return max2(NBElmntAtom(FirstList(S)), MaxNBElmntList(TailList(S)))
    else:
        return MaxNBElmntList(TailList(S))


# MaxSumElmt: list of list -> integer
# MaxSumElmt(S) mengembalikan elemen maksimum pada list of list S
#   jika elemen berupa list, maka dihitung jumlahan elemen dalam list tersebut


def MaxSumElmnt(S):
    if IsEmpty(S):
        return 0
    elif IsAtom(FirstList(S)):
        return max2(FirstList(S), MaxSumElmnt(TailList(S)))
    else:
        return max2(SumLol(FirstList(S)), MaxSumElmnt(TailList(S)))
