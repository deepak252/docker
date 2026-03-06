package users

import (
    "context"
    "errors"

    "gorm.io/gorm"
)

type UserRepository interface {
    Save(ctx context.Context, user *User) error
    FindByEmail(ctx context.Context, email string) (*User, error)
    GetById(ctx context.Context, id string) (*User, error)
    List(ctx context.Context) ([]*User, error)
}

type gormUserRepository struct {
    db *gorm.DB
}

func NewGormUserRepository(db *gorm.DB) UserRepository {
    return &gormUserRepository{db: db}
}

func (r *gormUserRepository) Save(ctx context.Context, user *User) error {
    return r.db.WithContext(ctx).Create(user).Error
}

func (r *gormUserRepository) FindByEmail(ctx context.Context, email string) (*User, error) {
    var user User
    err := r.db.WithContext(ctx).Where("email = ?", email).First(&user).Error

    if errors.Is(err, gorm.ErrRecordNotFound) {
        return nil, nil
    }
    if err != nil {
        return nil, err
    }

    return &user, nil
}

func (r *gormUserRepository) GetById(ctx context.Context, id string) (*User, error) {
    var user User
    err := r.db.WithContext(ctx).First(&user, "id = ?", id).Error

    if errors.Is(err, gorm.ErrRecordNotFound) {
        return nil, nil
    }
    if err != nil {
        return nil, err
    }

    return &user, nil
}

func (r *gormUserRepository) List(ctx context.Context) ([]*User, error) {
    var users []*User
    err := r.db.WithContext(ctx).Find(&users).Error

    if err != nil {
        return nil, err
    }

    return users, nil
}
