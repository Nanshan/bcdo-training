{% from "apache/map.jinja" import apache with context %}

include:
  - apache

/etc/apache2/sites-enabled/000-default:
  file:
   - absent 

/etc/apache2/sites-available/default:
  file:
    - absent

/etc/apache2/sites-available/default-ssl:
  file:
    - absent

/var/www/index.html:
  file:
   - absent

{% for id, site in salt['pillar.get']('apache:sites', {}).items() %}

{{ id }}:
  file:
    - managed
    - name: {{ apache.vhostdir }}/{{ id }}
    - source: {{ site.get('template_file', 'salt://apache/vhosts/standard.tmpl') }}
    - template: {{ site.get('template_engine', 'jinja') }}
    - context:
        id: {{ id|json }}
        site: {{ site|json }}
        map: {{ apache|json }}
    - require:
      - pkg: apache
    - watch_in:
      - cmd: apache-reload

{% if grains.os_family == 'Debian' %}
a2ensite {{ id }}:
  cmd:
    - run
    - require:
      - file: {{ id }}
    - watch_in:
      - cmd: apache-reload
{% endif %}

{% endfor %}
