#!/bin/bash

# Replace the placeholder with the actual backend host
sed -i "s/@BACKEND_HOST@/$BACKEND_HOST/g" /etc/nginx/sites-available/fundoo

# Start nginx
nginx -g "daemon off;"

