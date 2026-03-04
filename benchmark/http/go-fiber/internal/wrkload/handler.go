package wrkload

import (
	"benchmark-go-http/pkg/utils"
	"strconv"

	"github.com/gofiber/fiber/v3"
)

type WrkloadHandler struct {
	service WrkloadService
}

func NewWrkloadHandler(svc WrkloadService) *WrkloadHandler {
	return &WrkloadHandler{
		service: svc,
	}
}

func (h *WrkloadHandler) RegisterRoutes(app *fiber.App) {
	app.Get("/wrk", h.Wrk)
}


func (h *WrkloadHandler) Wrk(c fiber.Ctx) error {
	endpoint := c.Query("e", "https://example.com")
	method := c.Query("m", "get")

	connectionsStr := c.Query("c", "10")
	durationStr := c.Query("d", "10")

	connections, err := strconv.Atoi(connectionsStr)
	if err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"error": "invalid connections value",
		})
	}

	duration, err := strconv.Atoi(durationStr)
	if err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"error": "invalid duration value",
		})
	}

	apiDataB := ApiDataBuilder{}
	apiData := apiDataB.SetUrl(endpoint).SetMethod(method).Build()

	wrkResult, err := h.service.Wrk(c, apiData, uint(connections), uint(duration))

	if err != nil {
		return utils.ErrorResponse(
			c, fiber.StatusInternalServerError, err.Error(),
		)
	}
	return utils.SuccessResponse(c, &WrkResponse{
		Url: wrkResult.Url,
		Method: wrkResult.Method,
		TimeTaken: wrkResult.TimeTaken,
		Connections: wrkResult.Connections,
		TotalHits: wrkResult.TotalHits,
		SuccessHits: wrkResult.SuccessHits,
		FailureHits: wrkResult.FailureHits,
		SuccessMessages: wrkResult.SuccessMessages,
		FailureMessages: wrkResult.FailureMessages,
	})
}
