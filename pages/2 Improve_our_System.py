import streamlit as st

st.header("Improve our System")
st.write('Input your homes information and the price that you bought or sold it at.')

with st.popover("Advance Filters"):
    st.header("Advance Filters")

    options2 = st.multiselect(
            'Add your house features',
            ['Pool', 'Hot-tub', 'sauna', 'Gym', 'Basketball court', 'Tennis Court', 'Beachfront',
             'Fireplace', 'Solar panels', 'Smart-Home Technology'], key="options2")

    footage2 = st.number_input("Enter Homes square footage", min_value=1, max_value=None, value=2500,
                                  key="footage2")

    yearbuilt2 = st.number_input("Enter year home was built ", min_value=1, max_value=None, value=2000,
                                    key="yearbuilt2")
province2 = st.selectbox(
        "Select a province", (
        "Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Nova Scotia",
        "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan"), key='province2'
    )
st.write("You selected:", province2)

if (province2 == "Alberta"):
        city2 = st.selectbox(
            "Select a city", ("Calgary", "Edmonton"), key='city2'
        )
        st.write("You selected:", city2)
if (province2 == "British Columbia"):
        city2 = st.selectbox(
            "Select a city", ("Vancouver", "Victoria", "Abbotsford", "Kelowna"), key='city2'
        )
        st.write("You selected:", city2)
if (province2 == "Manitoba"):
        city2 = st.selectbox(
            "Select a city", ("Winnipeg", "Temp"), key='city2'
        )
        st.write("You selected:", city2)
if (province2 == "New Brunswick"):
        city2 = st.selectbox(
            "Select a city", ("Moncton", "Saint John"), key='city2'
        )
        st.write("You selected:", city2)
if (province2 == "Newfoundland and Labrador"):
        city2 = st.selectbox(
            "Select a city", ("St. John's", "Temp"), key='city2'
        )
        st.write("You selected:", city2)
if (province2 == "Nova Scotia"):
        city2 = st.selectbox(
            "Select a city", ("Halifax", "Temp"), key='city2'
        )
        st.write("You selected:", city2)
if (province2 == "Ontario"):
        city2 = st.selectbox(
            "Select a city", ("Toronto", "Hamilton", "Ottawa"), key='city2'
        )
        st.write("You selected:", city2)
if (province2 == "Prince Edward Island"):
        city2 = st.selectbox(
            "Select a city", ("Charlottetown", "Temp"), key='city2'
        )
        st.write("You selected:", city2)
if (province2 == "Quebec"):
        city2 = st.selectbox(
            "Select a city", ("Montreal", "Quebec City"), key='city2'
        )
        st.write("You selected:", city2)
if (province2 == "Saskatchewan"):
        city2 = st.selectbox(
            "Select a city", ("Regina", "Saskatoon"), key='city2'
        )
        st.write("You selected:", city2)

    # input bedroom number
beds2 = st.number_input("Type number of bedrooms", min_value=1, max_value=20, value=1, key="beds2")
    #st.write(bedroomnumber)

    # input for bathroom number
baths2 = st.number_input("Type number of bathrooms", min_value=1, max_value=20, value=1, key="baths2")

houseprice = st.number_input("Type price of your home in $CAD", min_value=1, max_value=None, value=1, key="Houseprice")

col1, col2 = st.columns(2)

def reset():
        st.session_state.province2 = "Alberta"
        st.session_state.city = "Calgary"

with col2:
        sendusinfo = st.button("send", key='result2')
        if (sendusinfo == True):
            container = st.container(border=True)
            st.write("Thank you for your information. This will help us greatly improve accuracy of the estimation inturn helping you as well!")

with col1:
        st.button('Reset', on_click=reset)

st.sidebar.write("Do a quick survey below.")
with st.sidebar.popover("Feedback Form"):
    st.write("rate the application on a scale from 1 to 5 with 1 being worst and 5 being best")
    col1, col2, col3 = st.columns(3)
    with col1:
        ask1 = st.radio(
            "Rate the speed of program",
            ["1", "2", "3","4","5"], key="ask1")
    with col2:
        ask2 = st.radio(
            "Rate the accuracy of program",
            ["1", "2", "3","4","5"], key="ask2")
    with col3:
        ask3 = st.radio(
            "Rate your satisfaction with program",
            ["1", "2", "3","4","5"], key="ask3")
    def sendinfo(ask1,ask2,ask3):
        return None #pseudo backend function to send collected data to a database
    send = st.button('Submit',on_click=sendinfo(ask1,ask2,ask3))
    if send == True:
        st.write("Thank for your feedback")
