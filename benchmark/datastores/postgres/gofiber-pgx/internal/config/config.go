package config

type Config struct {
	AppPort string
	PostgresDSN string
}

func Load() *Config {
	return &Config {
		AppPort: "8083",
		PostgresDSN: "postgres://root:root@postgres:5432/testdb?sslmode=disable",
	}
}