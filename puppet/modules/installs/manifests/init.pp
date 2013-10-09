class installs {
    package { 'launchy':
         ensure   => 'installed',
         provider => 'gem',
    }

}

