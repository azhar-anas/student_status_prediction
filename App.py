import streamlit as st
import pandas as pd
from joblib import load

# Set page configuration
st.set_page_config(
    page_title="Student Status Prediction - Jaya Jaya Institute",
    page_icon=":mortar_board:",
    layout="centered"
)

# Set Style for Streamlit
st.markdown("""
    <style>
        .block-container {
            max-width: 50%;
            padding-top: 4.5rem;
        }
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 1rem;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

# Load model and scaler
model = load("model/model.h5")
scaler = load("model/scaler.h5")

# Selected features (order must match training)
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

# Study Program Category Options
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

st.title(":mortar_board: Student Status Prediction")

st.subheader("Please enter the student data below")

# Input form
course_selected = st.selectbox("Study Program", options=list(course_options.keys()), format_func=lambda x: f"{x} - {course_options[x]}")
prev_qual_grade = st.number_input("Previous Institution Qualification Grade (0 to 200)", min_value=0.0, max_value=200.0, value=100.0, step=0.1)
admission_grade = st.number_input("Admission Exam Grade (0 to 200)", min_value=0.0, max_value=200.0, value=100.0, step=0.1)
age_at_enrollment = st.number_input("Age at Enrollment (years)", min_value=10, max_value=100, value=18, step=1)
curr_units_1st_approved = st.number_input("Number of Passed Credits in 1st Semester", min_value=0, max_value=50, value=15, step=1)
curr_units_1st_grade = st.number_input("Final Grade 1st Semester (0 to 20)", min_value=0.0, max_value=20.0, value=10.0, step=0.1)
curr_units_2nd_approved = st.number_input("Number of Passed Credits in 2nd Semester", min_value=0, max_value=50, value=15, step=1)
curr_units_2nd_grade = st.number_input("Final Grade 2nd Semester (0 to 20)", min_value=0.0, max_value=20.0, value=10.0, step=0.1)

# Map Course key to 0-16 index range
course_key_to_index = {key: idx for idx, key in enumerate(sorted(course_options.keys()))}
course_index = course_key_to_index[course_selected]

input_data = [
    course_index,
    prev_qual_grade,
    admission_grade,
    age_at_enrollment,
    curr_units_1st_approved,
    curr_units_1st_grade,
    curr_units_2nd_approved,
    curr_units_2nd_grade
]

# Button to predict student status
if st.button("Predict Status", use_container_width=True):
    # Pipeline process: scaling
    input_df = pd.DataFrame([input_data], columns=selected_features)
    input_scaled = scaler.transform(input_df)
    input_scaled_df = pd.DataFrame(input_scaled, columns=selected_features)
    # Prediction
    pred = model.predict(input_scaled_df)[0]
    probabilities = model.predict_proba(input_scaled_df)[0]
    # Label mapping
    label_map = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
    if pred == 0:
        st.error(f":material/error: The student is likely to Dropout with probability **{probabilities[0]*100:.2f}%**.")
    elif pred == 1:
        st.warning(f":material/warning: The student is likely to remain Enrolled with probability **{probabilities[1]*100:.2f}%**.")
    else:
        st.success(f":material/check_circle: The student is likely to Graduate with probability **{probabilities[2]*100:.2f}%**.")
