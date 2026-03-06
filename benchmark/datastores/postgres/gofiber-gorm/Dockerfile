### 🧱 Stage 1 — Build the Go binary
FROM golang:1.25.4-alpine AS builder
WORKDIR /app
COPY . .
# compile Go program into a binary named "server"
RUN go mod tidy && go build -o server ./cmd/server/


### 📦 Stage 2 — Create the lightweight runtime image
FROM alpine:3.19
WORKDIR /app
COPY --from=builder /app/server .
CMD ["./server"]