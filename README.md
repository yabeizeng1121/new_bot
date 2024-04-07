# Mini 9
Author: Yabei Zeng

## About
This project contains a Streamlit app that serves as a chatbot. It's designed to be an interactive and user-friendly interface for answering questions related to Streamlit updates and other inquiries.

## Preparation
To run this Streamlit app locally, follow these steps:

### 1. Install packages
Ensure you have Python and pip installed on your system. Then, install the required packages using:

```bash
pip3 install -r requirements.txt
```

### 2. Modify the `app.py`
Make any necessary changes to `app.py` as needed for your specific implementation.

### 3. Run Streamlit
To launch the app, use the following command:

```bash
python3 -m streamlit run app.py
```

### 4. Local Website
Once the Streamlit app is running, you can access it at: [http://localhost:8501](http://localhost:8501)


### 5. Login with your AWS console and launch an EC2 instance

### 6. Run the following commands
Note: Map your instance's port 8501 to the public internet for Streamlit to be accessible.

Update and upgrade the system packages:

```bash
sudo apt update
sudo apt-get update
sudo apt upgrade -y
```

Install essential tools:

```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```

Clone your project repository:

```bash
git clone "Your-repository-URL"
cd "Your-repository-folder"
```

Install Python 3 pip if not already installed:

```bash
sudo apt install python3-pip
```

Install required Python packages:

```bash
pip3 install -r requirements.txt
```

Run the Streamlit app (temporary):

```bash
python3 -m streamlit run app.py
```

Run the Streamlit app (permanent):

```bash
nohup python3 -m streamlit run app.py &
```

Note: Streamlit runs on port 8501 by default.



Make sure to replace `"Your-repository-URL"` and `"Your-repository-folder"` with the actual URL to your Git repository and the folder name where your `app.py` is located, respectively.