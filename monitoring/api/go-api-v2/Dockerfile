# Stage 1: Build the Go binary
FROM golang:1.25.0-alpine AS builder

# Set working directory
WORKDIR /app

# Copy only go.mod and go.sum first (caching)
COPY go.mod go.sum ./

# Download dependencies
RUN go mod download

# Copy the rest of the code
COPY . .

# Build the binary (main package is in /cmd/api)
RUN go build -o go-api ./cmd/api

# Stage 2: Minimal image
FROM gcr.io/distroless/base-debian12

# Copy the built binary
COPY --from=builder /app/go-api /go-api

# Expose ports
EXPOSE 8080 6060

# Run the binary
CMD ["/go-api"]


# FROM golang:1.25.0-alpine AS builder

# WORKDIR /app
# COPY . .
# RUN go build -o go-api main.go

# FROM gcr.io/distroless/base-debian12
# COPY --from=builder /app/go-api /go-api

# # Expose both API and pprof ports
# EXPOSE 8080 6060

# CMD ["/go-api"]

# FROM golang:1.25.0-alpine AS builder

# WORKDIR /app
# COPY . .
# RUN go build -o go-api main.go

# FROM gcr.io/distroless/base-debian12
# COPY --from=builder /app/go-api /go-api
# CMD ["/go-api"]