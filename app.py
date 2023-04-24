import streamlit as st

title = '<h1 style="color:#AA4A44	;text-align:center; font-size: 4rem">Min and Max</h1>'
st.markdown(title, unsafe_allow_html=True)

sub_heading = '<p style="color:#4861C9;text-align:center; font-size: 2rem">Please give me three numbers</p>'
st.markdown(sub_heading, unsafe_allow_html=True)





st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://i.pinimg.com/564x/14/76/37/147637ad0e03365d7fc672b68942b060.jpg");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

def calculate_max(num1:float, num2:float, num3:float):
     if num1 > num2 and num1 > num3:
           return st.write(":blue[Highest number is]: ", num1)
     elif num2 > num1 and num2 > num3:
          return st.write(":blue[Highest number is]: ", num2)
     elif num3 > num1 and num3 > num2:
          return st.write(":blue[Highest number is]: ", num3)
     


def calculate_min(num1:float, num2:float, num3:float):
     if num1 < num2 and num1 < num3:
           return st.write(":blue[Minor number is]: ", num1)
     elif num2 < num1 and num2 < num3:
          return st.write(":blue[Minor number is]: ", num2)
     elif num3 < num1 and num3 < num2:
          return st.write(":blue[Minor number is]: ", num3)



def main():
     x1 = st.slider(label=':red[Choose the first number]', min_value=0, max_value=100, help='slide to choose', label_visibility='visible')

     x2 = st.slider(label=':red[Choose the second number]', min_value=0, max_value=100, help='slide to choose', label_visibility='visible')

     x3 = st.slider(label=':red[Choose the third  number]', min_value=0, max_value=100, help='slide to choose', label_visibility='visible')

     calculate_max(x1,x2,x3)
     calculate_min(x1,x2,x3)
if __name__ == '__main__':
    main()


    