CI-CD-Pipeline-for-Python-Flask-Application-using-Jenkins-and-AWS

This is a Python Flask-based web application that lets users play Tic Tac Toe either against the computer or with friends.
The project uses HTML templates for the game interface (home.html, play_computer.html, play_friends.html) and integrates with a backend Flask server to handle game logic.
A CI/CD pipeline is implemented using Jenkins and GitHub webhooks, deploying the app to an AWS EC2 instance via Gunicorn for production-grade performance.

![Uploading Screenshot 2025-08-13 132926.png…]()


pipeline {
    agent any
 
    stages {
        stage('git cloning') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/tejasKhamkar2211/CI-CD-Pipeline-for-Python-Flask-Application-using-Jenkins-and-AWS.git']])
                echo 'cloning files from github'
            }
        }
        stage('Build') {
            steps {
                sh '''
                      python3 -m pip install -r requirements.txt  
                '''
                echo 'Building nodejs project'
            }
        }
        stage('Test') {
            steps {
                sh "python3 -m unittest discover -s test -v"
                echo 'Testing project'
            }
        }
        stage('Deploy') {
            steps {
                sshagent(['54.205.140.130']) {
                 // some block
                 sh '''
                  ssh -o StrictHostKeyChecking=no ec2-user@54.205.140.130 << EOF
                  echo "Connected to Server"
                 cd /home/ec2-user/tictacpro
                 git pull origin master
                 pip install -r requirements.txt
                 sudo service  tictac restart
                 '''
                }
                echo 'Deploying nodejs project on live server'
            }
        }
    }
}
