# 💻 Laptop Price Analytics Dashboard

## 📋 Overview
An interactive business intelligence dashboard for analyzing laptop market data, enabling stakeholders to filter, 
visualize, and extract insights from pricing, ratings, and hardware specifications.

## ✨ Features

- **🔍 Dynamic Filtering** – Refine data by brand, model, and processor type
- **📊 Key Metrics** – Real-time calculation of total price, average rating, and product count
- **📈 Data Visualization**
  - Price distribution by model (line chart)
  - Brand performance by average rating (bar chart)
  - Price-rating correlation analysis (strip plot)
  - RAM vs. screen size relationship (strip plot)
  - - **📋 Tabular Summary** – Expandable data table with grouped averages

## 📁 Repository Structure
| File | Description |
|------|-------------|
| `Dashboard.py` | Streamlit application entry point |
| `Analysis.ipynb` | Jupyter notebook for EDA and data preprocessing |
| `laptop.csv` | Cleaned and transformed dataset |
| `amazon_laptop_prices_v01.csv` | Raw source data |

## 🚀 Installation & Execution
### Clone repository
```git clone https://github.com/Olamilekan-23-ML/Laptop-Price-Analysis-Project.git```
### Install dependencies
```pip install -r requirements.txt```
### Launch dashboard
streamlit run Dashboard.py
_Then open the URL shown in your terminal (usually http://localhost:8501) in your web browser._

## 🛠️ Methodology
Data preprocessing performed in Analysis.ipynb:
🗑️ Removal of irrelevant features
🔄 Handling of missing values via row elimination
🔢 Type conversion for price, screen size, and RAM
📝 Column renaming for clarity

## 🧰 Technology Stack
⚡ Streamlit – Dashboard framework
📊 Plotly – Interactive charting library
🐼 Pandas – Data manipulation and aggregation

## 🤝 Contributing
Contributions are welcome! Please:
Fork the repository
Create a feature branch
Make your changes
Submit a pull request

## 📄 License
This project is for educational and portfolio purposes.

## 📧 Contact
For questions or suggestions about this project, please open an issue in the repository.


## 👤 Author
_DOGO PAUL OLAMILEKAN_
_GitHub: @Olamilekan-23-ML_


