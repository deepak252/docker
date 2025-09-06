# Multi-stage build
FROM maven:3.9.6-eclipse-temurin-21 AS builder

WORKDIR /app

# Copy everything and build directly (no dependency pre-download)
COPY . .
RUN mvn clean package -DskipTests -B

# Runtime stage
FROM eclipse-temurin:21-jre-alpine

WORKDIR /app

# Create non-root user for security
RUN addgroup -g 1001 -S appgroup && \
    adduser -S appuser -u 1001 -G appgroup

# Copy the JAR file from builder stage
COPY --from=builder /app/target/spring-api-1.0.0.jar app.jar

# Change ownership
RUN chown appuser:appgroup app.jar

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8080

# Configure JVM for container environment with memory limits
ENV JAVA_OPTS="-XX:+UseContainerSupport -XX:MaxRAMPercentage=75.0 -XX:+UseG1GC -Xms64m -Xmx192m"

# Run the application
CMD ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
