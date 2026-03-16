package ps

import (
    // "fmt"
	"os"
	// "github.com/shirou/gopsutil/v4/net"
    "github.com/shirou/gopsutil/v4/cpu"
    "github.com/shirou/gopsutil/v4/mem"
    "github.com/shirou/gopsutil/v4/host"
    "github.com/shirou/gopsutil/v4/process"
)


type PSService interface {
	GetHostInfo() (*HostInfo, error)
	GetMemoryInfo() (*MemoryInfo, error)
	GetCPUInfo() ([]*CPUInfo, error)
	GetProcessInfo() ([]*ProcessInfo, error)
	GetUsageInfo() (*UsageInfo, error)
}

type psService struct {
}

func NewPSService() PSService {
	return &psService{}
}
func (s *psService)GetHostInfo() (*HostInfo, error) {
	info, err := host.Info()

	if err != nil {
		return nil, err
	}

	return &HostInfo{
		HostName: info.Hostname,
		OS: info.OS,
		Platform: info.Platform,
		Uptime: info.Uptime,
		BootTime: info.BootTime,
	}, nil
}

func (s *psService) GetMemoryInfo() (*MemoryInfo, error) {
	v, err := mem.VirtualMemory()

	if err != nil {
		return nil, err
	}

	return &MemoryInfo{
		Total: v.Total,
		Used: v.Used,
		Free: v.Free,
		Usage: v.UsedPercent,
	}, nil
}

func (s *psService)GetCPUInfo() ([]*CPUInfo, error) {
	// CPU usage percentage (per core)
	percent, err := cpu.Percent(0, true)

	if err != nil {
		return nil, err
	}

	info, err := cpu.Info()
	if err != nil {
		return nil, err
	}

	n := min(len(percent), len(info))

	res := make([]*CPUInfo, n)

	for i := range n {
		res[i] = &CPUInfo{
			Model: info[i].Model,
			Cores: info[i].Cores,
			Usage: percent[i],
		}
	}
	return res, nil
}

func (s *psService)GetProcessInfo() ([]*ProcessInfo, error) {
	processes, err := process.Processes()

	if err != nil {
		return nil, err
	}
	n := len(processes)
	res := make([]*ProcessInfo, n)
	
	for i := range n {
		name, _ := processes[i].Name()
        cpu, _ := processes[i].CPUPercent()
        mem, _ := processes[i].MemoryPercent()
		res[i] = &ProcessInfo{
			PID: processes[i].Pid,
			Name: name,
			CPU: cpu,
			Mem: mem,
		}
	}
	return res, nil	
}


func (s *psService)GetUsageInfo() (*UsageInfo, error) {
	
	pid := int32(os.Getpid())
	proc, err := process.NewProcess(pid)

	if err != nil {
		return nil, err
	}
	memInfo, _ := proc.MemoryInfo()
	memPct, _ := proc.MemoryPercent()
	cpuPct, _ := proc.CPUPercent()

	return &UsageInfo{
		PID: pid,
		RSS: memInfo.RSS,
		VMS: memInfo.VMS,
		MemoryUsage: float64(memPct),
		CPUUsage: cpuPct,
	}, nil	
}