# init-config-kubernetes
Init container for Kubernetes to create config files with jinja2.

## Usage
Create a new image based on this image. Put the config files in `/templates`. If to be rendered with jinja2, the file must have the extension ".jinja2". Example Dockerfile:
```dockerfile
FROM vojeroen/init-config:latest
COPY config.ini /templates/config.ini.jinja2
```

The rendered files will have the same filename as the template files, without the ".jinja2" extension. They are stored in `/config`, so this directory must be mounted in both the init container and the containers for which the configuration is generated, e.g. as an emptyDir. 
