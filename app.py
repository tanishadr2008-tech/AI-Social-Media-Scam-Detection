import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from link_detector import detect_suspicious_link
from ml_model import predict_scam


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Scam Detection",
    page_icon="🛡️",
    layout="wide"
)


# ---------------- SESSION STATE ----------------

if "history" not in st.session_state:
    st.session_state.history = []

if "safe_count" not in st.session_state:
    st.session_state.safe_count = 0

if "suspicious_count" not in st.session_state:
    st.session_state.suspicious_count = 0

if "high_risk_count" not in st.session_state:
    st.session_state.high_risk_count = 0

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False


# ---------------- DARK MODE ----------------

dark_mode = st.toggle(
    "🌙 Dark Mode",
    value=st.session_state.dark_mode
)

st.session_state.dark_mode = dark_mode


if st.session_state.dark_mode:

    st.markdown("""
    <style>

    .stApp {
        background-color: #121212;
        color: white;
    }

    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp p,
    .stApp label {
        color: white;
    }

    </style>
    """, unsafe_allow_html=True)


# ---------------- TITLE ----------------

st.title("🛡️ AI Social Media and Online Scam Detection")

st.write(
    "Analyze social media messages and links for suspicious scam patterns using Rule-Based and AI/ML Detection."
)

st.divider()


# ---------------- DASHBOARD STATISTICS ----------------

st.subheader("📊 Dashboard Statistics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "🟢 Safe Messages",
    st.session_state.safe_count
)

col2.metric(
    "🟡 Suspicious Messages",
    st.session_state.suspicious_count
)

col3.metric(
    "🔴 High Risk Messages",
    st.session_state.high_risk_count
)


# ---------------- ADVANCED ANALYTICS ----------------

st.divider()

st.subheader("📈 Advanced Analytics")

if st.session_state.history:

    total_messages = len(st.session_state.history)

    total_score = sum(
        item.get("Score", 0)
        for item in st.session_state.history
    )

    average_score = total_score / total_messages

    highest_score = max(
        item.get("Score", 0)
        for item in st.session_state.history
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "📩 Total Messages Analyzed",
        total_messages
    )

    col2.metric(
        "📈 Average Risk Score",
        f"{average_score:.2f}"
    )

    col3.metric(
        "⚠️ Highest Risk Score",
        highest_score
    )

else:

    st.info(
        "Analyze some messages to see advanced analytics."
    )


# ---------------- USER INPUT ----------------

st.divider()

st.subheader("🔍 Analyze Message or Link")

message = st.text_area(
    "Enter a social media message or suspicious link:",
    placeholder="Example: URGENT! You won a lottery prize. Click here!"
)


# ---------------- ANALYZE BUTTON ----------------

if st.button("🔎 Analyze Message"):

    if message.strip():

        # ---------------- RULE-BASED DETECTION ----------------

        score, risk, patterns = detect_suspicious_link(message)


        # ---------------- AI / ML PREDICTION ----------------

        ml_prediction, ml_confidence = predict_scam(message)


        # ---------------- CLASSIFICATION ----------------

        if risk == "LOW":
            classification = "SAFE"

        elif risk == "MEDIUM":
            classification = "SUSPICIOUS"

        elif risk == "HIGH":
            classification = "HIGH RISK"

        else:
            classification = risk


        # ---------------- UPDATE STATISTICS ----------------

        if classification == "SAFE":

            st.session_state.safe_count += 1

        elif classification == "SUSPICIOUS":

            st.session_state.suspicious_count += 1

        elif classification == "HIGH RISK":

            st.session_state.high_risk_count += 1


        # ---------------- SAVE ANALYSIS HISTORY ----------------

        st.session_state.history.append({

            "Date & Time": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "Message": message,

            "Score": score,

            "Risk": risk,

            "Classification": classification,

            "ML Prediction": ml_prediction,

            "ML Confidence": f"{ml_confidence}%"

        })


        # ---------------- ANALYSIS RESULT ----------------

        st.divider()

        st.subheader("📊 Analysis Result")


        # ---------------- AI / ML RESULT ----------------

        st.subheader("🤖 AI/ML Scam Prediction")

        ml_col1, ml_col2 = st.columns(2)

        ml_col1.metric(
            "🤖 AI Prediction",
            ml_prediction
        )

        ml_col2.metric(
            "🎯 ML Confidence",
            f"{ml_confidence}%"
        )


        # ---------------- RISK SCORE ----------------

        st.subheader("📈 Rule-Based Risk Score")

        st.progress(
            min(int(score), 100)
        )

        st.write(
            f"**Score: {score}/100**"
        )


        # ---------------- CLASSIFICATION RESULT ----------------

        st.subheader("🛡️ Rule-Based Classification")

        if classification == "SAFE":

            st.success(
                "🟢 SAFE MESSAGE"
            )

        elif classification == "SUSPICIOUS":

            st.warning(
                "🟡 SUSPICIOUS MESSAGE"
            )

        else:

            st.error(
                "🔴 HIGH RISK MESSAGE"
            )


        # ---------------- SUSPICIOUS PATTERNS ----------------

        if patterns:

            st.subheader(
                "⚠️ Suspicious Patterns Found"
            )

            for pattern in patterns:

                st.write(
                    f"• {pattern}"
                )

        else:

            st.success(
                "✅ No suspicious patterns detected."
            )


    else:

        st.warning(
            "⚠️ Please enter a message or link first."
        )


