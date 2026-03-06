package books

import (
	"context"

	"github.com/jackc/pgx/v5/pgxpool"
)

type BookRepository interface {
	SaveBook(ctx context.Context, book *Book) error
	FindBookById(ctx context.Context, id string) *Book
}

type pgxBookRepository struct {
	db *pgxpool.Pool
} 

func NewPgxBookRepository(db *pgxpool.Pool) BookRepository {
	return &pgxBookRepository{
		db: db,
	}
}

func (r *pgxBookRepository)SaveBook(ctx context.Context, book *Book) error {
	_, err := r.db.Exec(ctx,
		`INSERT INTO books (title, author)
		VALUES ($1, $2)`,
		book.Title, book.Author,
	)
	return err
}

func (r *pgxBookRepository)FindBookById(ctx context.Context, id string) *Book {
	var book Book
	err := r.db.QueryRow(ctx,
		`SELECT id, title, author FROM books WHERE id = $1`,
		id,
	).Scan(&book.ID, &book.Title, &book.Author)
	
	if err != nil {
		return nil
	}
	return &book
}
