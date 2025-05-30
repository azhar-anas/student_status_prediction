import streamlit as st
import pandas as pd
from joblib import load

# Set page configuration
st.set_page_config(
    page_title="Prediksi Status Siswa Jaya Jaya Institut",
    page_icon=":mortar_board:",
    layout="centered"
)

# Set Style untuk Streamlit
st.markdown("""
    <style>
        .block-container {
            max-width: 57%;
            padding-top: 4.5rem;
        }
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 1rem;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

# Load model dan scaler
model = load("model/model.h5")
scaler = load("model/scaler.h5")

# Daftar fitur terpilih (urutan harus sesuai training)
selected_features = [
    "Course",
    "Previous_qualification_grade",
    "Admission_grade",
    "Age_at_enrollment",
    "Curricular_units_1st_sem_approved",
    "Curricular_units_1st_sem_grade",
    "Curricular_units_2nd_sem_approved",
    "Curricular_units_2nd_sem_grade"
]

# Opsi input Kategori Program Studi
course_options = {
    33: "Biofuel Production Technologies",
    171: "Animation and Multimedia Design",
    8014: "Social Service (evening attendance)",
    9003: "Agronomy",
    9070: "Communication Design",
    9085: "Veterinary Nursing",
    9119: "Informatics Engineering",
    9130: "Equinculture",
    9147: "Management",
    9238: "Social Service",
    9254: "Tourism",
    9500: "Nursing",
    9556: "Oral Hygiene",
    9670: "Advertising and Marketing Management",
    9773: "Journalism and Communication",
    9853: "Basic Education",
    9991: "Management (evening attendance)"
}

st.title(":mortar_board: Prediksi Status Siswa Jaya Jaya Institut")

st.subheader("Silakan masukkan data siswa sebagai berikut")

# Input form
course_selected = st.selectbox("Program Studi", options=list(course_options.keys()),format_func=lambda x: f"{x} - {course_options[x]}")
prev_qual_grade = st.number_input("Nilai Kualifikasi Institusi Sebelumnya (0 s.d. 200)", min_value=0.0, max_value=200.0, value=100.0, step=0.1)
admission_grade = st.number_input("Nilai Ujian Masuk (0 s.d. 200)", min_value=0.0, max_value=200.0, value=100.0, step=0.1)
age_at_enrollment = st.number_input("Usia Saat Pendaftaran (dalam tahun)", min_value=10, max_value=100, value=18, step=1)
curr_units_1st_approved = st.number_input("Jumlah SKS Lulus Semester 1", min_value=0, max_value=50, value=15, step=1)
curr_units_1st_grade = st.number_input("Nilai Akhir Semester 1 (0 s.d. 20)", min_value=0.0, max_value=20.0, value=10.0, step=0.1)
curr_units_2nd_approved = st.number_input("Jumlah SKS Lulus Semester 2", min_value=0, max_value=50, value=15, step=1)
curr_units_2nd_grade = st.number_input("Nilai Akhir Semester 2 (0 s.d. 20)", min_value=0.0, max_value=20.0, value=10.0, step=0.1)

input_data = [
    course_selected,
    prev_qual_grade,
    admission_grade,
    age_at_enrollment,
    curr_units_1st_approved,
    curr_units_1st_grade,
    curr_units_2nd_approved,
    curr_units_2nd_grade
]

# Tombol untuk memprediksi status siswa
if st.button("Prediksi Status", use_container_width=True):
    # Proses pipeline: scaling
    input_df = pd.DataFrame([input_data], columns=selected_features)
    input_scaled = scaler.transform(input_df)
    input_scaled_df = pd.DataFrame(input_scaled, columns=selected_features)
    # Prediksi
    pred = model.predict(input_scaled_df)[0]
    probabilities = model.predict_proba(input_scaled_df)[0]
    # Mapping label
    label_map = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
    if pred== 0:
        st.error(f":material/error: Siswa kemungkinan akan Dikeluarkan (**Dropout**) dengan probabilitas **{probabilities[0]*100:.2f}%**.")
    elif pred == 1:
        st.warning(f":material/warning: Siswa kemungkinan akan tetap melanjutkan studi (**Enrolled**) dengan probabilitas **{probabilities[1]*100:.2f}%**.")
    else:
        st.success(f" :material/check_circle: Siswa kemungkinan akan Lulus (**Graduate**) dengan probabilitas **{probabilities[2]*100:.2f}%**.")