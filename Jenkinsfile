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
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }   
    }
    stage('deploy') {
      steps {
                sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
        }
    }
  }
}
