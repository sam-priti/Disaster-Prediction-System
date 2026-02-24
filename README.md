#Disaster Prediction System
A Streamlit-based interactive dashboard for visualizing global natural disaster data and predicting disaster risk using machine learning models for floods, earthquakes, and wildfires.

 Features-
🗺️ Interactive World Map — visualize historical disasters by type and year range using Folium
📊 Data Analytics — summary statistics, total deaths, affected populations, and economic damage
🌊 Flood Risk Prediction — XGBoost model trained on historical flood data
🌋 Earthquake Risk Prediction — ML model for seismic event classification
🔥 Wildfire Risk Prediction — Deep learning model (TensorFlow/Keras) for fire risk assessment
🔍 Filter by Disaster Type & Year Range — interactive sidebar controls


Project Structure
Disaster-Prediction-System/
│
├── dashboard.py                          # Main Streamlit dashboard app
├── EMDA.ipynb                            # Data preprocessing notebook
│
├── Top 9 Disasters Filtered.csv          # Processed disaster dataset
├── flood.csv                             # Flood-specific training data
├── EMDAT Custom Request Apr 2025.xlsx    # Raw source data (EM-DAT)
│
├── Model/
│   ├── Final_XGBoost_Model_for_Flood_Prediction.pkl
│   ├── Earthquake_Model.pkl
│   └── Wildfire_Prediction_Model.h5
│
├── requirements.txt                      # Python dependencies
└── .gitignore

Getting Started:
1. Clone the repository
bashgit clone https://github.com/sam-priti/Disaster-Prediction-System.git
cd Disaster-Prediction-System
2. Create a virtual environment (recommended)
bashpython -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
3. Install dependencies
bashpip install -r requirements.txt
4. Run the dashboard
bashstreamlit run dashboard.py

Requirements:
streamlit
pandas
folium
streamlit-folium
openpyxl
xgboost
tensorflow
scikit-learn

See requirements.txt for the full list.


Data Source:
Disaster data sourced from EM-DAT: The International Disaster Database — maintained by the Centre for Research on the Epidemiology of Disasters (CRED).
The dataset covers the top 9 most frequent global disaster types, filtered and preprocessed for dashboard use.

ML Models:
ModelTypeFileFlood PredictionXGBoost ClassifierFinal_XGBoost_Model_for_Flood_Prediction.pklEarthquake PredictionScikit-learn ModelEarthquake_Model.pklWildfire PredictionDeep Learning (Keras)Wildfire_Prediction_Model.h5

Authors:
Sampriti Mohanty
Himanshu Maurya


📄 License
This project is for academic and educational purposes.
