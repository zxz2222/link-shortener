# Simple Link Shortener

This is a basic web application that shortens long URLs. It's built with Python (Flask) for the backend and vanilla HTML, CSS, and JavaScript for the frontend. The application is also containerized using Docker.

## Features

*   Enter a long URL and get a shortened version.
*   Accessing the short URL redirects to the original long URL.
*   Simple, clean interface.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

*   **Python 3.7+:** [Download Python](https://www.python.org/downloads/) (Make sure to check "Add Python to PATH" during installation on Windows).
*   **pip:** Python's package installer (usually comes with Python).
*   **Git:** [Download Git](https://git-scm.com/downloads/) (for cloning the repository).
*   **Docker:** [Download Docker Desktop](https://www.docker.com/products/docker-desktop/) (for running the application in a container). Make sure Docker Desktop is running before executing Docker commands.

## Installation and Setup

Follow these steps to get the project running on your local machine.

**1. Clone the Repository:**

Open your terminal or command prompt and run the following command to download the project files:

```bash
git clone https://github.com/zxz2222/link-shortener.git
```

This will create a folder named `link-shortener` in your current directory.

**2. Navigate to the Project Directory:**

Change your current directory to the newly cloned folder:

```bash
cd link-shortener
```

## Running the Application Locally (Without Docker)

This method runs the application directly using Python on your machine.


**1. Install Dependencies:**

Install the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

**2. Run the Flask Application:**

Start the development server:

```bash
python app.py
```

You should see output indicating the server is running, typically on `http://127.0.0.1:5000`.

**3. Access the Application:**

Open your web browser and navigate to:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

You should see the link shortener interface. You can now use the application.

**5. Stop the Application:**

Press `CTRL+C` in the terminal where the server is running.


## Running the Application with Docker

This method uses Docker to build an image and run the application inside a container. This ensures the application runs in a consistent environment.

**1. Ensure Docker Desktop is Running:**

Make sure Docker Desktop is started and running on your system.

**2. Build the Docker Image:**

Navigate to the `link-shortener` directory in your terminal (if you aren't already there). Run the following command to build the Docker image. The `-t` flag tags the image with a name (`link-shortener-app` in this case). The `.` indicates that the `Dockerfile` is in the current directory.

```bash
docker build -t link-shortener-app .
```

This might take a few minutes the first time as Docker downloads the base Python image and installs dependencies.

**3. Run the Docker Container:**

Once the image is built, run the following command to start a container from the image:

```bash
docker run --rm -p 5000:5000 link-shortener-app
```

*   `docker run`: Command to run a container.
*   `--rm`: Automatically removes the container when it stops.
*   `-p 5000:5000`: Maps port 5000 on your host machine to port 5000 inside the container (where the Flask app is running).
*   `link-shortener-app`: The name of the image to run.

You should see the Flask server startup messages in your terminal.

**4. Access the Application:**

Open your web browser and navigate to:

[http://127.0.0.1:5000](http://127.0.0.1:5000) or [http://localhost:5000](http://localhost:5000)

The application should be running inside the Docker container.

**5. Stop the Container:**

Press `CTRL+C` in the terminal where the `docker run` command is executing. The container will stop and be removed (due to `--rm`).

## Next Steps (Deployment)

This project is ready to be deployed to hosting services that support Docker containers, such as:

*   Render
*   Fly.io
*   Google Cloud Run
*   Railway

Follow the specific documentation of your chosen provider to deploy the application using the included `Dockerfile`. You will typically need to connect your GitHub repository to the hosting service.
