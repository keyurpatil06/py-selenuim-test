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
                // Make sure Python and pip are installed on Jenkins agent
                sh '''
                    python --version
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest and generate JUnit-style report
                sh 'pytest --junitxml=results.xml'
            }
        }

        stage('Publish Results') {
            steps {
                // Publish the pytest results in Jenkins
                junit 'results.xml'
            }
        }
    }

    post {
        always {
            echo "Pipeline finished (success or failure)"
        }
    }
}
