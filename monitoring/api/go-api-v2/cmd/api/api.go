package main

import (
	"log"
	"net/http"
	"time"
	"github.com/go-chi/chi/v5"
	// "github.com/go-chi/chi/v5/middleware"
)

type application struct{
	config config
}

type config struct{
	addr string
}

func (app *application) mount() http.Handler {
	// mux := http.NewServeMux()
	// mux.HandleFunc("GET /v1/health", app.healthCheckHandler)

	r := chi.NewRouter()
	// r.Use(middleware.RequestID)
	// r.Use(middleware.RealIP)
	// r.Use(middleware.Logger)
	// r.Use(middleware.Recoverer)
	// r.Use(middleware.Timeout(60 * time.Second))
    

	// r.Route("/v1", func(r chi.Router){
	// 	r.Get("/health", app.healthCheckHandler)
	// })

	r.Get("/", app.handler)
	r.Get("/heavy", app.heavyHandler)

	return r
}

func (app *application) run(mux http.Handler) error {
	
	srv := http.Server{
		Addr: app.config.addr,
		Handler: mux,
		WriteTimeout: time.Second*30,
		ReadTimeout: time.Second*10,
		IdleTimeout: time.Second*60,
	}

	log.Printf("Server is running on port %s", app.config.addr)

	return srv.ListenAndServe()
}