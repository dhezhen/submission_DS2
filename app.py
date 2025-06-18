import streamlit as st 
import pandas as pd
from joblib import load

st.set_page_config(layout="wide", page_title="Student Dropout Prediction App", page_icon=":school_satchel:")
st.title("Aplikasi Prediksi Dropout Siswa")
st.write("Fill in the details below to predict the likelihood of student dropout.")

data = pd.read_csv("filtered_data.csv", delimiter=",")

category_mapping = {
    33: 'Biofuel Production Technologies',
    171: 'Animation and Multimedia Design',
    8014: 'Social Service (evening attendance)',
    9003: 'Agronomy',
    9070: 'Communication Design',
    9085: 'Veterinary Nursing',
    9119: 'Informatics Engineering',
    9130: 'Equinculture',
    9147: 'Management',
    9238: 'Social Service',
    9254: 'Tourism',
    9500: 'Nursing',
    9556: 'Oral Hygiene',
    9670: 'Advertising and Marketing Management',
    9773: 'Journalism and Communication',
    9853: 'Basic Education',
    9991: 'Management (evening attendance)'
}
data['Course_Label'] = data['Course'].replace(category_mapping)

course_list = sorted(list(data.Course_Label.unique()))
course_selected_label = st.selectbox('Course', ['Select a course...'] + course_list)

if course_selected_label == 'Select a course...':
    st.error("Please select a valid course.")
    st.stop()

reverse_mapping = {v: k for k, v in category_mapping.items()}
course_selected = reverse_mapping[course_selected_label]

# Attendance time
time_selected = 0 if course_selected in [9991, 8014] else 1

Gender, Age = st.columns(2)
with Gender:
    gender_selected = st.selectbox('Gender', ['Male', 'Female'])
    gender_selected = 1 if gender_selected == "Male" else 0

with Age:
    age_selected = st.number_input("Age at enrollment", step=1, min_value=17, max_value=70)

application_mode, application_order_col = st.columns(2)
with application_mode:
    application_mode_selected = st.radio('Application mode', ['Regular', 'Special'])
    application_mode_selected = 1 if application_mode_selected == "Special" else 0

with application_order_col:
    application_order_selected = st.number_input("Application Order", min_value=1, step=1, key="application_order")

tuition_selected, scholarship_selected = st.columns(2)
with tuition_selected:
    tuition_selected = st.radio('Tuition up to date?', ['No', 'Yes'])
    tuition_selected = 1 if tuition_selected == "Yes" else 0

with scholarship_selected:
    scholarship_selected = st.radio('Scholarship holder?', ['No', 'Yes'])
    scholarship_selected = 1 if scholarship_selected == "Yes" else 0

grade1, grade2 = st.columns(2)
with grade1:   
    grade1_selected = st.number_input("First semester grade", value=0.0, step=0.1, min_value=0.0, max_value=20.0)
    grade1_selected = round(grade1_selected, 2)

with grade2:
    grade2_selected = st.number_input("Second semester grade", value=0.0, step=0.1, min_value=0.0, max_value=20.0)
    grade2_selected = round(grade2_selected, 2)
    
approved1, approved2 = st.columns(2)
with approved1:   
    approved1_selected = st.radio('First semester approved?', ['No', 'Yes'])
    approved1_selected = 1 if approved1_selected == "Yes" else 0

with approved2:
    approved2_selected = st.radio('Second semester approved?', ['No', 'Yes'])
    approved2_selected = 1 if approved2_selected == "Yes" else 0

marital_status_col, debtor = st.columns(2)
with marital_status_col:
    marital_status_selected = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"], key="marital_status") 
    marital_status_selected = {"Single": 0, "Married": 1, "Divorced": 2, "Widowed": 3}[marital_status_selected]
with debtor:
    debtor_selected = st.radio('Debtor?', ['No', 'Yes'])
    debtor_selected = 1 if debtor_selected == "Yes" else 0

day_time, admission_grade_selected = st.columns(2)
with day_time:
    day_time_selected = st.radio('Daytime/Evening attendance', ['Daytime', 'Evening'])
    day_time_selected = 1 if day_time_selected == "Evening" else 0

with admission_grade_selected:
    admission_grade_selected = st.number_input("Admission grade", value=0.0, step=0.1, min_value=0.0, max_value=200.0)
    admission_grade_selected = round(admission_grade_selected, 1)


