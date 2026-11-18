# Project 13: Welcome Webpage

> **DevOps External Exam / Lab Assignment**
> - **13.a:** Create a simple webpage to display a welcome message and the current date using JavaScript. Perform source code management using Git and GitHub.
> - **13.b:** Deploy the application using Kubernetes and perform automated webpage testing using Selenium.

---

## 1. Project Overview & Features
- **Frontend:** Pure HTML5, CSS3 (minimalist monochrome theme inspired by shadcn/ui), and Vanilla JavaScript.
- **Dynamic Date & Time:** Live date computation formatted with day, month, date, year, and ISO format toggling via JavaScript.
- **Containerization:** Production-ready `Dockerfile` based on `nginx:alpine`.
- **Orchestration:** Kubernetes manifests (`deployment.yaml` with 2 replicas and health probes, `service.yaml` with NodePort `30013`).
- **Automated QA:** Headless Selenium WebDriver automated test suite verifying DOM elements, dynamic date strings, and button events.

---

## 2. Project Structure
```text
13-welcome-webpage/
├── index.html                  # Main UI structure with test IDs
├── style.css                   # Minimalist black & white stylesheet
├── app.js                      # JavaScript logic for welcome & dynamic date
├── Dockerfile                  # Container definition using Nginx Alpine
├── k8s/
│   ├── deployment.yaml         # Kubernetes 2-replica deployment manifest
│   └── service.yaml            # Kubernetes NodePort service manifest
├── tests/
│   ├── test_welcome_page.py    # Automated Selenium test script
│   └── requirements.txt        # Python testing dependencies
├── setup_git.bat               # Automated Git initialization script (Windows)
├── .gitignore                  # Ignored build and test artifacts
└── README.md                   # Documentation & execution guide
```

---

## 3. Source Code Management with Git and GitHub (13.a)

### Step 1: Initialize Local Git Repository
Open a terminal in the `13-welcome-webpage` folder and run:
```bash
git init
git add .
git commit -m "feat: initial commit for Project 13 Welcome Webpage"
```

### Step 2: Push to GitHub
1. Create a new repository on [GitHub](https://github.com/new) named `welcome-webpage`.
2. Connect your local repository and push:
```bash
# Rename default branch to main
git branch -M main

# Add your remote repository URL (replace with your GitHub username)
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/welcome-webpage.git

# Push code to GitHub
git push -u origin main
```

---

## 4. Local Execution
You can open `index.html` directly in any web browser, or serve it using Python's built-in HTTP server:
```bash
# From inside 13-welcome-webpage directory
python -m http.server 8000
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 5. Containerization with Docker
Build and run the Docker image locally:
```bash
# Build the Docker image
docker build -t welcome-webpage:latest .

# Run container on port 8080
docker run -d --name welcome-app -p 8080:80 welcome-webpage:latest
```
Access the application at [http://localhost:8080](http://localhost:8080).

---

## 6. Deploying on Kubernetes (13.b)

Ensure your Kubernetes cluster (`Minikube`, `kind`, `Docker Desktop Kubernetes`, or `k3s`) is running:

```bash
# Apply deployment and service
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Verify pod status
kubectl get pods -l app=welcome-webpage

# Verify service
kubectl get service welcome-webpage-service
```

### Accessing the Application:
- **Minikube:**
  ```bash
  minikube service welcome-webpage-service --url
  ```
- **Port Forwarding (Universal):**
  ```bash
  kubectl port-forward svc/welcome-webpage-service 8080:80
  ```
  Visit [http://localhost:8080](http://localhost:8080).

---

## 7. Automated Webpage Testing using Selenium (13.b)

The test suite automatically tests the page using headless Google Chrome.

### Prerequisites:
Install Python dependencies:
```bash
pip install -r tests/requirements.txt
```

### Run Tests:
```bash
# Test against local index.html directly:
python tests/test_welcome_page.py

# Or test against running Kubernetes/Docker service:
python tests/test_welcome_page.py --url http://localhost:8080
```

### Automated Checks Performed:
1. **Page Title:** Validates that the `<title>` matches "Welcome Webpage | DevOps External".
2. **Welcome Message:** Validates presence and text of `#welcome-message`.
3. **Current Date:** Validates `#current-date` is populated via JavaScript and matches the current calendar year.
4. **Format Toggle Event:** Clicks `#toggle-format-btn` and asserts that the date toggles into `YYYY-MM-DD` ISO format.
5. **Refresh Action:** Clicks `#refresh-btn` and verifies DOM update integrity.
