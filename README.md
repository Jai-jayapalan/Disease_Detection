# Multiple Disease Detection from MRI Images Using CNN

This project aims to leverage the power of Convolutional Neural Networks (CNN) to detect multiple diseases from MRI images. Utilizing advanced deep learning techniques, we have developed a comprehensive solution capable of identifying the following conditions:

- Alzheimer's Disease
- Pneumonia
- Diabetes
- Brain Tumor

Our solution is designed to be user-friendly and accessible via a web API, created with Streamlit, allowing for easy interaction and utilization by clients without the need for in-depth technical knowledge.

## Features

- **Multiple Disease Detection:** Our models can accurately detect Alzheimer's disease, pneumonia, diabetes, and brain tumors from MRI images.
- **User-Friendly Interface:** Powered by Streamlit, our web API provides a simple and intuitive interface for users to upload MRI images and receive instant diagnosis results.
- **High Accuracy Models:** Utilizing Keras and TensorFlow, our CNN models are trained on extensive datasets to ensure high accuracy and reliability.

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/multiple-disease-detection.git
   cd multiple-disease-detection
   ```

2. **Set Up a Virtual Environment** (Optional but recommended)
   - For Unix/macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - For Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```
   
   This will install all necessary packages, including Keras, TensorFlow, Pickle, and Streamlit.

## Usage

To run the web application locally:

```bash
streamlit run app.py
```

Navigate to the displayed URL in your web browser to interact with the application. Follow the on-screen instructions to upload an MRI image and select the type of disease detection model you wish to use. The result will be displayed on the screen.

## Contributing

Contributions to enhance the project are welcome. Please fork the repository and create a pull request with your additions and improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Keras & TensorFlow:** For providing the deep learning framework used to build our models.
- **Streamlit:** For enabling us to create a user-friendly web interface.
- **Pickle:** For model serialization and deserialization.

Thank you for visiting our project. We hope it serves your needs and inspires further development in the field of medical image analysis.

---

Remember to replace placeholder links and texts (like `https://github.com/yourusername/multiple-disease-detection.git`) with your actual data. Adjust any section according to the specifics of your project, such as adding more detailed instructions or providing more context about the creation and purpose of your models.
