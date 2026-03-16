package ps

type HostInfo struct {
	HostName string
	OS string
	Platform string
	Uptime uint64
	BootTime uint64
}

type MemoryInfo struct {
	Total uint64
	Used  uint64
	Free  uint64
	Usage float64
}

type CPUInfo struct {
	Model string
	Cores int32
	Usage float64
}

type UsageInfo struct {
	PID int32
	RSS uint64
	VMS uint64
	MemoryUsage float64
	CPUUsage float64
}

type ProcessInfo struct {
	PID int32
	Name string
	CPU float64
	Mem float32
}
