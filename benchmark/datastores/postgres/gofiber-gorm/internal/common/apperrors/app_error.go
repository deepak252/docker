package apperrors

import "github.com/gofiber/fiber/v3"

type AppError struct {
    Code    int    `json:"code"`
    Message string `json:"message"`
    Err     error  `json:"error,omitempty"`
}

func (e *AppError) Error() string {
    return e.Message
}

func New(code int, message string, err error) *AppError {
    return &AppError{
        Code:    code,
        Message: message,
        Err:     err,
    }
}

func NotFound(message string, err error) *AppError {
    return New(fiber.StatusNotFound, message, err)
}

func Conflict(message string, err error) *AppError {
    return New(fiber.StatusConflict, message, err)
}

func BadRequest(message string, err error) *AppError {
    return New(fiber.StatusBadRequest, message, err)
}

func Internal(message string, err error) *AppError {
    return New(fiber.StatusInternalServerError, message, err)
}