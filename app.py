import streamlit as st





def main():

  st.title('Min & Max value')
  st.subheader("Pleas insert five numbers: I'll tell you the bigger and smaller")
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