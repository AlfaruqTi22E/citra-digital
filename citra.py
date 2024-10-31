# Impor pustaka yang dibutuhkan
import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt

# Fungsi untuk menampilkan gambar beserta judulnya
def tampilkan_gambar(gambar, judul):
    plt.imshow(gambar, cmap='gray' if len(gambar.shape) == 2 else None)
    plt.title(judul)
    plt.axis('off')
    plt.show()

# Muat gambar daun (sesuaikan path file gambar sesuai lokasi gambar)
gambar_path = "daun_pepaya.jpg"  # Ganti dengan gambar daun lain jika perlu
gambar = iio.imread(gambar_path)

# Ekstrak Channel R (Red)
gambar_red = gambar.copy()
gambar_red[:, :, 1] = 0  # Nonaktifkan channel Green
gambar_red[:, :, 2] = 0  # Nonaktifkan channel Blue
tampilkan_gambar(gambar_red, "Channel R (Red)")

# Ekstrak Channel G (Green)
gambar_green = gambar.copy()
gambar_green[:, :, 0] = 0  # Nonaktifkan channel Red
gambar_green[:, :, 2] = 0  # Nonaktifkan channel Blue
tampilkan_gambar(gambar_green, "Channel G (Green)")

# Ekstrak Channel B (Blue)
gambar_blue = gambar.copy()
gambar_blue[:, :, 0] = 0  # Nonaktifkan channel Red
gambar_blue[:, :, 1] = 0  # Nonaktifkan channel Green
tampilkan_gambar(gambar_blue, "Channel B (Blue)")

# Konversi ke Grayscale
# Menghitung rata-rata warna dengan bobot untuk hasil tampilan alami
grayscale = np.dot(gambar[..., :3], [0.2989, 0.5870, 0.1140])
tampilkan_gambar(grayscale, "Grayscale")

# Konversi ke Biner (Threshold)
# Menetapkan nilai threshold (contoh: 128)
threshold = 128
binary = (grayscale > threshold) * 255
tampilkan_gambar(binary, "Threshold (Biner)")
