a= 10
b= 20
c= 5

hasil = a + b
print (a, "+", b,"=", hasil)

hasik = a-c
print (a, "-", c , "=", hasil)

int main() {
    // Mendeklarasikan variabel untuk panjang sisi atas, panjang sisi bawah, dan tinggi trapesium
    float sisi_atas, sisi_bawah, tinggi, luas;

    // Meminta pengguna memasukkan panjang sisi atas, panjang sisi bawah, dan tinggi trapesium
    printf("Masukkan panjang sisi atas trapesium: ");
    scanf("%f", &sisi_atas);
    
    printf("Masukkan panjang sisi bawah trapesium: ");
    scanf("%f", &sisi_bawah);

    printf("Masukkan tinggi trapesium: ");
    scanf("%f", &tinggi);

    // Menghitung luas trapesium menggunakan rumus L = 0.5 * (sisi_atas + sisi_bawah) * tinggi
    luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi;

    // Menampilkan hasil
    printf("Luas trapesium dengan panjang sisi atas %.2f, panjang sisi bawah %.2f, dan tinggi %.2f adalah: %.2f\n", sisi_atas, sisi_bawah, tinggi, luas);

    return 0;
}

#include <stdio.h>

int main() {
    // Mendeklarasikan variabel untuk jari-jari dan luas lingkaran
    float jari_jari, luas;

    // Meminta pengguna memasukkan panjang jari-jari lingkaran
    printf("Masukkan panjang jari-jari lingkaran: ");
    scanf("%f", &jari_jari);

    // Menghitung luas lingkaran menggunakan rumus L = pi * r^2
    luas = 3.14 * jari_jari * jari_jari;

    // Menampilkan hasil
    printf("Luas lingkaran dengan jari-jari %.2f adalah: %.2f\n", jari_jari, luas);

    return 0;
}

#include <stdio.h>

int main() {
    // Mendeklarasikan variabel untuk jari-jari dan keliling lingkaran
    float jari_jari, keliling;

    // Meminta pengguna memasukkan panjang jari-jari lingkaran
    printf("Masukkan panjang jari-jari lingkaran: ");
    scanf("%f", &jari_jari);

    // Menghitung keliling lingkaran menggunakan rumus K = 2 * pi * r
    keliling = 2 * 3.14159 * jari_jari;

    // Menampilkan hasil
    printf("Keliling lingkaran dengan jari-jari %.2f adalah: %.2f\n", jari_jari, keliling);

    return 0;
}
