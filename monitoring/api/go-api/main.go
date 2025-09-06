
package main

import (
	"fmt"
	"log"
	"net/http"
	_ "net/http/pprof"
	"time"
)

var leakySlice [][]byte

func leakHandler(w http.ResponseWriter, r *http.Request) {
	// Allocate 1 MB on every request
	// data := make([]byte, 1024*1024)
	// leakySlice = append(leakySlice, data)
	// fmt.Fprintf(w, "Allocated 1MB, total: %dMB\n", len(leakySlice))

	data := make([]byte, 1024*1024)

	// Start a goroutine that never releases the reference
	go func(d []byte) {
		for {
			time.Sleep(time.Minute)
			_ = d // keep reference alive
		}
	}(data)

	fmt.Fprintf(w, "Leaked 1MB via goroutine")
}

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello from Go!")
}

func heavyHandler(w http.ResponseWriter, r *http.Request) {
	total := 0
	for i := 0; i < 100000; i++ {
		total += i
	}
	fmt.Fprintf(w, "{\"total\": %d}", total)
}

func main() {

	go func() {
		fmt.Println("pprof available at :6060/debug/pprof/")
		log.Println(http.ListenAndServe(":6060", nil))
	}()

	http.HandleFunc("/", handler)
	http.HandleFunc("/heavy", heavyHandler)
	http.HandleFunc("/leak", leakHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))

}

// package main

// import (
//     "fmt"
//     "net"
//     "net/http"
//     "time"
// )

// func handler(w http.ResponseWriter, r *http.Request) {
//     fmt.Fprintf(w, "Hello from Go!")
// }

// func heavyHandler(w http.ResponseWriter, r *http.Request) {
//     total := 0
//     for i := 0; i < 100000; i++ {
//         total += i
//     }
//     fmt.Fprintf(w, "{\"total\": %d}", total)
// }

// func main() {
//     http.HandleFunc("/", handler)
//     http.HandleFunc("/heavy", heavyHandler)

//     srv := &http.Server{
//         Addr:         ":8080",
//         Handler:      nil,
//         ReadTimeout:  10 * time.Second,
//         WriteTimeout: 10 * time.Second,
//         IdleTimeout:  60 * time.Second,
//     }

//     ln, err := net.Listen("tcp", srv.Addr)
//     if err != nil {
//         panic(err)
//     }

//     tcpListener := ln.(*net.TCPListener)
//     fmt.Println("Server running on :8080")
//     srv.Serve(tcpListener)
// }
