import streamlit as st





def main():

  title = '<h1 style="color:#AA4A44	;text-align:center; font-size: 30rem">Min and Max</h1>'
  st.markdown(title,unsafe_allow_html=True)

  st.subheader("Please insert five numbers: I'll tell you the bigger and smaller")
  st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://shorturl.at/himn0");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
        unsafe_allow_html=True
    )





if __name__ == '__main__':
    main()