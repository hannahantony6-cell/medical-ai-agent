import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def analyze_symptoms(name, age, symptoms, severity, history):
    prompt = f"""You are an expert medical AI assistant. Analyze this patient and respond professionally.

Patient Details:
- Name: {name}
- Age: {age}
- Symptoms: {symptoms}
- Severity: {severity}
- Medical History: {history}

Respond in this exact format:
POSSIBLE CONDITIONS: [list 2-3 possible conditions]
URGENCY LEVEL: [CRITICAL / HIGH / MODERATE / LOW]
IMMEDIATE ACTION: [what to do right now]
RECOMMENDED TESTS: [tests the doctor should order]
ADVICE: [general advice for patient]"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def parse_and_display(result, name, age, severity):
    lines = result.strip().split('\n')
    data = {}
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip()

    # Header
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #1a1a2e, #16213e); 
                padding: 20px; border-radius: 15px; margin-bottom: 20px;
                border-left: 5px solid #e94560;'>
        <h2 style='color: white; margin:0;'>🏥 Medical Analysis Report</h2>
        <p style='color: #a0a0a0; margin:0;'>Patient: {name} | Age: {age} | Severity: {severity}</p>
    </div>
    """, unsafe_allow_html=True)

    # Urgency Level with color
    urgency = data.get('URGENCY LEVEL', severity).upper()
    urgency_colors = {
        'CRITICAL': '#ff4444',
        'HIGH': '#ff8800',
        'MODERATE': '#ffcc00',
        'LOW': '#00cc44'
    }
    color = urgency_colors.get(urgency, '#ff8800')

    st.markdown(f"""
    <div style='background: {color}22; border: 2px solid {color}; 
                padding: 15px; border-radius: 10px; margin-bottom: 15px; 
                text-align: center;'>
        <h2 style='color: {color}; margin:0;'>⚠️ URGENCY: {urgency}</h2>
    </div>
    """, unsafe_allow_html=True)

    # Cards for each section
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style='background: #1e1e2e; padding: 15px; 
                    border-radius: 10px; margin-bottom: 15px;
                    border-top: 3px solid #7c3aed;'>
            <h4 style='color: #7c3aed;'>🔬 Possible Conditions</h4>
            <p style='color: #e0e0e0;'>{data.get('POSSIBLE CONDITIONS', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style='background: #1e1e2e; padding: 15px; 
                    border-radius: 10px; margin-bottom: 15px;
                    border-top: 3px solid #0ea5e9;'>
            <h4 style='color: #0ea5e9;'>🧪 Recommended Tests</h4>
            <p style='color: #e0e0e0;'>{data.get('RECOMMENDED TESTS', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style='background: #1e1e2e; padding: 15px; 
                    border-radius: 10px; margin-bottom: 15px;
                    border-top: 3px solid #e94560;'>
            <h4 style='color: #e94560;'>🚨 Immediate Action</h4>
            <p style='color: #e0e0e0;'>{data.get('IMMEDIATE ACTION', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style='background: #1e1e2e; padding: 15px; 
                    border-radius: 10px; margin-bottom: 15px;
                    border-top: 3px solid #10b981;'>
            <h4 style='color: #10b981;'>💡 Advice</h4>
            <p style='color: #e0e0e0;'>{data.get('ADVICE', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)

    # Disclaimer
    st.markdown("""
    <div style='background: #2a2a2a; padding: 10px; border-radius: 8px; 
                margin-top: 20px; text-align: center;'>
        <p style='color: #888; margin:0; font-size: 12px;'>
        ⚕️ This AI analysis is for informational purposes only. 
        Always consult a qualified medical professional for diagnosis and treatment.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Streamlit UI
st.set_page_config(
    page_title="Medical AI Agent", 
    page_icon="🏥",
    layout="wide"
)

st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h1 style='color: #e94560;'>🏥 AI Medical Emergency Response System</h1>
    <p style='color: #888;'>Powered by LLaMA 3.3 70B • For Medical Assistance Only</p>
</div>
""", unsafe_allow_html=True)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input("👤 Patient Name")
    age = st.number_input("🎂 Age", min_value=1, max_value=120, value=25)

with col2:
    severity = st.selectbox("⚠️ Severity Level",
                           ["Low", "Moderate", "High", "Critical"])
    history = st.text_input("📋 Medical History")

with col3:
    symptoms = st.text_area("🤒 Symptoms", height=103)

st.divider()

if st.button("🔍 Analyze Patient", use_container_width=True, type="primary"):
    if name and symptoms:
        with st.spinner("🤖 AI agents analyzing patient data..."):
            result = analyze_symptoms(name, age, symptoms, severity, history)
        parse_and_display(result, name, age, severity)
    else:
        st.error("⚠️ Please fill in Patient Name and Symptoms!")