from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from model import simulasi_sistem

app = Flask(__name__)
UPLOAD_FOLDER = "static"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    file = request.files['dataset']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Load dataset
    data = pd.read_csv(filepath)
    data['year'] = pd.to_datetime(data['year'], format='%Y')

    # Produksi tahunan
    prod_year = data.groupby(data['year'].dt.year)['production'].sum()
    produksi_rata2 = prod_year.mean()

    # Simulasi
    tahun_simulasi = np.arange(2020, 2041)
    stok_normal, prod_n, kons_n = simulasi_sistem(produksi_rata2, "normal")
    stok_optimis, prod_o, kons_o = simulasi_sistem(produksi_rata2, "optimis")
    stok_pesimis, prod_p, kons_p = simulasi_sistem(produksi_rata2, "pesimis")

    # Plot hasil simulasi
    plt.figure(figsize=(10, 5))
    plt.plot(tahun_simulasi, stok_normal[:-1], label="Normal")
    plt.plot(tahun_simulasi, stok_optimis[:-1], label="Optimis")
    plt.plot(tahun_simulasi, stok_pesimis[:-1], label="Pesimis")
    plt.title("Simulasi Sistem Dinamik Stok Beras (2020–2040)")
    plt.xlabel("Tahun")
    plt.ylabel("Stok (ton)")
    plt.legend()
    plot_path = os.path.join("static", "hasil_simulasi.png")
    plt.savefig(plot_path)
    plt.close()

    return render_template("result.html",
                           plot_path=plot_path,
                           produksi=round(produksi_rata2, 2))
    

if __name__ == "__main__":
    app.run(debug=True)
