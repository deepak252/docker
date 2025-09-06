package main

import (
	"log"
	"os"
	"social-app/internal/env"

	"github.com/joho/godotenv"
)

func init() {
	if os.Getenv("GO_ENV") != "production" {
		_ = godotenv.Load()
	}
}

func main(){
	// log.Printf("%s", env.GetString("ADDR", "3000"))
	cfg := config{
		addr: env.GetString("ADDR", ":8080"),
	}
	app := &application{
		config: cfg,
	}

	mux := app.mount()

	log.Fatal((*app).run(mux))
}