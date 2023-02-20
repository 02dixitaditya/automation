pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python3 py_filter_csv.py obs_misc-bookkeeper-operator-0.1.9-107-8c4f6b6-custom-report.csv'
                sh 'python3 component.py obs_misc-bookkeeper-operator-0.1.9-107-8c4f6b6-custom-report_filtered.csv bookkeeper-operator-report.csv'
                sh 'python3 scrape_SUSE.py task1.csv'
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