curricular_units_1st_sem_approved, curricular_units_2nd_sem_approved = st.columns(2)
with curricular_units_1st_sem_approved:
    curricular_units_1st_sem_approved = st.number_input("1st Sem Units Approved", min_value=0, step=1, key="1st_sem_approved")

with curricular_units_2nd_sem_approved:
    curricular_units_2nd_sem_approved = st.number_input("2nd Sem Units Approved", min_value=0, step=1, key="2nd_sem_approved")

curricular_units_1st_sem_enrolled, curricular_units_2nd_sem_enrolled = st.columns(2)
with curricular_units_1st_sem_enrolled:
    curricular_units_1st_sem_enrolled = st.number_input("1st Sem Units Enrolled", min_value=0, step=1, key="1st_sem_enrolled")

with curricular_units_2nd_sem_enrolled:
    curricular_units_2nd_sem_enrolled = st.number_input("2nd Sem Units Enrolled", min_value=0, step=1, key="2nd_sem_enrolled")


curricular_units_1st_sem_grade, curricular_units_2nd_sem_grade = st.columns(2)
with curricular_units_1st_sem_grade:
    curricular_units_1st_sem_grade = st.number_input("1st Sem Units Grade", min_value=0.0, max_value=20.0, step=0.1, key="1st_sem_grade")
    curricular_units_1st_sem_grade = round(curricular_units_1st_sem_grade, 2)

with curricular_units_2nd_sem_grade:
    curricular_units_2nd_sem_grade = st.number_input("2nd Sem Units Grade", min_value=0.0, max_value=20.0, step=0.1, key="2nd_sem_grade")
    curricular_units_2nd_sem_grade = round(curricular_units_2nd_sem_grade, 2)

# Tampilkan ringkasan input sebelum prediksi
st.subheader("Summary of Your Inputs")
summary_data = {
    "Course": course_selected_label,
    "Marital Status": marital_status_selected,
    "Application Mode": "Special" if application_mode_selected else "Regular",
    "Application Order": application_order_selected,
    "Daytime/Evening Attendance": "Evening" if day_time_selected else "Daytime",
    "Admission Grade": admission_grade_selected,
    "Debtor": "Yes" if debtor_selected else "No",
    "Tuition Fees Up To Date": "Yes" if tuition_selected else "No",
    "Gender": "Male" if gender_selected else "Female",
    "Scholarship Holder": "Yes" if scholarship_selected else "No",
    "Age at Enrollment": age_selected,
    "1st Sem Units Approved": curricular_units_1st_sem_approved,
    "1st Sem Units Grade": curricular_units_1st_sem_grade,
    "2nd Sem Units Grade": curricular_units_2nd_sem_grade,
    "2nd Sem Units Approved": curricular_units_2nd_sem_approved,
}
st.table(pd.DataFrame([summary_data]))

button_predict = st.button("Predict", key='custom_button')

if button_predict:
    try:
        model = load('model.joblib')

        user_data = {
        "Marital_status": [marital_status_selected], # Use the correct variable
        "Application_mode": [application_mode_selected],
        "Application_order": [application_order_selected],
        "Course": [course_selected],      
        "Daytime_evening_attendance": [day_time_selected],
        "Admission_grade": [admission_grade_selected],
        "Debtor": [debtor_selected],
        "Tuition_fees_up_to_date": [tuition_selected],
        "Gender": [gender_selected],
        "Scholarship_holder": [scholarship_selected],
        "Age_at_enrollment": [age_selected],
        "Curricular_units_1st_sem_approved": [curricular_units_1st_sem_approved],
        "Curricular_units_1st_sem_grade": [curricular_units_1st_sem_grade],
        "Curricular_units_2nd_sem_approved": [curricular_units_2nd_sem_approved],
        "Curricular_units_2nd_sem_grade": [curricular_units_2nd_sem_grade]
        }
        X_new = pd.DataFrame(user_data)
        predictions = model.predict(X_new)
        st.subheader("Hasil Prediksi")
        if predictions[0] == 0:
            st.write("Siswa kemungkinan besar akan dropout.")
        elif predictions[0] == 1:
            st.write("Siswa kemungkinan besar TIDAK akan dropout.")
        else:
            st.write("Hasil prediksi tidak jelas.")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memuat model atau melakukan prediksi: {e}")
