# 🚀 My Docker + Minikube + CI/CD Project

This project demonstrates a *full-stack application* (Frontend + Backend) running inside *Docker containers, deployed on **Kubernetes (Minikube), and automated using **GitHub Actions (CI/CD pipeline)*.

---

## 🧩 Tech Stack
- *Frontend:* React (Node.js)
- *Backend:* Python Flask
- *Containerization:* Docker & Docker Compose
- *Orchestration:* Kubernetes (Minikube)
- *Automation:* GitHub Actions (CI/CD)

---

## ⚙️ Project Structure
my-docker-minikube/ ├── backend/                 # Flask backend API ├── frontend/                # React frontend app ├── k8s/                     # Kubernetes deployment & service files │   ├── backend-deployment.yml │   ├── backend-service.yml │   ├── frontend-deployment.yml │   └── frontend-service.yml ├── docker-compose.yml       # Docker Compose setup └── .github/workflows/ci-cd.yml  # GitHub Actions CI/CD file

---

## 🐳 Docker Commands

Build and run locally:
```bash
docker-compose up --build

Check running containers:

docker ps


---

☸️ Kubernetes (Minikube) Setup

Start Minikube:

minikube start

Apply deployments and services:

kubectl apply -f k8s/

Access services:

minikube service frontend-service
minikube service backend-service


---

⚡ CI/CD Pipeline

GitHub Actions automatically:

1. Builds Docker images


2. Runs tests (if configured)


3. Deploys to Minikube or test environment



Check your workflow status under the Actions tab on GitHub ✅


---

🌐 URLs

Service	URL Example

Frontend http://localhost:8080/
Backend	 http://localhost:5000/


(Your URLs may vary — check using minikube service list)


---

🧠 Author

Ranjith Kumar
📧 ranjithkumar2003kpm@gmail.com
🎓 MCA Student | Full Stack Developer


---

🏁 Status

✅ Frontend Working
✅ Backend Working
✅ Minikube Deployment Successful
✅ CI/CD Pipeline Active
