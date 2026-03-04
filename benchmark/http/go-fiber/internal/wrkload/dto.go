package wrkload

type WrkResponse struct {
	Url             string `json:"url"`
	Method          string `json:"method"`
	TimeTaken       string `json:"time_taken"`
	Connections     int    `json:"connections"`
	TotalHits       int    `json:"total_hits"`
	SuccessHits     int    `json:"success_hits"`
	FailureHits     int    `json:"failure_hits"`
	SuccessMessages any    `json:"success_messages"`
	FailureMessages any    `json:"failure_messages"`
}
