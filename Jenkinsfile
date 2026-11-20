
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
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests'
                sh 'python3 -m unittest discover -s tests -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Creating deployment package'

                sh '''
                    mkdir -p deployment
                    cp metrics_exporter.py requirements.txt deployment/
                '''

                archiveArtifacts artifacts: 'deployment/**',
                                 fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check stage logs.'
        }
    }
}
