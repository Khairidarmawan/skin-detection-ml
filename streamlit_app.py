import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from recommend import recommend_skincare
from PIL import Image

model = load_model("model.h5")
labels = ["acne", "dry", "normal", "oily"]

st.title("🧠 Skin Detection AI")

uploaded_file = st.file_uploader("Upload gambar wajah", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img = image.resize((224, 224))

    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)
    idx = np.argmax(pred)
    label = labels[idx]
    confidence = float(np.max(pred))

    skincare = recommend_skincare(label)

    st.image(image, caption="Input Image", use_container_width=True)

    st.write(f"### Prediksi: {label}")
    st.write(f"Confidence: {confidence:.2f}")

    for s in skincare:
        st.write("✔ " + s)