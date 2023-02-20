pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python3 py_filter_csv.py obs_misc-bookkeeper-operator-0.1.9-107-8c4f6b6-custom-report.csv'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying stage....'
            }
        }
    }
}
