import pandas as pd
import streamlit as st
import plotly.express as px
from numerize.numerize import numerize


st.set_page_config(page_title = 'SaveYourLife Dashboard',
                    layout='wide',
                    initial_sidebar_state='collapsed')

@st.cache
def get_data():
    df = pd.read_csv('data/europa_df.csv')
    df['Año']= pd.to_datetime(df['Año'])
    return df

df = get_data()

header_left,header_mid,header_right = st.columns([1,2,1],gap='large')

with header_mid:
    st.title('SaveYourLife Dashboard')


with st.sidebar:
    Campaign_filter = st.multiselect(label= 'Selecciona Un Pais',
                                options=df['Región'].unique(),
                                default=df['Región'].unique())

    Age_filter = st.multiselect(label='Select Age Group',
                            options=df['Cáncer de mama'].unique(),
                            default=df['Cáncer de mama'].unique())

    Gender_filter = st.multiselect(label='Select Gender Group',
                            options=df['Cáncer de piel maligno'].unique(),
                            default=df['Cáncer de piel maligno'].unique())

df1 = df.query('Región == @Campaign_filter & Cáncer de mama == @Age_filter & Cáncer de piel maligno == @Gender_filter')

total_impressions = float(df1['numero de muertes totales'].sum())
#total_clicks = float(df1['Clicks'].sum())
#total_spent = float(df1['Spent'].sum())
#total_conversions= float(df1['Total_Conversion'].sum()) 
#total_approved_conversions = float(df1['Approved_Conversion'].sum())

st.image('images/impression.png',use_column_width='Auto')
st.metric(label = 'Total Impressions', value= numerize(total_impressions))

Q1,Q2 = st.columns(2)

with Q1:
    df3 = df1.groupby(by = ['Región']).sum()[['numero de muertes totales']].reset_index()
    df3['CTR'] =round(df3['Clicks']/df3['Impressions'] *100,3)
    fig_CTR_by_campaign = px.bar(df3,
                            x='campaign',
                            y='CTR',
                            title='<b>Click Through Rate</b>')
    fig_CTR_by_campaign.update_layout(title = {'x' : 0.5},
                                    plot_bgcolor = "rgba(0,0,0,0)",
                                    xaxis =(dict(showgrid = False)),
                                    yaxis =(dict(showgrid = False)))
    st.plotly_chart(fig_CTR_by_campaign,use_container_width=True)

with Q2:
    fig_impressions_per_day = px.line(df1,x='date',
                                    y=['Impressions'],
                                    color='campaign',
                                    title='<b>Daily Impressions By Campaign</b>')
    fig_impressions_per_day.update_xaxes(rangeslider_visible=True)
    fig_impressions_per_day.update_layout(xaxis_range=['2021-01-01','2021-01-31'],
                                        showlegend = False,
                                        title = {'x' : 0.5},
                                         plot_bgcolor = "rgba(0,0,0,0)",
                                        xaxis =(dict(showgrid = False)),
                                        yaxis =(dict(showgrid = False)),)
    st.plotly_chart(fig_impressions_per_day,use_container_width=True)

Q3,Q4 = st.columns(2)

with Q3:
    df4 = df1.groupby(by='gender').sum()[['Spent']].reset_index()
    fig_spend_by_gender = px.pie(df4,names='gender',values='Spent',title='<b>Ad Spend By Gender</b>')
    fig_spend_by_gender.update_layout(title = {'x':0.5}, plot_bgcolor = "rgba(0,0,0,0)")
    st.plotly_chart(fig_spend_by_gender,use_container_width=True)

with Q4:
    df5 = df1.groupby(by='age').sum()[['Spent','Total_Conversion']].reset_index()
    df5['CPC'] = round(df5['Spent']/df5['Total_Conversion'],2)
    fig_CPC_by_age = px.bar(df5,x = 'age',y='CPC',title='<b>Cost Per Conversion By Age Demographic</b>')
    fig_CPC_by_age.update_layout(title = {'x':0.5},xaxis =(dict(showgrid = False)),yaxis =(dict(showgrid = False)), plot_bgcolor = "rgba(0,0,0,0)")
    st.plotly_chart(fig_CPC_by_age,use_container_width=True)
