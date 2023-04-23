import streamlit as st





def main():

  title = '<h1 style="color:#AA4A44	;text-align:center; font-size: 5rem">Min and Max</h1>'
  st.markdown(title, unsafe_allow_html=True)

  sub_heading = '<p style="color:#4861C9;text-align:center; font-size: 2rem">Please give me five numbers</p>'
  st.markdown(sub_heading, unsafe_allow_html=True)

#   st.subheader("Please insert five numbers: I'll tell you the bigger and smaller")
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

st.slider(label='Choose a number', min_value=0, max_value=100, help='slide to choose', label_visibility='visible')



if __name__ == '__main__':
    main()