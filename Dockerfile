# Use official lightweight Nginx image
FROM nginx:alpine

# Metadata
LABEL maintainer="DevOps Team"
LABEL description="Welcome Webpage with JavaScript Date Display"

# Copy static web assets to Nginx default document directory
COPY index.html /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/
COPY app.js /usr/share/nginx/html/

# Expose standard HTTP port
EXPOSE 80

# Run Nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
