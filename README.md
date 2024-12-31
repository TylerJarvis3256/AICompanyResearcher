# AI Company Research Tool

An AI-powered tool built with Streamlit that leverages the OpenAI API to perform detailed company research. This application is designed for professionals conducting client research, with a focus on analyzing employee benefits programs and generating insights from company data.

Users can upload a CSV file containing company names and receive a downloadable CSV response with detailed employee benefit research for each company. This includes benefit providers, industry insights, and AI-driven summaries.

---

## 🚀 Features
- **CSV Upload and Output**: Easily upload a CSV file with company names and download a CSV file containing detailed research.
- **Employee Benefits Analysis**: Provides insights into company employee benefits programs and providers.
- **Company Summaries**: Generate concise overviews of a company's employee benefits programs and their providers.
- **Interactive UI**: Built with **Streamlit** for a user-friendly, browser-based interface.

---

## 🛠️ Tech Stack
- **Programming Language**: Python
- **Framework**: Streamlit
- **API**: OpenAI API
- **Libraries**: pandas

---

## 📂 Project Structure
```
root
├── main.py
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- OpenAI API key (sign up [here](https://platform.openai.com/signup/))
- Streamlit installed

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/TylerJarvis3256/AICompanyResearcher.git
   cd AICompanyResearcher
   ```

2. Install dependencies:
   ```bash
   pip install streamlit
   ```

3. Add your API key:
   - Open the `main.py` file.
   - Replace `Add-Your-Key-Here` with your OpenAI API key:
     ```python
     client = OpenAI(api_key='Add-Your-Key-Here',)
     ```

---

### 🖥️ Usage
1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

2. Open your browser to the link provided by Streamlit (usually `http://localhost:8501`).

3. Use the app’s interface to upload a csv of company names and generate downloadable AI-driven research.
   - **Upload a CSV file** containing company names.
   - **Generate AI-driven research** on employee benefits for each company.
   - **Download a CSV file** with the detailed results.

---

## 📝 To-Do
- [ ] Clean up UI and improve visual design.
- [ ] Add detailed error handling for invalid CSV formats.

---

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push:
   ```bash
   git add .
   git commit -m "Added feature-name"
   git push origin feature-name
   ```

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💬 Contact
- **Author**: Tyler Jarvis
- **Email**: tylerjarvis3256@gmail.com
- **LinkedIn**: [Tyler Jarvis LinkedIn](https://www.linkedin.com/in/tyler-jarvis-b8a72023b/)
- **GitHub**: [Tyler Jarvis GitHub](https://github.com/TylerJarvis3256)
