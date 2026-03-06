package config

type Config struct {
	AppPort     string
	PostgresDSN string
}

func Load() *Config {
	return &Config{
		AppPort:     "8082",
		PostgresDSN: "postgres://root:root@localhost:5432/testdb?sslmode=disable",
	}
}