# ---------------- ANALYSIS HISTORY ----------------

st.divider()

st.subheader("📝 Analysis History")

if st.session_state.history:

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        width="stretch"
    )

else:

    st.info(
        "No messages analyzed yet."
    )


# ---------------- DOWNLOAD HISTORY AS CSV ----------------

st.divider()

st.subheader("📁 Download Analysis History")

if st.session_state.history:

    history_df = pd.DataFrame(
        st.session_state.history
    )

    csv = history_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download Analysis History as CSV",
        data=csv,
        file_name="scam_analysis_history.csv",
        mime="text/csv"
    )

else:

    st.info(
        "Analyze some messages before downloading the history."
    )


# ---------------- RISK DISTRIBUTION ----------------

st.divider()

st.subheader("📊 Risk Distribution")

if st.session_state.history:

    safe_count = sum(
        1
        for item in st.session_state.history
        if item.get("Classification", "") == "SAFE"
    )

    suspicious_count = sum(
        1
        for item in st.session_state.history
        if item.get("Classification", "") == "SUSPICIOUS"
    )

    high_risk_count = sum(
        1
        for item in st.session_state.history
        if item.get("Classification", "") == "HIGH RISK"
    )


    # ---------------- CHART DATA ----------------

    chart_data = pd.DataFrame({

        "Risk Level": [
            "SAFE",
            "SUSPICIOUS",
            "HIGH RISK"
        ],

        "Count": [
            safe_count,
            suspicious_count,
            high_risk_count
        ]

    })


    # ---------------- BAR CHART ----------------

    st.subheader("📊 Bar Chart")

    st.bar_chart(
        chart_data,
        x="Risk Level",
        y="Count",
        width="stretch"
    )


    # ---------------- PIE CHART ----------------

    st.subheader(
        "🥧 Risk Distribution Pie Chart"
    )

    values = [
        safe_count,
        suspicious_count,
        high_risk_count
    ]

    labels = [
        "SAFE",
        "SUSPICIOUS",
        "HIGH RISK"
    ]


    if sum(values) > 0:

        fig, ax = plt.subplots()

        ax.pie(
            values,
            labels=labels,
            autopct="%1.1f%%"
        )

        ax.set_title(
            "Scam Risk Distribution"
        )

        st.pyplot(fig)


else:

    st.info(
        "Analyze some messages to see the risk distribution charts."
    )


# ---------------- CLEAR HISTORY ----------------

st.divider()

if st.button("🗑️ Clear History"):

    st.session_state.history = []

    st.session_state.safe_count = 0

    st.session_state.suspicious_count = 0

    st.session_state.high_risk_count = 0

    st.rerun()


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "🛡️ AI in Social Media and Online Scam Detection Project | Rule-Based + Machine Learning Detection"
)