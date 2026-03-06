package users

import (
    "context"
    "github.com/jackc/pgx/v5/pgxpool"
)

type UserRepository interface {
	Save(ctx context.Context, user *User) error
	FindByEmail(ctx context.Context, email string) *User
	GetById(ctx context.Context, id string) *User
	List(ctx context.Context) ([]*User, error)
}

type pgxUserRepository struct {
    db *pgxpool.Pool
}

func NewPgxUserRepository(db *pgxpool.Pool) UserRepository {
    return &pgxUserRepository{db: db}
}

func (r *pgxUserRepository) Save(ctx context.Context, user *User) error {
    _, err := r.db.Exec(ctx,
        `INSERT INTO users (name, email, created_at)
         VALUES ($1, $2, NOW())`,
         user.Name, user.Email,
    )
    return err
}

func (r *pgxUserRepository) FindByEmail(ctx context.Context, email string) *User {
    var user User
    err := r.db.QueryRow(ctx,
        `SELECT id, name, email, created_at FROM users WHERE email=$1`,
        email,
    ).Scan(&user.ID, &user.Name, &user.Email, &user.CreatedAt)

    if err != nil {
        return nil
    }
    return &user
}

func (r *pgxUserRepository) GetById(ctx context.Context, id string) *User {
    var user User
    err := r.db.QueryRow(ctx,
        `SELECT id, name, email, created_at FROM users WHERE id=$1`,
        id,
    ).Scan(&user.ID, &user.Name, &user.Email, &user.CreatedAt)

    if err != nil {
        return nil
    }
    return &user
}

func (r *pgxUserRepository) List(ctx context.Context) ([]*User, error) {
    rows, err := r.db.Query(ctx,
		`SELECT id, name, email, created_at FROM users`,
	)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var users []*User

	for rows.Next() {
		u := new(User)
		if err := rows.Scan(&u.ID, &u.Name, &u.Email, &u.CreatedAt); err != nil {
			return nil, err
		}
		users = append(users, u)
	}

	return users, rows.Err()

}