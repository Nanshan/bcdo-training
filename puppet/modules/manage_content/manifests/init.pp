class manage_content {
  $admins = ['Joe', 'Kate', 'Trey']
  file { '/etc/sudoers':
       owner => root,
       group => root,
       mode => 440, 
       #content => template("manage_content/sudoers.erb"),
       source => 'puppet:///manage_content/sudoers',
       }
  

  file { '/etc/sudoers.test':
       owner => root,
       group => root,
       mode => 440, 
       content => template("manage_content/sudoers.erb"),
       }
}
