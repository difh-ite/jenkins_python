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
            sh 'pwd' 
            sh 'ls -la' 
            sh 'python -V' 
            sh 'git clone https://github.com/difh-ite/jenkins_python.git' 
            sh 'ls -la jenkins_python'  
          } 
          stage('Static Code Check')  
          { 
            sh 'pwd' 
            sh 'ls -la' 
            sh 'python -V' 
            sh 'git clone https://github.com/difh-ite/jenkins_python.git' 
            sh 'ls -la jenkins_python' 
          } 
          stage('Unit Test Check')  
          { 
            sh 'python3 -m unittest check_os.py'
          } 
        }
      } 
    } 
  } 

