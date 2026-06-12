#  AI Medical Emergency Response System

An intelligent medical analysis system powered by LLaMA 3.3 70B AI that 
analyzes patient symptoms and provides instant emergency response guidance.

## What it does

- Patient enters name, age, symptoms, severity and medical history
- AI analyzes symptoms using LLaMA 3.3 70B model
- Instantly classifies urgency as CRITICAL / HIGH / MODERATE / LOW
- Provides possible conditions, immediate actions, recommended tests and advice
- Color coded urgency display — Red for Critical, Yellow for Moderate, Green for Low
- Medical disclaimer included for safety

##  Demo

<img width="1877" height="655" alt="image" src="https://github.com/user-attachments/assets/216515b6-ebe1-423d-972a-22a53dc91dde" />


<img width="1870" height="772" alt="image" src="https://github.com/user-attachments/assets/fa7a929e-5f9d-4cd7-ad3e-1833947dd642" />



##  Tech Stack

| Technology | Purpose |
|------------|---------|
| Streamlit | Frontend UI |
| Python | Backend logic |
| Groq API | AI inference engine |
| LLaMA 3.3 70B | Large language model |

##  How it works

Patient fills the form
↓
Python builds medical prompt
↓
Groq API sends to LLaMA 3.3 70B
↓
AI analyzes symptoms using medical knowledge
↓
Response parsed and displayed
with color coded urgency cards

##  How to run locally

**Step 1 — Clone the repo**
git clone https://github.com/hannahantony6-cell/medical-ai-agent.git
cd medical-ai-agent

**Step 2 — Install dependencies**
pip install -r requirements.txt

**Step 3 — Add your Groq API key**

Create a file `.streamlit/secrets.toml` and add:
GROQ_API_KEY = "your_groq_api_key_here"
Get your free API key at: https://console.groq.com

**Step 4 — Run the app**
streamlit run app.py

##  Sample Test Cases

### Critical Case
| Field | Value |
|-------|-------|
| Name | John Smith |
| Age | 58 |
| Severity | Critical |
| History | diabetic, hypertensive |
| Symptoms | severe chest pain radiating to left arm, shortness of breath, sweating, nausea |

### Moderate Case
| Field | Value |
|-------|-------|
| Name | Sarah Johnson |
| Age | 32 |
| Severity | Moderate |
| History | asthma |
| Symptoms | persistent cough for 5 days, mild fever, fatigue, slight difficulty breathing |


Live Demo
https://medical-ai-agent-sw9a2us5bhcvar5kfhh77k.streamlit.app/
