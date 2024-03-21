import os
import subprocess

def get_be_containers():
    # Run the docker command to get container names
    cmd = "docker ps -a --format '{{.Names}}' | grep '^be'"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()

    # Decode output and split it into a list of container names
    container_names = output.decode().splitlines()

    return container_names

def generate_nginx_conf(container_names):
    upstream_block = "upstream backend {\n"
    for idx, container_name in enumerate(container_names, start=1):
        upstream_block += f"    server {container_name}:8000;\n"
    upstream_block += "}\n\n"

    server_block = """server {
    listen 80;
    server_name _default;

    location / {
        include proxy_params;
        proxy_pass http://backend;
    }
}"""

    nginx_conf = upstream_block + server_block
    return nginx_conf

def write_nginx_conf_to_file(nginx_conf_content, file_path):
    if os.path.exists(file_path):
        # Empty the existing file content
        with open(file_path, "w") as nginx_file:
            nginx_file.write("")
    else:
        # Create a new file if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Write the nginx configuration content to the file
    with open(file_path, "a") as nginx_file:
        nginx_file.write(nginx_conf_content)

    print()
    print(f"Nginx configuration file '{file_path}' updated successfully.")
    print()

if __name__ == "__main__":
    be_containers = get_be_containers()
    nginx_conf_content = generate_nginx_conf(be_containers)
    nginx_conf_path = "/project/fe_part/nginx.conf"

    write_nginx_conf_to_file(nginx_conf_content, nginx_conf_path)

