package main

import (
	"benchmark-go-http/internal/config"
	"log"

	"github.com/gofiber/fiber/v3"
)

func main() {
	cfg := config.Load()

	app := fiber.New()

	app.Get("/", func (c fiber.Ctx) error {
		return c.JSON(fiber.Map{
			"message": "Server is up",
		})
	})
	
	err := app.Listen(":"+cfg.Port)
	if err != nil {
		log.Fatal(err)
	}
}