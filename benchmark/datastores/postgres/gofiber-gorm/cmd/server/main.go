package main

import (
	"gofiber-gorm/internal/common/middleware"
	"gofiber-gorm/internal/config"
	"gofiber-gorm/internal/db"
	"gofiber-gorm/internal/users"
	"log"

	"github.com/gofiber/fiber/v3"
	"github.com/gofiber/fiber/v3/middleware/recover"
)


func main() {
	cfg := config.Load()

	app := fiber.New(fiber.Config{
		ErrorHandler: middleware.ErrorHandler,
	})
	app.Use(recover.New())  // to recover from panics 
	db := db.NewPostgres(cfg.PostgresDSN)

	db.AutoMigrate(&users.User{})

	app.Get("/", func (c fiber.Ctx) error {
		// panic("This panic is caught by fiber")
		return c.JSON(fiber.Map{
			"status": "ok",
			"message": "go gorm application",
		})
	})

	userRepo := users.NewGormUserRepository(db)
	userSvc := users.NewUserService(userRepo)
	userHandler := users.NewUserHandler(userSvc)
	userHandler.RegisterRoutes(app)

	log.Println("Server running at port:", cfg.AppPort)

	err := app.Listen(":"+cfg.AppPort)
	if err != nil {
		log.Fatal(err)
	}

}
