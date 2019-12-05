#!/bin/bash
a2enmod rewrite

service apache2 stop

apachectl -D FOREGROUND
