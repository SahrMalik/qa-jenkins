pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh '''
                echo "Building the application..."
                pwd
                touch build.txt
                echo "Build completed" > build.txt
                ls -la
                '''
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                echo "Running tests..."
                mkdir -p test_results
                touch test_results/test_output.txt
                echo "Tests passed" > test_results/test_output.txt
                ls -la test_results/
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                sh '''
                echo "Deploying the application..."
                mv build.txt deploy.txt
                pwd
                ls -la
                echo "Deployment completed"
                '''
            }
        }
    }
}
