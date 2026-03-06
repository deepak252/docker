package users

import (
    "context"
    "gofiber-gorm/internal/common/apperrors"
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
    return &userService{repo: repo}
}

func (s *userService) RegisterUser(ctx context.Context, name, email string) (*User, error) {
    existing, err := s.repo.FindByEmail(ctx, email)
    if err != nil {
        return nil, apperrors.Internal("failed to lookup email", err)
    }

    if existing != nil {
        return nil, apperrors.Conflict("user with this email already exists", nil)
    }

    user := &User{
        Name:  name,
        Email: email,
    }

    if err := s.repo.Save(ctx, user); err != nil {
        return nil, apperrors.Internal("failed to save user", err)
    }

    return user, nil
}

func (s *userService) GetUserById(ctx context.Context, id string) (*User, error) {
    user, err := s.repo.GetById(ctx, id)
    if err != nil {
        return nil, apperrors.Internal("failed to fetch user", err)
    }

    if user == nil {
        return nil, apperrors.NotFound("user not found", nil)
    }

    return user, nil
}

func (s *userService) ListUsers(ctx context.Context) ([]*User, error) {
    users, err := s.repo.List(ctx)
    if err != nil {
        return nil, apperrors.Internal("failed to fetch users", err)
    }

    return users, nil
}
