pipeline {
    agent any
//     agent{
//         label 'IP_address'
//     }
    
//     environment {
//         FILE_NAME = "obs_misc"+${env.IMAGE}+"custom-report.csv"
//     }
    
    stages {
        stage('Blackduck scan') {
            steps {
                script {
                      env.IMAGE = input message: 'Please enter the image path',
                                         parameters: [string(defaultValue: '',
                                                      description: '',
                                                      name: 'Image')]
                      }
                script {
                 file_name = "obs_misc"
            }  
                echo "Image: ${env.IMAGE}"
                echo "blackduck scan running..."
                echo "${file_name}"
//                 sh 'curl -LO https://asdrepo.isus.emc.com:443/artifactory/devsvcs-config-local/obsscan && chmod 755 obsscan'
//                 sh "./obsscan --scan-image=${env.IMAGE}"
//                 workspace = env.WORKSPACE
//                 echo "Current workspace is ${env.WORKSPACE}"
            }
        }
        
//         stage('Requirements installation') {
//             steps {
//                 sh 'pip install -r requirements.txt'
//                 echo "Requirements installation done..."
//             }
//         }
        
//         stage('Task 1') {
//             steps {
//                 sh 'python3 py_filter_csv.py obs_misc-bookkeeper-operator-0.1.9-107-8c4f6b6-custom-report.csv'
//                 echo "xyz_filtered.csv and xyz-report.csv created..."
//             }
//         }
        
//         stage('Task 2') {
//             steps {
//                 sh 'python3 component.py obs_misc-bookkeeper-operator-0.1.9-107-8c4f6b6-custom-report_filtered.csv bookkeeper-operator-report.csv'
//                 echo "task1.csv created..."
//             }
//         }
        
//         stage('Task 3') {
//             steps {
//                 sh 'python3 scrape_SUSE.py task1.csv'
//                 echo "task3.csv created..."
//             }
//         }
//         stage('Task 4') {
//             steps {
//                 sh 'python3 compare_version.py task3.csv'
//                 echo "task4.csv created..."
//             }
//         }

    }
}
