from flask import Flask, render_template, request
import os

app = Flask(__name__)

def hitung_pph21(penghasilan_bruto, kategori, status_pegawai='tetap', bonus=0, natura=0, bpjs_kesehatan=0, bpjs_ketenagakerjaan=0):
    # Pengurang penghasilan bruto untuk pegawai tetap (Biaya Jabatan: 5% dari bruto, maks Rp500.000/bulan atau Rp6.000.000/tahun + iuran pensiun/JHT jika ada)
    # Namun untuk PPh 21 bulanan masa Januari-November menggunakan TER berdasarkan BRUTO langsung (PP 58/2023)
    # Sedangkan untuk perhitungan setahun penuh atau non-pegawai menggunakan DPP.
    
    total_bruto = penghasilan_bruto + bonus + natura
    
    # Perhitungan TER Bulanan Pegawai Tetap (PP 58 / PMK 168 2023)
    tarif = 0.0
    if status_pegawai == 'tetap':
        if kategori == 'A':
            if total_bruto <= 5400000: tarif = 0.0
            elif total_bruto <= 5650000: tarif = 0.0025
            elif total_bruto <= 5950000: tarif = 0.005
            elif total_bruto <= 6300000: tarif = 0.0075
            elif total_bruto <= 6750000: tarif = 0.01
            elif total_bruto <= 7500000: tarif = 0.015
            elif total_bruto <= 8550000: tarif = 0.02
            elif total_bruto <= 9650000: tarif = 0.025
            elif total_bruto <= 10850000: tarif = 0.03
            elif total_bruto <= 12500000: tarif = 0.04
            elif total_bruto <= 15000000: tarif = 0.05
            elif total_bruto <= 17100000: tarif = 0.06
            elif total_bruto <= 20000000: tarif = 0.07
            elif total_bruto <= 25000000: tarif = 0.08
            elif total_bruto <= 29000000: tarif = 0.09
            elif total_bruto <= 33000000: tarif = 0.10
            elif total_bruto <= 38000000: tarif = 0.11
            elif total_bruto <= 43000000: tarif = 0.12
            elif total_bruto <= 50000000: tarif = 0.13
            elif total_bruto <= 60000000: tarif = 0.14
            elif total_bruto <= 75000000: tarif = 0.15
            elif total_bruto <= 100000000: tarif = 0.17
            elif total_bruto <= 125000000: tarif = 0.18
            elif total_bruto <= 250000000: tarif = 0.25
            elif total_bruto <= 500000000: tarif = 0.30
            else: tarif = 0.34
        elif kategori == 'B':
            if total_bruto <= 6200000: tarif = 0.0
            elif total_bruto <= 6500000: tarif = 0.0025
            elif total_bruto <= 6850000: tarif = 0.005
            elif total_bruto <= 7300000: tarif = 0.0075
            elif total_bruto <= 7900000: tarif = 0.01
            elif total_bruto <= 8900000: tarif = 0.015
            elif total_bruto <= 10100000: tarif = 0.02
            elif total_bruto <= 11400000: tarif = 0.025
            elif total_bruto <= 12800000: tarif = 0.03
            elif total_bruto <= 14800000: tarif = 0.04
            elif total_bruto <= 17800000: tarif = 0.05
            elif total_bruto <= 20200000: tarif = 0.06
            elif total_bruto <= 23600000: tarif = 0.07
            elif total_bruto <= 29400000: tarif = 0.08
            elif total_bruto <= 34000000: tarif = 0.09
            elif total_bruto <= 39000000: tarif = 0.10
            elif total_bruto <= 45000000: tarif = 0.11
            elif total_bruto <= 51000000: tarif = 0.12
            elif total_bruto <= 59000000: tarif = 0.13
            elif total_bruto <= 70000000: tarif = 0.14
            elif total_bruto <= 88000000: tarif = 0.15
            elif total_bruto <= 115000000: tarif = 0.17
            elif total_bruto <= 145000000: tarif = 0.18
            elif total_bruto <= 280000000: tarif = 0.25
            elif total_bruto <= 550000000: tarif = 0.30
            else: tarif = 0.34
        elif kategori == 'C':
            if total_bruto <= 6600000: tarif = 0.0
            elif total_bruto <= 6950000: tarif = 0.0025
            elif total_bruto <= 7350000: tarif = 0.005
            elif total_bruto <= 7800000: tarif = 0.0075
            elif total_bruto <= 8400000: tarif = 0.01
            elif total_bruto <= 9400000: tarif = 0.015
            elif total_bruto <= 10700000: tarif = 0.02
            elif total_bruto <= 12100000: tarif = 0.025
            elif total_bruto <= 13600000: tarif = 0.03
            elif total_bruto <= 15700000: tarif = 0.04
            elif total_bruto <= 18900000: tarif = 0.05
            elif total_bruto <= 21500000: tarif = 0.06
            elif total_bruto <= 25000000: tarif = 0.07
            elif total_bruto <= 31300000: tarif = 0.08
            elif total_bruto <= 36000000: tarif = 0.09
            elif total_bruto <= 41000000: tarif = 0.10
            elif total_bruto <= 47000000: tarif = 0.11
            elif total_bruto <= 54000000: tarif = 0.12
            elif total_bruto <= 62000000: tarif = 0.13
            elif total_bruto <= 73000000: tarif = 0.14
            elif total_bruto <= 92000000: tarif = 0.15
            elif total_bruto <= 118000000: tarif = 0.17
            elif total_bruto <= 153000000: tarif = 0.18
            elif total_bruto <= 300000000: tarif = 0.25
            elif total_bruto <= 580000000: tarif = 0.30
            else: tarif = 0.34
        pph21 = total_bruto * tarif
        effective_rate = tarif * 100

    elif status_pegawai == 'tidak_tetap':
        # Bukan Pegawai / Freelancer: DPP 50% dari bruto, dikenakan lapis pertama Pasal 17 (5%)
        dpp = total_bruto * 0.50
        pph21 = dpp * 0.05
        effective_rate = 5.0

    elif status_pegawai == 'pesangon':
        # PPh Final Pesangon (PP No. 68 Tahun 2009)
        if total_bruto <= 50000000: pph21 = 0.0; effective_rate = 0.0
        elif total_bruto <= 100000000: pph21 = (total_bruto - 50000000) * 0.05; effective_rate = 5.0
        elif total_bruto <= 500000000: pph21 = 2500000 + (total_bruto - 100000000) * 0.15; effective_rate = 15.0
        else: pph21 = 62500000 + (total_bruto - 500000000) * 0.25; effective_rate = 25.0

    return round(pph21, 2), round(effective_rate, 2), total_bruto

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pph21', methods=['GET', 'POST'])
def kalkulator_pph21():
    result = None
    if request.method == 'POST':
        nama = request.form['nama']
        bruto = float(request.form['bruto'])
        kategori = request.form['kategori']
        status_pegawai = request.form.get('status_pegawai', 'tetap')
        bonus = float(request.form.get('bonus', 0) or 0)
        natura = float(request.form.get('natura', 0) or 0)
        
        pajak, persentase, total_bruto = hitung_pph21(bruto, kategori, status_pegawai, bonus, natura)
        neto = total_bruto - pajak
        result = {
            'nama': nama,
            'bruto': bruto,
            'bonus': bonus,
            'natura': natura,
            'total_bruto': total_bruto,
            'kategori': kategori,
            'status_pegawai': status_pegawai,
            'persentase': persentase,
            'pajak': pajak,
            'neto': neto
        }
    return render_template('pph21.html', result=result)

@app.route('/ppn', methods=['GET', 'POST'])
def kalkulator_ppn():
    result = None
    if request.method == 'POST':
        dpp_keluaran = float(request.form['dpp_keluaran'])
        dpp_masukan = float(request.form['dpp_masukan'])
        
        # PPN 12% (Berlaku efektif sesuai UU HPP / ketentuan terbaru 2026)
        ppn_keluaran = dpp_keluaran * 0.12
        ppn_masukan = dpp_masukan * 0.12
        selisih = ppn_keluaran - ppn_masukan
        
        status = "Kurang Bayar (Kurang Disetor)" if selisih > 0 else ("Lebih Bayar" if selisih < 0 else "Nihil")
        
        result = {
            'dpp_keluaran': dpp_keluaran,
            'ppn_keluaran': ppn_keluaran,
            'dpp_masukan': dpp_masukan,
            'ppn_masukan': ppn_masukan,
            'selisih': abs(selisih),
            'status': status
        }
    return render_template('ppn.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
