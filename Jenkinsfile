podTemplate(containers: [
  containerTemplate(
    name: 'python',
    image: 'jenkins/inbound-agent-python:latest',
    command: 'sleep',
    args: '30d'
  )
]) {
  node(POD_LABEL) {
    stage('Checkout Code') {
      container('python') {
        steps {
          checkout scm
        }
      }
    }

    stage('Installing Packages') {
      container('python') {
        steps {
          script {
            sh 'python -m pip install --upgrade pip'
            sh 'pip install -r requirements.txt'
          }
        }	
      }
    }

    stage('System Monitoring') {
      container('python') {
        steps {
          script {
            sh 'python sys2.py'
          }
        }
      }
    }
  }
}
