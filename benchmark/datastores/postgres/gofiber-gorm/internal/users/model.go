package users

import "time"

type User struct {
	// ID 	string `gorm:"primaryKey"`
	ID 	uint `gorm:"primaryKey;autoIncrement"`
	Name string
	Email string
	CreatedAt time.Time `gorm:"uniqueIndex"`
}