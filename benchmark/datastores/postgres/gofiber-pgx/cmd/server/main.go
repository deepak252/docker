package main

import (
	"log"
	"gofiber-pgx/internal/books"
	"gofiber-pgx/internal/config"
	"gofiber-pgx/internal/db"
	"gofiber-pgx/internal/users"

	"github.com/gofiber/fiber/v3"
)


func main() {
	cfg := config.Load()

	app := fiber.New()

	pool := db.NewPostgresPool(cfg.PostgresDSN)

	// db.AutoMigrate(&users.User{})
	// db.AutoMigrate(&books.Book{})

	userRepo := users.NewPgxUserRepository(pool)
	userSvc := users.NewUserService(userRepo)
	userHandler := users.NewUserHandler(userSvc)
	userHandler.RegisterRoutes(app)

	bookRepo := books.NewPgxBookRepository(pool)
	bookSvc := books.NewBookService(bookRepo)
	bookHandler := books.NewBookHandler(bookSvc)
	bookHandler.RegisterRoutes(app)

	log.Println("Server running at port:", cfg.AppPort)

	err := app.Listen(":"+cfg.AppPort)
	if err != nil {
		log.Fatal(err)
	}

}
