def tampilkan(mat, nama="Matriks"):
    print(f"--- {nama} ---")
    for baris in mat:
        print("  ".join(f"{elemen:4}" for elemen in baris))
    print()

def transpose(mat):
    baris = len(mat)
    kolom = len(mat[0])
    
    hasil = [[0 for _ in range(baris)] for _ in range(kolom)]
    
    for i in range(baris):
        for j in range(kolom):
            hasil[j][i] = mat[i][j]
            
    return hasil

def kalikan(A, B):
    baris_A = len(A)
    kolom_A = len(A[0])
    baris_B = len(B)
    kolom_B = len(B[0])
    
    if kolom_A != baris_B:
        raise ValueError("Jumlah kolom A harus sama dengan jumlah baris B!")
        
    hasil = [[0 for _ in range(kolom_B)] for _ in range(baris_A)]
    
    for i in range(baris_A):
        for j in range(kolom_B):
            for k in range(kolom_A):
                hasil[i][j] += A[i][k] * B[k][j]
                
    return hasil

def kalikan_skalar(mat, skalar):
    baris = len(mat)
    kolom = len(mat[0])
    
    hasil = [[0 for _ in range(kolom)] for _ in range(baris)]
    

    for i in range(baris):
        for j in range(kolom):
            hasil[i][j] = mat[i][j] * skalar
            
    return hasil