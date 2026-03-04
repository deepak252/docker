package utils

import "github.com/gofiber/fiber/v3"

type APIResponse struct {
	Success bool `json:"success"`
	Data    any `json:"data,omitempty"`
	Error   any `json:"error,omitempty"`
}

func SuccessResponse(c fiber.Ctx, data any) error {
	return c.JSON(APIResponse{
		Success: true,
		Data: data,
	})
}

func ErrorResponse(c fiber.Ctx, code int, err string) error {
	return c.Status(code).JSON(APIResponse{
		Success: false,
		Error: err,
	})
} 
