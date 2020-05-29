pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    python3 types.py
                    python3 python/files.py
                '''
            }
        }
    }
}
