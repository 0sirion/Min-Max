import streamlit as st

title = '<h1 style="color:#AA4A44	;text-align:center; font-size: 5rem">Min and Max</h1>'
st.markdown(title, unsafe_allow_html=True)

sub_heading = '<p style="color:#4861C9;text-align:center; font-size: 2rem">Please give me five numbers</p>'
st.markdown(sub_heading, unsafe_allow_html=True)

st.markdown(" :red[Please give me 3 numbers, I'll give you the smaller and bigger ones]")



#   st.subheader("Please insert five numbers: I'll tell you the bigger and smaller")
# st.markdown(
#         f"""
#          <style>
#          .stApp {{
#              background-image: url("https://shorturl.at/himn0");
#              background-attachment: fixed;
#              background-size: cover;
#          }}
#          </style>
#          """,
#         unsafe_allow_html=True
#     )

def calculate_max(num1, num2, num3):
       if num1 > num2 and num1 > num3:
           case1 =st.write("Highest number is" + num1)
           return case1
       if num2 > num1 and num2 > num3:
           case2 =st.write("Highest number is" + num2)
           return case2
       if num3 > num1 and num3 > num2:
           case3 =st.write("Highest number is" + num3)
           return case3

x1 = st.slider(label='Choose the first number', min_value=0, max_value=100, help='slide to choose', label_visibility='visible')
   
x2 = st.slider(label='Choose the second number', min_value=0, max_value=100, help='slide to choose', label_visibility='visible')

x3 = st.slider(label='Choose the third  number', min_value=0, max_value=100, help='slide to choose', label_visibility='visible')


def main():
     st.write('Biggest number is: ', calculate_max(x1,x2,x3))
                   
           


    



if __name__ == '__main__':
    main()