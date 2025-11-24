import numpy as np

tahun_simulasi = np.arange(2020, 2041)

penduduk_awal = 275_000_000
pertumbuhan_penduduk = 0.008
konsumsi_perkapita = 90

def hitung_konsumsi(tahun_ke):
    penduduk = penduduk_awal * ((1 + pertumbuhan_penduduk) ** tahun_ke)
    konsumsi = penduduk * konsumsi_perkapita / 1000
    return konsumsi


def simulasi_sistem(produksi_awal, skenario):
    stok = [2_000_000]
    produksi_list = []
    konsumsi_list = []

    for i, tahun in enumerate(tahun_simulasi):

        if skenario == "optimis":
            produksi = produksi_awal * 1.1
        elif skenario == "pesimis":
            produksi = produksi_awal * 0.9
        else:
            produksi = produksi_awal

        konsumsi = hitung_konsumsi(i)
        produksi_list.append(produksi)
        konsumsi_list.append(konsumsi)

        stok_baru = stok[-1] + produksi - konsumsi
        stok.append(stok_baru)

    return stok, produksi_list, konsumsi_list
