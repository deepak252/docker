package config

type Config struct {
	AppName string
	Port string
}

func Load() *Config {
	return &Config{
		AppName: "Go Fiber",
		Port: "8080",
	}
}