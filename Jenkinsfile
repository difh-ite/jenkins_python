podTemplate(containers: [
  containerTemplate(
    name: 'python', 
    image: 'jenkins/inbound-agent-python:latest', 
    command: 'sleep', 
    args: '30d')
]) 
{
  node(POD_LABEL)
  {
    stage('Get a Python Project')
    {
      container('python')
      {
          stage('Checkout Code')
          {
            sh 'pwd'
            sh 'ls -la'
            sh 'python -V'
            sh 'hostname'
            sh 'git clone https://github.com/difh-ite/jenkins_python.git'
            sh 'ls -la jenkins_python'
          }
          stage(' Installing packages')
          {
            sh 'pwd'
            sh 'ls -la'
            sh 'python -V'
            sh 'apt install -y pip'
            sh 'pip install requests'
          }
          stage('Static Code Check')
          {
            sh 'pwd'
            sh 'ls -la'
            sh 'python -V'
            sh 'ls -la jenkins_python'
          }
      }
    }
  }
}