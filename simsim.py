import streamlit as st

st.title(':red[Bmi Calculator]')

weight = st.number_input(
    'Weight (in Kg)',
    min_value=0.0,
    placeholder= 'Enter your weight... '
)

height = st.number_input(
    'Height (in cm)',
    min_value= 0.0,
    placeholder='Enter your height... '
)

def BMI_Calculate(weight, height):
    if height > 0:
        return weight/((height/100)**2)
    else:
        return 0
    
Bmi_result = BMI_Calculate(weight, height)
st.write(f'Your Bmi result : {Bmi_result:.2f}')  

if Bmi_result > 0:
    if Bmi_result <= 16:
        st.write('This is :red[***serverly underweight.***]')
    elif Bmi_result <= 18.5:
        st.write('This is :orange[***underweight.***]')
    elif Bmi_result < 24:
        st.write('This is :green[***normal.***]')
    elif Bmi_result < 30:
        st.write('This is :blue[***overweight.***]')
    else:
        st.write(':violet[***obese.***]')
    
st.write('***Thank you for using my little program.***')

like = st.slider(":red[***We value your feedback***]", 0,5)
st.write("**Thank you for** ", like, "**stars**")