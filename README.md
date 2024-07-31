# microservice-example
This example is the demonstration of using docker container to build the microservice    

Steps:
- Start the docker engine
- Go to project's folder (where Dockerfile is present) <br/>
  <b> cd microservice-example  </b>
- Build docker image <br/>
  <b> docker build -t my-first-microservice . </b>
- Run docker container <br/>
  <b> docker run -p 8000:8000 my-first-microservice </b>

- If you want to create CI/CD pipeline, then push the docker image to registry <br/>
    - Tag your Docker image <br/> 
      <b> docker tag my-microservice your-dockerhub-username/my-first-microservice:latest </b> <br/>
    - Log in to Docker Hub (if using Docker Hub) <br/>
      <b> docker login </b>
    - Push the image to Docker Hub <br/>
      <b> docker push your-dockerhub-username/my-microservice:latest </b>
