import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = '지역별도서관현황_20240724115856.csv'
library_data = pd.read_csv(file_path, encoding='cp949')

# Clean the data
library_data = library_data[library_data['지역(1)'] != '지역(1)']  # Remove header rows within the data
library_data['도서관 수'] = library_data['2021'].str.replace(',', '').astype(int)

# Streamlit app
st.title('지역별 도서관 수 비율')

# Select region
region = st.text_input('지역을 입력하세요:', '서울')

if region:
    # Filter data for the specified region
    region_data = library_data[library_data['지역(1)'].str.contains(region)]
    other_data = library_data[~library_data['지역(1)'].str.contains(region)]

    if not region_data.empty:
        region_count = region_data['도서관 수'].sum()
        other_count = other_data['도서관 수'].sum()
        
        # Values and labels for the pie chart
        values = [region_count, other_count]
        labels = [region, '기타']
        colors = ['#ff9999', '#66b3ff']
        
        # Plot pie chart
        fig1, ax1 = plt.subplots()
        ax1.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        
        st.pyplot(fig1)
        st.write(f"{region}의 도서관 수 비율")
        st.write(f"{region}의 도서관 수: {region_count}개")
        st.write(f"기타 지역의 도서관 수: {other_count}개")
    else:
        st.write(f"{region}에 해당하는 데이터가 없습니다.")

