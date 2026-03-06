package users

import (
	"context"
	"errors"

	// "github.com/google/uuid"
)


type UserService interface {
	RegisterUser(ctx context.Context, name, email string) (*User, error)
	GetUserById(ctx context.Context, id string) (*User, error)
	ListUsers(ctx context.Context) ([]*User, error)
}

type userService struct {
	repo UserRepository
}

func NewUserService(repo UserRepository) UserService {
	return &userService{
		repo: repo,
	}
}

func (s *userService) RegisterUser(ctx context.Context, name, email string) (*User, error)  {
	existing := s.repo.FindByEmail(ctx, email)
	if existing != nil {
		return nil, errors.New("user with this email already exists")
	}

	user := &User{
		// ID:    uuid.NewString(),
		Name:  name,
		Email: email,
	}

	if err := s.repo.Save(ctx, user); err != nil {
		return nil, err
	}

	return user, nil
}

func (s *userService) GetUserById(ctx context.Context, id string) (*User, error) {
	user := s.repo.GetById(ctx, id)

	if user == nil {
		return nil, errors.New("user not found")
	}
	return user, nil
}

func (s *userService) ListUsers(ctx context.Context) ([]*User, error) {
	users, err := s.repo.List(ctx)

	if err != nil {
		return nil, errors.New("user not found")
	}
	return users, nil
}