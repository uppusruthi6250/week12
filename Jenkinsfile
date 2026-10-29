
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat 'python -m pytest -v tests/test_registrationapp.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t seleniumdemapp:v1 .'
            }
        }

        stage('Docker Login and Push') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKERHUB_USER',
                        passwordVariable: 'DOCKERHUB_TOKEN'
                    )
                ]) {
                    bat 'echo %DOCKERHUB_TOKEN% | docker login -u %DOCKERHUB_USER% --password-stdin'
                    bat 'docker tag seleniumdemapp:v1 uppusruthi6250/sample:seleniumtestimage'
                    bat 'docker push uppusruthi6250/sample:seleniumtestimage'
                }
            }
        }

        stage('Deploy Week 12 to Kubernetes') {
            steps {
                bat 'kubectl apply -f week12-deployment.yaml'
                bat 'kubectl apply -f week12-service.yaml'
                bat 'kubectl rollout status deployment/week12-registration-deployment --timeout=120s'
            }
        }
    }

    post {
        success {
            echo 'Week-12 CI/CD pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the Jenkins console output.'
        }
    }
}
