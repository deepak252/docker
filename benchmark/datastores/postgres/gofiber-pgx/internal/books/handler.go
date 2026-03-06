package books

import "github.com/gofiber/fiber/v3"


type BookHandler struct {
	svc BookService
}

func NewBookHandler(svc BookService) *BookHandler {
	return &BookHandler{
		svc: svc,
	}
}

func (h *BookHandler) RegisterRoutes(app *fiber.App) {
	app.Post("books", h.SaveBook)
	app.Get("books/:id", h.GetBook)
	app.Get("books-static/:id", h.GetBookStatic)
}

func (h *BookHandler) SaveBook(c fiber.Ctx) error {
	var req struct {
		Title string `json:"title"`
		Author string `json:"author"`
	}
	if err := c.Bind().Body(&req); err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"error": "invalid request",
			"description": err.Error(),
		})
	}
	book, err := h.svc.CreateBook(c, req.Title, req.Author)

	if err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"error": "Something went wrong",
			"description": err.Error(),
		})
	}
	return c.Status(fiber.StatusCreated).JSON(book)
}

func (h *BookHandler) GetBook(c fiber.Ctx) error {
	id := c.Params("id")
	
	book, err := h.svc.GetBookById(c, id)

	if err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"error": err.Error(),
		})
	}

	if book == nil {
		return c.Status(fiber.StatusNotFound).JSON(fiber.Map{
			"error": "Book not found!",
		})
	}
	return c.JSON(book)
}

func (h *BookHandler) GetBookStatic(c fiber.Ctx) error {
	id := c.Params("id")
	id += ""
	return c.JSON(Book{
		Title: "C++ ",
		Author: "deepak",
	})
}