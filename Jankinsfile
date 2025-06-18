pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo "Cloning the repository..."
                git url: 'https://github.com/kushalPatel-kp/ML-Project', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t django_ml_app .'
            }
        }

        stage('Stop & Remove Old Container') {
            steps {
                echo "Stopping any previous container..."
                sh '''
                    if [ "$(docker ps -aq -f name=django_ml_container)" ]; then
                        docker rm -f django_ml_container
                    fi
                '''
            }
        }

        stage('Run Django Container') {
            steps {
                echo "Running Django container..."
                sh 'docker run -d -p 8000:8000 --name django_ml_container django_ml_app'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline finished successfully!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}
