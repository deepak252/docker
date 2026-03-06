package books

import (
	"context"
	"errors"
)

type BookService interface {
	CreateBook(ctx context.Context, title, author string) (*Book, error)
	GetBookById(ctx context.Context, id string) (*Book, error)
}

type bookService struct {
	repo BookRepository
}

func NewBookService(repo BookRepository) BookService {
	return &bookService{
		repo: repo,
	}
}


func (s *bookService)CreateBook(ctx context.Context, title, author string) (*Book, error) {
	book := &Book{
		Title: title,
		Author: author,
	}
	err := s.repo.SaveBook(ctx, book)
	if err != nil {
		return nil, err
	}
	return book, nil
}

func (s *bookService)GetBookById(ctx context.Context, id string) (*Book, error) {
	book := s.repo.FindBookById(ctx, id)
	if book == nil {
		return nil, errors.New("no book found")
	}
	return book, nil
}