package users

import (
	"gofiber-gorm/internal/common/apperrors"
	"gofiber-gorm/internal/common/response"

	"github.com/gofiber/fiber/v3"
)

type UserHandler struct {
	svc UserService
}

func NewUserHandler(svc UserService) *UserHandler {
	return &UserHandler{
		svc: svc,
	}
}

func (h *UserHandler) RegisterRoutes(app *fiber.App) {
	app.Post("/users", h.RegisterUser)
	app.Get("/users", h.ListUsers)
	app.Get("/users/:id", h.GetUser)
}

func (h *UserHandler) RegisterUser(c fiber.Ctx) error {
	var req struct {
		Name string `json:"name"`
		Email string `json:"email"`
	}

	if err := c.Bind().Body(&req); err != nil {
		return apperrors.New(fiber.StatusBadRequest, "invalid request", err)
	}

	user, err := h.svc.RegisterUser(c, req.Name, req.Email)

	if err != nil {
		return err
	}

	return c.Status(fiber.StatusCreated).JSON(response.Success{
		Code: 200,
		Data: user,
	})
}

func (h *UserHandler) GetUser(c fiber.Ctx) error {
	id := c.Params("id")

	user, err := h.svc.GetUserById(c, id)

	if err != nil {
		return err
	}

	if user == nil {
		return apperrors.New(fiber.StatusNotFound, "User not found", nil)
	}
	return c.Status(200).JSON(response.Success{
		Code: 200,
		Data: user,
	})
}

func (h *UserHandler) ListUsers(c fiber.Ctx) error {
	users, err := h.svc.ListUsers(c)
	if err != nil {
		return err
		// return fiber.ErrBadRequest
		// return fiber.NewError(fiber.StatusNotFound, "something went wrong")
		// return c.Status(fiber.StatusNotFound).JSON(fiber.Map{ // this not caught by global exception handler
		// 	"error": "Something went wrong!",
		// })
	}

	return c.Status(200).JSON(response.Success{
		Code: 200,
		Data: users,
	})
}