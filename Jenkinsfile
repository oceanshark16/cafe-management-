pipeline {
    agent any
    
    environment {
        PYTHON_PATH = 'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
        APP_NAME = 'main.py'
    }
    
    options {
        skipDefaultCheckout(true)
    }
    
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/oceanshark16/cafe-management-.git'
            }
        }
        
        stage('Check Python Version') {
            steps {
                bat "${env.PYTHON_PATH} --version"
            }
        }
        
        stage('Create/Update Requirements File') {
            steps {
                script {
                    // If requirements.txt doesn't exist, create it with minimal requirements
                    if (!fileExists('requirements.txt')) {
                        writeFile file: 'requirements.txt', text: 'streamlit>=1.28.0\npandas\npython-dateutil'
                        echo "Created requirements.txt with Streamlit dependencies"
                    } else {
                        // Check if streamlit is in requirements.txt, if not add it
                        def reqContent = readFile('requirements.txt')
                        if (!reqContent.contains('streamlit')) {
                            writeFile file: 'requirements.txt', text: reqContent + '\nstreamlit>=1.28.0'
                            echo "Added Streamlit to existing requirements.txt"
                        }
                    }
                }
            }
        }
        
        stage('Install Requirements') {
            steps {
                bat "${env.PYTHON_PATH} -m pip install --upgrade pip"
                bat "${env.PYTHON_PATH} -m pip install -r requirements.txt"
            }
        }
        
        stage('Syntax Check') {
            steps {
                bat "${env.PYTHON_PATH} -m py_compile ${env.APP_NAME}"
                echo "Python syntax check passed for ${env.APP_NAME}"
            }
        }
        
        stage('Generate Documentation') {
            steps {
                script {
                    writeFile file: 'README.md', text: '''# Cafe Management System

A Streamlit-based application for managing a cafe's orders, billing, and receipts.

## Features

- Add drinks and cakes to the order
- Calculate costs, taxes, and total bill
- Generate detailed receipts
- Reset functionality for new orders

## Installation

1. Clone the repository
2. Install required packages: `pip install -r requirements.txt`
3. Run the application: `streamlit run main.py`

## License

MIT
'''
                    echo "Generated README.md documentation"
                }
            }
        }
        
        stage('Prepare for Deployment') {
            steps {
                script {
                    // Create a simple deployment script
                    writeFile file: 'deploy.sh', text: '''#!/bin/bash
pip install -r requirements.txt
streamlit run main.py --server.port=8501
'''
                    // Create a Windows batch version too
                    writeFile file: 'deploy.bat', text: '''@echo off
pip install -r requirements.txt
streamlit run main.py --server.port=8501
'''
                    bat "attrib +x deploy.bat"
                    echo "Created deployment scripts"
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished.'
        }
        
        failure {
            echo 'Build failed! Check the logs for details.'
        }
        
        success {
            echo 'Build succeeded! Cafe Management System is ready for deployment.'
            // Archive the artifacts
            archiveArtifacts artifacts: '*.py, *.bat, *.sh, requirements.txt, README.md', fingerprint: true
        }
    }
}
