# DATING RECOMMENDATIONS

## 🏆 Introduction
Online dating platforms have revolutionized how people connect, but finding the right match can still be challenging. This project aims to enhance the matchmaking process by using user-inputted preferences and behavioral data to recommend the best potential matches.

## 🎯 Aim
The goal of this project is to develop a recommendation system that suggests the top 5 most compatible matches for a user based on various factors such as shared interests, age similarity, and past engagement in the app (swiping history). By leveraging a scoring algorithm, the system helps users find meaningful connections efficiently.

## 📊 Dataset Explanation
The dataset contains anonymized user data with the following attributes:

- **User ID**: Unique identifier for each user.
- **Age**: The age of the user.
- **Gender**: User's gender (Male/Female).
- **Height**: User's height (in arbitrary units).
- **Interests**: A list of activities and hobbies the user enjoys.
- **Looking For**: The type of relationship the user is seeking (Casual Dating, Friendship, Marriage, or Long-term Relationship).
- **Swiping History**: The user's engagement level with the app, represented as a percentage (0-100).
- **Frequency of Usage**: How often the user interacts with the app (Daily, Weekly, Monthly).

The system uses this data to calculate compatibility scores and recommend the best possible matches for users.

## 🤖 How It Works
The recommendation system works by evaluating each potential match based on multiple criteria:

- **Shared Interests**: The more interests two users have in common, the higher their compatibility score.
- **Age Difference**: A smaller age gap increases compatibility, with the algorithm awarding a higher score for closer age similarities.
- **Swiping History**: This metric considers the user’s activity on the app, with more active users being matched with others who have similar levels of engagement.
- **Relationship Type**: If both profiles are seeking the same type of relationship, a perfect score is given for this category.

The system calculates a **total compatibility score** for each possible match and recommends the most compatible profiles for the user.

## 📈 Conclusion
In this project, we developed a recommendation system designed to enhance the matchmaking process on online dating platforms by considering various factors such as shared interests, age similarity, swiping history, and relationship type preferences. The algorithm calculates a compatibility score for each potential match, helping users find the most suitable connections based on their unique profiles.

By using these criteria, the system effectively recommends users who are more likely to share meaningful connections, offering a more personalized and efficient online dating experience.

## 🚀 Demo
You can interact with the system through the Hugging Face demo [here](https://huggingface.co/spaces/Senasu/Dating_Recommendations).

