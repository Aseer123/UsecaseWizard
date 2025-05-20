# UsecaseWizard - Agentic AI Use Case Generator

## 🔍 Overview

The **Agentic AI Use Case Generator** is a lightweight web application built using **Streamlit**. It allows users to generate high-impact and realistic agentic AI use cases tailored to specific domains (Healthcare, Retail, and Banking). Users input a persona, pain point, and optional constraints, and the system leverages a language model (Zephyr-7B via Hugging Face) to return 3 use cases.

This project was developed as a solution for the **UST Agentic AI Hackathon**.

---

## 🎯 Key Features

* **Domain-specific AI use case generation**
* **Prompt customization using persona, pain points, and constraints**
* **Categorized agent types shown for inspiration**
* **Offline fallback use cases**
* **Download results as JSON or Markdown**

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/UST-Global-GenAI/Agentic-AI-Hackathon.git
cd Agentic-AI-Hackathon
```

### 2. Create and Activate Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Hugging Face Access

To enable use case generation via the Hugging Face Zephyr-7B model, you need a free API token.

#### Step 1: Sign Up or Log In

Go to [https://huggingface.co](https://huggingface.co) and create a free account or log in.

#### Step 2: Get Your API Token

1. Click your profile icon in the top-right corner.
2. Go to **Settings** → **Access Tokens**.
3. Click **New Token**:

   * Name it (e.g., `ust-hackathon-token`)
   * Role: `Read`
4. Copy the token.

#### Step 3: Add Token to Environment

Create a `.env` file in your project root (same folder as `app.py`) and paste:

```env
HF_TOKEN=your_token_here
```

🔒 **Note**: Never share this token publicly.

#### Step 4: You're Ready!

Now, when you run the app, it will authenticate securely with Hugging Face.

### 5. Run the App

```bash
streamlit run app.py
```

---

## 🧪 Usage

1. Select the domain (Healthcare, Retail, or Banking)
2. Enter the user persona (e.g., "Hospital Administrator")
3. Describe the pain point (e.g., "manual data entry")
4. Optionally, enter any constraints (e.g., "low cost, HIPAA compliance")
5. Click **Generate Use Cases**
6. View results and download them in your preferred format

---

## 📦 File Structure

```
UST-agentic-ai/
├── app.py                # Main Streamlit application
├── .env                  # Your Hugging Face API token
├── requirements.txt      # Python dependencies
├── sample_output.json    # Sample JSON output (generated)
├── sample_output.md      # Sample Markdown output (generated)
└── README.md             # You're reading it now
```

---

## 📹 Demo Video

A 3-minute demo video is included in the submission.

---

## 📎 Dependencies

* `streamlit`
* `requests`
* `python-dotenv`
* `pandas`
* `numpy`

Install all dependencies via:

```bash
pip install -r requirements.txt
```

---

## 📌 License

MIT License

---

## 🙌 Acknowledgments

Special thanks to UST and the organizing team for creating this opportunity to innovate with Agentic AI.

---

## ✍️ Author

\[Shaik Aseeruddin | UID: 287966] – \[shaik.aseeruddin@ust.com][personal- aseeruddin317@gmail.com]
