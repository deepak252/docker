package health

import (
	"benchmark-go-http/pkg/utils"
	"github.com/gofiber/fiber/v3"
)

type HealthHandler struct {
	service HealthService 
}

func NewHealthHandler(svc HealthService) *HealthHandler {
	return &HealthHandler{
		service: svc,
	}
}

func (h *HealthHandler) RegisterRoutes(app *fiber.App) {
	app.Get("/health", h.Health)
}

func (h *HealthHandler) Health(c fiber.Ctx) error {
	msg := h.service.Health()
	return utils.SuccessResponse(c, msg)
}