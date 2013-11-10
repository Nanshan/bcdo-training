/var/www/wordpress/wp-config.php:                        # ID declaration
  file:                                        # state declaration
    - managed                                  # function
    - source: salt://wordpress/wp-config.php   # function arg


/etc/apache2/sites-enabled/000-default:
  file:
    - managed
    - source: salt://wordpress/000-default
    - require:
      - pkg: apache2
