pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest tests/test_pipeline.py -v'
            }
        }

        stage('Dockerize') {
            steps {
                sh 'docker build -t data-pipeline .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run data-pipeline'
            }
        }
    }
}