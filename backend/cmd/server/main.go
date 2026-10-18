package main

import (
	"log"
	"net/http"
	"os"
	"time"

	"pode/backend/internal/transport/httpapi"
)

func main() {
	addr := os.Getenv("HTTP_ADDR")
	if addr == "" {
		addr = ":8080"
	}
	server := &http.Server{
		Addr:              addr,
		Handler:           httpapi.NewHandler(),
		ReadHeaderTimeout: 5 * time.Second,
		ReadTimeout:       15 * time.Second,
		WriteTimeout:      15 * time.Second,
		IdleTimeout:       60 * time.Second,
	}
	log.Printf("Pode listening on %s", addr)
	log.Fatal(server.ListenAndServe())
}
