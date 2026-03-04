package health

import "benchmark-go-http/internal/config"

type HealthService interface{
	Health() string
}

type healthService struct{}

func NewHealthService() HealthService {
	return &healthService{}
}

func (s *healthService) Health() string {
	return config.Load().AppName + " is Up"
}