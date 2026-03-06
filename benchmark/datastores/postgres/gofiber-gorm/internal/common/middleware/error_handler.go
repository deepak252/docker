package middleware

import (
	"gofiber-gorm/internal/common/apperrors"
	"gofiber-gorm/internal/common/response"
	"log"

	"github.com/gofiber/fiber/v3"
)

func ErrorHandler(c fiber.Ctx, err error) error {
	// If it's an AppError (custom error)
	if e, ok := err.(*apperrors.AppError); ok {
		if e.Err != nil {
			log.Println(e.Err.Error())
		}
		return c.Status(e.Code).JSON(response.Error{
			Code: e.Code,
			Message: e.Message,
			// Error:   e.Err.Error(),
		})
	}

	log.Println(err.Error())

	// fallback for unexpected errors
	return c.Status(500).JSON(response.Error{
		Code: fiber.StatusInternalServerError,
		Message: "Internal Server Error",
	})
}
