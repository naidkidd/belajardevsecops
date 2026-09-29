"""Modul untuk demonstrasi perbaikan kualitas kode."""


def tambah(angka_pertama, angka_kedua):
    """Menghitung hasil penjumlahan dua angka.

    Args:
        angka_pertama: Angka pertama yang akan dijumlahkan.
        angka_kedua: Angka kedua yang akan dijumlahkan.

    Returns:
        Hasil penjumlahan kedua angka.
    """
    hasil = angka_pertama + angka_kedua
    print(hasil)
    return hasil


def main():
    """Fungsi utama program."""
    tambah(1, 2)


if __name__ == "__main__":
    main()