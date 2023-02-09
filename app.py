import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
std_X = StandardScaler()
#from sklearn.preprocessing import StandardScaler
#Declaring Teams
Teams=['Sunrisers Hyderabad', 'Royal Challengers Bangalore',
       'Kolkata Knight Riders', 'Kings XI Punjab', 'Delhi Capitals',
       'Mumbai Indians', 'Chennai Super Kings', 'Rajasthan Royals'] 

#declaring city
cities=['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']
pipe = pickle.load(open('pipe.pkl', 'rb'))
st.title('match winning prediction')
col1,col2,col3=st.columns(3)

with col1:
       Battingteam=st.selectbox("select Batting Teams",sorted(Teams))
 
with col2:
       Bowlingteam=st.selectbox("select Bowlinging Teams",sorted(Teams))      

with col3:
       City=st.selectbox("Select the City where the match is played",sorted(cities))
Wickets=st.number_input("wickets")
target=st.number_input("total_runs_x")
runs_left =st.number_input("runs_left")	
balls_left = st.number_input("balls_left")		
curr_run_rate	=st.number_input("curr_run_rate")
required_run_rate= st.number_input("required_input")    
submitted = st.button('Submit')
if submitted:
    df = pd.DataFrame({
        'batting_team': [Battingteam],
        'bowling_team': [Bowlingteam],
        'city': [City],
        'total_runs_x': [target],
        'wickets': [Wickets],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'curr_run_rate':[curr_run_rate],
        'required_run_rate':[required_run_rate]})
    x = pd.DataFrame(df)
    prediction = pipe.predict_proba(x)
    if prediction[0][0] > 0.5:
        st.write("Batting team has highest chances of winning")
    else:
        st.write("Bowling team has highest chances of winning")
                 
    
  
       