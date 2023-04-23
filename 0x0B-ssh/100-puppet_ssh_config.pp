# Setting up a client ssh configuration file

file_line { 'Change the main private key': 
   path => '/etc/ssh/ssh_config', 
   line => 'IdentityFile ~/.ssh/school', 
} 
  
file_line { 'No Authenticate with passowrd': 
   path => '/etc/ssh/ssh_config', 
   line => 'PasswordAuthentication no', 
}
