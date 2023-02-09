import streamlit as st
import base64

st.set_page_config(
    page_title='RESEARCH ARTICLES', 
    layout = 'centered', 
    initial_sidebar_state = 'auto'
)

st.title("Research Papers PDFs")
def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

option = st.selectbox('RESEARCH ARTICLES',
    ('Machine Learning:The High-Interest Credit Card of Technical Debt',
        'Machine Learning Operations (MLOps):Overview-Definition and Architecture', 
        'Operationalizing Machine Learning: An Interview Study',
        'The Deep Learning Revolution and Its Implications for Computer Architecture and Chip Design',
        'Understanding Data Storage and Ingestion for Large-Scale Deep Recommendation Model Training',
        'A Large-Scale Comparison of Python Code in Jupyter Notebooks and Scripts',
        'Quality issues in Machine Learning Software Systems',
        'How to avoid machine learning pitfalls:a guide for academic researchers'))


if option == 'Machine Learning:The High-Interest Credit Card of Technical Debt':
    show_pdf('articles/Machine learning_ the high-interest credit card of technical debt.pdf')

elif option == 'Machine Learning Operations (MLOps):Overview-Definition and Architecture':
    show_pdf('articles/MLOps-overview-definition-architecture.pdf')

elif option == 'Operationalizing Machine Learning: An Interview Study':
    show_pdf('articles/Operationalizing-machine-learning.pdf')

elif option == 'The Deep Learning Revolution and Its Implications for Computer Architecture and Chip Design':
    show_pdf('articles/deep-learning-revolution.pdf')

elif option == 'Understanding Data Storage and Ingestion for Large-Scale Deep Recommendation Model Training':
    show_pdf('articles/data-storage-and-ingestion.pdf')

elif option == 'A Large-Scale Comparison of Python Code in Jupyter Notebooks and Scripts':
    show_pdf('articles/large-scale-compaison.pdf')

elif option == 'Quality issues in Machine Learning Software Systems':
    show_pdf('articles/Quality-issues-in-ML.pdf')

elif option == 'How to avoid machine learning pitfalls:a guide for academic researchers':
    show_pdf('articles/machine-learning-pitfalls.pdf')