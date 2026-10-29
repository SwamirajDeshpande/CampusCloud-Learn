# ☁️ CampusCloud Learn

### A Cloud-Based Academic Resource Sharing Platform

CampusCloud Learn is a web application designed to help students discover and share academic learning resources in one place. Built using Python and Streamlit, the application integrates Firebase Cloud Firestore to store academic resource information.

The project demonstrates how a web application can be deployed online and connected to a cloud database.

## 🚀 Live Demo

**Live Application:** https://campuscloud-learn.streamlit.app/.

## ✨ Features

- 📚 **Academic Resource Sharing:** Submit academic learning resources through the application.
- ☁️ **Cloud Database Integration:** Store resource information in Firebase Cloud Firestore.
- 🖥️ **Interactive Web Interface:** Built using Streamlit and Python.
- 📝 **Resource Information:** Organize resources using details such as title, subject, semester, and description.
- 🌐 **Online Deployment:** Access the application through a web browser.
- 🔐 **Secure Configuration:** Keep Firebase service-account credentials in Streamlit Secrets rather than hardcoding them in the source code.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web application interface |
| Firebase Cloud Firestore | Cloud NoSQL database |
| Firebase Admin SDK | Server-side database integration |
| Streamlit Community Cloud | Application deployment |
| Git and GitHub | Version control and source code hosting |

## 🏗️ Architecture

```text
          Student
             |
             v
    Streamlit Web App
             |
             v
      Python Backend
             |
             v
    Firebase Admin SDK
             |
             v
    Cloud Firestore
             |
             v
    Resource Information
```

The user interacts with the Streamlit interface. The Python backend processes submissions and communicates with Firestore through the Firebase Admin SDK. Resource information is stored in the cloud database.

## ⚙️ How It Works

1. A user opens the CampusCloud Learn web application.
2. The user enters academic resource information through the interface.
3. The application validates the submitted information.
4. The backend sends the resource information to Firebase Cloud Firestore.
5. The stored data can be inspected in the Firebase Console and retrieved by the application.

## 💻 Run Locally

### Prerequisites

- Python 3.10 or a compatible version for your dependencies.
- A Google account.
- A Firebase project with Cloud Firestore enabled.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/campuscloud-lite.git
cd campuscloud-lite
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

Create or use the project's `requirements.txt` file:

```text
streamlit
firebase-admin
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 4. Configure Firebase

- Open the Firebase Console.
- Select your Firebase project.
- Enable Cloud Firestore.
- Configure a Firebase Admin SDK service account.
- Keep the service-account credentials private.

For local development, place the credentials in a secure location and configure the application to read them securely. Do not commit credential files to GitHub.

### 5. Configure Streamlit Secrets

For deployment, open your application's **Settings → Secrets** in Streamlit Community Cloud and add the Firebase service-account configuration in TOML format.

Use the following structure with your own credentials:

```toml
[firebase]
type = "service_account"
project_id = "YOUR_FIREBASE_PROJECT_ID"
private_key_id = "YOUR_PRIVATE_KEY_ID"
private_key = "YOUR_PRIVATE_KEY"
client_email = "YOUR_SERVICE_ACCOUNT_EMAIL"
client_id = "YOUR_CLIENT_ID"
token_uri = "https://oauth2.googleapis.com/token"
```

Include any additional fields required by your service-account JSON file. Preserve the private key's newline formatting when configuring it.

**Never publish real credentials, private keys, or secrets in your repository.**

### 6. Run the application

```bash
streamlit run app.py
```

The application will open locally in your browser.

## ☁️ Cloud Integration

### Firebase Cloud Firestore

Cloud Firestore is a managed NoSQL document database used to store academic resource information.

The application uses the Firebase Admin SDK to interact with the database from its Python backend.

Example of storing a resource:

```python
db.collection("resources").add({
    "title": "Python Programming Guide",
    "subject": "Python",
    "semester": "Semester 1"
})
```

The example illustrates the basic database write operation. The actual application may store additional fields depending on the submission form.

### Deployment

The application is deployed using Streamlit Community Cloud, which hosts the Streamlit interface and runs the Python application.

Firebase Cloud Firestore provides the cloud database functionality. Although Firestore is part of Google's cloud ecosystem, the web application itself is hosted on Streamlit Community Cloud rather than directly on Google Cloud Run or Compute Engine.

## 🔒 Security Considerations

- Store service-account credentials in secure secrets configuration.
- Never commit private keys or credential JSON files to GitHub.
- Validate user-submitted data before saving it.
- Restrict access to service-account credentials.
- Follow the principle of least privilege wherever possible.
- Avoid exposing sensitive error messages to application users.

## 🎯 Learning Outcomes

Through this project, I explored:

- Building web applications using Python and Streamlit.
- Deploying an application to a cloud-hosted platform.
- Integrating a web application with a managed NoSQL database.
- Storing and retrieving information using Firebase Cloud Firestore.
- Managing application configuration and credentials securely.
- Understanding practical cloud computing concepts.

## 🔮 Future Enhancements

- Upload and store PDF files using cloud object storage.
- Add authentication and role-based access control.
- Implement resource search and filtering.
- Add resource editing and deletion functionality.
- Introduce categories and improved resource organization.
- Improve validation, logging, and error handling.
- Explore deployment using Google Cloud Run or another cloud platform.

These are proposed enhancements and are not necessarily part of the current implementation.

## 👨‍💻 Author

**Swamiraj Deshpande**

Student | Computer Science and Engineering (AI & ML)

Interested in cloud computing, artificial intelligence, machine learning, and software development.

---

*CampusCloud Learn — Making academic resources easier to share and access.*

