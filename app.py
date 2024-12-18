import streamlit as st
import pandas as pd
from data_preprocessing import preprocess_data
from prediction import load_model, make_prediction

# Mappings for categorical columns
marital_status_mapping = {
    1: 'single', 2: 'married', 3: 'widower', 4: 'divorced', 5: 'facto union', 6: 'legally separated'
}

application_mode_mapping = {
    1: '1st phase - general contingent',
    2: 'Ordinance No. 612/93',
    5: '1st phase - special contingent (Azores Island)',
    7: 'Holders of other higher courses',
    10: 'Ordinance No. 854-B/99',
    15: 'International student (bachelor)',
    16: '1st phase - special contingent (Madeira Island)',
    17: '2nd phase - general contingent',
    18: '3rd phase - general contingent',
    26: 'Ordinance No. 533-A/99, item b2 (Different Plan)',
    27: 'Ordinance No. 533-A/99, item b3 (Other Institution)',
    39: 'Over 23 years old',
    42: 'Transfer',
    43: 'Change of course',
    44: 'Technological specialization diploma holders',
    51: 'Change of institution/course',
    53: 'Short cycle diploma holders',
    57: 'Change of institution/course (International)'
}

course_mapping = {
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

daytime_evening_mapping = {
    1: 'daytime', 0: 'evening'
}

previous_qualification_mapping = {
    1: 'Secondary education',
    2: 'Higher education - bachelor\'s degree',
    3: 'Higher education - degree',
    4: 'Higher education - master\'s',
    5: 'Higher education - doctorate',
    6: 'Frequency of higher education',
    9: '12th year of schooling - not completed',
    10: '11th year of schooling - not completed',
    12: 'Other - 11th year of schooling',
    14: '10th year of schooling',
    15: '10th year of schooling - not completed',
    19: 'Basic education 3rd cycle (9th/10th/11th year) or equiv.',
    38: 'Basic education 2nd cycle (6th/7th/8th year) or equiv.',
    39: 'Technological specialization course',
    40: 'Higher education - degree (1st cycle)',
    42: 'Professional higher technical course',
    43: 'Higher education - master (2nd cycle)'
}

nationality_mapping = {
    1: 'Portuguese', 2: 'German', 6: 'Spanish', 11: 'Italian', 13: 'Dutch', 14: 'English',
    17: 'Lithuanian', 21: 'Angolan', 22: 'Cape Verdean', 24: 'Guinean', 25: 'Mozambican',
    26: 'Santomean', 32: 'Turkish', 41: 'Brazilian', 62: 'Romanian', 100: 'Moldova (Republic of)',
    101: 'Mexican', 103: 'Ukrainian', 105: 'Russian', 108: 'Cuban', 109: 'Colombian'
}

qualification_mapping = {
    1: 'Secondary Education - 12th Year of Schooling or Eq.',
    2: 'Higher Education - Bachelor\'s Degree',
    3: 'Higher Education - Degree',
    4: 'Higher Education - Master\'s',
    5: 'Higher Education - Doctorate',
    6: 'Frequency of Higher Education',
    9: '12th Year of Schooling - Not Completed',
    10: '11th Year of Schooling - Not Completed',
    11: '7th Year (Old)',
    12: 'Other - 11th Year of Schooling',
    14: '10th Year of Schooling',
    18: 'General commerce course',
    19: 'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.',
    22: 'Technical-professional course',
    26: '7th year of schooling',
    27: '2nd cycle of the general high school course',
    29: '9th Year of Schooling - Not Completed',
    30: '8th year of schooling',
    34: 'Unknown',
    35: 'Can\'t read or write',
    36: 'Can read without having a 4th year of schooling',
    37: 'Basic education 1st cycle (4th/5th year) or equiv.',
    38: 'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.',
    39: 'Technological specialization course',
    40: 'Higher education - degree (1st cycle)',
    41: 'Specialized higher studies course',
    42: 'Professional higher technical course',
    43: 'Higher Education - Master (2nd cycle)',
    44: 'Higher Education - Doctorate (3rd cycle)'
}

occupation_mapping = {
    0: 'Student',
    1: 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers',
    2: 'Specialists in Intellectual and Scientific Activities',
    3: 'Intermediate Level Technicians and Professions',
    4: 'Administrative staff',
    5: 'Personal Services, Security and Safety Workers and Sellers',
    6: 'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry',
    7: 'Skilled Workers in Industry, Construction and Craftsmen',
    8: 'Installation and Machine Operators and Assembly Workers',
    9: 'Unskilled Workers',
    10: 'Armed Forces Professions',
    90: 'Other Situation',
    99: 'blank',
    122: 'Health professionals',
    123: 'teachers',
    125: 'Specialists in information and communication technologies (ICT)',
    131: 'Intermediate level science and engineering technicians and professions',
    132: 'Technicians and professionals, of intermediate level of health',
    134: 'Intermediate level technicians from legal, social, sports, cultural and similar services',
    141: 'Office workers, secretaries in general and data processing operators',
    143: 'Data, accounting, statistical, financial services and registry-related operators',
    144: 'Other administrative support staff',
    151: 'Personal service workers',
    152: 'Sellers',
    153: 'Personal care workers and the like',
    171: 'Skilled construction workers and the like, except electricians',
    173: 'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like',
    175: 'Workers in food processing, woodworking, clothing and other industries and crafts',
    191: 'Cleaning workers',
    192: 'Unskilled workers in agriculture, animal production, fisheries and forestry',
    193: 'Unskilled workers in extractive industry, construction, manufacturing and transport',
    194: 'Meal preparation assistants'
}

# Title for the app
st.title('Prediction App for Student Data')

# Define a form for user input
with st.form(key='prediction_form'):
    marital_status = st.selectbox('Marital Status', list(marital_status_mapping.values()))
    application_mode = st.selectbox('Application Mode', list(application_mode_mapping.values()))
    application_order = st.number_input('Application Order', min_value=0, max_value=9)
    course = st.selectbox('Course', list(course_mapping.values()))
    attendance = st.selectbox('Attendance Mode', list(daytime_evening_mapping.values()))
    prev_qualification = st.selectbox('Previous Qualification', list(previous_qualification_mapping.values()))
    prev_qualification_grade = st.number_input('Previous Qualification Grade', min_value=0, max_value=200)
    nationality = st.selectbox('Nationality', list(nationality_mapping.values()))
    mothers_qualification = st.selectbox('Mother’s Qualification', list(qualification_mapping.values()))
    fathers_qualification = st.selectbox('Father’s Qualification', list(qualification_mapping.values()))
    mothers_occupation = st.selectbox('Mother’s Occupation', list(occupation_mapping.values()))
    fathers_occupation = st.selectbox('Father’s Occupation', list(occupation_mapping.values()))
    admission_grade = st.number_input('Admission Grade', min_value=0, max_value=200)
    displaced = st.selectbox('Displaced', ['Yes', 'No'])
    educational_special_needs = st.selectbox('Educational Special Needs', ['Yes', 'No'])
    debtor = st.selectbox('Debtor', ['Yes', 'No'])
    tuition_fees_up_to_date = st.selectbox('Tuition Fees Up To Date', ['Yes', 'No'])
    gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
    scholarship_holder = st.selectbox('Scholarship Holder', ['Yes', 'No'])
    age_at_enrollment = st.number_input('Age at Enrollment')
    international = st.selectbox('International', ['Yes', 'No'])
    first_sem_enrolled = st.number_input('First Semester Enrolled', min_value=0, max_value=26)
    first_sem_evaluations = st.number_input('First Semester Evaluations', min_value=0, max_value=45)
    first_sem_approved = st.number_input('First Semester Approved', min_value=0, max_value=26)
    first_sem_grade = st.number_input('First Semester Grade', min_value=0, max_value=20)
    second_sem_enrolled = st.number_input('Second Semester Enrolled', min_value=0, max_value=23)
    second_sem_evaluations = st.number_input('Second Semester Evaluations', min_value=0, max_value=33)
    second_sem_approved = st.number_input('Second Semester Approved', min_value=0, max_value=20)
    second_sem_grade = st.number_input('Second Semester Grade', min_value=0, max_value=20)
    unemployment_rate = st.number_input('Unemployment Rate', min_value=0.0, max_value=100.0)
    inflation_rate = st.number_input('Inflation Rate', min_value=0.0, max_value=100.0)
    GDP = st.number_input('GDP')

    submit_button = st.form_submit_button('Submit')

# If the form is submitted
if submit_button:
    user_data = {
        'Marital Status': marital_status_mapping[marital_status],
        'Application Mode': application_mode_mapping[application_mode],
        'Application Order': application_order,
        'Course': course_mapping[course],
        'Attendance Mode': daytime_evening_mapping[attendance],
        'Previous Qualification': previous_qualification_mapping[prev_qualification],
        'Previous Qualification Grade': prev_qualification_grade,
        'Nationality': nationality_mapping[nationality],
        'Mother’s Qualification': qualification_mapping[mothers_qualification],
        'Father’s Qualification': qualification_mapping[fathers_qualification],
        'Mother’s Occupation': occupation_mapping[mothers_occupation],
        'Father’s Occupation': occupation_mapping[fathers_occupation],
        'Admission Grade': admission_grade,
        'Displaced': displaced,
        'Educational Special Needs': educational_special_needs,
        'Debtor': debtor,
        'Tuition Fees Up To Date': tuition_fees_up_to_date,
        'Gender': gender,
        'Scholarship Holder': scholarship_holder,
        'Age at Enrollment': age_at_enrollment,
        'International': international,
        'First Semester Enrolled': first_sem_enrolled,
        'First Semester Evaluations': first_sem_evaluations,
        'First Semester Approved': first_sem_approved,
        'First Semester Grade': first_sem_grade,
        'Second Semester Enrolled': second_sem_enrolled,
        'Second Semester Evaluations': second_sem_evaluations,
        'Second Semester Approved': second_sem_approved,
        'Second Semester Grade': second_sem_grade,
        'Unemployment Rate': unemployment_rate,
        'Inflation Rate': inflation_rate,
        'GDP': GDP
    }

    # Preprocess data
    processed_data = preprocess_data(user_data)

    # Load model and make prediction
    model = load_model()  # Make sure to define this function in your code
    prediction = make_prediction(model, processed_data)  # Define this function in your code

    # Display prediction
    st.write(f'Prediction: {prediction}')
