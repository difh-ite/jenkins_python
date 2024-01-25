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
            sh 'git clone https://github.com/difh-ite/jenkins_python.git'
            sh 'ls -la jenkins_python'  
          } 
          stage('Installing Packages')  
          { 
            sh 'apt-get install python3-pip -y'
            sh 'apt-get install python3-requests -y'
            sh 'apt-get install python3-psutil -y'
            sh 'apt install pylint -y'

          } 
          stage('Static Code Check')  
          { 
            sh 'pylint jenkins_python/sys2.py' 
          } 
          stage('Unit Test Check')  
          { 
            sh 'python3 -m unittest jenkins_python/sys2.py'
          } 
        }
      } 
    } 
  } 

