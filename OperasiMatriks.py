import Dzakya055 as dz
Mat_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Mat_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

Vek_D = [
    [5],
    [6],
    [7]
]

Sca_E = 5

Mat_AT = dz.transpose(Mat_A)
dz.tampilkan(Mat_AT, "Transpose A")

Mat_AMat_B = dz.kalikan(Mat_A, Mat_B)
dz.tampilkan(Mat_AMat_B, "Hasil A * B")

Mat_AVek_D = dz.kalikan(Mat_A, Vek_D)
dz.tampilkan(Mat_AVek_D, "Hasil A * vektor D")

Mat_ASca_E = dz.kalikan_skalar(Mat_A, Sca_E)
dz.tampilkan(Mat_ASca_E, "Hasil A * scalar E")

