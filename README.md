Here's the README in markdown format as code:

```
# Image Classifier Comparison

This application allows you to compare the performance of various image classifiers available on the Hugging Face Hub. You can upload an image, and the application will display the top k predictions for each model, along with a bar chart of the mean scores for each label across all models.

## Features

- Upload an image in JPG, JPEG, or PNG format
- Select the top k classes for the predictions
- Compare the predictions of multiple image classification models
- Display the mean scores for each label in a bar chart
- Download the mean scores data as a CSV file

## Models

The following image classification models are compared in this application:

- apple/mobilevit-small
- facebook/deit-base-patch16-224
- facebook/convnext-base-224
- google/vit-base-patch16-224
- microsoft/resnet-50
- microsoft/swin-base-patch4-window7-224
- microsoft/beit-base-patch16-224
- nvidia/mit-b0

## Installation

1. Clone this repository or download the source code.

   ```
   git clone https://github.com/your_username/image-classifier-comparison.git
   ```

2. Change to the project directory.

   ```
   cd image-classifier-comparison
   ```

3. Create a new virtual environment (optional, but recommended).

   ```
   python -m venv venv
   ```

4. Activate the virtual environment.

   ```
   # For Windows:
   venv\Scripts\activate

   # For macOS/Linux:
   source venv/bin/activate
   ```

5. Install the required packages from the `requirements.txt` file.

   ```
   pip install -r requirements.txt
   ```

6. Run the Streamlit application.

   ```
   streamlit run app.py
   ```

7. Open the provided URL in your web browser to use the application.

## Usage

1. Upload an image using the file uploader in the sidebar.
2. Adjust the slider to select the top k classes for the predictions.
3. Click the "Classify" button to process the image and display the results.
4. View the bar chart of mean scores for each label.
5. Download the mean scores data as a CSV file by clicking the "Download data as CSV" button.
```
