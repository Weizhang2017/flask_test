pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
        sh 'python -m pip install -r requirements.txt --user --no-cache'
        }      
      }
    }
    stage('test') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'python test.py'
         } 
      }   
    }
  }
}
