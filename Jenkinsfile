pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/keyurpatil06/py-selenuim-test.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                    python --version
                    python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=results.xml'
            }
        }

        stage('Publish Results') {
            steps {
                junit 'results.xml'
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
    }
}
