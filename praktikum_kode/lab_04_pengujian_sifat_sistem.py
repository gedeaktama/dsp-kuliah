"""
Laboratorium 04: Pengujian Empiris & Formal Sifat Sistem Waktu Diskrit
Mata Kuliah: Pengolahan Sinyal Digital - Universitas Nusantara Manado
Dosen Pengampu: Gede Erik Aktama, S.Pd., M.Pd.
Capaian Pembelajaran: CPMK 2 (CPL-A, CPL-B)
"""

import numpy as np

def test_linearity(system_func, N=50, tolerance=1e-5):
    x1 = np.random.randn(N)
    x2 = np.random.randn(N)
    a, b = 2.5, -1.7
    
    # Jalur A: Transformasi kombinasi linear masukan
    y_combo = system_func(a * x1 + b * x2)
    # Jalur B: Kombinasi linear dari masing-masing keluaran
    y_sep = a * system_func(x1) + b * system_func(x2)
    
    max_diff = np.max(np.abs(y_combo - y_sep))
    return max_diff < tolerance, max_diff

def test_time_invariance(system_func, N=50, delay=3, tolerance=1e-5):
    x = np.random.randn(N)
    # Geser input x sejauh delay
    x_delayed = np.roll(x, delay)
    x_delayed[:delay] = 0.0 # Clear circular wrap
    
    # Respons terhadap input tergeser
    y_from_delayed_x = system_func(x_delayed)
    
    # Output asli digeser
    y_orig = system_func(x)
    y_delayed = np.roll(y_orig, delay)
    y_delayed[:delay] = 0.0
    
    max_diff = np.max(np.abs(y_from_delayed_x[delay:] - y_delayed[delay:]))
    return max_diff < tolerance, max_diff

def main():
    print("=== LAB 04: OTOMASI PENGUJIAN SIFAT SISTEM DISKRIT ===")
    
    systems = {
        "Sistem A: y[n] = 3 x[n] + 2 x[n-1] (LTI)": lambda x: 3.0 * x + 2.0 * np.roll(x, 1),
        "Sistem B: y[n] = (x[n])^2 (Non-Linear)": lambda x: x ** 2,
        "Sistem C: y[n] = n * x[n] (Time-Varying)": lambda x: np.arange(len(x)) * x,
        "Sistem D: y[n] = x[n] + 5.0 (Affine / Non-Linear)": lambda x: x + 5.0
    }
    
    print(f"{'Nama Sistem':<45} | {'Linear?':<8} | {'TI?':<8}")
    print("-" * 68)
    for name, func in systems.items():
        is_lin, _ = test_linearity(func)
        is_ti, _ = test_time_invariance(func)
        print(f"{name:<45} | {str(is_lin):<8} | {str(is_ti):<8}")

if __name__ == '__main__':
    main()
