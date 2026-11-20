pipeline {
    agent any

    options {
        timestamps()
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out successfully'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing Python dependencies'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests'
                bat 'python -m unittest discover -s tests -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Creating deployment package'

                bat '''
                    if not exist deployment mkdir deployment
                    copy /Y metrics_exporter.py deployment\\
                    copy /Y requirements.txt deployment\\
                '''

                archiveArtifacts artifacts: 'deployment/**', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the stage logs.'
        }
    }
}
