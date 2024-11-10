import streamlit as st
import pickle

model = pickle.load(open('penguins2.pkl', 'rb'))

def run():
    st.title("Penguins Species Prediction using Machine Learning")
    
    
    
    ## bill_length_mm
    bill_length_mm= st.slider('Enter bill_length_mm')

     ## bill_depth_mm
    bill_depth_mm = st.slider('Enter bill_depth_mm')


    ## flipper_length_mm 
    flipper_length_mm = st.slider('Enter flipper_length_mm ')

    ## body_mass_g  
    body_mass_g   = st.slider('Enter body_mass_g')


    
    if st.button("Submit"):
        features = [[bill_length_mm, bill_depth_mm,flipper_length_mm, body_mass_g]]
        print(features)
        prediction = model.predict(features)
        weight = [str(i) for i in prediction]
        ans = ', '.join(weight)
        if ans==0:
            st.error("Error in the Inputs: Please Try Again")

        else:
            st.success("The Penguins Species is"+" "+ans)


            

run()