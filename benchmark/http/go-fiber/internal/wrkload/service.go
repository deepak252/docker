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
	
	var wgWorker sync.WaitGroup
	var mu sync.Mutex
	chStatusCodes := make(chan int)
	successCodes := make(map[int]int)
	failureCodes := make(map[int]int)
	totalHits, failureHits := 0, 0
	start := time.Now()
	
	client := http.Client{
		Timeout: 2 * time.Second,
		Transport: &http.Transport{
			MaxIdleConns:        1000,
			MaxIdleConnsPerHost: int(connections),
			IdleConnTimeout:     90 * time.Second,
		},
	}

	ctx, cancel := context.WithTimeout(ctx, time.Duration(duration)*time.Second)
	defer cancel()

	for range connections {
		wgWorker.Go(func() {
			Worker(ctx, &client, apiData, &totalHits, &failureHits, &mu, chStatusCodes)
		})
	}

	go func() {
		wgWorker.Wait()
		close(chStatusCodes)
	}()

	for code := range chStatusCodes {
		if code <= 299 {
			successCodes[code]++
		} else {
			failureCodes[code]++
		}
	}

	return &WrkResult{
		Url: apiData.Url,
		Method: apiData.Method,
		Connections: int(connections),
		TimeTaken: fmt.Sprintf("%.3fs", time.Since(start).Seconds()),
		TotalHits: totalHits,
		SuccessHits: totalHits - failureHits,
		FailureHits: failureHits,
		SuccessMessages: successCodes,
		FailureMessages: failureCodes,
	}, nil

}

func Worker(ctx context.Context, client *http.Client, apiData *ApiData, totalHits *int, failureHits *int, mu *sync.Mutex, chStatusCodes chan<- int) {
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
			if err != nil || ( resp != nil && resp.StatusCode >= 400) {
				cntFailed++
			}
			if resp != nil {
				chStatusCodes <- resp.StatusCode
				resp.Body.Close()
			}
		}
	}
	
}