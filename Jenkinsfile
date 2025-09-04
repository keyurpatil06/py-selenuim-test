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
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                withEnv(["PATH=C:\\path\\to\\chromedriver;${env.PATH}"]) {
                    sh 'pytest --junitxml=results.xml'
                }
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
            echo "Pipeline finished (success or failure)"
        }
    }
}
