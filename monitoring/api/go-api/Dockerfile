FROM golang:1.25.0-alpine AS builder

WORKDIR /app
COPY . .
RUN go build -o go-api main.go

FROM gcr.io/distroless/base-debian12
COPY --from=builder /app/go-api /go-api

# Expose both API and pprof ports
EXPOSE 8080 6060

CMD ["/go-api"]

# FROM golang:1.25.0-alpine AS builder

# WORKDIR /app
# COPY . .
# RUN go build -o go-api main.go

# FROM gcr.io/distroless/base-debian12
# COPY --from=builder /app/go-api /go-api
# CMD ["/go-api"]