import pickle
import streamlit as st
import time

# loading the trained model
pickle_in = open('rfc_model.p', 'rb') 
classifier = pickle.load(pickle_in)
      
@st.cache_data()

# defining the function which will make the prediction using the data which the user inputs 
def prediction(pregnancies, glucose, diastolic, triceps, insulin, bmi, dpf, age):   
 
    # Making predictions 
    prediction = classifier.predict( 
        [[pregnancies, glucose, diastolic, triceps, insulin, bmi, dpf, age]])
    return prediction
      
# this is the main function in which we define our webpage 
def main():       
    # front end elements of the web page 
    # html_temp = """ 
    # <div style ="background-color:black;padding:13px"> 
    # <h1 style ="color:blue;text-align:center;">Diabetes Prediction ML App</h1> 
    # </div> 
    # """
      
    # display the front end aspect
    # st.markdown(html_temp, unsafe_allow_html = True) 
    st.title('Diabetes Prediction ML App')
    # st.header('Diabetes Prediction ML App')
    col1, col2= st.columns(2, gap='medium')
    # following lines create boxes in which user can enter data required to make prediction
    with col1:
        pregnancies = st.number_input("Pregnancies: ")
        glucose = st.number_input("Glucose: ")
        diastolic = st.number_input("Diastolic: ")
        triceps = st.number_input("Triceps: ")

    with col2:
        insulin = st.number_input("Insulin: ")
        bmi = st.number_input("BMI: ")
        dpf = st.number_input("DPF: ")
        age = st.number_input("Age: ")
    y=st.button("Predict")
    
    # when 'Predict' is clicked, make the prediction and store it 
    if y: 
        result = prediction(pregnancies, glucose, diastolic, triceps, insulin, bmi, dpf, age) 
        with st.spinner('Wait for it..'):
            time.sleep(2)
            
            if result[0]==1:
                st.error('Patient is Diabetic, Medical consultation is required!!', icon='🚨')
            else:
                st.success('Patient is non diabetic.',icon='✅')
    
    footer_temp = """  
    <div>
    <br>
    <h6 style = "text-align:center;">&copy; Shreyash Somvanshi</h6>
    </div>
    """
    st.markdown(footer_temp, unsafe_allow_html = True)
     
if __name__=='__main__': 
    main()