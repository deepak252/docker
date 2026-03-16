package ps

import (
	"benchmark-go-http/pkg/utils"

	"github.com/gofiber/fiber/v3"
)

type PSHandler struct {
	svc PSService
}

func NewPSHandler(psService PSService) *PSHandler {
	return &PSHandler{
		svc: psService,
	}
}

func (h *PSHandler)RegisterRoutes(app *fiber.App) {
	app.Get("/ps/cpu", h.CPUInfo)
	app.Get("/ps/host", h.HostInfo)
	app.Get("/ps/memory", h.MemoryInfo)
	app.Get("/ps/process", h.ProcessInfo)
	app.Get("/ps/usage", h.UsageInfo)
}

func (h *PSHandler)CPUInfo(c fiber.Ctx) error {
	cpuInfo, err := h.svc.GetCPUInfo()
	if err != nil {
		return utils.ErrorResponse(
			c, fiber.StatusInternalServerError, err.Error(),
		)
	}
	res := []*CPUInfoResponse{}
	for _, info := range cpuInfo {
		res = append(res, &CPUInfoResponse{
			Model: info.Model,
			Cores: info.Cores,
			Usage: info.Usage,
		})
	}
	return utils.SuccessResponse(c, res)
}

func (h *PSHandler)HostInfo(c fiber.Ctx) error {
	hostInfo, err := h.svc.GetHostInfo()
	if err != nil {
		return utils.ErrorResponse(
			c, fiber.StatusInternalServerError, err.Error(),
		)
	}
	return utils.SuccessResponse(c, &HostInfoResponse{
		HostName: hostInfo.HostName,
		OS: hostInfo.OS,
		Platform: hostInfo.Platform,
		Uptime: hostInfo.Uptime,
		BootTime: hostInfo.BootTime,
	})
}

func (h *PSHandler)MemoryInfo(c fiber.Ctx) error {
	memInfo, err := h.svc.GetMemoryInfo()
	if err != nil {
		return utils.ErrorResponse(
			c, fiber.StatusInternalServerError, err.Error(),
		)
	}
	return utils.SuccessResponse(c, &MemoryInfoResponse{
		Total: utils.FormatBytes(memInfo.Total), 
		Used: utils.FormatBytes(memInfo.Used), 
		Free: utils.FormatBytes(memInfo.Free), 
		Usage: memInfo.Usage, 
	})
}

func (h *PSHandler)ProcessInfo(c fiber.Ctx) error {
	processInfo, err := h.svc.GetProcessInfo()
	if err != nil {
		return utils.ErrorResponse(
			c, fiber.StatusInternalServerError, err.Error(),
		)
	}
	res := []*ProcessInfoResponse{}
	for _, info := range processInfo {
		res = append(res, &ProcessInfoResponse{
			PID: info.PID,
			Name: info.Name,
			CPU: info.CPU,
			Mem: info.Mem,
		})
	}
	return utils.SuccessResponse(c, res)
}

func (h *PSHandler)UsageInfo(c fiber.Ctx) error {
	usageInfo, err := h.svc.GetUsageInfo()
	if err != nil {
		return utils.ErrorResponse(
			c, fiber.StatusInternalServerError, err.Error(),
		)
	}
	return utils.SuccessResponse(c, &UsageInfoResponse{
		PID: usageInfo.PID,
		RSS: utils.FormatBytes(usageInfo.RSS),
		VMS: utils.FormatBytes(usageInfo.VMS),
		MemoryUsage: usageInfo.MemoryUsage,
		CPUUsage: usageInfo.CPUUsage,
	})
}