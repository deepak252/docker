package db

import (
	"context"
	"log"
	"time"

	"github.com/jackc/pgx/v5/pgxpool"
)

func NewPostgresPool(dsn string) *pgxpool.Pool {


    cfg, err := pgxpool.ParseConfig(dsn)
    if err != nil {
        log.Fatal("pgx config error:", err)
    }

    cfg.MaxConns = 25
    cfg.MinConns = 5
    cfg.MaxConnLifetime = 5 * time.Minute

    pool, err := pgxpool.NewWithConfig(context.Background(), cfg)
    if err != nil {
        log.Fatal("failed to connect postgres:", err)
    }

	defer pool.Close()

    return pool
}
