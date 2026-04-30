import streamlit as st
from PIL import Image
from model import predict_image
import time

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="SkinVision",
    page_icon="🧠",
    layout="centered"
)

# -------------------------
# Custom CSS (UI upgrade 🔥)
# -------------------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 20px;
}
.result-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #1c1f26;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------
st.markdown('<div class="title">🧠 SkinVision</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Skin Disease Detection</div>', unsafe_allow_html=True)
st.markdown("---")

# -------------------------
# Upload Section
# -------------------------
uploaded_file = st.file_uploader("📤 Upload a skin image", type=["jpg", "png", "jpeg"])

# -------------------------
# Main Logic
# -------------------------
if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", width=300)

    st.markdown("### 🔍 Analyzing...")

    with st.spinner("Running AI model..."):
        time.sleep(1.5)
        prediction, confidence = predict_image(image)

    # Result Card
    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    st.markdown(f"### 🧾 {prediction}")
    st.markdown(f"### 📊 Confidence: {confidence}%")

    if confidence > 90:
        st.success("High confidence prediction")
    else:
        st.warning("Moderate confidence - verify result")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# Footer
# -------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:gray;'>Built with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)