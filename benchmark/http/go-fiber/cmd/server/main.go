package main

import (
	"benchmark-go-http/internal/config"
	"benchmark-go-http/internal/health"
	"benchmark-go-http/internal/wrkload"
	"log"

	"github.com/gofiber/fiber/v3"
)

func main() {
	cfg := config.Load()

	app := fiber.New()

	healthService := health.NewHealthService()
	healthHandler := health.NewHealthHandler(healthService)
	healthHandler.RegisterRoutes(app)

	wrkloadService := wrkload.NewWrkLoadService()
	wrkloadHandler := wrkload.NewWrkloadHandler(wrkloadService)
	wrkloadHandler.RegisterRoutes(app)

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