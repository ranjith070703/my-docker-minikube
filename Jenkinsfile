pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/ranjith070703/my-docker-minikube.git'
            }
        }

        stage('Start Minikube') {
            steps {
                bat '''
                echo 🚀 Starting Minikube...
                minikube start --driver=docker
                echo ✅ Minikube started successfully!
                '''
            }
        }

        stage('Setup Docker Environment') {
            steps {
                bat '''
                echo 🔧 Setting up Docker environment for Minikube...
                for /f "delims=" %%i in ('minikube docker-env') do @%%i
                echo ✅ Docker environment configured.
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                bat '''
                echo 🐳 Building backend and frontend images...
                docker build -t my-backend:latest ./backend
                docker build -t my-frontend:latest ./frontend
                echo ✅ Docker images built successfully!
                '''
            }
        }

        stage('Deploy to Minikube') {
            steps {
                bat '''
                echo 🚀 Deploying to Minikube...
                kubectl apply -f k8s/
                echo ✅ Deployment files applied!
                '''
            }
        }

        stage('Verify Pods and Services') {
            steps {
                bat '''
                echo 📊 Checking Pods...
                kubectl get pods
                echo ✅ Pods are running!

                echo 🔍 Checking Services...
                kubectl get svc
                echo ✅ Services are active!
                '''
            }
        }
    }

    post {
        success {
            echo '🎉 Jenkins Pipeline Completed Successfully! ✅'
        }
        failure {
            echo '❌ Jenkins Pipeline Failed — Check build logs.'
        }
    }
}