import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

# Definisikan transformer khusus untuk menangani outlier
class OutlierHandler(BaseEstimator, TransformerMixin):
    def __init__(self, cols):
        """
        Inisialisasi OutlierHandler.
        
        Parameters:
        cols: list of str
            Nama kolom yang ingin diproses untuk mengatasi outlier.
        """
        self.cols = cols
        self.lower_bounds = {}
        self.upper_bounds = {}

    def fit(self, X, y=None):
        """
        Hitung batas bawah dan atas untuk outlier berdasarkan IQR (Interquartile Range).
        
        Parameters:
        X: DataFrame
            Data untuk mempelajari batas bawah dan atas dari setiap kolom.
        y: None
            Parameter tambahan, tidak digunakan dalam kasus ini.
        
        Returns:
        self: OutlierHandler
            Mengembalikan objek ini setelah fit.
        """
        for col in self.cols:
            # Menghitung kuartil pertama dan kuartil ketiga untuk setiap kolom
            Q1 = X[col].quantile(0.25)
            Q3 = X[col].quantile(0.75)
            IQR = Q3 - Q1
            # Menentukan batas bawah dan atas untuk mendeteksi outlier
            self.lower_bounds[col] = Q1 - 1.5 * IQR
            self.upper_bounds[col] = Q3 + 1.5 * IQR
        return self

    def transform(self, X):
        """
        Transformasi data dengan mengatasi outlier, dengan memotong nilai di luar batas.
        
        Parameters:
        X: DataFrame
            Data yang akan ditransformasi (nilai outlier akan dipotong).
        
        Returns:
        X: DataFrame
            Data setelah outlier dipotong sesuai batas bawah dan atas.
        """
        X = X.copy()  # Membuat salinan data untuk menghindari perubahan data asli
        for col in self.cols:
            lower = self.lower_bounds[col]
            upper = self.upper_bounds[col]
            # Mengganti nilai di luar batas dengan batas yang sesuai
            X[col] = np.clip(X[col], lower, upper)
        return X