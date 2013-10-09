class test {
  file { "/home/vagrant/test":
       content => template("test/test2.rb"),
       ensure => present
     }
} 
