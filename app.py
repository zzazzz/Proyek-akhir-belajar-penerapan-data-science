import pandas as pd
import joblib
import numpy as np
import streamlit as st
from sklearn.base import BaseEstimator, TransformerMixin

# Definisi class OutlierHandler
class OutlierHandler(BaseEstimator, TransformerMixin):
    def __init__(self, cols):
        self.cols = cols
        self.lower_bounds = {}
        self.upper_bounds = {}

    def fit(self, X, y=None):
        for col in self.cols:
            Q1 = X[col].quantile(0.25)
            Q3 = X[col].quantile(0.75)
            IQR = Q3 - Q1
            self.lower_bounds[col] = Q1 - 1.5 * IQR
            self.upper_bounds[col] = Q3 + 1.5 * IQR
        return self

    def transform(self, X):
        X = X.copy()  # Menghindari perubahan pada X asli
        for col in self.cols:
            lower = self.lower_bounds[col]
            upper = self.upper_bounds[col]
            X[col] = np.clip(X[col], lower, upper)  # Mengatasi outlier
        return X

# Muat model dan encoder saat aplikasi dimulai
outlier_handler_pipeline = joblib.load('model/outlier_handler_pipeline.joblib')
encoders = joblib.load('model/encoder.joblib')

def preprocess_data(form_input):
    # Create a DataFrame directly from the input dictionary
    data_df = pd.DataFrame(form_input, index=[0])  # Ensure it is 2D with a single row

    # Kolom kategori
    category_cols = data_df.select_dtypes(include=['category', 'object']).columns.tolist()

    # Lakukan encoding untuk kolom kategori
    for col in category_cols:
        encoder = encoders[col]  # Mengambil encoder yang sesuai dengan kolom
        data_df[col] = encoder.transform(data_df[col])  # Lakukan transformasi
        encoders[col] = encoder  # Simpan encoder untuk kolom tersebut

    # Columns to process for outlier handling
    columns_to_process = [
        'Admission_grade', 'Age_at_enrollment',
        'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_evaluations',
        'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
        'Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_evaluations',
        'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade'
    ]
    
    # Apply outlier handler
    data_df[columns_to_process] = outlier_handler_pipeline.transform(data_df[columns_to_process])

    # Return the processed data
    return data_df


# Fungsi untuk melakukan prediksi
def prediction(data):
    # Memuat model prediksi yang telah dilatih
    model = joblib.load('model/random_forest_pipeline.joblib')
    
    # Memproses data input menggunakan preprocessing
    data_processed = preprocess_data(data)
    
    # Melakukan prediksi menggunakan model
    prediction = model.predict(data_processed)
    
    # Mengembalikan hasil prediksi (0: Tidak Dropout, 1: Dropout)
    return prediction

# Streamlit: Judul aplikasi
st.title("Prediksi Dropout Mahasiswa")

import streamlit as st

