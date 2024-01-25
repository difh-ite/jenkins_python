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
            sh 'pip install -r requirements.txt' 
          } 
          stage('Static Code Check')  
          { 
            sh 'python3 sys2.py' 
 
          } 
          stage('Unit Test Check')  
          { 
            sh 'python3 -m unittest sys2.py'
          } 
        }
      } 
    } 
  } 

