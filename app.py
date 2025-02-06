import streamlit as st
import pandas as pd
import ast

def calculate_match(profile1, profile2):
    interests1 = set(ast.literal_eval(profile1['Interests']))
    interests2 = set(ast.literal_eval(profile2['Interests']))
    shared_interests_score = len(interests1.intersection(interests2))
    
    age_difference_score = max(0, 10 - abs(profile1['Age'] - profile2['Age']))
    swiping_history_score = min(profile1['Swiping History'], profile2['Swiping History']) / 100
    
    relationship_type_score = 1 if profile1['Looking For'] == profile2['Looking For'] else 0
    
    total_score = (shared_interests_score + age_difference_score + swiping_history_score +
                   relationship_type_score)
    
    return total_score

def recommend_profiles(user_profile, all_profiles):
    matches = []
    for _, profile in all_profiles.iterrows():
        if profile['Gender'] != user_profile['Gender']:
            score = calculate_match(user_profile, profile)
            matches.append((profile, score))
    
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches[:5]

def main():
    st.set_page_config(page_title="Dating App Matcher", layout="centered", initial_sidebar_state="collapsed")
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            background-color: #FF4B4B;
            color: white;
            font-size: 18px;
            border-radius: 8px;
        }
        .stTextInput>div>div>input, .stSelectbox>div>div>select, .stNumberInput>div>div>input {
            border-radius: 8px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("💘 Dating App Matcher")
    st.write("### Enter your details to find the best matches!")
    
    with st.form("user_input_form"):
        age = st.number_input("Enter your age", min_value=18, max_value=100, step=1)
        gender = st.selectbox("Select your gender", ["Male", "Female"])
        interests = st.text_area("Enter your interests (comma-separated)")
        looking_for = st.multiselect("Looking for", ['Casual Dating', 'Friendship', 'Marriage', 'Long-term Relationship'])
        swiping_history = st.slider("Swiping History", 0, 100, 50)
        
        submitted = st.form_submit_button("🔍 Find Matches")
    
    if submitted:
        df = pd.read_csv('dating_app_dataset.csv')
        
        if {'User ID', 'Age', 'Gender', 'Height', 'Interests', 'Looking For', 'Swiping History', 'Frequency of Usage'}.issubset(df.columns):
            user_profile = {
                'Age': age,
                'Gender': gender,
                'Interests': str(interests.split(',')),
                'Looking For': looking_for,
                'Swiping History': swiping_history
            }
            
            matches = recommend_profiles(user_profile, df)
            
            st.write("### 💑 Top 5 Matches")
            for profile, score in matches:
                with st.expander(f"User ID {profile['User ID']} - Score: {score:.2f}"):
                    st.write(f"**Age:** {profile['Age']}")
                    st.write(f"**Gender:** {profile['Gender']}")
                    st.write(f"**Interests:** {profile['Interests']}")
                    st.write(f"**Looking For:** {profile['Looking For']}")
                    st.write(f"**Swiping History:** {profile['Swiping History']}")
        else:
            st.error("Dataset must contain the required columns.")

if __name__ == "__main__":
    main()