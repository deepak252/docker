package ps

type CPUInfoResponse struct {
	Model string  `json:"model"`
	Cores int32   `json:"cores"`
	Usage float64 `json:"usage"`
}

type HostInfoResponse struct {
	HostName string `json:"hostname"`
	OS       string `json:"os"`
	Platform string `json:"platform"`
	Uptime   uint64 `json:"uptime"`
	BootTime uint64 `json:"boottime"`
}

type MemoryInfoResponse struct {
	Total string  `json:"total"`
	Used  string  `json:"used"`
	Free  string  `json:"free"`
	Usage float64 `json:"usage"`
}

type ProcessInfoResponse struct {
	PID  int32   `json:"pid"`
	Name string  `json:"name"`
	CPU  float64 `json:"cpu"`
	Mem  float32 `json:"mem"`
}

type UsageInfoResponse struct {
	PID         int32   `json:"pid"`
	RSS         string  `json:"rss"`
	VMS         string  `json:"vms"`
	MemoryUsage float64 `json:"memory-usage"`
	CPUUsage    float64 `json:"cpu-usage"`
}
