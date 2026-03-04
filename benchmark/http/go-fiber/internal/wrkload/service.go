package wrkload

import (
	"context"
	"fmt"
	"net/http"
	"sync"
	"time"
)

type WrkloadService interface {
	Wrk(ctx context.Context, apiData *ApiData,  connections uint, duration uint) (*WrkResult, error)
}

type wrkloadService struct {

}

func NewWrkLoadService() WrkloadService {
	return &wrkloadService{}
}

func (s *wrkloadService)Wrk(ctx context.Context, apiData *ApiData, connections uint, duration uint) (*WrkResult, error) {
	
	var wg sync.WaitGroup
	var mu sync.Mutex
	totalHits, failureHits := 0, 0
	start := time.Now()
	
	client := http.Client{
		Timeout: 1*time.Second,
	}

	ctx, cancel := context.WithTimeout(ctx, time.Duration(duration)*time.Second)
	defer cancel()

	for range connections {
		wg.Go(func() {
			Worker(ctx, &client, apiData, &totalHits, &failureHits, &mu)
		})
	}

	wg.Wait()

	return &WrkResult{
		Url: apiData.Url,
		Method: apiData.Method,
		Connections: int(connections),
		TimeTaken: fmt.Sprintf("%.3fs", time.Since(start).Seconds()),
		TotalHits: totalHits,
		SuccessHits: totalHits - failureHits,
		FailureHits: failureHits,
	}, nil

}

func Worker(ctx context.Context, client *http.Client, apiData *ApiData, totalHits *int, failureHits *int, mu *sync.Mutex) {
	cntTotal, cntFailed := 0, 0
	for {
		select {
		case <-ctx.Done():
			mu.Lock()
			*totalHits += cntTotal
			*failureHits += cntFailed
			mu.Unlock()
			return
		default:
			resp, err := client.Get(apiData.Url)
			cntTotal++
			if err != nil {
				cntFailed++
			} else {
				resp.Body.Close()
			}
		}
	}
	
}