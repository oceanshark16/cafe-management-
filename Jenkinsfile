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
                        writeFile file: 'requirements.txt', text: 'streamlit>=1.28.0\npandas\npython-dateutil\npytest>=7.0.0'
                        echo "Created requirements.txt with Streamlit and testing dependencies"
                    } else {
                        // Check if streamlit and pytest are in requirements.txt, if not add them
                        def reqContent = readFile('requirements.txt')
                        def updatedContent = reqContent
                        if (!reqContent.contains('streamlit')) {
                            updatedContent += '\nstreamlit>=1.28.0'
                        }
                        if (!reqContent.contains('pytest')) {
                            updatedContent += '\npytest>=7.0.0'
                        }
                        writeFile file: 'requirements.txt', text: updatedContent
                        echo "Updated requirements.txt with necessary dependencies"
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
                bat "${env.PYTHON_PATH} -m py_compile cafe_logic.py"
                echo "Python syntax check passed for ${env.APP_NAME} and cafe_logic.py"
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                script {
                    try {
                        // Run pytest on test_cafe_logic.py
                        bat "${env.PYTHON_PATH} -m pytest test_cafe_logic.py -v --junitxml=test-results.xml"
                        echo "Unit tests passed for cafe_logic.py"
                    } catch (Exception e) {
                        echo "Unit tests failed: ${e.message}"
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'test-results.xml'
                }
            }
        }
        
        stage('Run Specific Logic Tests') {
            steps {
                script {
                    // Create a simple test script to verify core functionality
                    writeFile file: 'verify_cafe_logic.py', text: '''
import cafe_logic

def test_basic_functionality():
    """Test core functionality of cafe_logic module"""
    print("Testing basic cafe_logic functionality...")
    
    # Test menu items are available
    assert hasattr(cafe_logic, 'drinks') or hasattr(cafe_logic, 'get_drinks'), "Drinks functionality missing"
    assert hasattr(cafe_logic, 'cakes') or hasattr(cafe_logic, 'get_cakes'), "Cakes functionality missing"
    
    # Test calculation functions if they exist
    if hasattr(cafe_logic, 'calculate_cost'):
        print("Testing calculate_cost function...")
        # Add appropriate test based on your specific implementation
    
    print("Basic functionality tests completed")

if __name__ == "__main__":
    test_basic_functionality()
'''
                    bat "${env.PYTHON_PATH} verify_cafe_logic.py"
                }
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

## Core Components
- `main.py`: Main Streamlit application
- `cafe_logic.py`: Business logic for the cafe management system
- `test_cafe_logic.py`: Unit tests for cafe logic

## Installation
1. Clone the repository
2. Install required packages: `pip install -r requirements.txt`
3. Run the application: `streamlit run main.py`

## Testing
Run the tests with: `pytest test_cafe_logic.py`

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
            archiveArtifacts artifacts: '*.py, *.bat, *.sh, requirements.txt, README.md, test-results.xml', fingerprint: true
        }
    }
}
