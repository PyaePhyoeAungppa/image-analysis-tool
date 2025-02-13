# Image Analysis Tool

A simple yet powerful web application that analyzes images and provides natural language descriptions. Built with Streamlit and the BLIP image captioning model.

## 🌟 Demo

Try out the live demo here: [Image Analysis Tool Demo](https://image-analysis-tool.streamlit.app)

## 🎯 Features

- Clean, minimalist user interface
- Instant image upload and display
- Advanced image analysis using BLIP model
- Real-time image description generation
- Centered layout design
- Support for multiple image formats (PNG, JPG, JPEG)

## 🛠️ Technology Stack

- Python 3.8+
- Streamlit
- Transformers (Hugging Face)
- PIL (Python Imaging Library)
- PyTorch
- BLIP Image Captioning Model

## 📋 Prerequisites

Before running the application, make sure you have Python 3.8 or higher installed on your system.

## ⚙️ Installation

1. Clone the repository:
```bash
git clone git@github.com:PyaePhyoeAungppa/image-analysis-tool.git
cd image-analysis-tool
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## 🚀 Running the Application Locally

1. Navigate to the project directory
2. Run the Streamlit application:
```bash
streamlit run app.py
```
3. Open your web browser and go to `http://localhost:8501`

## 📦 Deployment

This application can be deployed on Streamlit Cloud:

1. Push your code to GitHub
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click on "New app"
4. Select your repository and branch
5. Set the main file path as `app.py`
6. Click "Deploy"

## 📁 Project Structure

```
image-analysis-tool/
├── app.py                 # Main application file
├── requirements.txt       # Project dependencies
├── README.md             # Project documentation
└── .gitignore           # Git ignore file
```

## 📄 Requirements.txt Content

```
streamlit==1.31.0
pillow==10.2.0
transformers==4.37.2
torch==2.2.0
protobuf==4.25.2
```

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

Pyae Phyoe Aung
- GitHub: [@PyaePhyoeAungppa](https://github.com/PyaePhyoeAungppa)