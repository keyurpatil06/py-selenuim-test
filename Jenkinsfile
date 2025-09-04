pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/keyurpatil06/py-selenuim-test.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh 'python -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }

    post {
        always {
            junit '**/test-results/*.xml' // if you configure pytest to generate XML
        }
    }
}