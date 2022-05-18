FROM java:8
EXPOSE 80

ARG JAR_FILE=java-web-app.jar
ADD target/${JAR_FILE} /java-web-app.jar
ENTRYPOINT ["java", "-jar","/java-web-app.jar"]