with st.form(key='input_form'):
    # Default values
    default_marital_status = 'single'
    default_application_mode = 'International student (bachelor)'
    default_application_order = 1
    default_course = 'Tourism'
    default_daytime_evening_attendance = 'daytime'
    default_previous_qualification = 'Secondary education'
    default_previous_qualification_grade = 160
    default_nationality = 'Portuguese'
    default_mothers_qualification = 'Secondary Education - 12th Year of Schooling or Eq.'
    default_fathers_qualification = 'Higher Education - Degree'
    default_mothers_occupation = 'Intermediate Level Technicians and Professions'
    default_fathers_occupation = 'Intermediate Level Technicians and Professions'
    default_admission_grade = 142.5  # Default as float
    default_displaced = 'yes'
    default_educational_special_needs = 'no'
    default_debtor = 'no'
    default_tuition_fees_up_to_date = 'no'
    default_gender = 'male'
    default_scholarship_holder = 'no'
    default_age_at_enrollment = 19
    default_international = 'no'
    default_curricular_units_1st_sem_enrolled = 6
    default_curricular_units_1st_sem_evaluations = 6
    default_curricular_units_1st_sem_approved = 6
    default_curricular_units_1st_sem_grade = 14
    default_curricular_units_2nd_sem_enrolled = 6
    default_curricular_units_2nd_sem_evaluations = 6
    default_curricular_units_2nd_sem_approved = 6
    default_curricular_units_2nd_sem_grade = 13.66666667
    default_unemployment_rate = 13.9
    default_inflation_rate = -0.3
    default_gdp = 0.79

    # Existing inputs
    marital_status = st.selectbox('Marital Status', ['single', 'married', 'widower', 'divorced', 'facto union', 'legally separated'], index=['single', 'married', 'widower', 'divorced', 'facto union', 'legally separated'].index(default_marital_status))
    application_mode = st.selectbox('Application Mode', ['1st phase - general contingent', 'Ordinance No. 612/93', '1st phase - special contingent (Azores Island)', 'Holders of other higher courses', 'Ordinance No. 854-B/99', 'International student (bachelor)', '1st phase - special contingent (Madeira Island)', '2nd phase - general contingent', '3rd phase - general contingent', 'Ordinance No. 533-A/99, item b2 (Different Plan)', 'Ordinance No. 533-A/99, item b3 (Other Institution)', 'Over 23 years old', 'Transfer', 'Change of course', 'Technological specialization diploma holders', 'Change of institution/course', 'Short cycle diploma holders', 'Change of institution/course (International)'], index=['1st phase - general contingent', 'Ordinance No. 612/93', '1st phase - special contingent (Azores Island)', 'Holders of other higher courses', 'Ordinance No. 854-B/99', 'International student (bachelor)', '1st phase - special contingent (Madeira Island)', '2nd phase - general contingent', '3rd phase - general contingent', 'Ordinance No. 533-A/99, item b2 (Different Plan)', 'Ordinance No. 533-A/99, item b3 (Other Institution)', 'Over 23 years old', 'Transfer', 'Change of course', 'Technological specialization diploma holders', 'Change of institution/course', 'Short cycle diploma holders', 'Change of institution/course (International)'].index(default_application_mode))
    application_order = st.number_input('Application Order', min_value=0, max_value=9, value=default_application_order)
    course = st.selectbox('Course', ['Biofuel Production Technologies', 'Animation and Multimedia Design', 'Social Service (evening attendance)', 'Agronomy', 'Communication Design', 'Veterinary Nursing', 'Informatics Engineering', 'Equinculture', 'Management', 'Social Service', 'Tourism', 'Nursing', 'Oral Hygiene', 'Advertising and Marketing Management', 'Journalism and Communication', 'Basic Education', 'Management (evening attendance)'], index=['Biofuel Production Technologies', 'Animation and Multimedia Design', 'Social Service (evening attendance)', 'Agronomy', 'Communication Design', 'Veterinary Nursing', 'Informatics Engineering', 'Equinculture', 'Management', 'Social Service', 'Tourism', 'Nursing', 'Oral Hygiene', 'Advertising and Marketing Management', 'Journalism and Communication', 'Basic Education', 'Management (evening attendance)'].index(default_course))
    daytime_evening_attendance = st.selectbox('Daytime/Evening Attendance', ['daytime', 'evening'], index=['daytime', 'evening'].index(default_daytime_evening_attendance))
    previous_qualification = st.selectbox('Previous Qualification', ['Secondary education', 'Higher education - bachelor\'s degree', 'Higher education - degree', 'Higher education - master\'s', 'Higher education - doctorate', 'Frequency of higher education', '12th year of schooling - not completed', '11th year of schooling - not completed', 'Other - 11th year of schooling', '10th year of schooling', '10th year of schooling - not completed', 'Basic education 3rd cycle (9th/10th/11th year) or equiv.', 'Basic education 2nd cycle (6th/7th/8th year) or equiv.', 'Technological specialization course', 'Higher education - degree (1st cycle)', 'Professional higher technical course', 'Higher education - master (2nd cycle)'], index=['Secondary education', 'Higher education - bachelor\'s degree', 'Higher education - degree', 'Higher education - master\'s', 'Higher education - doctorate', 'Frequency of higher education', '12th year of schooling - not completed', '11th year of schooling - not completed', 'Other - 11th year of schooling', '10th year of schooling', '10th year of schooling - not completed', 'Basic education 3rd cycle (9th/10th/11th year) or equiv.', 'Basic education 2nd cycle (6th/7th/8th year) or equiv.', 'Technological specialization course', 'Higher education - degree (1st cycle)', 'Professional higher technical course', 'Higher education - master (2nd cycle)'].index(default_previous_qualification))
    previous_qualification_grade = st.number_input('Previous Qualification Grade', min_value=0, max_value=200, value=default_previous_qualification_grade)
    nationality = st.selectbox('Nationality', ['Portuguese', 'German', 'Spanish', 'Italian', 'Dutch', 'English', 'Lithuanian', 'Angolan', 'Cape Verdean', 'Guinean', 'Mozambican', 'Santomean', 'Turkish', 'Brazilian', 'Romanian', 'Moldova (Republic of)', 'Mexican', 'Ukrainian', 'Russian', 'Cuban', 'Colombian'], index=['Portuguese', 'German', 'Spanish', 'Italian', 'Dutch', 'English', 'Lithuanian', 'Angolan', 'Cape Verdean', 'Guinean', 'Mozambican', 'Santomean', 'Turkish', 'Brazilian', 'Romanian', 'Moldova (Republic of)', 'Mexican', 'Ukrainian', 'Russian', 'Cuban', 'Colombian'].index(default_nationality))
    mothers_qualification = st.selectbox('Mother\'s Qualification', ['Secondary Education - 12th Year of Schooling or Eq.', 'Higher Education - Bachelor\'s Degree', 'Higher Education - Degree', 'Higher Education - Master\'s', 'Higher Education - Doctorate', 'Frequency of Higher Education', '12th Year of Schooling - Not Completed', '11th Year of Schooling - Not Completed', '7th Year (Old)', 'Other - 11th Year of Schooling', '10th Year of Schooling', 'General commerce course', 'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.', 'Technical-professional course', '7th year of schooling', '2nd cycle of the general high school course', '9th Year of Schooling - Not Completed', '8th year of schooling', 'Unknown', 'Can\'t read or write', 'Can read without having a 4th year of schooling', 'Basic education 1st cycle (4th/5th year) or equiv.', 'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.', 'Technological specialization course', 'Higher education - degree (1st cycle)', 'Specialized higher studies course', 'Professional higher technical course', 'Higher Education - Master (2nd cycle)', 'Higher Education - Doctorate (3rd cycle)'], index=['Secondary Education - 12th Year of Schooling or Eq.', 'Higher Education - Bachelor\'s Degree', 'Higher Education - Degree', 'Higher Education - Master\'s', 'Higher Education - Doctorate', 'Frequency of Higher Education', '12th Year of Schooling - Not Completed', '11th Year of Schooling - Not Completed', '7th Year (Old)', 'Other - 11th Year of Schooling', '10th Year of Schooling', 'General commerce course', 'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.', 'Technical-professional course', '7th year of schooling', '2nd cycle of the general high school course', '9th Year of Schooling - Not Completed', '8th year of schooling', 'Unknown', 'Can\'t read or write', 'Can read without having a 4th year of schooling', 'Basic education 1st cycle (4th/5th year) or equiv.', 'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.', 'Technological specialization course', 'Higher education - degree (1st cycle)', 'Specialized higher studies course', 'Professional higher technical course', 'Higher Education - Master (2nd cycle)', 'Higher Education - Doctorate (3rd cycle)'].index(default_mothers_qualification))
    fathers_qualification = st.selectbox('Father\'s Qualification', ['Secondary Education - 12th Year of Schooling or Eq.', 'Higher Education - Bachelor\'s Degree', 'Higher Education - Degree', 'Higher Education - Master\'s', 'Higher Education - Doctorate', 'Frequency of Higher Education', '12th Year of Schooling - Not Completed', '11th Year of Schooling - Not Completed', '7th Year (Old)', 'Other - 11th Year of Schooling', '10th Year of Schooling', 'General commerce course', 'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.', 'Technical-professional course', '7th year of schooling', '2nd cycle of the general high school course', '9th Year of Schooling - Not Completed', '8th year of schooling', 'Unknown', 'Can\'t read or write', 'Can read without having a 4th year of schooling', 'Basic education 1st cycle (4th/5th year) or equiv.', 'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.', 'Technological specialization course', 'Higher education - degree (1st cycle)', 'Specialized higher studies course', 'Professional higher technical course', 'Higher Education - Master (2nd cycle)', 'Higher Education - Doctorate (3rd cycle)'], index=['Secondary Education - 12th Year of Schooling or Eq.', 'Higher Education - Bachelor\'s Degree', 'Higher Education - Degree', 'Higher Education - Master\'s', 'Higher Education - Doctorate', 'Frequency of Higher Education', '12th Year of Schooling - Not Completed', '11th Year of Schooling - Not Completed', '7th Year (Old)', 'Other - 11th Year of Schooling', '10th Year of Schooling', 'General commerce course', 'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.', 'Technical-professional course', '7th year of schooling', '2nd cycle of the general high school course', '9th Year of Schooling - Not Completed', '8th year of schooling', 'Unknown', 'Can\'t read or write', 'Can read without having a 4th year of schooling', 'Basic education 1st cycle (4th/5th year) or equiv.', 'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.', 'Technological specialization course', 'Higher education - degree (1st cycle)', 'Specialized higher studies course', 'Professional higher technical course', 'Higher Education - Master (2nd cycle)', 'Higher Education - Doctorate (3rd cycle)'].index(default_fathers_qualification))

    # New inputs for occupation, admission grade, and age
    mothers_occupation = st.selectbox('Mother\'s Occupation', ['Student', 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers', 'Specialists in Intellectual and Scientific Activities', 'Intermediate Level Technicians and Professions', 'Administrative staff', 'Personal Services, Security and Safety Workers and Sellers', 'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry', 'Skilled Workers in Industry, Construction and Craftsmen', 'Installation and Machine Operators and Assembly Workers', 'Unskilled Workers', 'Armed Forces Professions', 'Other Situation', 'blank', 'Health professionals', 'teachers', 'Specialists in information and communication technologies (ICT)', 'Intermediate level science and engineering technicians and professions', 'Technicians and professionals, of intermediate level of health', 'Intermediate level technicians from legal, social, sports, cultural and similar services', 'Office workers, secretaries in general and data processing operators', 'Data, accounting, statistical, financial services and registry-related operators', 'Other administrative support staff', 'Personal service workers', 'Sellers', 'Personal care workers and the like', 'Skilled construction workers and the like, except electricians', 'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like', 'Workers in food processing, woodworking, clothing and other industries and crafts', 'Cleaning workers', 'Unskilled workers in agriculture, animal production, fisheries and forestry', 'Unskilled workers in extractive industry, construction, manufacturing and transport', 'Meal preparation assistants'], index=['Student', 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers', 'Specialists in Intellectual and Scientific Activities', 'Intermediate Level Technicians and Professions', 'Administrative staff', 'Personal Services, Security and Safety Workers and Sellers', 'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry', 'Skilled Workers in Industry, Construction and Craftsmen', 'Installation and Machine Operators and Assembly Workers', 'Unskilled Workers', 'Armed Forces Professions', 'Other Situation', 'blank', 'Health professionals', 'teachers', 'Specialists in information and communication technologies (ICT)', 'Intermediate level science and engineering technicians and professions', 'Technicians and professionals, of intermediate level of health', 'Intermediate level technicians from legal, social, sports, cultural and similar services', 'Office workers, secretaries in general and data processing operators', 'Data, accounting, statistical, financial services and registry-related operators', 'Other administrative support staff', 'Personal service workers', 'Sellers', 'Personal care workers and the like', 'Skilled construction workers and the like, except electricians', 'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like', 'Workers in food processing, woodworking, clothing and other industries and crafts', 'Cleaning workers', 'Unskilled workers in agriculture, animal production, fisheries and forestry', 'Unskilled workers in extractive industry, construction, manufacturing and transport', 'Meal preparation assistants'].index(default_mothers_occupation))
    fathers_occupation = st.selectbox('Father\'s Occupation', ['Student', 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers', 'Specialists in Intellectual and Scientific Activities', 'Intermediate Level Technicians and Professions', 'Administrative staff', 'Personal Services, Security and Safety Workers and Sellers', 'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry', 'Skilled Workers in Industry, Construction and Craftsmen', 'Installation and Machine Operators and Assembly Workers', 'Unskilled Workers', 'Armed Forces Professions', 'Other Situation', 'blank', 'Health professionals', 'teachers', 'Specialists in information and communication technologies (ICT)', 'Intermediate level science and engineering technicians and professions', 'Technicians and professionals, of intermediate level of health', 'Intermediate level technicians from legal, social, sports, cultural and similar services', 'Office workers, secretaries in general and data processing operators', 'Data, accounting, statistical, financial services and registry-related operators', 'Other administrative support staff', 'Personal service workers', 'Sellers', 'Personal care workers and the like', 'Skilled construction workers and the like, except electricians', 'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like', 'Workers in food processing, woodworking, clothing and other industries and crafts', 'Cleaning workers', 'Unskilled workers in agriculture, animal production, fisheries and forestry', 'Unskilled workers in extractive industry, construction, manufacturing and transport', 'Meal preparation assistants'], index=['Student', 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers', 'Specialists in Intellectual and Scientific Activities', 'Intermediate Level Technicians and Professions', 'Administrative staff', 'Personal Services, Security and Safety Workers and Sellers', 'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry', 'Skilled Workers in Industry, Construction and Craftsmen', 'Installation and Machine Operators and Assembly Workers', 'Unskilled Workers', 'Armed Forces Professions', 'Other Situation', 'blank', 'Health professionals', 'teachers', 'Specialists in information and communication technologies (ICT)', 'Intermediate level science and engineering technicians and professions', 'Technicians and professionals, of intermediate level of health', 'Intermediate level technicians from legal, social, sports, cultural and similar services', 'Office workers, secretaries in general and data processing operators', 'Data, accounting, statistical, financial services and registry-related operators', 'Other administrative support staff', 'Personal service workers', 'Sellers', 'Personal care workers and the like', 'Skilled construction workers and the like, except electricians', 'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like', 'Workers in food processing, woodworking, clothing and other industries and crafts', 'Cleaning workers', 'Unskilled workers in agriculture, animal production, fisheries and forestry', 'Unskilled workers in extractive industry, construction, manufacturing and transport', 'Meal preparation assistants'].index(default_fathers_occupation))
    admission_grade = st.number_input('Admission Grade', min_value=0.0, max_value=200.0, value=float(default_admission_grade))
    age_at_enrollment = st.number_input('Age at Enrollment', min_value=15, max_value=100, value=default_age_at_enrollment)

    displaced = st.selectbox('Displaced', ['yes', 'no'], index=['yes', 'no'].index(default_displaced))
    educational_special_needs = st.selectbox('Educational Special Needs', ['yes', 'no'], index=['yes', 'no'].index(default_educational_special_needs))
    debtor = st.selectbox('Debtor', ['yes', 'no'], index=['yes', 'no'].index(default_debtor))
    tuition_fees_up_to_date = st.selectbox('Tuition Fees Up To Date', ['yes', 'no'], index=['yes', 'no'].index(default_tuition_fees_up_to_date))
    gender = st.selectbox('Gender', ['male', 'female'], index=['male', 'female'].index(default_gender))
    scholarship_holder = st.selectbox('Scholarship Holder', ['yes', 'no'], index=['yes', 'no'].index(default_scholarship_holder))
    international = st.selectbox('International', ['yes', 'no'], index=['yes', 'no'].index(default_international))

    # Semester inputs
    curricular_units_1st_sem_enrolled = st.number_input('Curricular Units 1st Sem Enrolled', min_value=0.0, max_value=26.0, value=float(default_curricular_units_1st_sem_enrolled))
    curricular_units_1st_sem_evaluations = st.number_input('Curricular Units 1st Sem Evaluations', min_value=0.0, max_value=45.0, value=float(default_curricular_units_1st_sem_evaluations))
    curricular_units_1st_sem_approved = st.number_input('Curricular Units 1st Sem Approved', min_value=0.0, max_value=26.0, value=float(default_curricular_units_1st_sem_approved))
    curricular_units_1st_sem_grade = st.number_input('Curricular Units 1st Sem Grade', min_value=0.0, max_value=20.0, value=float(default_curricular_units_1st_sem_grade))

    curricular_units_2nd_sem_enrolled = st.number_input('Curricular Units 2nd Sem Enrolled', min_value=0.0, max_value=23.0, value=float(default_curricular_units_2nd_sem_enrolled))
    curricular_units_2nd_sem_evaluations = st.number_input('Curricular Units 2nd Sem Evaluations', min_value=0.0, max_value=33.0, value=float(default_curricular_units_2nd_sem_evaluations))
    curricular_units_2nd_sem_approved = st.number_input('Curricular Units 2nd Sem Approved', min_value=0.0, max_value=20.0, value=float(default_curricular_units_2nd_sem_approved))
    curricular_units_2nd_sem_grade = st.number_input('Curricular Units 2nd Sem Grade', min_value=0.0, max_value=20.0, value=float(default_curricular_units_2nd_sem_grade))

    # Economic factors
    unemployment_rate = st.number_input('Unemployment Rate (%)', min_value=0.0, max_value=100.0, value=default_unemployment_rate)
    inflation_rate = st.number_input('Inflation Rate (%)', value=float(default_inflation_rate))
    gdp = st.number_input('GDP (Billion)', value=float(default_gdp))

    # Submit button
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    # Prepare data for prediction
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
        'Mothers_occupation': [mothers_occupation],
        'Fathers_occupation': [fathers_occupation],
        'Admission_grade': [admission_grade],
        'Age_at_enrollment': [age_at_enrollment],
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

    # Preprocessing and prediction
    preprocessed_data = preprocess_data(input_data)
    result = prediction(preprocessed_data)

    # Display result
    if result[0] == 0:
        st.write("Prediksi: Mahasiswa Dropout")
    else:
        st.write("Prediksi: Mahasiswa Graduate")
