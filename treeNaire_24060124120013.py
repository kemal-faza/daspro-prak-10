# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def makePN(A, PN):
    return [A, PN]


# DEFINISI DAN SPESIFIKASI SELEKTOR
# Akar : PohonN-ner tidak kosong -> elemen
#   {Akar(P) adalah akar dari P. Jika P adalah (A, PN) = Akar(P) adalah A}
def Akar(PN):
    return PN[0]


# Anak: PohonN-ner tidak kosong → list of PohonN-ner
# #{ Anak(P) adalah list of pphon N-ner yang merupakan anak-anak (sub phon) # dari P. Jika P adalah (A, PN) = Anak (P) adalah PN }
def Anak(PN):
    return PN[1]


# DEFINISI DAN SPESIFIKASI PREDIKAT
# #IsTreeNEmpty : PohonN-ner → boolean_
# # {IsTreeNEmpty(PN) true jika PN kosong : () }
def isTreeNEmpty(PN):
    return PN == []


# IsOneElmt : PohonN-ner → boolean
# {IsOneElmt(PN) true jika PN hanya terdiri dari Akar
def isOneElmt(PN):
    return (isTreeNEmpty(PN) == False) and (isTreeNEmpty(Anak(PN)) == True)


# NbNELmt: PohonN-ner → integer ≥ 0
# {NbNElmt(P) memberikan banyaknya node dari pohon P
# Basis 1: NbNELmt ((A)\) = 1
# Rekurens NbNELmt ((A,PN)) = 1 + NbELmt(PN)
def NbNElmt(PN):
    # Basis: Jika pohon kosong
    if isTreeNEmpty(PN):
        return 0

    # Jika hanya ada satu elemen (akar saja)
    elif isOneElmt(PN):
        return 1

    # Hitung 1 untuk akar, dan rekursif pada setiap anak pohon
    # Tanpa menggunakan loop, kita memanggil fungsi untuk setiap anak secara rekursif
    # Pertama pada anak pertama
    else:
        return 1 + NbNElmt(Anak(PN)[0]) + NbNElmtChild(Anak(PN)[1:])


# Fungsi tambahan untuk menghitung jumlah elemen pada sisa anak-anak
def NbNElmtChild(PN):
    # Basis: Jika tidak ada anak
    if isTreeNEmpty(PN):
        return 0

    # Jika ada anak, rekursif pada anak pertama dan sisa anak-anak
    else:
        return NbNElmt(PN[0]) + NbNElmtChild(PN[1:])


def NbNDaun(PN):
    # Basis: Jika pohon kosong
    if isTreeNEmpty(PN):
        return 0

    # Jika pohon adalah daun (anak kosong)
    elif isOneElmt(PN):
        return 1

    # Rekursi pada akar dan anak-anak
    else:
        return NbNDaunChild(Anak(PN))


# Fungsi tambahan untuk menghitung jumlah daun pada sisa anak-anak
def NbNDaunChild(PN):
    # Basis: Jika tidak ada anak
    if isTreeNEmpty(PN):
        return 0

    # Jika ada anak, rekursif pada anak pertama dan sisa anak-anak
    else:
        return NbNDaun(Akar(PN)) + NbNDaunChild(PN[1:])


T3 = ["A", [["B", [["D", []], ["E", []]]], ["C", [["F", []], ["G", []]]]]]
# APLIKASI
T = makePN(2, [])
print(makePN(2, []))
print(isTreeNEmpty([]))
print(isOneElmt(T))
print(
    f"NbNElmt(['A', [['B', [['D', []], ['E', []]]], ['C', [['F', []], ['G', []]]]]]) => {NbNElmt(makePN('A', [makePN('B', [makePN('D', []), makePN('E', [])]), makePN('C', [makePN('F', []), makePN('G', [])])]))}"
)
print(
    f"NbNElmtChild(Anak(['A', [['B', [['D', []], ['E', []]]], ['C', [['F', []], ['G', []]]]]])) => {NbNElmtChild(
        Anak(
            makePN(
                "A",
                [
                    makePN("B", [makePN("D", []), makePN("E", [])]),
                    makePN("C", [makePN("F", []), makePN("G", [])]),
                ],
            )
        )
    )}"
)
print(
    f"NbNDaun(['A', [['B', [['D', []], ['E', []]]], ['C', [['F', []], ['G', []]]]]]) => {NbNDaun(
            makePN(
                "A",
                [
                    makePN("B", [makePN("D", []), makePN("E", [])]),
                    makePN("C", [makePN("F", []), makePN("G", [])]),
                ],
            )
        )}"
)
print(
    f"NbNDaunChild(Anak(['A', [['B', [['D', []], ['E', []]]], ['C', [['F', []], ['G', []]]]]])) => {NbNDaunChild(
        Anak(
            makePN(
                "A",
                [
                    makePN("B", [makePN("D", []), makePN("E", [])]),
                    makePN("C", [makePN("F", []), makePN("G", [])]),
                ],
            )
        )
    )}"
)
