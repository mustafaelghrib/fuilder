# Fuilder
A dashboard for users to build dynamic forms easily!

## Features
- Build forms dynamically and preview what you are building simultaneously.
- Add long forms with pages and sections and questions of type number, text and many more.
- The question types include number, text, image, multiple and single choice, location, and slider.
- You could build forms at the same time, the dashboard add forms to a queue and build them in background.
- Generate a unique link for your users to submit the forms.
- A real time notification service that notify you when users submit forms.

## Architecture
Fuilder is built on a microservices' architecture, and contain those microservices:
- **Users Service**: This service is responsible for registering, logining and validating users.
- **Forms Service**: This service is responsible for managing forms.
- **Form Builder Service**: This service is responsible for building forms.

## Tech Stacks
- **Backend**: Python, Django, PostgreSQL
- **Infrastructure**: Terraform, Google Cloud Platform (GCP)
- **Deployment**: Docker, Kubernetes


