FROM golang:1.25.0-alpine AS builder

WORKDIR /app
COPY . .
RUN go build -o go-api main.go

FROM gcr.io/distroless/base-debian12
COPY --from=builder /app/go-api /go-api
CMD ["/go-api"]