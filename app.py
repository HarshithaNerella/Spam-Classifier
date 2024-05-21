import pickle
import streamlit as st
import pickle



tfidf_vector=pickle.load(open('C:\\Users\\nerella\\Downloads\\Desktop\\Mail Spam Classification\\vector.pkl','rb'))
model=pickle.load(open('C:\\Users\\nerella\\Downloads\\Desktop\\Mail Spam Classification\\model.pkl','rb'))
mnb=pickle.load(open('C:\\Users\\nerella\\Downloads\\Desktop\\Mail Spam Classification\\mnb.pkl','rb'))


st.title("Email/SMS Spam Classifier")

input_txt=st.text_area("Enter Your Text")

if st.button("Predict"):
    # Check if input is not empty
    if input_txt:
        # Transform the input text using the loaded TF-IDF vectorizer
        transformed_txt = tfidf_vector.transform([input_txt])
        # Make prediction using the loaded model
        predict_val = mnb.predict(transformed_txt)
        # Display the prediction result]
        if predict_val[0] == 1:
            mail = "Spam"
            st.write(f"Prediction: <span style='color:red'> {mail}</span>", unsafe_allow_html=True)
        else:
            mail = "Ham"
            st.write(f"Prediction:<span style='color:green'> {mail}</span>", unsafe_allow_html=True)

    else:
        # If input is empty, show a message
        st.write("Please enter some text for prediction.")


