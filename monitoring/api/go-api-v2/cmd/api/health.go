package main

import (
	"fmt"
	"net/http"
)

func (app* application) healthCheckHandler(w http.ResponseWriter, r *http.Request){
	w.Write([]byte("ok"))
}


func (app* application) handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello from Go!")
}

func (app* application) heavyHandler(w http.ResponseWriter, r *http.Request) {
	total := 0
	for i := 0; i < 100000; i++ {
		total += i
	}
	fmt.Fprintf(w, "{\"total\": %d}", total)
}
