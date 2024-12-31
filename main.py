import streamlit as st
import pandas as pd
from openai import OpenAI 
import time
import os
import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()

# Set Open AI API Key Here
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))




# Define the ChatGPT prompt function
def get_chatgpt_response(company_name):
    prompt = f"""
    You are a corporate research assistant specializing in analyzing employee benefits and vendor partnerships for companies. Your task is to research and generate a structured summary of a company's employee benefits programs, vendor relationships, and notable features. The company you are providing research for is {company_name}. Provide your findings in the format below:
    Company Name: [Company Name]
    Medical Carriers: [List medical carriers, specify plan types if available (e.g., HMO, PPO, HDHP)]
    PBM: [List pharmacy benefit managers used]
    Diabetes Management: [Programs or vendors addressing diabetes management]
    Chronic Conditions: [Programs or vendors addressing chronic conditions]
    Weight Loss: [Weight loss programs or providers used]
    Benefits Administration: [Vendors managing benefits administration]
    Employee Benefits Navigator: [Tools or vendors offering benefits navigation for employees]
    Other Vendors: [Other relevant benefits-related vendors or programs]
    Notes/Observations: [Key takeaways, unique programs, or observations about the company's benefits strategy]
    Instructions:
    Begin by researching the company's benefits programs. Use search terms like:
    "[Company Name] employee benefits"
    "[Company Name] benefits guide"
    "[Company Name] employee benefits vendors"
    Look for specific details about the company's medical insurance carriers, pharmacy benefit managers, and partnerships with diabetes management or chronic condition solutions.
    Identify any weight loss programs or notable wellness initiatives.
    Search for vendors managing benefits administration or providing employee benefits navigation tools.
    Note any additional benefits-related vendors or unique programs offered by the company.
    If information is unavailable for a category, mark it as "N/A" and provide no additional commentary.
    Example Input:
    Company Name: Acme Inc.
    Example Output:
    Company Name: Acme Inc.
    Medical Carriers: Blue Cross Blue Shield (PPO), Aetna (HMO)
    PBM: Express Scripts
    Diabetes Management: Omada, Livongo
    Chronic Conditions: Livongo
    Weight Loss: Noom
    Benefits Administration: ADP
    Employee Benefits Navigator: Castlight Health
    Other Vendors: Hinge Health, Progeny
    Notes/Observations: Focus on wellness programs with significant investment in chronic condition management and digital health tools.
    Guidelines:
    Use publicly available information, prioritizing credible sources like company websites, benefits handbooks, and news articles.
    Ensure results are concise, accurate, and match the specified output format exactly.
    Emphasize findings from the last two years for relevance.
    Provide no content or commentary beyond the requested format.
    """
    
    try:
        response = client.chat.completions.create(
            messages = [{"role": "user", "content": prompt}],
            model = "gpt-4"
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error {e}"

# Streamlit UI
st.title("Company Research Tool")
st.write("Upload a list of companies , and the program will provide detailed research results using ChatGPT")

# File Uploader
uploaded_file = st.file_uploader("Upload a CSV file with a column named 'Company'", type="csv")

if uploaded_file is not None:
    # Load the CSV file
    df = pd.read_csv(uploaded_file)
    
    if "Company" not in df.columns:
        st.error("The uploaded CSV must have a column named 'Company'.")
    else:
        # Display the list of companies
        st.write(f"Loaded {len(df)} companies from the file:")
        st.dataframe(df.head())
        
        # Start Processing
        if st.button("Start Research"):
            results = pd.DataFrame(columns=[
                "Company", "Medical Carriers", "PBM", "Diabetes Management",
                "Chronic Conditions", "Weight Loss", "Benefits Administration",
                "Employee Benefits Navigator", "Other Vendors", "Notes/Observations"
            ])
            
            progress_bar = st.progress(0)
            widget = st.empty()
            
            with st.spinner("Processing companies... This may take awhile"):
                for i, row in df.iterrows():
                    company = row["Company"]
                    #widget.write(f"Processing {i+1}/{len(df)}: {company}")
                    
                    response = get_chatgpt_response(company)
                    widget.write(response)
                    
                    # Parse the response into structured
                    try:
                        lines = response.split("\n")
                        medical_carriers = next((line.split(":")[1].strip() for line in lines if "Medical Carriers:" in line), "N/A")
                        pbm = next((line.split(":")[1].strip() for line in lines if "PBM:" in line), "N/A")
                        diabetes_management = next((line.split(":")[1].strip() for line in lines if "Diabetes Management:" in line), "N/A")
                        chronic_conditions = next((line.split(":")[1].strip() for line in lines if "Chronic Conditions:" in line), "N/A")
                        weight_loss = next((line.split(":")[1].strip() for line in lines if "Weight Loss:" in line), "N/A")
                        benefits_administration = next((line.split(":")[1].strip() for line in lines if "Benefits Administration:" in line), "N/A")
                        employee_benefits_navigator = next((line.split(":")[1].strip() for line in lines if "Employee Benefits Navigator:" in line), "N/A")
                        other_vendors = next((line.split(":")[1].strip() for line in lines if "Other Vendors:" in line), "N/A")
                        notes_and_observations = next((line.split(":")[1].strip() for line in lines if "Notes/Observations:" in line), "N/A")
                        
                        results.loc[len(results)] = {
                            "Company": company,
                            "Medical Carriers": medical_carriers,
                            "PBM": pbm,
                            "Diabetes Management": diabetes_management,
                            "Chronic Conditions": chronic_conditions,
                            "Weight Loss": weight_loss,
                            "Benefits Administration": benefits_administration,
                            "Employee Benefits Navigator": employee_benefits_navigator,
                            "Other Vendors": other_vendors,
                            "Notes/Observations": notes_and_observations
                        }
                    except Exception as e:
                        results.loc[len(results)] = {
                            "Company": company,
                            "Medical Carriers": "Error",
                            "PBM": "Error",
                            "Diabetes Management": "Error",
                            "Chronic Conditions": "Error",
                            "Weight Loss": "Error",
                            "Benefits Administration": "Error",
                            "Employee Benefits Navigator": "Error",
                            "Other Vendors": "Error",
                            "Notes/Observations": "Error"
                        }
                        
                    # Update progress bar
                    progress_bar.progress((i+1)/len(df))
                        
                    # Delay to avoid rate limits    
                    time.sleep(2)
            
            # Save results to an excel file
            results_file = "company_research_results.xlsx"
            results.to_excel(results_file, index=False)
            
            st.success("Research Completed!")
            with open(results_file, "rb") as file:
                st.download_button(
                    label = "Download Results",
                    data = file,
                    file_name = "company_research_results.xlsx",
                    mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
                        
    