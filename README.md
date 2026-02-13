# Ronak Pradhan - Portfolio Website

A minimalist, dashboard-style portfolio website built with **Flask**, featuring an AI-powered chatbot integrated with **Groq**.

![Dashboard Screenshot](/Users/ronakpradhan15/.gemini/antigravity/brain/edc313d9-7b0c-4c3a-9adb-5d3dc7c2cb99/.system_generated/click_feedback/click_feedback_1770952807349.png)

## Features

-   **Dashboard UI**: Clean, responsive design with a dark sidebar and light content area.
-   **Dynamic Content**: Profile data, experience, projects, and skills are loaded dynamically.
-   **AI Chatbot**: A floating chat widget powered by Groq (`llama-3.3-70b-versatile`) that answers questions based on your resume.
-   **Resume Parsing**: Automatically extracts text from `2026_Resume.pdf` to provide context for the chatbot.

## Tech Stack

-   **Backend**: Flask (Python)
-   **Frontend**: HTML, CSS, JavaScript
-   **AI/LLM**: Groq API
-   **PDF Processing**: pypdf

## Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd Portfolio
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Environment Variables**:
    Create a `.env` file in the root directory and add your Groq API key:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    ```

4.  **Add your Resume**:
    Ensure your resume file is named `2026_Resume.pdf` and placed in the root directory.

## Usage

1.  **Run the application**:
    ```bash
    python3 app.py
    ```

2.  **Open in Browser**:
    Navigate to `http://127.0.0.1:5000`

## Customization

-   **Data**: Edit `data.py` to update your profile information manually if PDF extraction misses anything or for fallback data.
-   **Styles**: Modify `static/css/style.css` to change the look and feel.
