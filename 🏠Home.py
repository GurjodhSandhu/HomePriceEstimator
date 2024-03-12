import streamlit as st
import sklearn
import pandas as pd #importing libraries
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
def predict(beds, baths, city, province):
    house = pd.read_csv('house.csv') #read in housing dataset
    house.head()
    house = house[(house['Province'] == province) & (house['City'] == city)] # restrict dataset to a certain province
    house.tail() #display restricted dataset
    # ---------------------------------------------------------------------------------------------
    user_house = pd.DataFrame({'City': [city],'Number_Beds': [beds], 'Number_Baths': [baths]}) #take user input for data
    user_house.head() #display the user inputed values

    X = house[['Number_Beds','Number_Baths']] #predictors
    y = house['Price'] #price of houses

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5, random_state=1) #split up the training and testing data

    linmod2 = LinearRegression() #use linear regression to create a model
    linmod2.fit(X_train, y_train)
    preds = linmod2.predict(X_test) #predict house prices of test data using test predictors


    inputX = user_house[['Number_Beds','Number_Baths']]  #get user inputted data
    print(user_house[['Number_Beds','Number_Baths','City']]) #display user inputted data
    prediction = linmod2.predict(inputX) #predict house prices based on user inputted data

    output = prediction[0] #estimated price for house based of factors given
    print("value of your house is: $", output) #print out price



    return round(output,2)

                                        #uses function to get mean

st.set_page_config(
    page_icon="🏠"
)
st.header("🏠Home Price Estimator")
with st.popover("Advance Filters"):
    st.header("Advance Filters")

    options = st.multiselect(
        'Add your house features',
        ['Pool', 'Hot-tub', 'sauna', 'Gym', 'Basketball court', 'Tennis Court', 'Beachfront',
         'Fireplace', 'Solar panels', 'Smart-Home Technology'],key="options")

    footage = st.number_input("Enter Homes square footage", min_value=1, max_value=None, value=2500,
                                      key="footage1")

    yearbuilt = st.number_input("Enter year home was built ", min_value=1, max_value=None, value=2000,
                                        key="yearbuilt1")
province = st.selectbox(
    "Select a province", ("Alberta", "British Columbia", "Manitoba", "New Brunswick" , "Newfoundland and Labrador" , "Nova Scotia" , "Ontario" , "Prince Edward Island" , "Quebec" , "Saskatchewan"), key='province'
)
st.write("You selected:", province)


if(province == "Alberta"):
    city = st.selectbox(
        "Select a city", ("Calgary", "Edmonton"), key= 'city'
    )
    st.write("You selected:", city)
if(province == "British Columbia"):
    city = st.selectbox(
        "Select a city", ("Vancouver", "Victoria", "Abbotsford", "Kelowna"), key= 'city'
    )
    st.write("You selected:", city)
if(province == "Manitoba"):
    city = st.selectbox(
        "Select a city", ("Winnipeg","Temp"), key= 'city'
    )
    st.write("You selected:", city)
if(province == "New Brunswick"):
    city = st.selectbox(
        "Select a city", ("Moncton", "Saint John"), key= 'city'
    )
    st.write("You selected:", city)
if(province == "Newfoundland and Labrador"):
    city = st.selectbox(
        "Select a city", ("St. John's","Temp"), key= 'city'
    )
    st.write("You selected:", city)
if(province == "Nova Scotia"):
    city = st.selectbox(
        "Select a city", ("Halifax","Temp"), key= 'city'
    )
    st.write("You selected:", city)
if(province == "Ontario"):
    city = st.selectbox(
        "Select a city", ("Toronto", "Hamilton", "Ottawa"), key= 'city'
    )
    st.write("You selected:", city)
if(province == "Prince Edward Island"):
    city = st.selectbox(
        "Select a city", ("Charlottetown","Temp"), key= 'city'
    )
    st.write("You selected:", city)
if(province == "Quebec"):
    city = st.selectbox(
        "Select a city", ("Montreal", "Quebec City"), key= 'city'
    )
    st.write("You selected:", city)
if(province == "Saskatchewan"):
    city = st.selectbox(
        "Select a city", ("Regina", "Saskatoon"), key= 'city'
    )
    st.write("You selected:", city)

#input bedroom number
beds = st.number_input("Type number of bedrooms",min_value=1, max_value=20, value = 1, key="beds")
#st.write(bedroomnumber)

#input for bathroom number
baths = st.number_input("Type number of bathrooms",min_value=1, max_value=20, value = 1, key="baths")
#st.write(bathroomnumber)
#button to calculate price

#button to clear output
#output itself

predict(beds, baths, city, province)

col1, col2,col3 = st.columns(3)

def reset():
    st.session_state.province2 = "Alberta"
    st.session_state.city = "Calgary"
with col2:
    result = st.button("calculate", key='result')
    if (result == True):
        container = st.container(border=True)
        st.write("The house price is estimated to be $",predict(beds, baths, city, province))

with col1:
    st.button('Reset', on_click=reset)


#fix province and cities
st.sidebar.header("About")
st.sidebar.write("Quickly and efficently estimate the price of your home.")

st.sidebar.header("Guide")
st.sidebar.write("Have you recently bought or sold an house? Help improve our program by providing some simple data in the Improve our System page")
st.sidebar.write("Having difficulty running the application? Head over to the Help page for some help")
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


#1.fix cities and province values
#3.sidebar.let user input they're home values break make new page
#4.sidebar. help extension
