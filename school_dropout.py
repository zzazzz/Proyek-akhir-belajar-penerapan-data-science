import streamlit as st
import pandas as pd
from data_preprocessing import preprocess_data
from prediction import prediction  # Mengimpor fungsi prediction yang benar

# Judul aplikasi
st.title("Prediksi Dropout Mahasiswa")

# Form untuk input data
with st.form(key='input_form'):
    marital_status = st.selectbox('Marital Status', ['single', 'married', 'widower', 'divorced', 'facto union', 'legally separated'])
    application_mode = st.selectbox('Application Mode', ['1st phase - general contingent', 'Ordinance No. 612/93', '1st phase - special contingent (Azores Island)', 'Holders of other higher courses', 'Ordinance No. 854-B/99', 'International student (bachelor)', '1st phase - special contingent (Madeira Island)', '2nd phase - general contingent', '3rd phase - general contingent', 'Ordinance No. 533-A/99, item b2 (Different Plan)', 'Ordinance No. 533-A/99, item b3 (Other Institution)', 'Over 23 years old', 'Transfer', 'Change of course', 'Technological specialization diploma holders', 'Change of institution/course', 'Short cycle diploma holders', 'Change of institution/course (International)'])
    application_order = st.number_input('Application Order', min_value=0, max_value=9)
    course = st.selectbox('Course', ['Biofuel Production Technologies', 'Animation and Multimedia Design', 'Social Service (evening attendance)', 'Agronomy', 'Communication Design', 'Veterinary Nursing', 'Informatics Engineering', 'Equinculture', 'Management', 'Social Service', 'Tourism', 'Nursing', 'Oral Hygiene', 'Advertising and Marketing Management', 'Journalism and Communication', 'Basic Education', 'Management (evening attendance)'])
    daytime_evening_attendance = st.selectbox('Daytime/Evening Attendance', ['daytime', 'evening'])
    previous_qualification = st.selectbox('Previous Qualification', ['Secondary education', 'Higher education - bachelor\'s degree', 'Higher education - degree', 'Higher education - master\'s', 'Higher education - doctorate', 'Frequency of higher education', '12th year of schooling - not completed', '11th year of schooling - not completed', 'Other - 11th year of schooling', '10th year of schooling', '10th year of schooling - not completed', 'Basic education 3rd cycle (9th/10th/11th year) or equiv.', 'Basic education 2nd cycle (6th/7th/8th year) or equiv.', 'Technological specialization course', 'Higher education - degree (1st cycle)', 'Professional higher technical course', 'Higher education - master (2nd cycle)'])
    previous_qualification_grade = st.number_input('Previous Qualification Grade', min_value=0, max_value=200)
    nationality = st.selectbox('Nationality', ['Portuguese', 'German', 'Spanish', 'Italian', 'Dutch', 'English', 'Lithuanian', 'Angolan', 'Cape Verdean', 'Guinean', 'Mozambican', 'Santomean', 'Turkish', 'Brazilian', 'Romanian', 'Moldova (Republic of)', 'Mexican', 'Ukrainian', 'Russian', 'Cuban', 'Colombian'])
    mothers_qualification = st.selectbox('Mother\'s Qualification', ['Secondary Education - 12th Year of Schooling or Eq.', 'Higher Education - Bachelor\'s Degree', 'Higher Education - Degree', 'Higher Education - Master\'s', 'Higher Education - Doctorate'])
    fathers_qualification = st.selectbox('Father\'s Qualification', ['Secondary Education - 12th Year of Schooling or Eq.', 'Higher Education - Bachelor\'s Degree', 'Higher Education - Degree', 'Higher Education - Master\'s', 'Higher Education - Doctorate'])
    displaced = st.selectbox('Displaced', ['yes', 'no'])
    educational_special_needs = st.selectbox('Educational Special Needs', ['yes', 'no'])
    debtor = st.selectbox('Debtor', ['yes', 'no'])
    tuition_fees_up_to_date = st.selectbox('Tuition Fees Up To Date', ['yes', 'no'])
    gender = st.selectbox('Gender', ['male', 'female'])
    scholarship_holder = st.selectbox('Scholarship Holder', ['yes', 'no'])
    international = st.selectbox('International', ['yes', 'no'])

    # Input untuk semester 1
    curricular_units_1st_sem_enrolled = st.number_input('Curricular Units 1st Sem Enrolled', min_value=0, max_value=26)
    curricular_units_1st_sem_evaluations = st.number_input('Curricular Units 1st Sem Evaluations', min_value=0, max_value=45)
    curricular_units_1st_sem_approved = st.number_input('Curricular Units 1st Sem Approved', min_value=0, max_value=26)
    curricular_units_1st_sem_grade = st.number_input('Curricular Units 1st Sem Grade', min_value=0, max_value=20)

    # Input untuk semester 2
    curricular_units_2nd_sem_enrolled = st.number_input('Curricular Units 2nd Sem Enrolled', min_value=0, max_value=23)
    curricular_units_2nd_sem_evaluations = st.number_input('Curricular Units 2nd Sem Evaluations', min_value=0, max_value=33)
    curricular_units_2nd_sem_approved = st.number_input('Curricular Units 2nd Sem Approved', min_value=0, max_value=20)
    curricular_units_2nd_sem_grade = st.number_input('Curricular Units 2nd Sem Grade', min_value=0, max_value=20)

    # Input untuk faktor ekonomi
    unemployment_rate = st.number_input('Unemployment Rate (%)', min_value=0, max_value=100)
    inflation_rate = st.number_input('Inflation Rate (%)', min_value=0, max_value=100)
    gdp = st.number_input('GDP (Billion)')

    # Submit button
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    # Menyiapkan data untuk prediksi
    input_data = pd.DataFrame({
        'Marital_status': [marital_status],
        'Application_mode': [application_mode],
        'Application_order': [application_order],
        'Course': [course],
        'Daytime_evening_attendance': [daytime_evening_attendance],
        'Previous_qualification': [previous_qualification],
        'Previous_qualification_grade': [previous_qualification_grade],
        'Nacionality': [nationality],
        'Mothers_qualification': [mothers_qualification],
        'Fathers_qualification': [fathers_qualification],
        'Displaced': [displaced],
        'Educational_special_needs': [educational_special_needs],
        'Debtor': [debtor],
        'Tuition_fees_up_to_date': [tuition_fees_up_to_date],
        'Gender': [gender],
        'Scholarship_holder': [scholarship_holder],
        'International': [international],
        'Curricular_units_1st_sem_enrolled': [curricular_units_1st_sem_enrolled],
        'Curricular_units_1st_sem_evaluations': [curricular_units_1st_sem_evaluations],
        'Curricular_units_1st_sem_approved': [curricular_units_1st_sem_approved],
        'Curricular_units_1st_sem_grade': [curricular_units_1st_sem_grade],
        'Curricular_units_2nd_sem_enrolled': [curricular_units_2nd_sem_enrolled],
        'Curricular_units_2nd_sem_evaluations': [curricular_units_2nd_sem_evaluations],
        'Curricular_units_2nd_sem_approved': [curricular_units_2nd_sem_approved],
        'Curricular_units_2nd_sem_grade': [curricular_units_2nd_sem_grade],
        'Unemployment_rate': [unemployment_rate],
        'Inflation_rate': [inflation_rate],
        'GDP': [gdp]
    })

    # Melakukan preprocessing pada data
    preprocessed_data = preprocess_data(input_data)

    # Melakukan prediksi
    result = prediction(preprocessed_data)  # Menggunakan fungsi prediction yang benar

    # Menampilkan hasil prediksi
    if result[0] == 0:
        st.write("Prediksi: Mahasiswa Tidak Dropout")
    else:
        st.write("Prediksi: Mahasiswa Dropout")
