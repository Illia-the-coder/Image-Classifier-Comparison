import streamlit as st
from transformers import pipeline
from PIL import Image
import pandas as pd

model_names = [
    "apple/mobilevit-small",
    "facebook/deit-base-patch16-224",
    "facebook/convnext-base-224",
    "google/vit-base-patch16-224",
    "microsoft/resnet-50",
    "microsoft/swin-base-patch4-window7-224",
    "microsoft/beit-base-patch16-224",
    "nvidia/mit-b0",
]

def process(image_file, top_k):
    labels = []
    for m in model_names:
        p = pipeline("image-classification", model=m)
        pred = p(image_file)
        labels.append({x["label"]: x["score"] for x in pred[:top_k]})
    return labels

@st.cache_data
def convert_df(df):
    # Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

st.set_page_config(page_title="Image Classifier Comparison", page_icon=None, layout="centered", initial_sidebar_state="expanded")

st.title("Image Classifier Comparison")
st.sidebar.title("Settings")
image = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
top_k = st.sidebar.slider("Top k classes", min_value=1, max_value=5, value=5)

if image is not None:
    st.image(image, use_column_width=True)
    image = Image.open(image)

    if st.sidebar.button("Classify"):
        labels = process(image, top_k)

        combined_scores = {}
        label_count = {}
        for i, model in enumerate(model_names):
            for label, score in labels[i].items():
                if label not in combined_scores:
                    combined_scores[label] = score
                    label_count[label] = 1
                else:
                    combined_scores[label] += score
                    label_count[label] += 1

        # Calculate mean scores for each label
        mean_scores = {label: combined_scores[label] / label_count[label] for label in combined_scores}

        # Create a DataFrame with the mean_scores and display as a bar chart
        mean_df = pd.DataFrame(list(mean_scores.items()), columns=["Label", "Mean Score"])
        st.bar_chart(mean_df.groupby("Label")["Mean Score"].mean().sort_values())

        # Export data as CSV
        st.markdown("## Download Data")
        csv_data = convert_df(mean_df)
        st.download_button(
            label="Download data as CSV",
            data=csv_data,
            file_name='mean_scores.csv',
            mime='text/csv',
        )
