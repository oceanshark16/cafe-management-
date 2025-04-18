pipeline {
    agent any

    environment {
        PYTHON_PATH = 'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/oceanshark16/cafe-management-.git'
            }
        }

        stage('Check Python Version') {
            steps {
                bat "${env.PYTHON_PATH} --version"
            }
        }

        stage('Install Requirements') {
            steps {
                bat "${env.PYTHON_PATH} -m pip install --upgrade pip"
                script {
                    def reqFile = 'requirements.txt'
                    if (fileExists(reqFile) && readFile(reqFile).trim()) {
                        bat "${env.PYTHON_PATH} -m pip install -r ${reqFile}"
                    } else {
                        echo "No external packages to install from requirements.txt"
                    }
                }
            }
        }

        stage('Syntax Check') {
            steps {
                bat "${env.PYTHON_PATH} -m py_compile main.py"
            }
        }

        stage('Run GUI App (Optional)') {
            steps {
                echo 'This app uses Tkinter. GUI can run only if Jenkins has desktop support.'
                // Uncomment below line if Jenkins is running on a GUI-supported system
                // bat "${env.PYTHON_PATH} main.py"
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Build failed!'
        }
        success {
            echo 'Build succeeded.'
        }
    }
}
