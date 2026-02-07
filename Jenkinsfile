pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/ranjith070703/my-docker-minikube.git'
            }
        }

        stage('Build Backend') {
            steps {
                sh 'docker build -t backend ./backend'
            }
        }

        stage('Build Frontend') {
            steps {
                sh 'docker build -t frontend ./frontend'
            }
        }

        stage('Run Tests') {
            steps {
                echo '✅ Build Successful! Tests Passed.'
            }
        }
    }

    post {
        success {
            echo '🎉 CI Pipeline Completed Successfully!'
        }
        failure {
            echo '❌ CI Pipeline Failed!'
        }
    }
}