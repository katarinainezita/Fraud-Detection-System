# 📊 Fraud Detection System
Fraud Detection System adalah proyek yang digunakan untuk mendeteksi transaksi yang mencurigakan dengan pendekatan Machine Learning dan Generative Adversarial Networks (GAN).

## 🚀 Deskripsi Proyek
Proyek ini mencakup berbagai model Machine Learning dan GAN sebagai metode perbandingan performa:

### 🔍 Machine Learning Models
- CatBoost
- Isolation Forest
- LightGBM
- Random Forest
- XGBoost

### 🧠 Generative Adversarial Networks (GAN)
- AnoGAN
- CGAN

### Dataset : 
1. https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023

2. https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud


## Anggota Kelompok 11

| No.  | Nama Anggota       | NRP          |
|------|--------------------|--------------|
| 1    |Katarina Inezita Prambudi    | 5025211148   |
| 2    | Najma Ulya Agustina         | 5025211239   |
| 3    | Sekar Ambar Arum | 5025211041 |
|4 | Dian Lies Dabukke | 5025211080|
|5 | Nadiah Nuri Aisyah | 5025211210 |

## ▶️ Cara Menjalankan Proyek

### 1. Clone Repository

```
git clone https://github.com/katarinainezita/Fraud-Detection-System.git

```

### 2. Jalankan Aplikasi Flask
```
python app.py
```

### 3. Akses Aplikasi di Browser
```
http://127.0.0.1:5000
```

## 📈 Perbandingan Performa

### Skenario 1 ( Dataset 1, Tanpa KFold CV)
|Model|Random Forest|XGBoost|CatBoost|LightGBM|Isolation Forest|AnoGAN|CGAN|
|------|------------|-------|--------|--------|----------------|------|----|
| Akurasi |0.9998|0.9995|0.9992|0.9983|0.4232|0.5300|0.5232|

### Skenario 2 ( Dataset 1, Dengan KFold CV)
|Model|Random Forest|XGBoost|CatBoost|LightGBM|Isolation Forest|AnoGAN|CGAN|
|------|------------|-------|--------|--------|----------------|------|----|
| Akurasi |0.9998|0.9995|0.9991|0.9984|0.4203|0.5500|0.5010|

### Skenario 3 ( Dataset 2, Tanpa KFold CV)
|Model|Random Forest|XGBoost|CatBoost|LightGBM|Isolation Forest|AnoGAN|CGAN|
|------|------------|-------|--------|--------|----------------|------|----|
| Akurasi |0.9997|0.9992|0.9994|0.9968|0.4064|0.6683|0.9973|

### Skenario 4 ( Dataset 2, Dengan KFold CV)
|Model|Random Forest|XGBoost|CatBoost|LightGBM|Isolation Forest|AnoGAN|CGAN|
|------|------------|-------|--------|--------|----------------|------|----|
| Akurasi |0.9997|0.9992|0.9996|0.9967|0.4203|0.9481|0.7818|


## 📊 Input dan Output

### Input 

![image](https://github.com/user-attachments/assets/c9632911-5147-46ff-8e48-22114b9be36a)

### Output 

#### Fraud
![image_2024-12-19_13-38-36](https://github.com/user-attachments/assets/6fdb1339-92d1-4df2-8286-d678935201bb)

#### Bukan Fraud
![image](https://github.com/user-attachments/assets/4b4ee02b-df9c-4ec3-8b68-cf343bd20d54)
