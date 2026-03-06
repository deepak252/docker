package users

import "github.com/gofiber/fiber/v3"

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
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": "invalid request"})
	}

	user, err := h.svc.RegisterUser(c, req.Name, req.Email)

	if err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
	}

	return c.Status(fiber.StatusCreated).JSON(user)
}

func (h *UserHandler) GetUser(c fiber.Ctx) error {
	id := c.Params("id")

	user, err := h.svc.GetUserById(c, id)

	if err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"error": err.Error(),
		})
	}

	if user == nil {
		return c.Status(fiber.StatusNotFound).JSON(fiber.Map{
			"error": "User not found!",
		})
	}
	return c.JSON(user)
}

func (h *UserHandler) ListUsers(c fiber.Ctx) error {
	users, err := h.svc.ListUsers(c)

	if err == nil {
		return c.Status(fiber.StatusNotFound).JSON(fiber.Map{
			"error": "Something went wrong!",
		})
	}
	return c.JSON(users)
}