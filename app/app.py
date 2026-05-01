import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# Load model
model = pickle.load(open("../outputs/model.pkl", "rb"))

st.set_page_config(page_title="SalesAI Pro", layout="centered")

# ---------- SESSION STATE ----------
if "prediction" not in st.session_state:
    st.session_state.prediction = None

# ---------- PREMIUM CSS ----------
st.markdown("""
<style>

/* ---------- FULL BACKGROUND FIX ---------- */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* ---------- REMOVE WHITE BLOCK ---------- */
[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stToolbar"] {
    right: 2rem;
}

/* ---------- TEXT COLORS ---------- */
h1, h2, h3, p, label {
    color: #e0f2fe !important;
}

/* ---------- INPUT BOXES ---------- */
.stNumberInput input {
    background-color: rgba(255,255,255,0.1);
    color: white;
    border-radius: 8px;
}

/* ---------- BUTTON BASE ---------- */
.stButton > button {
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-weight: 600;
    border: none;
    transition: all 0.3s ease;
}

/* ---------- HOVER FIX (IMPORTANT) ---------- */
.stButton > button:hover {
    background: linear-gradient(135deg, #00f260, #0575e6);
    transform: scale(1.03);
    box-shadow: 0px 6px 20px rgba(0,0,0,0.4);
}

/* ---------- REMOVE BUTTON RED BORDER ---------- */
button:focus {
    outline: none !important;
    box-shadow: none !important;
}
/* ---------- NUMBER INPUT BOX ---------- */
.stNumberInput input {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 10px;
    border: none;
    padding: 10px;
    font-weight: 500;
}

/* ---------- LABEL TEXT ---------- */
label {
    color: #e0f2fe !important;
    font-weight: 500;
}

/* ---------- + / - BUTTONS ---------- */
.stNumberInput button {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title(" Smart Marketing Intelligence")
st.write("Optimize your advertising strategy with AI-powered predictions 📊")

st.divider()

# ---------- INPUT ----------
st.subheader("💰 Advertising Budget Planner")

col1, col2, col3 = st.columns(3)

with col1:
    tv = st.number_input("TV Ads", 0.0, 300.0, 150.0)

with col2:
    radio = st.number_input("Radio Ads", 0.0, 50.0, 25.0)

with col3:
    newspaper = st.number_input("Newspaper Ads", 0.0, 100.0, 50.0)

st.divider()

# ---------- BUTTONS ----------
colA, colB = st.columns(2)

with colA:
    predict_clicked = st.button("🚀 Predict Sales")

with colB:
    graph_clicked = st.button("📊 Show Insights")

# ---------- PREDICTION ----------
if predict_clicked:
    input_data = pd.DataFrame(
        [[tv, radio, newspaper]],
        columns=["TV", "Radio", "Newspaper"]
    )

    st.session_state.prediction = model.predict(input_data)[0]

# ---------- RESULT ----------
if st.session_state.prediction is not None:
    st.success(f"📈 Predicted Sales: {st.session_state.prediction:.2f} units")

    st.subheader("📌 Key Insight")

    if tv > radio and tv > newspaper:
        st.write("👉 TV advertising is your strongest growth driver")
    elif radio > tv:
        st.write("👉 Radio ads are giving solid engagement")
    else:
        st.write("👉 Balanced strategy — diversify for better reach")

# ---------- GRAPHS ----------
if graph_clicked:

    # Bar Chart
    st.subheader("📊 Budget Distribution")

    spends = ["TV", "Radio", "Newspaper"]
    values = [tv, radio, newspaper]

    fig1, ax1 = plt.subplots()
    ax1.bar(spends, values)
    ax1.set_title("Ad Spend Allocation")
    st.pyplot(fig1)

    # Pie Chart
    st.subheader("🥧 Budget Share")

    fig2, ax2 = plt.subplots()
    ax2.pie(values, labels=spends, autopct='%1.1f%%')
    ax2.set_title("Spending Ratio")
    st.pyplot(fig2)

    # Simulated Trend Graph (🔥 looks advanced)
    st.subheader("📈 Sales vs TV Spend Trend")

    tv_range = list(range(0, 300, 20))
    predictions = []

    for val in tv_range:
        temp = pd.DataFrame([[val, radio, newspaper]],
                            columns=["TV", "Radio", "Newspaper"])
        predictions.append(model.predict(temp)[0])

    fig3, ax3 = plt.subplots()
    ax3.plot(tv_range, predictions)
    ax3.set_xlabel("TV Spend")
    ax3.set_ylabel("Predicted Sales")
    ax3.set_title("Impact of TV Advertising")
    st.pyplot(fig3)

# ---------- FOOTER ----------
st.divider()
st.write(f"💼 Budget → TV: {tv} | Radio: {radio} | Newspaper: {newspaper}")
