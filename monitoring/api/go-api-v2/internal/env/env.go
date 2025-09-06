package env

import (
	"os"
	"strconv"
)

func GetEnv(key, fallback string) string {
	if val, ok := os.LookupEnv(key); ok {
		return val
	}
	return fallback
}

func GetString(key, fallback string) string {
	val, ok := os.LookupEnv(key)
	if !ok {
		return fallback
	}
	return val
}

func GetInt(key string, fallback int) int {
	val, ok := os.LookupEnv(key)
	if !ok {
		return fallback
	}
	
	valInt, err := strconv.Atoi(val)
	if err!=nil {
		return fallback
	}

	return valInt

}